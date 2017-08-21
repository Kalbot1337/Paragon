#!/usr/bin/env python
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

import os
import sys
import platform
import time
import numpy as np
import math
import random
import requests
import tempfile
import base64
import subprocess





if len(sys.argv) != 2:
    print('usage: ' + sys.argv[0] + ' [country name | country code]')
    exit(1)
country = sys.argv[1]

if len(country) == 2:
    i = 6 # short name for country
elif len(country) > 2:
    i = 5 # long name for country
else:
    print('Country is too short!')
    exit(1)

try:
    vpn_data = requests.get('http://www.vpngate.net/api/iphone/').text.replace('\r','')
    servers = [line.split(',') for line in vpn_data.split('\n')]
    labels = servers[1]
    labels[0] = labels[0][1:]
    servers = [s for s in servers[2:] if len(s) > 1]
except:
    print('Cannot get VPN servers data')
    exit(1)

desired = [s for s in servers if country.lower() in s[i].lower()]
found = len(desired)
print('Found ' + str(found) + ' servers for the country:[ ' + country + ']')
if found == 0:
    exit(1)

supported = [s for s in desired if len(s[-1]) > 0]
print(str(len(supported)) + ' of these servers support OpenVPN')
# We pick the best servers by score
winner = sorted(supported, key=lambda s: s[2], reverse=True)[0]

print("\n== Best server ==")
pairs = list(zip(labels, winner))[:-1]
for (l, d) in pairs[:4]:
    print(l + ': ' + d)

print(pairs[4][0] + ': ' + str(float(pairs[4][1]) / 10**6) + ' MBps')
print("Country: " + pairs[5][1])

print("\nLaunching VPN...")
_, path = tempfile.mkstemp()



x = subprocess.Popen(['sudo', 'openvpn', '--config', path])

try:
    while True:
        time.sleep(600)
# termination with Ctrl+C
except:
    try:
        x.kill()
    except:
        pass
    while x.poll() != 0:
        time.sleep(1)
    print('\nVStealth mode deactivated')
