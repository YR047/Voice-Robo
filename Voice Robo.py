from gtts import gTTS
import os

try:
    print("WELCOME TO SPEAK ROBOT 1.1")
    while True:
        text = input("Enter the text or Enter 'QUIT' to exit the Program : ")
        if text == "QUIT":
            break
        tts = gTTS(text=text, lang="en")
        tts.save("welcome.mp3")
        os.system("welcome.mp3")
except Exception as e:
    print(e)
