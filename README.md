# SIS150 SmartLight Class

An introductory Python object-oriented programming project demonstrating classes, methods, conditionals, and unit testing.

## Project purpose

The `SmartLight` class models a light with an on/off state and a brightness value. It is a small, reusable program developed for SIS150 coursework.

## What it demonstrates

- **Object-oriented programming:** The `SmartLight` class creates light objects with their own state.
- **Methods:** `turn_on()`, `turn_off()`, and `set_brightness()` change the state of the light.
- **Conditionals and validation:** Brightness must be between 0 and 100; invalid values raise a `ValueError`.
- **Modular code:** Class definition, example program, and tests are separate files.
- **Unit testing:** Four tests check power controls, brightness, and invalid input.

## Files

| File | Purpose |
| --- | --- |
| `smart_light.py` | Defines the `SmartLight` class. |
| `main.py` | Demonstrates how to use the class. |
| `test_smart_light.py` | Runs four unit tests with Python's built-in `unittest` module. |

## Run the example

From the project folder, enter:

```bash
python main.py
```

Expected output:

```text
Light is on: True
Brightness: 75
Light is on: False
Brightness: 0
```

## Run the unit tests

```bash
python -m unittest discover -v
```

Expected result: four tests run and all pass (`OK`).

## Future improvements

Possible extensions include multiple light objects, scheduled activation, and saving light settings to a file. These are **future ideas**, not features in this version.
