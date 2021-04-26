The Archivist's Friend
----------------------

This is an [Adafruit](https://adafruit.com) [MagTag](https://www.adafruit.com/magtag) and [SGP30](https://www.adafruit.com/product/3709) based device designed to detect [vinegar syndrome](https://grkblog.archives.qld.gov.au/2020/11/09/a-stinker-of-a-problem-film-and-vinegar-syndrome/) decay on cellulite film in archives, although the SGP30 doesn't distinguish between vinegar sydrome and other volatile compounds. It is designed to be self-contained -- attached close to wherever the detection is needed, but connected through the MagTag's [ESP32-S2](https://www.espressif.com/en/products/socs/esp32-s2) processor to WiFi, and using [MQTT](https://en.wikipedia.org/wiki/MQTT) to alert people in case it detects a hazardous level of vinegar. It will also display the last x vinegar readings on the eInk display.

Given that the Archivists's Friend is intended to be a device that functions off a battery for a long time before needing recharging, it won't be sampling all day, but something like once a day (probably taking multiple samples over a period of minutes so as to not get a false positive or negative from one reading), writing the level to the screen. Since it's eInk, the screen will remain visible even without power.


TODOS:

1) ~~set up libraries~~
2) Set up screen frame
3) Set up periodic SGP30 sampling of VOC
4) Display VOC on screen
4a) have something like a graph of VOC samples over time on one side and
    a numeric reading of last VOC on the other.
5) Set up network
6) Set up MQTT
  
