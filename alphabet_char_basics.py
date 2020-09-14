import sqlite3
from translate_text import *
import random
from process_speach import *
from Important_Arrays import MODIFIERS


def get_word_with_same_char(char):
    connection = sqlite3.connect("my_malayalam.db")
    cursor = connection.cursor()

    if char in MODIFIERS:
        return get_word_with_like_char(char)

    sql_command = """SELECT mal_word, english_trans, phonetic FROM malayalam_vocab WHERE alphabet=?"""
    string = cursor.execute(sql_command, (char,)).fetchall()
    connection.commit()
    cursor.close()
    if len(string) != 0:
        result_num = len(string)

        if result_num == 1:
            return string
        else:
            num = random.randint(0, result_num)
            if num == len(string):
                return string[num - 1]
            return string[num]
    else:
        string = "No Example Available"

    if string == "No Example Available":
        return get_word_with_like_char(char)


# Because phonetic in database isn't that reliable
def get_phonetic(word):
    return get_pronunciation(word)


def get_sound(word):
    speak(word)


def get_word_with_like_char(pattern):
    connection = sqlite3.connect("my_malayalam.db")
    cursor = connection.cursor()

    command = "SELECT mal_word, english_trans, phonetic FROM malayalam_vocab WHERE mal_word LIKE '%" + pattern + "%' AND difficulty != 5 "
    string = cursor.execute(command).fetchall()
    connection.commit()
    cursor.close()
    if len(string) != 0:
        result_num = len(string)

        if result_num == 1:
            return string
        else:
            num = random.randint(0, result_num)
            if num == len(string):
                return string[num - 1]
            return string[num]
    else:
        return "No Example Available"


def update_difficuty():
    connection = sqlite3.connect("my_malayalam.db")
    cursor = connection.cursor()
    command = "UPDATE malayalam_vocab SET difficulty = 5 WHERE LENGTH(mal_word) >= 14"
    cursor.execute(command)
    connection.commit()
    cursor.close()
