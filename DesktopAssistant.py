# first we have to import a library which is deigned for
# speech to text conversion
# Microsoft Speech API (SAPI5) is the technology for voice recognition 
# and synthesis provided by Microsoft.
# pyttsx3 Included TTS engines: sapi5, nsss, espeak
import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import numpy as np
import smtplib
engine = pyttsx3.init("sapi5") 
voices = engine.getProperty("voices")
# print(voices[0].id)
engine.setProperty("voice", voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour<=12 and hour<18:
        speak("Good Afternoon!")
    else :
        speak("Good Evening!")
    speak("I am Jarvis, How can I help you")

def takecommand():
    """
    It takes microphone input from user 
    and returns string of the input.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception:
        # print(Exception)
        print("Please say that again...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    
    speak("Hi Master")
    wishme()
    in_ = True
    while in_ == True:
        query = takecommand().lower()
        # logic for executing tasks as per query
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            speak("opening Youtube...")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("opening google...")
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            speak("opening stackoverflow...")
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            speak("playing music...")
            music_dir = 'F:\\MUsic\\Others'
            songs = os.listdir(music_dir)
            print(songs)
            song = np.random.randint(0, len(songs)-1)
            os.startfile(os.path.join(music_dir, songs[song]))
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"Hello sir, The time is {strTime}")
        elif 'open code' in query:
            file_ = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(file_)
        elif 'email to harsh' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "yourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry master. I am unable to send this email") 
        elif 'bye' in query:
            speak('good bye master...')
            print('good bye master...')
            in_ = False
