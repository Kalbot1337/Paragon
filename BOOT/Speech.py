#!/usr/bin/env python3

# ==============================================================================
# Copyright 2015 The Paragon Authors. All Rights Reserved.
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

import random
import os
import string
import pygame
import talkey
def say(rand,n,mixer):
    tts = talkey.Talkey(
        # The order of preference of using a TTS engine for a given language.
        # Note, that networked engines (Google, Mary) is disabled by default, and so is dummy
        # default: ['google', 'mary', 'espeak', 'festival', 'pico', 'flite', 'dummy']
        # This sets eSpeak as the preferred engine, the other engines may still be used
        #  if eSpeak doesn't support a requested language.
        engine_preference=['espeak'],

        # Here you segment the configuration by engine
        # Key is the engine SLUG, in this case ``espeak``
        espeak={
            # Specify the engine options:
            'options': {
                'enabled': True,
            },

            # Specify some default voice options
            'defaults': {
                    'words_per_minute': 135,
            },

            # Here you specify language-specific voice options
            # e.g. for english we prefer the mbrola en1 voice
            'languages': {

                'en': {
                    'voice': 'english-mb-en1',
                    'words_per_minute': 114,
                    'pitch_adjustment': 60
                },
            }
        }
    )
    tts.say(random.choice(rand))
    '''
    This is old programs
    '''
    #The old code, use this if you want a higher quality voice, requires internet however.
    '''
    tts = gTTS(text=random.choice(rand), lang = 'en-au')
    tts.save('ArcVoice.mp3')
    mixer.init()
    mixer.music.load('ArcVoice.mp3')
    mixer.music.play()
    '''
    """
    We need to activate the timer, otherwise
    programs will exit with status 0, meaning they finished, but the files used
    zweren't given enough time to be used.
    """
'''
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(13)
'''

def wifi():
    '''
    Pings google.com to check if you're connected to the internet
    '''
    REMOTE_SERVER = "www.google.com"
    def is_connected():
        try:
            host = socket.gethostbyname(REMOTE_SERVER)
            s = socket.create_connection((host, 80), 2)
            return True
        except:
            pass
        return False
