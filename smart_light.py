"""A simple SmartLight class for SIS150 object-oriented programming."""


class SmartLight:
    """Track a light's power state and brightness (0 through 100)."""

    def __init__(self):
        self.is_on = False
        self.brightness = 0

    def turn_on(self):
        """Turn the light on."""
        self.is_on = True

    def turn_off(self):
        """Turn the light off and reset its brightness."""
        self.is_on = False
        self.brightness = 0

    def set_brightness(self, level):
        """Set brightness if it is between 0 and 100, inclusive."""
        if not 0 <= level <= 100:
            raise ValueError("Brightness must be between 0 and 100.")
        self.brightness = level
