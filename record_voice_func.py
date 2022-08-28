

#sr.Microphone.list_microphone_names()
#https://realpython.com/python-speech-recognition/#working-with-microphones
def record_voice():
    import speech_recognition as sr
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    txt = r.recognize_google(audio, language="zh-TW")
    return txt




