# core modules import
import time, board, busio, wifi, ipaddress, ssl, socketpool, terminalio, displayio, rtc
from secrets import secrets
# adafruit add-on modules
import adafruit_requests
import adafruit_sgp30
import adafruit_portalbase
import adafruit_bitmap_font
import adafruit_display_text
from adafruit_datetime import datetime, date, timezone
from adafruit_magtag.magtag import MagTag

# No zfill on circuitpython!!!
def zeroize(number):
    if number < 10:
        return "0" + str(number)
    else:
        return str(number)

def returntime():
    return zeroize(time.localtime()[3]) + ":" + zeroize(time.localtime()[4])


# we get the time from adafruit's server, as apparently NTP is too heavy
r = rtc.RTC()
aio_username = secrets["aio_username"]
aio_key = secrets["aio_key"]
location = secrets.get("timezone", None)
# EST offset in seconds. This works, but I hate how crude it is. :/
time_offset = -14400

TIME_URL = "https://io.adafruit.com/api/v2/%s/integrations/time/strftime?x-aio-key=%s" % (aio_username, aio_key)
# reponse.text.split(" ")[0] is date, reponse.text.split(" ")[1] is time. 
#TIME_URL += "&fmt=%25Y-%25m-%25d+%25H%3A%25M+%25j+%25u+%25z+%25Z"
# below returns time in Unix seconds
TIME_URL += "&fmt=%25s"

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
r.datetime = time.localtime(int(response.text) + time_offset)
print("-" * 40)

#magtag.set_text("Hello!")
#magtag.set_text(time_list[0])
#magtag.set_text(time_list[1])
#print(returntime())
while True:
    # only change the display if seconds are 0, then sleep 5s to debounce
    # (otherwise display refreshes a second time, needlessly.
    if datetime.now().second == 0:
        magtag.set_text(sgp30.TVOC)
        time.sleep(5)
        
