# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 01:22:55 2022

@author: fffmm
"""

import speech_recognition as sr
import pyttsx3    # text2speech
#install all the below mentioned modules
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys
#PyAudio
#PyWhatKit
#PyJokes
#Wikipedia
#OpenweatherApi
listener = sr.Recognizer()

engine= pyttsx3.init()   # engine defined
voices=engine.getProperty("voices")
engine.setProperty('voice',voices[1].id)

def engine_talk(text):
    engine.say(text)
    engine.runAndWait()
    

def user_commands():
    try:
        with sr.Microphone() as source:
            print('Start Speaking!!')
            voice= listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if "alexa" in command:
                command=command.replace('alexa','')
                print(command)
    except:
        pass
    return command
    
def run_alexa():
    command=user_commands()
    if 'play' in command:
        song=command.replace('play','')
        #print('New command is'+command)
        #print('The bot is telling us: playing'+command)
        engine_talk('Playing'+song)
        pywhatkit.playonyt(song)
        
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        engine_talk('The current time is'+time)
        

    elif 'who is' in command:
        name = command.replace('who is' , '')
        info =  wikipedia.summary(name, 1)
        print(info)
        engine_talk(info)
    elif 'joke' in command:
        engine_talk(pyjokes.get_joke())

    elif 'stop' in command:
        sys.exit()
    else:
        engine_talk('I could not hear you properly')
        
run_alexa()