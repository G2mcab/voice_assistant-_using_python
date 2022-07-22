import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=5)
    print('Say something')
    audio = r.listen(source)
    voice_data = r.recognize_google(audio)
    print(voice_data)
