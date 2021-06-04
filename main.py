from tkinter import *
import tkinter
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from pynput.keyboard import Key, Controller
from time import sleep
from datetime import date, datetime
import speech_recognition
import pyttsx3

option = Options()
keyboard = Controller()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
})

troly_nghe = speech_recognition.Recognizer()
troly = pyttsx3.init()
troly_noi = ""

while True:
    with speech_recognition.Microphone() as mic:
        print("Troly: I'm Listening")
        audio = troly_nghe.listen(mic)
    print("Trợ Lý: ....")

    try:
        you = troly_nghe.recognize_google(audio)
    except:
        you = ""

    print("you: " + you)

    if you == "":
        troly_noi = "Can You Speak Again !!"
    elif "hello" in you:
        troly_noi = "Hello Huy"
    elif "open Facebook" in you:
        browser = webdriver.Chrome(executable_path="chromedriver.exe")
        browser.get("https://www.facebook.com/profile.php?id=100006131910859")
    elif "open YouTube" in you:
        browser = webdriver.Chrome(executable_path="chromedriver.exe")
        browser.get("https://www.youtube.com")
        troly_noi = "What do you want to play ?"
    elif "today" in you:
        today = date.today()
        troly_noi = today.strftime("%B %d, %Y")

    elif "bye" in you:
        troly_noi = " Bye Huy"
        troly.say(troly_noi)
        troly.runAndWait()

        break
    else:
        troly_noi = "Can You Speak Again !!"

    print("Trợ Lý : " + troly_noi)

    troly.say(troly_noi)
    troly.runAndWait()



# window = Tk()
# window.title("Assistant")
# window.geometry("250x100")
#
# lblUser = Label(window, text="Alexa Assistant", fg="black", font=('Roboto', 12))
# lblUser.grid(column=0, row=0)
#
# window.mainloop()