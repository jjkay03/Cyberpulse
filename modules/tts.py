# Cyberpulse tts module by jjkay03

import pyttsx3

# Function: Set the voice for the TTS
def tts_set_voice(engine, voice_id):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice_id].id)

# Function: Speak the text with the TTS
def tts(text, voice_id=0, rate=175):
    engine = pyttsx3.init()
    tts_set_voice(engine, voice_id)
    engine.setProperty('rate', rate) # Set the speech rate
    engine.say(text)
    engine.runAndWait()
