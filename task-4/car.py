# Import necessary modules and classes
import unittest
from car_factory import SpindlerBattery, CarriganTire, OctoprimeTire

class TestCarFactory(unittest.TestCase):

    def test_spindler_battery_upgrade(self):
        # Test the Spindler battery upgrade
        spindler_battery = SpindlerBattery()
        self.assertFalse(spindler_battery.service_required(24))  # Two years
        self.assertTrue(spindler_battery.service_required(36))   # Three years

    def test_carrigan_tire_servicing(self):
        # Test tire servicing criteria for Carrigan tires
        carrigan_tire = CarriganTire()
        carrigan_tire.set_tire_wear([0.1, 0.5, 0.9, 0.3])
        self.assertTrue(carrigan_tire.service_required())

    def test_octoprime_tire_servicing(self):
        # Test tire servicing criteria for Octoprime tires
        octoprime_tire = OctoprimeTire()
        octoprime_tire.set_tire_wear([0.7, 1.0, 0.6, 0.8])
        self.assertTrue(octoprime_tire.service_required())

# Run the tests
if __name__ == '__main__':
    unittest.main()
