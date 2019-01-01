#!/usr/bin/env python3

# ==============================================================================
# Copyright 2015 The Everest Authors. All Rights Reserved.
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

'''
Import the operating system libraries here
'''
import os, sys, subprocess, base64, tempfile, pexpect, platform , shutil
import smtplib, requests
import numpy as np
import math, random
import tempfile, time

'''
Place variables you decide to use later here, such as this neat little
hash variable, so I didn't have to copy paste all these hashs!
'''

hashtag = "##########################"

class OS():
    '''
    This is where things about the OS and the interfacing is done directly. Either through
    External custom libraries I have made, or through the program itself.
    '''
    def scan_protocol():
        sysresult = sys.path
        text_file = open("Information.txt", "w")
        text_file.write("SYSTEM INFORMATION " + '\n')
        text_file.write(hashtag + '\n' "System Variables" + '\n' + hashtag +  '\n' + repr(sysresult) + '\n')
        text_file.write(hashtag + '\n' "System UName" + '\n' + hashtag +  '\n' + repr(platform.uname()) + '\n')
        text_file.write(hashtag + '\n' "System Architecture" + '\n' + hashtag +  '\n' + repr(platform.architecture()) + '\n')
        text_file.write(hashtag + '\n' "System Machine Type" + '\n' + hashtag +  '\n' + repr(platform.machine()) + '\n')
        text_file.write(hashtag + '\n' "System Name" + '\n' + hashtag +  '\n' + repr(platform.node()) + '\n')
        text_file.write(hashtag + '\n' "System Processor" + '\n' + hashtag +  '\n' + repr(platform.processor()) + '\n')
        text_file.write(hashtag + '\n' "System PythonBuild" + '\n' + hashtag +  '\n' + repr(platform.python_build()) + '\n')
        text_file.write(hashtag + '\n' "System Release" + '\n' + hashtag +  '\n' + repr(platform.release()) + '\n')
        text_file.write(hashtag + '\n' "Real System Name" + '\n' + hashtag +  '\n' + repr(platform.system()) + '\n')
        text_file.write(hashtag + '\n' "System Modules" + '\n' + hashtag +  '\n' + repr(sys.modules) + '\n')
        text_file.write(hashtag + '\n' "System Prefix" + '\n' + hashtag +  '\n' + repr(sys.prefix) + '\n')
        #If you're wondering what this last one is, its what your computer uses to convert those random little japanese characters into actual english readable stuff, fun right
        text_file.write(hashtag + '\n' "System Unicode" + '\n' + hashtag +  '\n' + repr(sys.getfilesystemencoding()) + '\n')
        text_file.close()


    def usb_dump():
        '''
        This dumps any/all of the USB's plugged into the computer.
        Works on all types of usb ports, but make sure they work with the
        os before you plug it in. Make sure you don't include SSD's or whitelist
        them!
        '''
        #--
        target_folder = "~/USB Dump"
        excluded = ["/media/klaminite/RESEARCH"]
        #--

    #Get's mounted USB's and other drives.
        def get_mountedlist():
            '''
            Gets the mounted usb/hdd/sdd drives.
            '''
            return [(item.split()[0].replace("├─", "").replace("└─", ""),
                     item[item.find("/"):]) for item in subprocess.check_output(
                    ["/bin/bash", "-c", "lsblk"]).decode("utf-8").split("\n") if "/" in item]

        def identify(disk):
            command = "find /dev/disk -ls | grep /"+disk
            output = subprocess.check_output(["/bin/bash", "-c", command]).decode("utf-8")
            if "usb" in output:
                return True
            else:
                return False

        done = []
        while True:
            mounted = get_mountedlist()
            new_paths = [dev for dev in get_mountedlist() if not dev in done and not dev[1] == "/"]
            valid = [dev for dev in new_paths if (identify(dev[0]), dev[1].split("/")[-1]  in excluded) == (True, False)]
            for item in valid:
                target = target_folder+"/"+item[1].split("/")[-1]
                try:
                    shutil.rmtree(target)
                except FileNotFoundError:
                    pass
                shutil.copytree(item[1], target)
            done = mounted
            time.sleep(4)

        def clone_protocol():
            '''
            Here you can automate a clone script thats found in the protocols folder.
            '''
            subprocess.call("python3 ~/Protocols/Clone_Protocol.py", shell=True)

def email_protocol():
    '''
    This has been depricated. The file entry is no longer listed under protocols,
    but rather is a seperate file in itself, this allows for a more extensive program
    to be built in place of it.
    '''
    subprocess.call("python3 ~/Protocols/Communication/Email.py")

def monitor_protocol():
    #displays current status of the entire system.
    subprocess.call("gnome-system-monitor", shell=True)



def Gesture():
    subprocess.call("python ~/Protocols/Gestures_Protocol.py", shell=True)

def KnightsTemplar():
    #Makes a new code file, technically initiating the said user into the society.
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        pw_length = 4028
        PasswordGen = ""

        for i in range(pw_length):
            next_index = random.randrange(len(alphabet))
            PasswordGen = PasswordGen + alphabet[next_index]

    # replace 1 or 2 characters with a number
        for i in range(random.randrange(1,3)):
            replace_index = random.randrange(len(PasswordGen)//2)
            PasswordGen = PasswordGen[0:replace_index] + str(random.randrange(10)) + PasswordGen[replace_index+1:]

    # replace 1 or 2 letters with an uppercase letter
        for i in range(random.randrange(1,3)):
            replace_index = random.randrange(len(PasswordGen)//2,len(PasswordGen))
            PasswordGen = PasswordGen[0:replace_index] + PasswordGen[replace_index].upper() + PasswordGen[replace_index+1:]

            text_file = open("Password.txt", "w")
            text_file.write("Users Access password, changes weekly. " + '\n')
            text_file.write("4028:" + repr(PasswordGen))
            text_file.close()
