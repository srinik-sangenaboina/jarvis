import pyttsx3
engine= pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[0].id)