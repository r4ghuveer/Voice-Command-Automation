import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import pywhatkit as pwt
import smtplib
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pickle
import random
from pywinauto import application
import pyautogui as B
import pywhatkit as kit
i=[]
engine = pyttsx3.init('sapi5')
engine.setProperty("volume", 1)
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)      
        return "None"
    return query


def Activation(ac):
    if ac==3:
            speak(" Activation code required! ")
            print(" Please give activation code ")
    else :
        print(" Please give activation code ")
    ac=ac-1
    query = takeCommand().lower()
    if '14211' in query:
        if len(query)==5:
            from win10toast import ToastNotifier
            n = ToastNotifier()
            n.show_toast("CODEX", "Tracy Is Now Activated", duration = 3)
            speak("Access granted!")
            pass
    else:
        print("Access Denied")
        if (ac!=0):
            speak("Access Denied!"+str(ac)+"tries left")
        else:
            speak("No tries remaining!")
        if (ac!=0):
            Activation(ac)
        else:
            speak("I am Shutting down CODEX")
            quit()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")   

    else:
        speak("Good Evening sir!")  
    speak("I am Tracy, your personal voice assistant, Please tell me how may I help you")

def button():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    button=driver.find_element_by_class_name('J-Ke n0')
    button.click()
    time.sleep(10)


def Gmail():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://mail.google.com")
    time.sleep(2) # Let the user actually see something!
    search_box = driver.find_element_by_id('identifierId')
    search_box.send_keys('raghuveer.2020@vitbhopal.ac.in')
    button=driver.find_element_by_class_name('VfPpkd-vQzf8d')
    button.click()
    time.sleep(2)
    search_box = driver.find_element_by_name('password')
    f = open('C:\\Users\\HP\\Desktop\\readme.txt','r')
    P= f.read()
    time.sleep(5)
    search_box.send_keys(P)  
    button=driver.find_element_by_class_name('VfPpkd-vQzf8d')
    button.click()
    time.sleep(10) # Let the user actually see something!
    
    


'''def sendEmail(to, content):

    f = open('C:\\Users\\HP\\Desktop\\readme.txt','r')
    P= f.read()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('raghuveerofficial08@gmail.com', P)
    server.sendmail('raghuveerofficial08@gmail.com', to, content)
    server.close()'''

if __name__ == "__main__":
    Activation(3)  
    wishMe()
    while True:      
        
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'register name' in query:
            speak("Sir please say your name")
            i=takeCommand().lower()
            name=[i]
            pickle.dump(name,open("name.dat","wb"))
            speak("Name registered")

        elif 'youtube' in query:
            query=query.replace('youtube','')
            kit.playonyt(query)


        elif 'what is my name' in query:

            name=pickle.load(open("name.dat","rb"))
            speak(f'How can i forget your name {name}')
        
        elif 'recent' in query:
            speak ("Opening the recent tabs that you browsed")
            B.hotkey('ctrl','shift','t')
           
        
        elif 'note' in query:
            speak("What should I note down for you sir!")
            a=application.Application()
            a.start("Notepad.exe")
            i=takeCommand()
            a.Notepad.Edit.type_keys(i,with_spaces=True)
            speak("By what name should I save it?")
            r=takeCommand()
            a.Notepad.menu_select("File->SaveAs")
            a.SaveAs.Edit.set_edit_text(r+".txt")
            a.SaveAs.Save.click(double=True)
            B.hotkey('alt','f4')
            speak ("File successfully saved as"+r)
            

        elif 'screenshot' in query:
            speak("Crop the part which you want as screenshot") 

            B.hotkey('win','shift','s')
            
 
        

        elif 'open google'in query:
            os.startfile('C:/Program Files/Google/Chrome/Application/chrome.exe')
            speak("Opening Google")

        elif 'whatsapp' in query:
            D={"devansh":'+917898912818',"sanskar":'+917023192504',"gaurav":'+917073022350'}
            speak("To whom should I send message?")
            print(list(D.keys()))
            take=takeCommand().lower()
            R=[take]
            pickle.dump(R,open("name.dat","wb"))
            phone=pickle.load(open("name.dat","rb"))
            phone_=phone[0]
            speak("What should I say?")
            take2=takeCommand().lower()
            S=[take2]
            pickle.dump(S,open("msg.dat","wb"))
            msg=pickle.load(open("msg.dat","rb"))
            msg_=msg[0]
            print(D[phone_])
            print(msg_)
            speak("At which hour")
            h=takeCommand()
            h=int(h)
            speak("minute?")
            m=takeCommand()
            m=int(m)
            pwt.sendwhatmsg(D[phone_],msg_,h,m)

        elif 'play music' in query:
            speak("Playing your favourite music")
            music_dir = 'G:\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            i=random.randint(0,5)  
            os.startfile(os.path.join(music_dir, songs[i]))
    
        elif 'next' in query:
            music_dir = 'G:\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            i=random.randint(0,5)  
            os.startfile(os.path.join(music_dir, songs[i]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'check gmail' in query:
            speak("Just a moment sir, Iam working on it.")
            Gmail()


        elif 'quit' in query:
            speak("Quitting Sir")
            exit()

        """elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = str(input(" Enter email of the receiver : - "))    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)"""
    
    
     
   
