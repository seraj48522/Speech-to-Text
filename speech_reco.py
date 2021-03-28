# This program is used to convert speech to text

import speech_recognition as sp


rec = sp.Recognizer()

my_micro = sp.Microphone(device_index=1)


with my_micro as source:
    print("Say Anything")
    aud = rec.listen(source)

    to_text = rec.recognize_google(aud)

print(to_text)
