import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as s:
    print("Speak now...")
    audio = r.listen(s)

try:
    t = r.recognize_google(audio)
    print("You said:", t)

except sr.UnknownValueError:
    print("Sorry, I could not understand your speech.")

except sr.RequestError:
    print("Could not connect to the speech recognition service.")