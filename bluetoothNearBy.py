import os
import threading
import time
import subprocess
import constants
from logs.log import log
from bluetooth import *

pwd = constants.attributes['pwd']
mi_band = "iPad de Javier"
mi_band_MAC_2 = "D8:6E:34:F2:37:19"

def near_by():
    global mi_band
    found = False
    nearby_devices = discover_devices(lookup_names=True)


    for name, addr in nearby_devices:
        if addr == mi_band:
            found = True
    return found
    bluetooth_scan_thread = threading.Thread(target=bluetooth_scan)
    bluetooth_scan_thread.start()
    time.sleep(5)
    os.system("killall bluetoothctl")
    time.sleep(1)
    os.system("cat " + pwd + "ImportantFiles/bluetoothctl.txt > " + pwd + "ImportantFiles/test.txt")
    scan_result = subprocess.run(['cat', pwd + 'ImportantFiles/test.txt'], stdout=subprocess.PIPE)
    found = mi_band_MAC in str(scan_result.stdout) or mi_band_MAC_2 in str(scan_result.stdout)
    # HACER UNA FUNCION DE ESTO
    if mi_band_MAC +" RSSI is nil" in str(scan_result.stdout) or mi_band_MAC +" RSSI: -8" in str(
            scan_result.stdout) or mi_band_MAC +" RSSI: -9" in str(scan_result.stdout):
        found = False
    print("Mi band cerca: " + str(found))
    log("BLUETOOTH_NEAR_BY", "NEAR_BY()", "La pulsera con la direccion MAC: " + mi_band_MAC + 'encontrada: '
        + str(found))
    return found


def empty_file():
    os.system("cat /dev/null > " + pwd + "ImportantFiles/bluetoothctl.txt && sleep 1")


def bluetooth_scan():
    empty_file()
    os.system("bluetoothctl scan on >> " + pwd + "ImportantFiles/bluetoothctl.txt")
