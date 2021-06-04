import speech_recognition #Speech to text chuyển giọng nói thành văn bản Tiếng việt
from gtts import gTTS #Chuyển văn bản thành giọng nói Tiếng Việt
import os #Thực thi câu lệnh trong CMD
from playsound import playsound #Chạy âm thanh mp3
import datetime #Lấy ngày hiện tại
from selenium import webdriver #Mô phỏng thao tác click chuột trên Browser
from time import sleep #Nghỉ
from pynput.keyboard import Key, Controller #Tự động sử dụng bàn phím
from selenium.webdriver.common.keys import Keys
import xlrd
import xlwt
import xlsxwriter

bot_brain= "" #Khởi tạo biến suy nghĩ của robot
bot_ear = speech_recognition.Recognizer() #Khởi tạo biến bot_ear bằng Giọng nói người thật truyền vào chuyển thành văn bản dưới dạng chuỗi



while True:
    file_listened = "Listened/output.xls"
    wb = xlrd.open_workbook(file_listened)
    workbook = xlwt.Workbook()

    sheet = wb.sheet_by_index(0)
    sohang = sheet.nrows
    codeLearnend = sohang
    print('Số lệnh đã học:')
    print(codeLearnend)
    with speech_recognition.Microphone() as mic: #Chờ đợi sử dụng Mic để chuyển thành văn bản
        print("\nSiri: I'm listening")
        audio = bot_ear.record(mic, duration= 5) #Sau khi nghe từ Mic, nhận biến audio là sound
        print("\nSiri: ....")
    try:
        you = bot_ear.recognize_google(audio,language='vi-VN').upper() #truyền biến audio lên API GG, nhận về chuỗi kí tự theo giọng nói
        print(you)
    except:
        you=""
        print("\nSiri: "+you)
    if you == "":
        break
    i=0
    a=1
    while i < codeLearnend:
        codelearn = sheet.cell_value(i, 0)
        pathAnswer = sheet.cell_value(i, 1)
        if codelearn == you:
            playsound(pathAnswer)
            a=0
        i+=1
    if a != 0:
        print('Siri: lệnh này chưa học, bạn muốn máy tính trả lời cho câu này là gì ?')
        with speech_recognition.Microphone() as mic:
            print("\nSiri: Đang nhận lệnh mới")
            audio = bot_ear.record(mic, duration=5)
            print("\nSiri: ....")
        try:
            lenhhoc = bot_ear.recognize_google(audio, language='vi-VN').upper()
            print("\nYou: " + lenhhoc)
        except:
            you = ""
            print("\nSiri: " + you)
            break
        e=0
        sheet1 = workbook.add_sheet("file_listened")
        while e < codeLearnend:
            codelearn = sheet.cell_value(e, 0)
            pathAnswer = sheet.cell_value(e, 1)
            sheet1.write(e, 0, codelearn)
            sheet1.write(e, 1, pathAnswer)
            e+=1
        sheet1.write(codeLearnend, 0, you)
        tts = gTTS(text=lenhhoc, lang='vi')
        pathluu = "Listened/" + str(codeLearnend) + ".mp3"
        tts.save(pathluu)
        sheet1.write(codeLearnend, 1, pathluu)
        workbook.save('Listened/output.xls')
    codeLearnend +=1








