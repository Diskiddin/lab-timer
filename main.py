
#Need to install pyaudio
#brew install portaudio
#pip install pyaudio

import time

import speech_recognition as sr

times = []

now = time.time()
go = True

# called from recognizer background
def callback(recognizer, audio):
    #Some kind of audio data recieved
    print("voice")
    temp = time.time()
    try:
        #Using google with default api key
        word = recognizer.recognize_google(audio)
        print(word)
        if(word == 'time'):
            times.append(temp - now)
        elif(word == 'stop'):
            print(times)
            go = False
            stop(wait_for_stop=False)
    except sr.UnknownValueError:
        print("unrecognizable")
    except sr.RequestError as e:
        print("Problem with Google; {0}".format(e))



#Use microfphone as audio source
r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source)

print("begin")

stop = r.listen_in_background(m, callback)

while(go): time.sleep(0.01)
#A function to stop listening



#for _ in range(50): time.sleep(0.1)

#Example to stop listening
#stop_listening(wait_for_stop=False)
