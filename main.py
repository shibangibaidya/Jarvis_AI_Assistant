import speech_recognition as sr   # sr is written to simplify the whole name speech_recoginition , we can simply write sr and do our operations here

import webbrowser  # to open webbrowser
import pyttsx3   # speech to text
import musicLibrary  
import requests
import client
import re
from datetime import datetime
from musicLibrary import play_music, get_music_files, play_random_music,stop_music
import os


# pip install pocketsphinx---> we wont use this instead we will be using recognize_google


recoginzer = sr.Recognizer()   # recognizer object
engine=pyttsx3.init()




def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    try:
        response = client.generate_text(command)
        # Extract the answer from the response
        answer = response['candidates'][0]['content']['parts'][0]['text']
        # Remove asterisks and other unwanted characters
        clean_answer = re.sub(r'[*]', '', answer)
        return clean_answer
    except Exception as e:
        return f"An error occurred while asking Gemini: {e}"

def music_command(command, music_files):
    if "start playing music" in command.lower():
        speak("Playing random music.")
        play_random_music(music_files)
    elif "stop playing music" in command.lower():
        speak("Stopping the music.")
        stop_music()
    # else:
    #     song_name = command.lower().split("play ")[1]
    #     song = play_specific_music(command, music_files)
    #     if song:
    #         speak(f"Playing {os.path.basename(song)}")
    #     else:
    #         speak("No matching song found, playing a random song.")
    #         play_random_music(music_files)
   

def processCommand(c):


    
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]  # it will break the command like this: play delicate ["play","delicate"]
        link=musicLibrary.music[song]
        webbrowser.open(link)

    

    elif "news" in c.lower():
        api_key = "{enter your api key here}"
      
        # url = f"https://newsapi.org/v2/top-headlines?country=IN&apiKey={api_key}"
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                articles = data.get('articles', [])
                for article in articles:
                    print(article['title'])
                    speak(article['title'])
            else:
                print(f"Error fetching news: {response.status_code}")
        except Exception as e:
            print(f"An error occurred: {e}")

    elif "time" in c.lower():
         current_time = datetime.now().strftime("%I:%M %p")
         print(f"The time is {current_time}")
         speak(f"The time is {current_time}")  

    elif "date" in c.lower():
        current_date=datetime.today()
        formatted_date = current_date.strftime("%A, %B %d, %Y")
        print(f"The date is {formatted_date}")
        speak(f"The date is {formatted_date}")

    elif "start playing music" in c.lower():
        music_command(c.lower(), music_files)
        # speak(c)
        print(c)

    elif "stop playing music" in c.lower():
        music_command(c.lower(), music_files)
        # speak(c)
        # print(c) 

    elif "quit" in c.lower():
        exit()
        # else:
        # #    
        # #     # question="what is the capital of india?"
        # #     # response=client.generate_text(question)
        # #     # speak(response)
        #     question = "What is the capital of France?"
        #     try:
        #         response = client.generate_text(question)
        #         print(response)
        #         speak(response)
        #     except Exception as e:
        #         print(f"An error occurred while asking Gemini: {e}")

    
    elif "hello" in c.lower():
        
        speak("Hey Shibangi ! How can I help You Today?")
        print("Hey Shibangi ! How can I help You Today?")

    else:
         # let Gemini handle the request
        output=aiProcess(command)
        print(output)
        speak(output)



        

if __name__=="__main__":
    speak("Initializing Jarvis......")

    music_directory = "C:/Users/shiba/Music"
    music_files = get_music_files(music_directory)

    while True:
     # Listen for the wake word "Jarvis"

    
 # obtain audio from the microphone
        r = sr.Recognizer()

        print("recognizing...")
        
    # recognize speech using google
        try:
           
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source)
                # audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word= r.recognize_google(audio)


            if(word.lower()=="jarvis"):
                speak("Yeah !")
            


            #listen for command
            with sr.Microphone() as source:
                print("Jarvis active....")
                r.pause_threshold=1
                audio = r.listen(source)
                command=r.recognize_google(audio,language="en-in")

                # processCommand(command)
                processCommand(command)
                music_command(command,music_files)
                
                
       
        except Exception as e:
            print("Error; {0}".format(e))



          
