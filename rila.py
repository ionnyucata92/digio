from seleniumbase import SB
import time
import requests
import sys
import requests
import os
import random
import subprocess
from dataclasses import dataclass
from typing import List, Optional
import requests
import base64
aga = "aHR0cHM6Ly93d3cudHdpdGNoLnR2L2JydXRhbGxlcw=="
decoded_bytes = base64.b64decode(aga)
url = decoded_bytes.decode("utf-8")
geo_data = requests.get("http://ip-api.com/json/").json()

latitude = geo_data["lat"]
longitude = geo_data["lon"]
timezone_id = geo_data["timezone"]
language_code = geo_data["countryCode"].lower()  # e.g., 'us' -> 'en-US'
with SB(uc=True, test=True,locale=f"{language_code.upper()}") as tsatw:
    tsatw.execute_cdp_cmd(
        "Emulation.setGeolocationOverride",
        {
            "latitude": latitude,
            "longitude": longitude,
            "accuracy": 100
        }
    )
    tsatw.execute_cdp_cmd(
        "Emulation.setTimezoneOverride",
        {"timezoneId": timezone_id}
    )

    tsatw.uc_open_with_reconnect(url, 5)
    tsatw.sleep(14)
    if tsatw.is_element_present("#live-channel-stream-information"):
    
        if tsatw.is_element_present('button:contains("Accept")'):
            tsatw.uc_click('button:contains("Accept")', reconnect_time=4)
        if True:
            tsatw2 = tsatw.get_new_driver(undetectable=True)
            tsatw2.uc_open_with_reconnect(url, 5)
            tsatw2.sleep(10)
            if tsatw2.is_element_present('button:contains("Accept")'):
                tsatw2.uc_click('button:contains("Accept")', reconnect_time=4)
            while tsatw2.is_element_present("#live-channel-stream-information"):
                tsatw2.sleep(120)
            tsatw.quit_extra_driver()
