
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

#=====================================================================================================

__main__ = '''
        The Paragon framework made in python. c++, prolog, fortran, and C.

        External Libraries are not mine, cubecorps, or owned representivavely of any individual
        associated with CubeCorps or the Paragon project currently. All respected rights are of the
        copyright owner.

                                        Simulated Artificially Intelligent Companion

                                            -= Author: Klaminite & Blue =-
                                          -= Project Name: The Paragon Project =-

        About:

        Simulates intelligence using external libraries and inside code to parse data,
        graph and predict the modeled equation. On top of the neural networks here, we also have an interface.


'''

#=====================================================================================================

__about__ = '''Simulates intelligence using external libraries and inside code to parse data,
graph and predict the modeled equation. On top of the recurrent neural networks, we have perceptron, svm's, bayesian theorum, and a
more.'''
__version__ = '1.3.2'

'''
Initiliaze the system wide variables
here
'''

comm = MPI.COMM_WORLD
rank = comm.Get_rank()  #Applies computer ranking for the backend servers
null_error = '//NULL//ERROR'

"""
#debug later
class Intelligence():
    '''
    All the machine learning goes on here, scipy classifaction, etc.
    '''
    #variables
    x = 0
    def lingTran(word):
        #=====================
        import textblob, nltk
        #=====================
        '''
        Translate any language to english, or to any other
        language
        '''

    def txtSum():
        #=====================
        import nltk
        from textblob import TextBlob
        #=====================
        trs_message = TextBlob(message)
    def science():
        None

    def sIC():
        '''
        Still Image Recognizer/classifier using the imagenet model,
        trained off of keras, only trains once, and prints form in tuples.
        '''
        #Not for use with the webcam, although that might be a neat idea
        model = ResNet50(weights='imagenet')
        img_path = 'elephant.jpg'
        img = image.load_img(img_path, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        preds = model.predict(x)
        # decode the results into a list of tuples (class, description, probability)
        # (one such list for each sample in the batch)
        print('Predicted:', decode_predictions(preds, top=3)[0])
        # Predicted: [(u'n02504013', u'Indian_elephant', 0.82658225), (u'n01871265', u'tusker', 0.1122357), (u'n02504458', u'African_elephant', 0.061040461)]


    class AngularGyrus():
        '''
        Must call a mathematical function
        '''

        #variables

        x = 0
        def Mach_FFT(x):
            #Compute a fast fourier transform on a seperate computer to ease loads
            x1 = arange(x)
            return fft(x1)

        def Matr_Det(x):
            #Computes the determinate of matrice X
            answer = sp.det(x)
            return answer

        def digitRecon():
            '''
            useful for when your handwriting becomes sloppy
            '''
            # Import the modules
            import cv2
            from sklearn.externals import joblib
            from skimage.feature import hog
            import numpy as np
            # Load the classifier
            clf = joblib.load("digits_cls.pkl")
            # Read the input image
            im = cv2.imread("photo_1.jpg")
            # Convert to grayscale and apply Gaussian filtering
            im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            im_gray = cv2.GaussianBlur(im_gray, (5, 5), 0)
            # Threshold the image
            ret, im_th = cv2.threshold(im_gray, 90, 255, cv2.THRESH_BINARY_INV)
            # Find contours in the image
            ctrs, hier = cv2.findContours(im_th.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            # Get rectangles contains each contour
            rects = [cv2.boundingRect(ctr) for ctr in ctrs]
            # For each rectangular region, calculate HOG features and predict
            # the digit using Linear SVM.
            for rect in rects:
                # Draw the rectangles
                cv2.rectangle(im, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0, 255, 0), 3)
                # Make the rectangular region around the digit
                leng = int(rect[3] * 1.6)
                pt1 = int(rect[1] + rect[3] // 2 - leng // 2)
                pt2 = int(rect[0] + rect[2] // 2 - leng // 2)
                roi = im_th[pt1:pt1+leng, pt2:pt2+leng]
                # Resize the image
                roi = cv2.resize(roi, (28, 28), interpolation=cv2.INTER_AREA)
                roi = cv2.dilate(roi, (3, 3))
                # Calculate the HOG features
                roi_hog_fd = hog(roi, orientations=9, pixels_per_cell=(14, 14), cells_per_block=(1, 1), visualise=False)
                nbr = clf.predict(np.array([roi_hog_fd], 'float64'))
                cv2.putText(im, str(int(nbr[0])), (rect[0], rect[1]),cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 255), 3)
            cv2.imshow("Resulting Image with Rectangular ROIs", im)
            cv2.waitKey()
"""
class spn():
    '''
    This contains all the classes and functions that is utilized by the master node; also used as the "core" of the software.
    '''
    def main():
        #Start by loading all libraries
        sys.path.append('./Paragon/Drivers')
        print("\033[0;31m[System]" + "\033[0;32m | Importing all modules from system;")
        #===============================================================================================
        #import all of the needed files here, note they all are imported via importance.
        try:
            import os, subprocess, signal, pexpect, time, datetime, random, Speech, protocols, pyaudio, pprint, json, nltk, scipy, math, textblob, webbrowser, keras
            from Drivers.Speech import SpeechDriver as sr
            from pygame import mixer
            import yahoo_finance as fc
            from time import strftime
            import requests, pywapi, feedparser
            import tensorflow as tf
            import numpy as np
            from multiprocessing import Process
            from keras.applications.resnet50 import ResNet50
            from keras.preprocessing import image
            from keras.applications.resnet50 import preprocess_input, decode_predictions
            import googlemaps as gmaps
        except ImportError:
            print("It appears as if you do not have all the packages!")
        #===============================================================================================
        '''
        Load all of the files needed for
        basic operation into memory
        '''
        print("\033[0;31m[System]" + "\033[0;32m | Loading files into memory;")
        datafile = json.loads(open('./Paragon/Data/Databases/Data/data.json').read())
        '''
        After this, we can safely start up the system.
        '''
        #Globals
        #sp.init_printing()
        n = 0
        word_to_number_mapping = {}
        #My client access token.
        print("VER: " + __version__)

        #Start other processes within the script.
        #subprocess.call("ipython3 ./Paragon/Protocols/Pitch.py &", shell=True)
        #subprocess.call("ipython3 ./Paragon/Protocols/Pitch.py &", shell=True)
        '''
        If the webcam isn't already prioritized, then it needs to be set manually, prompting the
        user for a password if they aren't dropped to root.
        '''
        #Checks if there is an external camera, if so, it'll use it.
        '''if os.path.isdir("/dev/video1") == False:
            subprocess.call("python ./Paragon/Startups/Startup_Extern_Webcam", shell=True)
            subprocess.call("python ./Paragon/Protocols/vInter.py &", shell=True)
        else:
            subprocess.call("python ./Paragon/Protocols/vInter.py &", shell=True)
            '''
        print(__about__)
        print(__main__)
        print("//STRT//EVS//GO//VER//" + __version__)
        ct = strftime("%I:%M, %p")
        rand = ["Hello" + (datafile["Identity"][0]["nameFirst"]) + ", welcome back. The current time is" + repr(ct)] #go ahead and welcome whatever you set this to.
        Speech.say(rand,n,mixer)
        class start():
            '''
            The main class, other classes might be related to this or not, really
            classes are just used in this program as a case around any other systems or infrastructures.
            '''
            def Interface():
                '''
                The audio version, and the primary version of the interface.
                '''
                doss = os.getcwd()
                i=0
                n=0
                while (i<1):
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        audio = r.adjust_for_ambient_noise(source)
                        n = (n+1)
                        audio = r.listen(source)
                        subprocess.call("sensors", shell=True)
                    '''
                    This uses the driver that is installed on the system
                    '''
                    try:
                        s = (r.recognize_google(audio))
                        print(s)
                        message = (s.lower())
                        # Paragon's main interface.
                        '''
                        Most of where this started was from a rather small github repo, in which I ammased this MONSTER code.
                        '''
                        if ('wikipedia') in message:
                            message = message.replace("wikipedia", "")
                            message = message.replace(" ", "_")
                            message = message.capitalize()
                            proxies = {
                            }
                            headers = {
                                "User-Agent": "Definitions/1.0"
                            }
                            params = {
                                'action':'query',
                                'prop':'extracts',
                                'format':'json',
                                'exintro':1,
                                'explaintext':1,
                                'generator':'search',
                                'gsrseParagonh':message,
                                'gsrlimit':1,
                                'continue':''
                            }
                            r = requests.get('http://en.wikipedia.org/w/api.php',
                                             params=params,
                                             headers=headers,
                                             proxies=proxies)
                            json1 = r.json1()
                            result = list(json1["query"]["pages"].items())[0][1]["extract"]
                            print(result)
                            rand = [(result) + '.']
                            Chrome = ("google-chrome %s")
                            webbrowser.get(Chrome)
                            webbrowser.open('https://en.wikipedia.org/wiki/' + message, new=2, autoraise=True)
                            Speech.say(rand,n,mixer)

                        if ('goodbye') in message:
                            rand = ['Goodbye ' + (datafile["Identity"][0]["pronouns"]), 'Paragon powering off']
                            Speech.say(rand,n,mixer)
                            break
                        if ('evening') in message:
                            rand = ['Good evening ' + (datafile["Identity"][0]["pronouns"])]
                            Speech.say(rand,n,mixer)

                        if ('morning') in message:
                            mTime = time.strftime('%B:%d:%Y')
                            rand = ['Good morning ' + (datafile["Identity"][0]["pronouns"]) + ', I grabbed the news for,' + mTime]
                            Chrome = ("google-chrome %s")
                            Speech.say(rand,n,mixer)
                            webbrowser.get(Chrome)
                            webbrowser.open('https://www.sciencenews.org/topic/math-technology', new=2, autoraise=True)
                            print ('')
                        if message == ('Paragon'):
                            rand = ['Yes Sir?', 'What can I, do for you ' + (datafile["Identity"][0]["pronouns"])]
                            Speech.say(rand,n,mixer)
                        if ('are we connected') in message:
                            REMOTE_SERVER = "www.google.com"
                            Speech.wifi()
                            rand = ['We are connected']
                            Speech.say(rand,n,mixer)
                        if ('.com') in message :
                            rand = ['Opening' + message]
                            Chrome = ("google-chrome %s")
                            Speech.say(rand,n,mixer)
                            webbrowser.get(Chrome).open('http://www.'+message)
                            print ('')
                        if ('.net') in message :
                            rand = ['Opening' + message]
                            Chrome = ("google-chrome %s")
                            Speech.say(rand,n,mixer)
                            webbrowser.get(Chrome).open('http://www.'+message)
                            print ('')
                        if ('.org') in message :
                            rand = ['Opening' + message]
                            Chrome = ("google-chrome %s")
                            Speech.say(rand,n,mixer)
                            webbrowser.get(Chrome).open('http://www.'+ message)
                            print ('')
                        if ('what is the time') in message or ('what time is it') in message or ('can you get me the current time') in message or ('can you tell me the time') in message:
                            lTime = time.strftime('%I:%M')
                            rand = ['the time is,' + lTime + ',sir.']
                            Speech.say(rand,n,mixer)
                        if ('what day is it') in message or ('what is the date') in message or ('date please') in message:
                            tDate = time.strftime('%B:%d:%Y')
                            rand = ['Today is,' + tDate + (datafile["Identity"][0]["pronouns"])]
                            Speech.say(rand,n,mixer)
                        if ('Paragon can you get me the weather') in message or ('can you get the weather') in message or ('Paragon weather please') in message or ('weather please') in message:
                            noaa_result = pywapi.get_weather_from_noaa('KPWT')
                            rand = ["I've fetched the weather for you." + "It is currently" + noaa_result['weather'] + '\n' + 'Current Temperature is: ' + noaa_result['temp_f'] +  'Degrees.'+ '\n' + 'Information grabbed from' + noaa_result['location']]
                            Speech.say(rand,n,mixer)
                        if ('can you get the news') in message or ('get the news please') in message or ('Paragon get the news please') in message:
                            rand = ['Fetching todays headlines, sir, please wait.']
                            Speech.say(rand,n,mixer)
                            time.sleep(5)
                            d = feedparser.parse('http://rss.nytimes.com/services/xml/rss/nyt/Science.xml')
                            rand = [d.feed['title'] + d.feed['description']]
                            Speech.say(rand,n,mixer)
                        if ('night mode') in message:
                            rand = ['Ok, sir, turning on your nightmode settings.']
                            Speech.say(rand,n,mixer)
                            subprocess.call("xbacklight -time 5000 -set 5", shell=True)
                            time.sleep(4)
                            rand = ['Ok sir, night mode is active.']
                            Speech.say(rand,n,mixer)
                        if ('day mode') in message:
                            rand = ['Ok,sir, turning on your daytime settings.']
                            Speech.say(rand,n,mixer)
                            subprocess.call("xbacklight -time 5000 -set 100", shell=True)
                            time.sleep(3)
                            rand = ['Ok sir, daytime mode is now active.']
                            Speech.say(rand,n,mixer)
                        if ('sleep mode') in message:
                            subprocess.call("xbacklight -time 5000 -set 0", shell=True)
                        if ('mute computer') in message or ('mute please') in message or ('mute') in message:
                            subprocess.call("pactl set-sink-mute 2 1", shell=True)
                        if ('unmute computer') in message or ('unmute please') in message or ('unmute') in message:
                            subprocess.call("pactl set-sink-mute 2 0", shell=True)
                        if ('mute all') in message or ('please mute all') in message:
                            subprocess.call("Scripts/muteall.sh", shell=True)
                        if ('Paragon log out') in message or ('log off') in message or ('log out protocol') in message or ('initiate logout protocol') in message:
                            rand = ['Logging out']
                            Speech.say(rand,n,mixer)
                            time.sleep(3)
                            subprocess.call("gnome-session-quit --no-prompt", shell=True)
                        if ('clean up your folder') in message or ("clean up protocol") in message or ('initiate cleanup protocol') in message:
                            rand = ['Ok sir, cleaning up my folders.']
                            Speech.say(rand,n,mixer)
                            subprocess.call("find . -name './Paragon/*.mp3' -delete", shell=True)
                        if ('monitor protocol') in message:
                            rand = ['Monitoring system functions, sir.']
                            Speech.say(rand,n,mixer)
                            time.sleep(1)
                            protocols.monitor_protocol()
                        if ('where is') in message:
                            rand = ['Searching for' + message + ', please wait.']
                            LocSrch_Message = message.replace("where is", "")
                            Chrome = ("google-chrome %s")
                            Speech.say(rand,n,mixer)
                            webbrowser.get(Chrome).open('http://www.'+ message)
                        if ('what is a') in message or ("what is an") in message:
                            if "an" in message:
                                message = message.replace("an ","")
                            if "a" in message:
                                message = message.replace("a ","")
                            spoken_def = Word(x).definitions
                            colist = str(len(spoken_def))
                            rand = ['Sir, there are ' + colist + 'entries, reading the first one: ' + spoken_def]
                            webbrowser.get(Chrome)
                            webbrowser.open("http://www.dictionary.com/browse/" + message)
                        if ('medical') in message:
                            #Searches the entire medical dictionary for a term of definition
                            term = message.replace("medical","")
                            import nltk.corpus
                            medical = open('./Paragon/Data/Databases/Medical_Dictionary.txt')
                            #Converts the text file into an actual corpus, the reason it isn't converted or loaded above,
                            #is because it would consume to many resources if it were constantly loaded.
                            text = medical.read()
                            text1 = text.split()
                            conc_term = nltk.corpus.nltk.Text(text1)
                            med_term = conc_term.concordance(term)
                            rand = [med_term]
                            Speech.say(rand,n,mixer)
                        if ('stock opening') in message:
                            message = message.replace("stock opening", "")
                            #Search the stock database for the given company name
                            df[df['Name'].str.contains(message)]
                            #Further break down the stock table, and find the first hit.
                            TableDi = x.iloc[-1]['Symbol']
                            #Now it's easy sailing.
                            TableConv = stocks.Share(TableDi)
                            rand = ['The opening value of' + message + 'is: ' + TableConv.get_open()]
                            Speech.say(rand,n,mixer)
                        if ('stock price') in message:
                            message = message.replace("stock price", "")
                            #Saearh the stock database for the given company name
                            df[df['Name'].str.contains(message)]
                            #Further break down the stock table, and find the first hit.
                            TableDi = x.iloc[-1]['Symbol']
                            #Now it's easy sailing. x2
                            TableConv = stocks.Share(TableDi)
                            rand = ['The price value of' + message + 'is: ' + TableConv.get_price()]
                            Speech.say(rand,n,mixer)
                        if ('image scan') or ('scan this image') or ('scan image') in message:
                            #Send start command to the still image recognizer class
                            Intelligence.sIC()
                        wrdl1 = ['what city', 'address']
                        if wrdll in message
                            client = googlemaps.Client(key='register for a google key')
                            locaord = googlemaps.geolocation.geolocate(client, consider_ip=True)
                            lat = (locaord['location']['lat']);lng = (locaord['location']['lng'])
                            rgr = gmaps.reverse_geocode((lat, lng))
                            #Handle the index out of range error, since it will be thrown if there is not exactly
                            #ten completed iterations
                            try:
                                #There may be more then 10 results to returned, but the chances
                                #of them containing the correct result past that point is very low, the machine doesn't
                                #need to be concerned with accounting for them at that point.
                                for i in range(10):
                                    locsay = rgr[2]['address _components'][i]['long_name'])
                                    rand = [locsay]
                                    Speech.say(rand,n,mixer)
                            except IndexError:
                                print("")


                        else:
                            print(null_error)
                            #write message to a text file

                            #have the computer read that text file by checking for updated files, either by using time sleep and forcing an updated

                            #print that file readout here

                            #repeat using the else method

                    #exceptions
                    except (KeyboardInterrupt,SystemExit):
                        print("Goodbye, Paragon powering down now")
                        break
                    except sr.UnknownValueError:
                        print("error")
                    except sr.RequestError as e:
                        print("Error, no internet found.")
        if __name__ == '__main__':
            start.Interface()
if __name__ == '__main__':
    spn.main()
