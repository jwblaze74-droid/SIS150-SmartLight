"""Demonstrate a SmartLight object."""

from smart_light import SmartLight


def main():
    living_room_light = SmartLight()
    living_room_light.turn_on()
    living_room_light.set_brightness(75)

    print(f"Light is on: {living_room_light.is_on}")
    print(f"Brightness: {living_room_light.brightness}")

    living_room_light.turn_off()
    print(f"Light is on: {living_room_light.is_on}")
    print(f"Brightness: {living_room_light.brightness}")


if __name__ == "__main__":
    main()
