import unittest
from datetime import datetime

from battery.NubbinBattery import NubbinBattery
from battery.SpindlerBattery   import SpindlerBattery
from carfactory import carfactory 

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine





class testengine (unittest.TestCase):
    def testenginecapulet (self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        Engine= CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(Engine.engine_should_be_serviced())
    def testenginesternaman (self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        Engine= SternmanEngine(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(Engine.engine_should_be_serviced())



class testbattery (unittest.TestCase):
    def testbatteryN (self):
           
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        Battery = NubbinBattery(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(Battery.needs_service())
    def testbatteryS (self):
           
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        Battery = SpindlerBattery(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(Battery.needs_service())


# if __name__ == '__main__':
#     unittest.main()
