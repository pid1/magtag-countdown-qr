# magtag-countdown-qr

Adafruit Magtag countdown display with an associated QR for linking to an event page

![Example](https://github.com/pid1/magtag-countdown-qr/blob/main/example.png?raw=true)

## Dependencies

This assumes that you are running [CircuitPython](https://circuitpython.org/board/adafruit_magtag_2.9_grayscale/)

From the [CircuitPython libraries bundle](https://circuitpython.org/libraries):

* adafruit_bitmap_font
* adafruit_display_shapes
* adafruit_display_text
* adafruit_io
* adafruit_minimiqtt
* adafruit_miniqr
* simpleio

This also requires the [Adafruit CircuitPython MagTag helper library](https://github.com/adafruit/Adafruit_CircuitPython_MagTag).

## Usage

Adjust `QR_URL`, `EVENT`, and `DATE` variables appropriately. The code counts the number of days from today until the target date, so more handling is required for cases where the date is more than a year out, past January 1st, etc. Patches welcome.

Depending on the size of your QR code payload, you may need to slightly adjust the scaling of the QR code to maximize utilization of the screen real estate.
