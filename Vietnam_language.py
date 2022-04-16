
import speech_recognition
Tom_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    audio = Tom_ear.listen(mic)
try:
    you = Tom_ear.recognize_google(audio, language="vi-VI")
    print(you)
except:
    you = ""