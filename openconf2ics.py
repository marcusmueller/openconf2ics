#!/usr/bin/env python3
#  SPDX-License-Identifier: GPL-3.0-or-later
import constants

import requests

json = requests.get(constants.URL).json()
sessions = json["sessions"]
ids = sessions.keys()

ics = requests.post(constants.ICS_URL, data={"mysessions":",".join(ids)})
print(ics.text)
