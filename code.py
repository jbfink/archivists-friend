# core modules import
import time, board, busio, wifi, ipaddress, ssl, socketpool, terminalio, displayio
from secrets import secrets
# adafruit add-on modules
import adafruit_requests
import adafruit_sgp30
import adafruit_portalbase
import adafruit_bitmap_font
import adafruit_display_text
from adafruit_magtag.magtag import MagTag

# we get the time from adafruit's server, as apparently NTP is too heavy
aio_username = secrets["aio_username"]
aio_key = secrets["aio_key"]
location = secrets.get("timezone", None)
TIME_URL = "https://io.adafruit.com/api/v2/%s/integrations/time/strftime?x-aio-key=%s" % (aio_username, aio_key)
TIME_URL += "&fmt=%25Y-%25m-%25d+%25H%3A%25M%3A%25S.%25L+%25j+%25u+%25z+%25Z"

# setup sgp30 sensor
i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)
sgp30.iaq_init()
sgp30.set_iaq_baseline(secrets['eCO2'], secrets['TVOC'])

# setup MagTag object:
magtag = MagTag()
# since network connections take time, this is commented out until I actually
# need the network.
try:
    magtag.network.connect()
except:
    print("Can't connect to access point!")


print("Hello World!")
requests = adafruit_requests.Session(pool, ssl.create_default_context())
print("Fetching time from", TIME_URL)
response = requests.get(TIME_URL)
print("-" * 40)
print(response.text)
print("-" * 40)
