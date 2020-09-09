# import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
# import webbrowser
import os
from playsound import playsound
from selenium import webdriver
from gtts import gTTS 
from io import BytesIO
import random


chromedriver = './chromedriver' 

dir = os.getcwd()
language = 'en'
mp3_fp = BytesIO()

def speak(audio):  

    myobj = gTTS(text=audio, lang=language, slow=False) 
    myobj.write_to_fp(mp3_fp)
    ur = myobj.get_urls()
    for i in ur:
        playsound(i)
    # myobj.save("welcome.mp3")
    
    # os.system(f"mpg321 welcome.mp3")

def wishMe():
    always = "I am Satyam's assistant Computer, How may I help you Sir??"
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(f"Good Morning!{always}")
    elif hour>=12 and hour<18:
        speak(f"Good Afternoon!{always}")
    else:
        speak(f"Good Evening! {always}")

def takeCommand():

    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 22000
        audio= r.listen(source)

    try:
        print("Recognizing")
        query= r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    
    except Exception as e:
        print(e)

        print("User voice unrecognizable. Try again...")
        return "None"
    return query
    

if __name__ == "__main__":
    wishMe()
    if 1:
        query=takeCommand().lower()
    
        if 'wikipedia' in query:
            speak('Searching Wikipedia.....')
            query= query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            driver = webdriver.Chrome(executable_path=chromedriver)
            driver.get("http:youtube.com")
            # webbrowser.open("http://youtube.com")
        
        elif 'open google' in query:
            driver = webdriver.Chrome(executable_path=chromedriver)
            driver.get("http:google.com")
            # webbrowser.open_new("http://google.co.in")
        
        elif 'play music' in query:
            music_dir='/home/satyam/Music'
            songs=os.listdir(music_dir)

            while(1):
                d = random.choice(songs)
                playsound(f'/home/satyam/Music/{d}')
        
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f'The Time right now is {strTime}')
