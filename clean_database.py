import sqlite3
from translate_text import *
import re

"""
The purpose of this script is to clean the database a bit and take out the words that do not have a direct translation 
from english to malayalam. Better to make a separate script for that then do everything in the web_scrapping script
"""


def remove_non_mal_word(cursor, connection, i):
    sql = 'DELETE FROM malayalam_vocab WHERE id_number=?'
    cursor.execute(sql, ((i),))
    connection.commit()
    print("Deleted entry")


if __name__ == '__main__':
    # connecting to database
    connection = sqlite3.connect("my_malayalam.db")
    # creating a cursor to work with
    cursor = connection.cursor()

    # remove all non malayalam translations
    array = [863, 822, 528, 438, 425]  # these are the ones that didn't translate well
    for integers in array:
        sql = "SELECT mal_word FROM malayalam_vocab WHERE id_number=?"
        words = cursor.execute(sql, (integers,)).fetchall()
        print(words)
        remove_non_mal_word(cursor, connection, integers)

    cursor.close()
    connection.close()

# Comments: now all the words that couldn't be translated to malayalam are not in database
# The ID number doesn't match with the row number because you took our 2 entries -
# That is okay, just be aware of that
