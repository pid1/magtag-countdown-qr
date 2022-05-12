import time

import terminalio
from adafruit_display_text import label
from adafruit_display_shapes.rect import Rect
from adafruit_magtag.magtag import MagTag, Graphics

# Make sure we can successfully import our secrets
try:
    from secrets import secrets
except ImportError:
    print("Failed to parse secrets from secrets.py")
    raise

# Instantiate our magtag and graphics and objects
magtag = MagTag()
graphics = Graphics(auto_refresh=False)

# Power savings, before we do anything else
magtag.peripherals.neopixel_disable = True

# Connect to WiFi so we can do NTP later
magtag.network.connect()

# Vars
QR_URL = "<url>"
EVENT = "<event>"
DATE = 0

TIMESTAMP = 0

# Set the display background
background = Rect(0, 0, 296, 128, fill=0xFFFFFF)
graphics.splash.append(background)

def update_display():
    graphics.qrcode(QR_URL,qr_size=4,x=170,y=0)
    magtag.get_local_time()
    now = time.localtime()
    days_until = DATE - now[7]
    main_text = label.Label (
        terminalio.FONT,
        text = f"   {days_until} days until \n{EVENT}",
        color=0xFFFFFF,
        background_color=0x666666,
        padding_top=1,
        padding_bottom=3,
        padding_right=4,
        padding_left=4,
        scale=1,
    )
    main_text.x = 25
    main_text.y = 50
    graphics.splash.append(main_text)
    graphics.display.show(graphics.splash)
    magtag.display.refresh()

update_display()
while True:
    if time.monotonic() - TIMESTAMP > 3600: # Hourly NTP sync
        magtag.get_local_time() # Reach out to adafruit.io for our NTP service
        TIMESTAMP = time.monotonic()
        update_display()
    time.sleep(1800)