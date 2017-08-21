#!/usr/bin/env python3
# ==============================================================================
# Copyright 2015 The ParAI Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import schedule
import time
import pywapi
import psutil

def job():
    ACCOUNT_SID = ''
    AUTH_TOKEN = ''
    myNumber = ''
    twilioNumber = ''
    noaa_result = pywapi.get_weather_from_noaa('KPWT')

    from twilio.rest import TwilioRestClient
    import feedparser
    import json
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    f = feedparser.parse('http://www.technewsworld.com/perl/syndication/rssfull.pl')

    newsload = json.loads(f)
    client.messages.create(
            to = myNumber,
            from_ = twilioNumber,
            body = "Good morning sir, I've went ahead and fetched you todays weather report\n" + "\n" + "Current Tech News: \n" + "\n" + repr(f.entries[0].summary_detail['value']) + "\n======================" + "\n""Current Weather\n " + "Weather is currently: " + noaa_result['weather'] + "\n" + "Temperature:" + noaa_result['temp_f'] +
                "F" + "\n" + noaa_result['wind_string']
        )

'''def SysStats():
    ACCOUNT_SID = 'ACab1a974aef5316111c156f0462569fae'
    AUTH_TOKEN = 'acee77533268ab784bd5978082649890'
    myNumber = '+13605359098'
    twilioNumber = '+13603299244'


    from twilio.rest import TwilioRestClient

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

    client.messages.create(
            to = myNumber,
            from_ = twilioNumber,
            body = "System Statistics" + "\n" + "RAM" + "\n" + "Percentage: " + str(round(psutil.virtual_memory().percent)) + "%") + "\n" + "Used: " + repr((psutil.virtual_memory().used) + "bytes\n" + "Total Hard Memorry\n" + repr(psutil.disk_usage())
    )

'''

schedule.every().day.at("06:30").do(job)
'''schedule.every().hour.do(SysStats)
'''

while 1:
    schedule.run_pending()
    time.sleep(1)
