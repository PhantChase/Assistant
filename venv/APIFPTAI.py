import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty("voices")

for voice in voices:
    print("Voice:")
    print("ID: %s" %voice.id)
    print("Name: %s" %voice.name)
    print("Age: %s" %voice.age)
    print("Gender: %s" %voice.gender)
    print("Languages Known: %s" %voice.languages)

vi_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens"

engine.setProperty("voice",vi_voice_id)
engine.say('Xin chào')
engine.runAndWait()