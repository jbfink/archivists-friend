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
# I believe the correct thing to do here is figure out how to change this
# line so that it *just* returns the time, and possibly another (DATE_URL?)
# one for the date, if we are looking to isolate time and/or date in a single
# text variable. Either that, or figure out how to regex (ha) the returned text
# or just split it on spaces. Many ways to gut this fish.
#  e.g. parse the list yielded by reponse.text.split(" ") --
# reponse.text.split(" ")[0] is date, reponse.text.split(" ")[1] is time. 
TIME_URL += "&fmt=%25Y-%25m-%25d+%25H%3A%25M+%25j+%25u+%25z+%25Z"

# setup MagTag object
magtag = MagTag()
# setup text display
magtag.add_text(
    text_font=terminalio.FONT,
    text_position=(140, 55),
    text_scale=5,
    text_anchor_point=(0.5, 0.5),
)

# setup sgp30 sensor
i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)
sgp30.iaq_init()
sgp30.set_iaq_baseline(secrets['eCO2'], secrets['TVOC'])

# comment this out if you don't need the network -- establishing the connection
# is slightly time-intensive.
try:
    magtag.network.connect()
except:
    print("Can't connect to access point!")
pool = socketpool.SocketPool(wifi.radio)

print("Hello World!")
requests = adafruit_requests.Session(pool, ssl.create_default_context())
print("Fetching time from", TIME_URL)
response = requests.get(TIME_URL)
time_list = response.text.split(" ")
print("-" * 40)
print(response.text)
print(response)
print("-" * 40)

#magtag.set_text("Hello!")
#magtag.set_text(time_list[0])
magtag.set_text(time_list[1])
