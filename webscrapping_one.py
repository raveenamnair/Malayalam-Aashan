from lxml.html import parse
import re
import sqlite3
from translate_text import *
from os import path
import re

"""
This script will take words from a website that has 500 most popular Malayalam words. 
These will be helpful to generate Malayalam words
"""


def web_scrape(url):
    temp = []  # temporary array to hold raw contents of website
    count = 0
    doc = parse(url).getroot()  # get document
    for div in doc.cssselect('tr'):  # separate by <tr> tag
        if count >= 2:  # first two elements are not needed
            row = div.text_content()
            s = row.strip()  # removes tab in row (weird format)
            array = s.split("\t")  # splits into array separated whenever a tab is present
            temp.append(array)
        count = count + 1

    # removing the last three because they are not needed
    k = 3
    # using len() + list slicing
    # remove last K elements
    web_words = temp[: len(temp) - k]
    return web_words


def pop_word_to_english(web_stuff):
    english_words = []  # array to store english words
    for elements in web_stuff:
        # now get only english words to be translated (always first element)
        english_words.append(elements[0])

    return english_words


def create_table_command(cursor):
    sql_command = """
    CREATE TABLE IF NOT EXISTS malayalam_vocab (
    id_number INTEGER PRIMARY KEY,
    alphabet CHAR(1),
    mal_word VARCHAR(500),
    english_trans VARCHAR(500),
    phonetic VARCHAR(500),
    difficulty INTEGER DEFAULT 0);"""

    cursor.execute(sql_command)


def translate_and_load_DB(english_array):
    mal_trans = []  # to store malayalam translation
    phonetic = []  # to store pronunciation
    no_translation_available = []  # for words that could not be translated to english
    for i in range(len(english_array)):
        try:
            translated = english_to_malayalam(english_array[i])
            # if there is no malayalam translation available
            if translated == english_array[i]:
                no_translation_available.append(i)
            mal_trans.append(translated)
        except Exception:
            print("Error translating")
            pass

    # works better if they are separated - not sure why
    for x in range(len(mal_trans)):
        try:
            pronunciation = get_pronunciation(mal_trans[x])
            phonetic.append(pronunciation)
        except Exception:
            print("Error phonetic")
            pass

    print(len(mal_trans))  # should be 579
    print(len(phonetic))  # should be 579

    # NOTICE: takes about 4 minutes to load all arrays

    # LOADING DATABASE

    # connecting to database
    connection = sqlite3.connect("my_malayalam.db")
    # creating a cursor to work with
    cursor = connection.cursor()

    create_table_command(cursor)  # only creates it once

    # Add existing words to database
    for i in range(len(english_array)):
        english = english_array[i]
        malayalam = mal_trans[i]
        speak = phonetic[i]
        alphabet = ""  # blank if its a sentence
        difficulty = 0

        res = bool(re.search(r"\s", malayalam))
        if not res:
            alphabet = malayalam[0]  # get first character
            length = len(malayalam)
            if length <= 5:
                difficulty = 1
            else:
                difficulty = 2
        else:
            difficulty = 3  # automatically a level 3 b/c sentence

        if i is not no_translation_available:
            cursor.execute('''INSERT INTO malayalam_vocab(alphabet, mal_word, english_trans, phonetic, difficulty)
                    VALUES(?,?,?,?,?)''', (str(alphabet), str(malayalam), str(english), str(speak), int(difficulty),))

    # Make sure all values saved and database closes properly
    connection.commit()
    cursor.close()
    print("All values were put into database properly")


if __name__ == '__main__':
    # COLLECT WORDS

    # Setting up the extraction
    URL = "http://learn101.org/malayalam_voc500.php"
    web_words = web_scrape(URL)
    eng_words = pop_word_to_english(web_words)

    print(len(eng_words))  # should be 579
    print(len(web_words))  # should be 579

    # This method will take the english words given and translate them and get their phonetic
    # Reason why this is all in one method is because I will be using same method for other URLS
    # in other scripts. Therefore, it is easier to do this way

    translate_and_load_DB(eng_words)

# Comments: The rough Database is loaded, but some values are not what I want it to be. Instead re-doing this scrip
# I will create another script to clean up the values I don't like
