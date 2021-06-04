import pyttsx3
from datetime import date, datetime
import speech_recognition

from selenium import webdriver
from time import sleep
from pynput.keyboard import Key, Controller

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

	if you == "" :
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



	elif you == "video 1" in you:
			browser.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-item-renderer[1]/div/ytd-rich-grid-media/div[1]/ytd-thumbnail/a').click()
	elif you == "video one" in you:
			browser.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-item-renderer[1]/div').click()
	elif you == "video two" in you:
			browser.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[5]/ytd-rich-item-renderer[2]/div').click()
	elif you == "video 2" in you:
			browser.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[5]/ytd-rich-item-renderer[2]/div').click()
	elif you == "today" or  you =="Today"  in you:
		today = date.today()
		troly_noi = today.strftime("%B %d, %Y")
	elif you == "login facebook" or you == "login Facebook" in you:
		browser = webdriver.Chrome(executable_path="chromedriver.exe")
		browser.get("https://www.facebook.com")
		sleep(2)
		browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input')
		browser.send_keys("thao9x_1999@yahoo.com.vn")
		browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/input')
		browser.send_keys("Lonelistar30121998")
		browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()

	
	elif "bye" in you :
		troly_noi = " Bye Huy"
		troly.say(troly_noi)
		troly.runAndWait()
		break
	else: 
		troly_noi = "Can You Speak Again !!"

	print("Trợ Lý : " +troly_noi)

	troly.say(troly_noi)
	troly.runAndWait()