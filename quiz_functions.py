"""
This script will take care of creating quizzes for each sub category
"""

import sqlite3
from translate_text import *
import random
from process_speach import *
from Important_Arrays import MODIFIERS


def get_vowel_quiz(level):
    connection = sqlite3.connect("my_malayalam.db")
    cursor = connection.cursor()
    command = ""
    if level == "Expert":
        command = "SELECT * FROM malayalam_vocab"
    else:
        difficulty = ""
        if level == "Beginner\n":
            difficulty = "= 1 or difficulty = 2"
        elif level == "Novice\n":
            difficulty = "!= 4 or difficulty != 5"
        elif level == "Advanced\n":
            difficulty = "!= 5"
        command = "SELECT * FROM malayalam_vocab WHERE difficulty " + difficulty
    result = cursor.execute(command).fetchall()

    i = 0
    word_array = []
    while i < 20:
        num = random.randint(0, len(result))
        if result[num] not in word_array:
            word_array.append(result[num])
        i = i + 1

    connection.commit()
    cursor.close()

    return word_array

