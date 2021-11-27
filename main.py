# main.py -- put your code here!
import network, time
from pyb import LED
from pyb import Timer

# network setup
wl = network.WLAN()

# timer setup
tim = pyb.Timer(4, freq=2)  # create a timer object using timer 4, trigger at 2Hz

# LED setup
red_led = LED(1)
red_led.on() # initialize red to on
grn_led = LED(2)

def check_wifi_connection():
  if wl.isconnected():
    red_led.off()
    grn_led.on()
  else:
    grn_led.off()
    red_led.on()


# timer callback setup
tim.callback(lambda t: check_wifi_connection())

wl.active(1)            # bring up the interface
wl.config('mac')        # get the MAC address
wl.config(antenna=0)    # select antenna, 0=chip, 1=external
wl.scan()               # scan for access points, returning a list
# connect to an access point
# wl.connect('ssid', 'passwd') // do this from the console when logged in for now
