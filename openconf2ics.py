#!/usr/bin/env python3
import constants

import copy
import dateutil
import requests

json = requests.get(constants.URL).json()
sessions = json["sessions"]
ids = sessions.keys()

ics = requests.post(constants.ICS_URL, data={"mysessions":",".join(ids)})
print(ics.text)
