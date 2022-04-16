from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ScreenAI import Ui_MainWindow

import sys
import speech_recognition
import pyttsx3
import subprocess

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.uic.Start_Button.clicked.connect(self.online_AI)
        self.uic.Stop_Button.clicked.connect(self.stop_AI)

    def stop_AI(self):
        self.uic.On_off_screen.setText("Tom offline")
    def online_AI(self):
        # khai báo giọng nói nam [1] hoặc nữ [0]
        Tom_ear = speech_recognition.Recognizer()
        Tom_mouth = pyttsx3.init()
        voices = Tom_mouth.getProperty("voices")
        Tom_mouth.setProperty("voice", voices[1].id)

        # with speech_recognition.Microphone() as mic:
        #     audio = Tom_ear.listen(mic)
        # try:
        #     you = Tom_ear.recognize_google(audio)
        #     self.uic.Me_Chat.setText(str(you))
        # except:
        #     you = ""
        # if "hello Tom" in you:
        #     Tom_brain = "hello life, what can i do for you?"
        #     Tom_mouth.say(Tom_brain)
        #     Tom_mouth.runAndWait()
        while True:
            self.uic.On_off_screen.setText("Tom online")
            with speech_recognition.Microphone() as mic:
                audio = Tom_ear.listen(mic)
            try:
                you = Tom_ear.recognize_google(audio)
                self.uic.Me_Chat.setText(str(you))
            except:
                you = ""
            if you == "":
                Tom_brain = "i can't hear you, please try again"
            elif "doing" in you:
                Tom_brain = "i'm sleeping"
            elif "sure" in you:
                Tom_brain = "i'm not sure"
            elif "do" in you:
                Tom_brain = "i can do something for you"
            elif "nice" in you:
                Tom_brain = "nice to see you too"
            elif "hello" in you:
                Tom_brain = "hello life, what can i do for you?"
            # mở một chương trình bất kỳ
            elif "note" in you:
                Tom_brain = "ok i'm open note program for you"
                sublime = "C:\WINDOWS\system32\notepad.exe"
                subprocess.Popen("notepad.exe")
            # elif self.uic.On_off_screen.Text() == "Tom offline":
            #     Tom_brain = "goodbye life"
            elif "bye" in you:
                Tom_brain = "goodbye life"
                self.uic.Tom_Chat.setText(str(Tom_brain))
                Tom_mouth.say(Tom_brain)
                Tom_mouth.runAndWait()
                break
            else:
                Tom_brain = "oh thank you"
            self.uic.Tom_Chat.setText(str(Tom_brain))
            Tom_mouth.say(Tom_brain)
            Tom_mouth.runAndWait()

    def show(self):
        self.main_win.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())