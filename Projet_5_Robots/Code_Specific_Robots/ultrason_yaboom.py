from pico_car_mjc import ultrasonic
import time

class Ultrason:

    def __init__(self, usonic):
        self.ultrasonic = usonic

    def distance_mm(self):
        """
        Get the distance in milimeters without floating point operations.
        """
        mm = self.ultrasonic.Distance_accurate()*10
        return mm

    def distance_cm(self):
        """
        Get the distance in centimeters with floating point operations.
        It returns a float
        """
        cms = self.ultrasonic.Distance_accurate()
        return cms


if __name__ == '__main__':
    print('test classe ultrason')
    ultrasonic = ultrasonic()
    sensor = Ultrason(ultrasonic)
    while True:
        distance = sensor.distance_cm()
        print('Distance:', "{0:2.2f}".format(distance), 'cm')
        time.sleep(1)