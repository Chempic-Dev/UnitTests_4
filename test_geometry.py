import unittest
from geometry import cube_volume, power



class TestGeometry(unittest.TestCase):
    #тесты для cube_volume
    def test_cube_volume_positive(self):
        self.assertEqual(cube_volume(3), 27)
        self.assertEqual(cube_volume(5), 125)

    def test_cube_volume_zero(self):
        self.assertEqual(cube_volume(0), 0)

    def test_cube_volume_negative(self):
        self.assertEqual(cube_volume(-2), "Error, the length of the edge of a cube cannot be <0")
        self.assertEqual(cube_volume(-4), "Error, the length of the edge of a cube cannot be <0")

    #тесты для power
    def test_power_positive(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 2), 25)
        self.assertEqual(power(3, 4), 81)

    def test_power_in_zero(self):
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(0, 0), 1)


    def test_power_zero_base(self):
        self.assertEqual(power(0, 5), 0)

    def test_power_one(self):
        self.assertEqual(power(1, 100), 1)
        self.assertEqual(power(10, 1), 10)
    
    def test_power_negative(self):
        self.assertEqual(power(-2,3), -8)
        self.assertEqual(power(-5, 2), 25)
        self.assertEqual(power(-5, 3), -125)





