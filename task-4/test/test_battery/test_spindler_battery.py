import unittest
from datetime import date
from battery.spindler_battery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    def setUp(self):
        # Common setup for both tests
        self.current_date = date.fromisoformat("2020-05-15")

    def test_needs_service_true(self):
        last_service_date = date.fromisoformat("2018-01-25")
        battery = SpindlerBattery(self.current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        last_service_date = date.fromisoformat("2019-01-10")
        battery = SpindlerBattery(self.current_date, last_service_date)
        self.assertFalse(battery.needs_service())

if __name__ == "__main__":
    unittest.main()
