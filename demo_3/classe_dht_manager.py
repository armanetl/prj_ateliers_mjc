from machine import Pin
import dht

class DHTManager:
    def __init__(self, pin_num):
        self.sensor = dht.DHT11(Pin(pin_num))
    
    def read(self):
        self.sensor.measure()
        temp = self.sensor.temperature()
        hum = self.sensor.humidity()
        return temp, hum

if __name__ == '__main__':
    dht = DHTManager(22)
    temp, hum = dht.read()
    print("Température:", temp, "°C  |  Humidité:", hum, "%")

