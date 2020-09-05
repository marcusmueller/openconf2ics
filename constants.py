URL = "https://www.openconf.org/GRCon20/mobile/data.php"
ICS_URL = "https://www.openconf.org/GRCon20/modules/request.php?module=oc_program&action=myprogram-ics.php"
calendar_default = {}
calendar_stub = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//hacksw/handcal//NONSGML v1.0//EN
END:VCALENDAR
"""

event_default = {
    "timezone": "America/New York",
    "description": "",
    "email": "grcon@gnuradio.org"
}
event_stub = """BEGIN:VEVENT
UID:{uid}
DTSTAMP:{timestamp}
ORGANIZER;CN={session_chair}:MAILTO:{email}
DTSTART:TZID={timezone}:{start}
DTEND:TZID={timezone}:{end}
GEO:{room}
SUMMARY:{title}
DESCRIPTION:{info}
END:VEVENT
"""

markdown_default = {
    "title": "GRCon'20 Schedule",
    "author": "GRCon'20 Program Committee",
    "content": ""
}
markdown_stub = """---
title: "{title}"
author: "GRCon committee"
---
{content}
"""
