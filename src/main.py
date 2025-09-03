# -*- coding: utf-8 -*-
# =============================================================================
# Project       : pokeTheWebpage
# Module name   : -
# File name     : main.py
# File type     : Python script (Python 3)
# Purpose       : 
# Author        : QuBi (nitrogenium@outlook.fr)
# Creation date : Wednesday, 03 September 2025
# -----------------------------------------------------------------------------
# Best viewed with space indentation (2 spaces)
# =============================================================================

# =============================================================================
# EXTERNALS
# =============================================================================
# Project specific constants
# -> None.

# Standard libraries
import requests                 # To retrieve the webpage
import hashlib                  # To evaluate the hash
import time
from datetime import datetime
from plyer import notification



# =============================================================================
# CONSTANTS
# =============================================================================
URL = "https://www.parisversailles.com/inscription_bourse.php"
POLLING_INTERVAL_SEC = 5



def getPageHash() :
  try :
    response = requests.get(URL, timeout = 10)
    response.raise_for_status()
    return hashlib.sha256(response.text.encode("utf-8")).hexdigest()
  except Exception as e:
    print(f"Error fetching page: {e}")
    return None



def notifyChange() :
  notification.notify(
    title="Webpage Changed!",
    message=f"The page at {URL} has been updated.",
    timeout=5
  )



def main() :
  lastHash = getPageHash()
  
  if lastHash is None :
    print("[ERROR] The webpage could not be fetched :(")
    return

  print("[INFO] Monitoring started... Press Ctrl+C to stop.")

  # Polling loop
  while True :
    time.sleep(POLLING_INTERVAL_SEC)
    currHash = getPageHash()
    if (currHash and (currHash != lastHash)) :
      print("[INFO] A change occured!")
      notify_change()
      lastHash = currHash
    else :
      now = datetime.now()
      print(f"- last check at {now.strftime("%H:%M:%S")} - No change.")



# =============================================================================
# ENTRY POINT
# =============================================================================
if (__name__ == "__main__") :
  main()
