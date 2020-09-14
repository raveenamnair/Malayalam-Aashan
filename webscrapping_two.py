import requests
from webscrapping_one import *
from translate_text import *
from Important_Arrays import *


def get_english_words(array):
    eng = []
    for rows in array:
        output = ""
        word = rows.split(" ")
        for item in word:
            if detect_language(item) == 'ml':
                break
            else:
                output = output + " " + item

        if output not in ignore_words:
            eng.append(output)
    return eng


def remove_text_inside_brackets(text, brackets="()[]"):
    count = [0] * (len(brackets) // 2)  # count open/close brackets
    saved_chars = []
    for character in text:
        for i, b in enumerate(brackets):
            if character == b:  # found bracket
                kind, is_close = divmod(i, 2)
                count[kind] += (-1) ** is_close  # `+1`: open, `-1`: close
                if count[kind] < 0:  # unbalanced bracket
                    count[kind] = 0  # keep it
                else:  # found bracket to remove
                    break
        else:  # character is not a [balanced] bracket
            if not any(count):  # outside brackets
                saved_chars.append(character)
    return ''.join(saved_chars)


def clean_array(array):
    new_array = []
    for item in array:
        text = remove_text_inside_brackets(item)
        new_array.append(text)
    return new_array


def print_array(array):
    for a in array:
        print(a)


# Will use the "main" method from webscrapping_one.py to add words from the rest of the urls
# Due to limitations from googletrans module, I have to go through the links manually or else I'll reach the limit
# Ideally - I would use a for loop and go through the links I have saved
if __name__ == '__main__':
    INDEX = 8  # I will use this to update. There are 8 links
    links = URLS
    web_words = web_scrape(links[INDEX])
    web_words = pop_word_to_english(web_words)

    engs = get_english_words(web_words)
    engs = clean_array(engs)

    # using webscrapping method - passing english array
    translate_and_load_DB(engs)

# Comments: even tho this has manual work, it is better than going through data and cleaning it up again
