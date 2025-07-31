import bluetooth
import struct
import time
import ubinascii
from machine import Pin
from micropython import const
from ble_advertising import advertising_payload
from ble_advertising import decode_services
from classe_ecranTFT import EcranTFT

# --- Constantes BLE ---
_IRQ_CENTRAL_CONNECT = const(1)
_IRQ_CENTRAL_DISCONNECT = const(2)
_IRQ_GATTS_INDICATE_DONE = const(20)
_IRQ_SCAN_RESULT = const(5)
_IRQ_SCAN_DONE = const(6)
_IRQ_PERIPHERAL_CONNECT = const(7)
_IRQ_PERIPHERAL_DISCONNECT = const(8)
_IRQ_GATTC_SERVICE_RESULT = const(9)
_IRQ_GATTC_SERVICE_DONE = const(10)
_IRQ_GATTC_CHARACTERISTIC_RESULT = const(11)
_IRQ_GATTC_CHARACTERISTIC_DONE = const(12)
_IRQ_GATTC_NOTIFY = const(18)

# --- UUIDs / Flags ---
DATA_SERVICE_UUID = bluetooth.UUID(0x181A)
DATA_CHAR_UUID = bluetooth.UUID(0x2A6E)
CHAR_PROPS = bluetooth.FLAG_READ | bluetooth.FLAG_NOTIFY | bluetooth.FLAG_INDICATE
DATA_CHAR = (DATA_CHAR_UUID, CHAR_PROPS)
DATA_SERVICE = (DATA_SERVICE_UUID, (DATA_CHAR,))

class BLEDataChat:
    def __init__(self):
        self._ble = bluetooth.BLE()
        self._ble.active(True)
        self._ble.irq(self._irq)

        # TFT
        self._tft = EcranTFT()
        self._log("Init BLE")

        # BLE Service (Serveur / Émetteur)
        ((self._data_handle,),) = self._ble.gatts_register_services((DATA_SERVICE,))
        self._connections = set()
        self._data_to_send = 0x42

        # BLE Advertising
        mac = ubinascii.hexlify(self._ble.config('mac')[1], ':').decode().upper()
        self._name = f"Pico {mac[-5:]}"
        self._payload = advertising_payload(name=self._name, services=[DATA_SERVICE_UUID])
        self._advertise()

        # Variables client (récepteur)
        self._scan_complete = False
        self._peer_addr = None
        self._peer_conn = None
        self._peer_value_handle = None

        # Démarre le scan
        self._ble.gap_scan(2000, 30000, 30000)

    def _log(self, msg):
        print(msg)
        self._tft.tftprint(msg + "\n")

    def _advertise(self, interval_us=500000):
        self._ble.gap_advertise(interval_us, adv_data=self._payload)
        self._log("Publicité BLE active")

    def _irq(self, event, data):
        if event == _IRQ_CENTRAL_CONNECT:
            conn_handle, _, _ = data
            self._connections.add(conn_handle)
            self._log("Central connecté")

        elif event == _IRQ_CENTRAL_DISCONNECT:
            conn_handle, _, _ = data
            self._connections.discard(conn_handle)
            self._log("Central déconnecté")
            self._advertise()

        elif event == _IRQ_SCAN_RESULT:
            addr_type, addr, adv_type, rssi, adv_data = data
            if DATA_SERVICE_UUID in decode_services(adv_data):
                self._log("Appareil trouvé")
                self._peer_addr = bytes(addr)
                self._ble.gap_scan(None)  # stop scan
                self._ble.gap_connect(addr_type, self._peer_addr)

        elif event == _IRQ_PERIPHERAL_CONNECT:
            conn_handle, addr_type, addr = data
            self._peer_conn = conn_handle
            self._log("Connecté à périphérique")
            self._ble.gattc_discover_services(conn_handle)

        elif event == _IRQ_PERIPHERAL_DISCONNECT:
            self._log("Déconnecté du périphérique")
            self._peer_conn = None
            self._ble.gap_scan(2000, 30000, 30000)

        elif event == _IRQ_GATTC_SERVICE_RESULT:
            conn_handle, start_handle, end_handle, uuid = data
            if uuid == DATA_SERVICE_UUID:
                self._start_handle = start_handle
                self._end_handle = end_handle

        elif event == _IRQ_GATTC_SERVICE_DONE:
            if self._peer_conn:
                self._ble.gattc_discover_characteristics(
                    self._peer_conn, self._start_handle, self._end_handle
                )

        elif event == _IRQ_GATTC_CHARACTERISTIC_RESULT:
            conn_handle, def_handle, value_handle, props, uuid = data
            if uuid == DATA_CHAR_UUID:
                self._peer_value_handle = value_handle

        elif event == _IRQ_GATTC_CHARACTERISTIC_DONE:
            if self._peer_conn and self._peer_value_handle:
                self._log("Prêt à recevoir")
                # On active la notification
                self._ble.gattc_write(
                    self._peer_conn,
                    self._peer_value_handle + 1,
                    struct.pack("h", 1),
                    1
                )

        elif event == _IRQ_GATTC_NOTIFY:
            conn_handle, value_handle, notify_data = data
            value = struct.unpack("<h", notify_data)[0]
            self._log(f"Reçu: 0x{value:X}")

    def send_data(self):
        data = struct.pack("<h", self._data_to_send)
        self._ble.gatts_write(self._data_handle, data)
        self._log(f"Émission: 0x{self._data_to_send:X}")

        for conn_handle in self._connections:
            self._ble.gatts_notify(conn_handle, self._data_handle)

# --- Programme principal ---
def main():
    ble_chat = BLEDataChat()
    led = Pin('LED', Pin.OUT)
    counter = 0

    while True:
        if counter % 10 == 0:
            ble_chat.send_data()
        led.toggle()
        time.sleep(1)
        counter += 1

if __name__ == "__main__":
    main()
