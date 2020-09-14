import csv
import re
import sqlite3
chars = ['ഊ', 'ഋ', 'ഌ', 'ഐ', 'ഓ', 'ഔ', 'ൠ', 'ൡ', 'ഖ', 'ഘ', 'ങ', 'ഛ', 'ഝ', 'ഠ', 'ഡ', 'ഢ', 'ണ', 'ഥ', 'ദ', 'ധ', 'ഩ', 'യ', 'ള', 'ഴ']

def get_difficulty(word):
    difficulty = 0
    res = bool(re.search(r"\s", word))
    if not res:
        length = len(word)
        if length <= 5:
            difficulty = 1
        else:
            difficulty = 2
    else:
        difficulty = 3  # automatically a level 3 b/c sentence

    return difficulty


def add_csv_words(alphabet, mal, eng, pho, diff):
    # LOADING DATABASE
    cursor.execute('''INSERT INTO malayalam_vocab(alphabet, mal_word, english_trans, phonetic, difficulty)
                            VALUES(?,?,?,?,?)''',
                   (str(alphabet), str(mal), str(eng), str(pho), int(diff),))

if __name__ == '__main__':
    with open('olam-enml.csv') as csv_file:
        readCSV = csv.reader(csv_file, delimiter='\t')
        count = 0
        sentences = 0

        # connecting to database
        connection = sqlite3.connect("my_malayalam.db")
        # creating a cursor to work with
        cursor = connection.cursor()

        for row in readCSV:
            try:
                english = row[1]
                malayalam = row[3]
                ch = ""

                print(english + ": " + malayalam)
                res = bool(re.search(r"\s", malayalam))
                if res:
                    sentences = sentences+1
                else:
                    ch = malayalam[0]

                add_csv_words(ch, malayalam, english, "", 4)

            except IndexError:
                count = count + 1
                pass


        # Make sure all values saved and database closes properly
        connection.commit()
        cursor.close()
        print("All values were put into database properly")

    print(count)
    print(sentences)