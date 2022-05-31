import os
import threading
import time
import subprocess
import constants
from logs.log import log
from bluetooth import *

pwd = constants.attributes['pwd']
mi_band = "MiBand"
mi_band_MAC_2 = "D8:6E:34:F2:37:19"

def near_by():
    global mi_band
    found = False
    nearby_devices = discover_devices(lookup_names=True)


    for name, addr in nearby_devices:
        if addr == mi_band:
            found = True
    return found
   


