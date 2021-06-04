
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

keyboard = Controller() #Khởi tạo bàn phím ảo
bot_brain= "" #Khởi tạo biến suy nghĩ của robot
bot_ear = speech_recognition.Recognizer() #Khởi tạo biến bot_ear bằng Giọng nói người thật truyền vào chuyển thành văn bản dưới dạng chuỗi
file_location = "output.xls"
wb = xlrd.open_workbook(file_location)
sheet1 = wb.sheet_by_index(0)
hang = sheet1.nrows
cot = sheet1.ncols
print('số hàng trong Excel:')
print(sheet1.nrows)
print('số cột trong Excel:')
print(sheet1.ncols)
i=0
dem=0
workbook = xlrd.open_workbook('driendlist.xlsx')
sheet = workbook.sheet_by_index(0)
data = [sheet.cell_value(0, 1) for col in range(sheet.ncols)]
workbook = xlwt.Workbook()
sheet = workbook.add_sheet('Friend')
mangtim = []
linktim = []

while True: #Biến vô tận
    with speech_recognition.Microphone() as mic: #Chờ đợi sử dụng Mic để chuyển thành văn bản
        print("\nSiri: I'm listening")
        #audio = bot_ear.listen(mic)
        audio = bot_ear.record(mic, duration= 5) #Sau khi nghe từ Mic, nhận biến audio là sound
        print("\nSiri: ....")
    try:
        you = bot_ear.recognize_google(audio,language='vi-VN').upper() #truyền biến audio lên API GG, nhận về chuỗi kí tự theo giọng nói
        print("\nYou: "+you)
    except:
        you=""
        print("\nSiri: "+you)
    if "XIN CHÀO" in you:
        bot_brain = "Xin chào Dũng"
    elif you == "":
        bot_brain =""
    elif "GIỎI" in you:
        bot_brain ="Cảm ơn nhé ! Đó là điều tôi nên làm"
    elif "BẠN CÓ THỂ GIÚP GÌ" in you:
        bot_brain = "Tôi có thể giúp bạn tìm kiếm thông tin, chơi nhạc, chụp ảnh"
    elif "GỌI" in you:
        bot_brain = "Gọi cho ai"
        tts = gTTS(text=bot_brain, lang='vi')
        tts.save("Siri.mp3")
        playsound("Siri.mp3")
        os.remove("Siri.mp3")
        with speech_recognition.Microphone() as mic:
            print("\nSiri: I'm listening")
            # audio = bot_ear.listen(mic)
            audio = bot_ear.record(mic, duration=5)
            print("\nSiri: ....")
        try:
            you = bot_ear.recognize_google(audio, language='vi-VN').upper()
            print("\nYou: " + you)
        except:
            you = ""
            print("\nSiri: " + you)
        if you == "":
            bot_brain = "Google đây, bạn tự tìm lấy nhé"
            os.system("start www.google.com")
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--incognito")
        # browser = webdriver.Chrome(chrome_options=chrome_options)
        # browser.get("https://www.facebook.com/videocall/incall/?peer_id=100006131910859")
        # sleep(1)
        # mail = browser.find_element_by_id('email')
        # mail.send_keys('phantridungdz')
        # password = browser.find_element_by_id('pass')
        # password.send_keys('buonthicukhocdi123')
        # password.send_keys(Keys.ENTER)
        # sleep(2)
        # browser.get("https://www.facebook.com/messages/t/100006131910859")
        # doit = browser.find_element_by_xpath(
        #     '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/span/div[1]/ul/li[1]/a')
        # doit.click()
        else:
            tencantim = you
            while i < hang:
                nickname = sheet1.cell_value(i, 0).upper()
                link = sheet1.cell_value(i, 1)
                b = nickname.split()
                count = len(b)
                if tencantim in b:
                    d = ' '.join(b)
                    link1 = link.lstrip('https://www.faceboo')
                    link2 = link1.lstrip('k.com')
                    link3 = link2.lstrip('/')
                    kiemtra = link3.startswith('profile.php?id=')
                    if kiemtra == True:
                        link4 = link3.lstrip('profile.php?id=')
                        mangtim.append(d)
                        linktim.append(link4)
                i += 1
            # soketqua = len(mangtim)
            # bot_brain = "có "+ str(soketqua) + " "+ tencantim + " trong danh sách bạn bè, bạn muốn gọi " + tencantim +" mấy?"
            # tts = gTTS(text=bot_brain, lang='vi')
            # tts.save("Siri.mp3")
            # playsound("Siri.mp3")
            # os.remove("Siri.mp3")

            bot_brain = "đang gọi "+ mangtim[1]
            tts = gTTS(text=bot_brain, lang='vi')
            tts.save("Siri.mp3")
            playsound("Siri.mp3")
            os.remove("Siri.mp3")

            os.system("start www.facebook.com/videocall/incall/?peer_id="+linktim[1])
            sleep(4)
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)


    elif "chụp ảnh"in you:
        bot_brain ="Cười lên nào !"
        os.system("start microsoft.windows.camera:")
        sleep(2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        bot_brain = "Xong rồi đó, một bức ảnh tuyệt đẹp!"
    elif "thời tiết" in you:
        bot_brain = " Hôm nay trời nhiều mây"
    elif "Facebook" in you:
        os.system("start www.facebook.com")
        bot_brain = "Em mở facebook cho anh rồi nhé"
    elif "Youtube" in you:
        os.system("start www.youtube.com")
        bot_brain = "Em mở youtube cho anh rồi nhé"
    elif "Google" in you:
        os.system("start www.google.com")
        bot_brain = "Em mở Google cho anh rồi nhé"

    elif "ngày" in you:
        bot_brain = datetime.datetime.now().strftime("%A") #=Monday
    elif "Mở nhạc" in you:
        bot_brain = "Bạn muốn nghe bài gì ?"
        tts = gTTS(text=bot_brain, lang='vi')
        tts.save("Siri.mp3")
        playsound("Siri.mp3")
        os.remove("Siri.mp3")
        with speech_recognition.Microphone() as mic:
            print("\nSiri: I'm listening")
            # audio = bot_ear.listen(mic)
            audio = bot_ear.record(mic, duration=5)
            print("\nSiri: ....")
        try:
            you = bot_ear.recognize_google(audio, language='vi-VN')
            print("\nYou: " + you)
        except:
            you = ""
            print("\nSiri: " + you)
        if you == "":
            bot_brain = "Google đây, bạn tự tìm lấy nhé"
            os.system("start www.google.com")
        else:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--incognito")
            browser = webdriver.Chrome(chrome_options=chrome_options)
            browser.get("http://youtube.com/")
            doit = browser.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')
            doit.send_keys(you)
            doit = browser.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button')
            doit.click()
            sleep(3)
            doit = browser.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a/yt-img-shadow')
            doit.click()
            bot_brain = "Chúc bạn nghe nhạc vui vẻ"
    elif "tìm" in you:
        bot_brain = "Bạn muốn tìm gì ?"
        tts = gTTS(text=bot_brain, lang='vi')
        tts.save("Siri.mp3")
        playsound("Siri.mp3")
        os.remove("Siri.mp3")
        with speech_recognition.Microphone() as mic:
            print("\nSiri: I'm listening")
            # audio = bot_ear.listen(mic)
            audio = bot_ear.record(mic, duration=5)
            print("\nSiri: ....")
        try:
            you = bot_ear.recognize_google(audio, language='vi-VN')
            print("\nYou: " + you)
        except:
            you = ""
            print("\nSiri: " + you)
        if you == "":
            bot_brain = "Google đây, bạn tự tìm lấy nhé"
        else:
            os.system("start www.google.com/search?q="+you.replace(' ','+'))
            bot_brain = "Đây là kết quả tôi tìm được"

    else:
        os.system("start www.google.com/search?q=" + you.replace(' ', '+'))
        bot_brain = "Đây là kết quả tìm kiếm trên google !"
        print("\nSiri: " + bot_brain)
    try:
        tts = gTTS(text = bot_brain,lang='vi')
        tts.save("Siri.mp3")
        playsound("Siri.mp3")

    except:
        bot_brain=""