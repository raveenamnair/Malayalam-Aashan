from cryptography.fernet import Fernet
from datetime import datetime
from Important_Arrays import *
import sqlite3
import os

# symmetric key which we’ll later use to encrypt and decrypt our password
key = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY='


def create_header(username, fname, lname):
    filename = username + ".txt"
    if not os.path.exists(filename):
        # opening in append mode because you don't always want to read through entire file
        file = open(filename, "a+")
        file.write("MALAYALAM AASHAN REPORT\n")
        file.write(fname + " " + lname + "\n")
        # datetime object containing current date and time
        now = datetime.now()
        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        file.write("Joined: " + dt_string + "\n")
        file.write("Session Count: 0\n")
        file.write("Memorized: 0\n")
        file.write("Level: Beginner\n")

        file.close()
    return os.path.abspath(filename)


def replace_line(file_name, line_num, text):
    # storing all the lines
    lines = open(file_name, 'r').readlines()
    # modifying the specific line (replacing in the array)
    lines[line_num] = text
    # rewriting file
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()


def get_value_from_line(file_name, line_num):
    f = open(file_name, "r")
    i = 0
    for line in f:
        # For Python3, use print(line)
        if i == line_num:
            line = line.split(": ")[1]
            f.close()
            return line
        i = i + 1



def encrypt_password(password_str):
    cipher_suite = Fernet(key)
    ciphered_text = cipher_suite.encrypt(password_str.encode())
    return ciphered_text


def decrypt_password(password_hash):
    cipher_suite = Fernet(key)
    unciphered_text = (cipher_suite.decrypt(password_hash))
    return unciphered_text


def check_password_similarity(username_entered, password_entered):

    connection = sqlite3.connect("user_info.db")
    # creating a cursor to work with
    cursor = connection.cursor()
    sql_command = "SELECT password_hash FROM user_info WHERE username=?"
    try:
        password_in_db = cursor.execute(sql_command, (username_entered,)).fetchone()[0]
    except TypeError:
        print("incorrect credentials")
        return False
    connection.commit()
    cursor.close()
    decrypt = decrypt_password(password_in_db)  # have to encode because this is a string
    if str.encode(password_entered) == decrypt:
        return True
    else:
        return False


def create_table(cursor):
    sql_command = """
        CREATE TABLE IF NOT EXISTS user_info (
        id_number INTEGER PRIMARY KEY,
        username VARCHAR(200) NOT NULL UNIQUE,
        password_hash BLOB,
        file_path VARCHAR(500));"""

    cursor.execute(sql_command)


def add_login_info(username, password, fname, lname):
    connection = sqlite3.connect("user_info.db")
    # creating a cursor to work with
    cursor = connection.cursor()
    create_table(cursor)  # if the table doesn't exist
    file_path = create_header(username, fname, lname)
    result = cursor.execute("SELECT * FROM user_info")

    en_password = encrypt_password(password)
    print(en_password)

    if username != '' or en_password != '' or (len(username) != 0):
        for i in result:
            if i[1] == username:
                # tkinter.messagebox.showerror("DUPLICATE", "USER ALREADY EXISTS!")
                print("Username already exists...")
                return False

        else:
            try:
                cursor.execute('''INSERT INTO user_info(username, password_hash, file_path)
                                        VALUES(?,?,?)''',
                               (str(username), en_password, str(file_path),))
                connection.commit()
                cursor.close()
                print("Added successfully...")
                return True
            except Exception:
                print("Error while adding...")
                return False

    else:
        print("Fields were empty...")
        return False


def getFullInfo(username):
    connection = sqlite3.connect("user_info.db")
    # creating a cursor to work with
    cursor = connection.cursor()
    result = cursor.execute("SELECT * FROM user_info").fetchall()
    for i in result:
        if i[1] == username:
            return i
    connection.commit()
    cursor.close()


def start_session_write(username):
    # first need to increase the number of sessions in file
    filename = username + ".txt"
    count = get_value_from_line(filename, 3)
    count = int(count) + 1
    string = "Session Count: " + str(count) + "\n"
    replace_line(filename, 3, string)

    file = open(filename, "a+")
    file.write("---------------------------------------------\n")
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    file.write("Started: " + dt_string + "\n")
    file.close()


def review_write(username, clicked_mod, array):
    filename = username + ".txt"
    file = open(filename, "a+")
    size = len(MODIFIERS)
    if "Vowels" in clicked_mod:
        size = len(VOWELS)
    elif "Consonants" in clicked_mod:
        size = len(CONSONANTS)

    file.write("Review: " + clicked_mod + " [" + str(len(array)) + "/" + str(size) + "]\n")
    file.write(str(array) + "\n")
    # Updated Memorized Count
    count = get_value_from_line(filename, 4)
    count = int(count) + len(array)
    string = "Memorized: " + str(count) + "\n"
    replace_line(filename, 4, string)
    file.close()

def learn_write(username, clicked_mod):
    filename = username + ".txt"
    file = open(filename, "a+")
    file.write("Module: " + clicked_mod + "\n")
    # if "Test" in clicked_mod:
    #     file.write("Module: " + clicked_mod + "\n")
    #     file.write("Score: INSERT\n")
    # else:
    #     file.write("Module: " + clicked_mod + "\n")
    file.close()


def quiz_write(username, score):
    filename = username + ".txt"
    file = open(filename, "a+")
    file.write("Practice Quiz: [" + str(score) + "/20]\n")
    file.close()



def end_session_write(username):
    filename = username + ".txt"
    file = open(filename, "a+")
    file.write("-Clicked EXIT-\n")
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    file.write("Ended: " + dt_string + "\n")

def get_level_from_memorized(count):
    if 0 <= count <= 22:
        return "Beginner"
    elif 23 <= count <= 45:
        return "Novice"
    elif 46 <= count <= 67:
        return "Advanced"
    elif count == 68:
        return "Expert"

def check_level(username):
    filename = username + ".txt"
    file = open(filename, "a+")
    memorized = get_value_from_line(filename, 4)
    real_level = get_level_from_memorized(int(memorized))
    file_level = get_value_from_line(filename, 5)
    if real_level != file_level:
        string = "Level: " + real_level + "\n"
        replace_line(filename, 5, string)

def levels_left(level):
    if level == "Beginner\n":
        return 3
    elif level == "Novice\n":
        return 2
    elif level == "Advanced\n":
        return 1
    else:
        return 0


