import speech_recognition as sr
r=sr.Recognizer()
mp=sr.Microphone()

with mp as source:
    print("Say Something...")
    audio=r.listen(source,timeout=10)
    try:
        text=r.recognize_google(audio)
        print(text)
    except:
        print("Try again")