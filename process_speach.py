import os

import speech_recognition as sr  # Library for performing speech recognition with support for engines and API
from pydub import AudioSegment  # Manipulate audio with a simple and easy high level interface
from pydub.playback import play
from gtts import gTTS as tts  # Python library and CLI tool to interface with Google Translates text to speech


# function to capture speech
def capture():
    rec = sr.Recognizer()

    with sr.Microphone() as source:
        print("I am listening...")
        audio = rec.listen(source, phrase_time_limit=5)

    try:
        text = rec.recognize_google(audio, language='ml')
        return text

    except Exception:
        speak('Sorry, I could not understand what you said')
        return 0


# this function will process what is said
def process_text(name, input):
    speak(name + ', you said: ' + input)
    return


# function so our app can speak
def speak(text):
    # Write output to console
    print(text)

    # save audio file
    speech = tts(text=text, lang='ml')
    speech_file = 'input.mp3'
    speech.save(speech_file)

    # Play audio file
    sound = AudioSegment.from_mp3(speech_file)
    play(sound)
    os.remove(speech_file)


def loop_speaking():
    # First get name
    speak('What is your name?')
    name = capture()
    speak('Hello, ' + name)

    # Then just keep listening & responding
    while 1:
        speak('Speak: ')
        captured_text = capture().lower()

        if captured_text == 0:
            continue
        if 'മതി' in str(captured_text):
            speak('Ok bye!' + name)
            break

        # process captured text
        process_text(name, captured_text)


if __name__ == '__main__':
    # speak("അമ്മ")
    speak("kale" + "\u200d")
    #loop_speaking()
