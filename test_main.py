import unittest
from main import Car

class TestCar(unittest.TestCase):
    def test_car_attributes(self):
        car = Car('Tesla', 'Model S', 2022)
        self.assertEqual(car.make, 'Tesla')
        self.assertEqual(car.model, 'Model S')
        self.assertEqual(car.year, 2022)

    def test_start_engine(self):
        car = Car('Tesla', 'Model S', 2022)
        car.start_engine()
        self.assertTrue(car.engine_on)

    def test_stop_engine(self):
        car = Car('Tesla', 'Model S', 2022)
        car.start_engine()
        car.stop_engine()
        self.assertFalse(car.engine_on)

if __name__ == '__main__':
    unittest.main()
