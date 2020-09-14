# For Docs for this visit here:
# https://py-googletrans.readthedocs.io/en/latest/

from googletrans import Translator
from LanguageCodes import LANGUAGES

translator = Translator()  # Two main things it can do is translate and detect


# Finding the language. If not found, message is printed
def find_language():
    choice = input("What language do you want to translate: ")
    found = False
    for key in LANGUAGES:
        choice = choice.lower()
        if LANGUAGES.get(key) == choice:
            print("Found! " + choice + " " + LANGUAGES.get(key))
            found = True
            break

    if not found:
        print("Language not found")


# Detects the language and gives back prediction confidence
def detect_language(text):
    # text = 'എന്റെ പേര്‌ രവീന'
    return translator.detect(text).lang


def get_word(word):
    print("in method")
    s = translator.translate(word, dest='ml')
    print(s)
    return s.text


# Translates from Malayalam to English
def malayalam_to_english(text):
    translation = translator.translate(text, dest='en')
    print(translation.text)


# Translates from Malayalam to English
def english_to_malayalam(text):
    translation = translator.translate(text, dest='ml')
    return translation.text
    # print(translation.text)


def get_pronunciation(text):
    pronunciation = translator.translate(text, dest='ml')
    # print(pronunciation.pronunciation)
    return pronunciation.pronunciation


if __name__ == '__main__':
    print("IN MAIN")
    malayalam_to_english("കുഴപ്പം പിടിച്ച സമയം")
    print(get_pronunciation("ൠ"))
    print(english_to_malayalam("Moisture"))
    # get_pronunciation("കളസം")
