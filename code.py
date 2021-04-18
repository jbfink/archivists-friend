# core modules import
import time, board, busio, secrets
# adafruit add-on modules
import adafruit_sgp30
import adafruit_portalbase
import adafruit_bitmap_font
import adafruit_display_text
from adafruit_magtag.magtag import MagTag

# setup sgp30 sensor
i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)
sgp30.iaq_init()
sgp30.set_iaq_baseline(secrets.secrets['eCO2'], secrets.secrets['TVOC'])

# setup MagTag object:
magtag = MagTag()

print("Hello World!")

