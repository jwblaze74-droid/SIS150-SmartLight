"""Unit tests for SmartLight."""

import unittest

from smart_light import SmartLight


class TestSmartLight(unittest.TestCase):
    def setUp(self):
        self.light = SmartLight()

    def test_turn_on(self):
        self.light.turn_on()
        self.assertTrue(self.light.is_on)

    def test_turn_off(self):
        self.light.turn_on()
        self.light.set_brightness(75)
        self.light.turn_off()
        self.assertFalse(self.light.is_on)
        self.assertEqual(self.light.brightness, 0)

    def test_set_brightness(self):
        self.light.set_brightness(75)
        self.assertEqual(self.light.brightness, 75)

    def test_invalid_brightness(self):
        with self.assertRaises(ValueError):
            self.light.set_brightness(150)


if __name__ == "__main__":
    unittest.main()
