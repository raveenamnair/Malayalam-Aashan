import tkinter as tk
import tkinter.font as tkFont
from Important_Arrays import *
from tkmacosx import Button
from user_report import *
from tkinter import messagebox
from PIL import ImageTk, Image, ImageDraw
import image as i
from alphabet_char_basics import *
from quiz_functions import *
from process_speach import *

HEIGHT = 550
WIDTH = 1000
DARK_PURPLE = '#160F29'
MING = '#246A73'
DARK_CYAN = '#368F8B'
CHAMPAGNE = '#F3DFC1'
DESSERT_SAND = '#DDBEA8'
LIGHT_GRAY = '#8AA29E'

# Making global variables
G_USERNAME = ""


class Login:

    def __init__(self, master, state):
        self.master = master
        self.master.title(state)
        self.state = state
        self.entering_frame = tk.Frame(self.master, bg=DARK_CYAN)
        self.entering_frame.place(relx=0.5, rely=0.25, relwidth=0.45, relheight=0.5, anchor='n')
        fontStyle = tkFont.Font(family="Lucida Grande", size=45)
        # Main header
        header = tk.Label(self.master, text="MALAYALAM AASHAN", bg=CHAMPAGNE, fg=DARK_PURPLE, font=fontStyle)
        header.place(anchor='n', relx=0.5, rely=0.1)
        # Welcome label
        welcome_label = tk.Label(self.entering_frame, text="Welcome!\nPlease Login or Sign Up", bg=DARK_CYAN,
                                 fg='white')
        welcome_label.place(anchor='n', relx=0.5, rely=0.1)

        # Username widgets
        username_label = tk.Label(self.entering_frame, text="USERNAME", bg=DARK_CYAN, fg='white')
        username_label.place(anchor='n', relx=0.25, rely=0.3)
        self.username_entry = tk.Entry(self.entering_frame)
        self.username_entry.place(anchor='n', relx=0.7, rely=0.3)
        # Password widgets
        password_label = tk.Label(self.entering_frame, text="PASSWORD", bg=DARK_CYAN, fg='white')
        password_label.place(anchor='n', relx=0.25, rely=0.5)
        self.password_entry = tk.Entry(self.entering_frame)
        self.password_entry.place(anchor='n', relx=0.7, rely=0.5)

        btn_frame = tk.Frame(self.entering_frame, bg=DARK_CYAN)
        btn_frame.place(relx=0.5, rely=0.8, relwidth=1, relheight=0.2, anchor='n')
        login_btn = Button(btn_frame, text="Login", command=self.login, bg='white', fg="black", borderless=1)
        login_btn.place(relx=0.3, rely=0.2, anchor='n')
        signup_btn = Button(btn_frame, text="Sign up", bg='white', fg="black", borderless=1,
                            command=self.show_sign_up_frame)
        signup_btn.place(relx=0.7, rely=0.2, anchor='n')

    def close_windows(self):
        self.entering_frame.destroy()

    def login(self):
        status = check_password_similarity(self.username_entry.get(), self.password_entry.get())
        if status:
            global G_USERNAME
            G_USERNAME = self.username_entry.get()
            print("Globably saved username: " + G_USERNAME)
            start_session_write(G_USERNAME)
            check_level(G_USERNAME)
            Dashboard(self.master, "Dashboard Window")
            self.close_windows()
        else:
            tk.messagebox.showerror("Invalid Credentials", "Incorrect password or username. Try again")

    def show_sign_up_frame(self):
        self.entering_frame.destroy()
        signup_frame = tk.Frame(self.master, bg=DARK_CYAN)
        signup_frame.place(relx=0.5, rely=0.25, relwidth=0.45, relheight=0.6, anchor='n')
        fontStyle = tkFont.Font(family="Lucida Grande", size=45)
        # Main header
        header = tk.Label(self.master, text="MALAYALAM SCHOOL", bg=CHAMPAGNE, fg=DARK_PURPLE, font=fontStyle)
        header.place(anchor='n', relx=0.5, rely=0.1)
        # Welcome label
        welcome_label = tk.Label(signup_frame, text="Welcome!\nPlease Login or Sign Up", bg=DARK_CYAN,
                                 fg='white')
        welcome_label.place(anchor='n', relx=0.5, rely=0.1)
        # First Name
        fname_label = tk.Label(signup_frame, text="FIRST NAME", bg=DARK_CYAN, fg='white')
        fname_label.place(anchor='n', relx=0.25, rely=0.3)
        self.fname_entry = tk.Entry(signup_frame)
        self.fname_entry.place(anchor='n', relx=0.7, rely=0.3)
        # Last Name
        lname_label = tk.Label(signup_frame, text="LAST NAME", bg=DARK_CYAN, fg='white')
        lname_label.place(anchor='n', relx=0.25, rely=0.45)
        self.lname_entry = tk.Entry(signup_frame)
        self.lname_entry.place(anchor='n', relx=0.7, rely=0.45)
        # Username widgets
        username_label = tk.Label(signup_frame, text="USERNAME", bg=DARK_CYAN, fg='white')
        username_label.place(anchor='n', relx=0.25, rely=0.6)
        self.username_entry = tk.Entry(signup_frame)
        self.username_entry.place(anchor='n', relx=0.7, rely=0.6)
        # Password widgets
        password_label = tk.Label(signup_frame, text="PASSWORD", bg=DARK_CYAN, fg='white')
        password_label.place(anchor='n', relx=0.25, rely=0.75)
        self.password_entry = tk.Entry(signup_frame)
        self.password_entry.place(anchor='n', relx=0.7, rely=0.75)

        btn_frame = tk.Frame(signup_frame, bg=DARK_CYAN)
        btn_frame.place(relx=0.5, rely=0.85, relwidth=1, relheight=0.2, anchor='n')
        # login_btn = Button(btn_frame, text="Login", command=self.login, bg='white', fg="black", borderless=1)
        # login_btn.place(relx=0.3, rely=0.2, anchor='n')
        confirm_btn = Button(btn_frame, text="Confirm", bg='white', fg="black", borderless=1, command=self.sign_up_btn)
        confirm_btn.place(relx=0.5, rely=0.2, anchor='n')

    def sign_up_btn(self):
        # Take username and password and store into db
        if (len(self.username_entry.get()) == 0) or (len(self.password_entry.get()) == 0) or (
                len(self.fname_entry.get()) == 0) or (len(self.lname_entry.get()) == 0):
            tk.messagebox.showerror("Error", "Empty Fields")
        else:
            status = add_login_info(self.username_entry.get(), self.password_entry.get(), self.fname_entry.get(),
                                    self.lname_entry.get())
            if status is False:
                tk.messagebox.showerror("Error", "Error while trying to sign up. Try a different username")
            else:
                global G_USERNAME
                G_USERNAME = self.username_entry.get()
                print("Globably saved username: " + G_USERNAME)
                start_session_write(G_USERNAME)
                check_level(G_USERNAME)
                self.close_windows()
                Dashboard(self.master, "Dashboard Window")
            print(status)


class Dashboard:

    def __init__(self, master, state):
        self.master = master
        master.title(state)
        self.main_frame = tk.Frame(self.master, height=HEIGHT, width=WIDTH)
        self.main_frame.pack()
        self.current_mod = tk.StringVar()
        self.current_mod.set('Current Module:')

        self.comp_stat = tk.StringVar()
        self.comp_stat.set("Completion Status: 10/100")

        fontStyle = tkFont.Font(family="Lucida Grande", size=20)

        db_title = tk.Label(self.main_frame, text="Dashboard Activity", font=fontStyle, bg='white', fg=DARK_PURPLE)
        db_title.place(anchor='n', relx=0.4, rely=0.05)

        name_frame = tk.Frame(self.main_frame, bg='#8AA29E')
        name_frame.place(relx=0.15, rely=0, relwidth=0.3, relheight=0.1, anchor='n')
        name = tk.Label(name_frame, text="Company Name", font=fontStyle, bg='#8AA29E', fg='white')
        name.place(relx=0.2, rely=0.1)

        self.module_list_frame = tk.Frame(self.main_frame, bg=MING)
        self.module_list_frame.place(relx=0.15, rely=0.1, relwidth=0.3, relheight=1, anchor='n')
        scrollbar = tk.Scrollbar(self.module_list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        # scrollbar.place(relx=0.1, rely=0.2)
        self.mylist = tk.Listbox(self.module_list_frame, borderwidth=0, yscrollcommand=scrollbar.set, width=WIDTH,
                                 height=HEIGHT, font=fontStyle, bg=MING, fg='white')
        i = 0
        for mod in MODULES:
            self.mylist.insert(tk.END, mod)
            if i > 5:
                self.mylist.itemconfig(i, fg="gray")
            i = i + 1
        self.mylist.pack(padx=10, pady=10, fill="both", expand=True)
        # self.mylist.place(relx=0.1, rely=0.3)
        scrollbar.config(command=self.mylist.yview)

        self.mylist.bind('<<ListboxSelect>>', self.click_button)  # basically list box on click listener
        # self.disable_item(1)

        # statistics frames
        self.box1 = tk.Frame(self.main_frame, bg=CHAMPAGNE)
        self.box1.place(relx=0.385, rely=0.2, width=150, height=130, anchor='n')
        self.box2 = tk.Frame(self.main_frame, bg=MING)
        self.box2.place(relx=0.55, rely=0.2, width=150, height=130, anchor='n')
        self.box3 = tk.Frame(self.main_frame, bg=LIGHT_GRAY)
        self.box3.place(relx=0.725, rely=0.2, width=150, height=130, anchor='n')
        self.box4 = tk.Frame(self.main_frame, bg=DARK_PURPLE)
        self.box4.place(relx=0.9, rely=0.2, width=150, height=130, anchor='n')
        self.set_stats()

        self.your_mod_frame = tk.Frame(self.main_frame, bg=DESSERT_SAND)
        self.your_mod_frame.place(relx=0.64, rely=0.5, relwidth=0.66, relheight=0.3, anchor='n')
        self.your_mod_label = tk.Label(self.your_mod_frame, textvariable=self.current_mod, font=fontStyle,
                                       bg=DESSERT_SAND)
        self.your_mod_label.place(relx=0.05, rely=0.1)
        self.completion_label = tk.Label(self.your_mod_frame, textvariable=self.comp_stat, bg=DESSERT_SAND)
        self.completion_label.place(relx=0.05, rely=0.4)

        self.start_sess_btn = tk.Button(self.main_frame, text="Start Session", command=self.start_session)
        self.start_sess_btn.place(relx=0.5, rely=0.9)
        self.start_sess_btn["state"] = tk.DISABLED
        start_sess_btn = tk.Button(self.main_frame, text="View Session Reports")
        start_sess_btn.place(relx=0.7, rely=0.9)

        profile_btn = Button(self.main_frame, text="View Profile", bg=LIGHT_GRAY, fg='black', borderless=1)
        profile_btn.place(relx=0.87, rely=0.05)
        self.value = ""

    # display the clicked location
    def click_button(self, event):
        w = event.widget
        index = int(w.curselection()[0])
        self.value = w.get(index)
        #print(self.value)
        self.current_mod.set('Clicked Module: ' + self.value)

        if self.value == "":
            self.start_sess_btn["state"] = tk.DISABLED
        else:
            self.start_sess_btn["state"] = tk.NORMAL

    def close_windows(self):
        self.main_frame.destroy()

    def start_session(self):
        if self.value == "":
            self.start_sess_btn["state"] = tk.DISABLED
        else:
            self.close_windows()
            if "Learn" in self.value:
                Learn_Characters(self.master, self.value)
                learn_write(G_USERNAME, self.value)

            if "Review" in self.value:
                Review_Characters(self.master, self.value)
            Quiz(self.master)

    def set_stats(self):
        filename = G_USERNAME + ".txt"
        stats_font = tkFont.Font(family="Lucida Grande", size=40)
        memorized = tk.Label(self.box1, text=get_value_from_line(filename, 4), font=stats_font, bg=CHAMPAGNE, fg='white')
        memorized.place(relx=0.5, rely=0.5, anchor='center')
        b1_label = tk.Label(self.box1, text="Memorized", bg=CHAMPAGNE, fg='white')
        b1_label.place(relx=0.5, rely=0.8, anchor='center')
        sessions = tk.Label(self.box2, text=get_value_from_line(filename, 3), font=stats_font, bg=MING, fg='white')
        sessions.place(relx=0.5, rely=0.5, anchor='center')
        b2_label = tk.Label(self.box2, text="Sessions", bg=MING, fg='white')
        b2_label.place(relx=0.5, rely=0.8, anchor='center')
        level = tk.Label(self.box3, text=get_value_from_line(filename, 5)[0], font=stats_font, bg=LIGHT_GRAY, fg='white')
        level.place(relx=0.5, rely=0.3, anchor='center')
        b3_label = tk.Label(self.box3, text="Current Level", bg=LIGHT_GRAY, fg='white')
        b3_label.place(relx=0.5, rely=0.8, anchor='center')
        left = tk.Label(self.box4, text=str(levels_left(get_value_from_line(filename, 5))), font=stats_font, bg=DARK_PURPLE, fg='white')
        left.place(relx=0.5, rely=0.3, anchor='center')
        b4_label = tk.Label(self.box4, text="Levels Left", bg=DARK_PURPLE, fg='white')
        b4_label.place(relx=0.5, rely=0.8, anchor='center')



class Learn_Characters:

    def __init__(self, master, clicked_mod):
        self.master = master
        master.title("Learning Characters")
        self.main_frame = tk.Frame(self.master, height=HEIGHT, width=WIDTH, bg='white', borderwidth=1)
        self.main_frame.pack()
        print(clicked_mod)

        self.training_set = []
        if clicked_mod == "Learn Vowels":
            self.training_set = VOWELS
        elif clicked_mod == "Learn Consonants":
            self.training_set = CONSONANTS
        else:
            self.training_set = MODIFIERS
        print(self.training_set)

        topborder = tk.Frame(self.main_frame, bg=CHAMPAGNE)
        topborder.place(relx=0, rely=0, relwidth=1, relheight=0.07)

        self.fontStyle = tkFont.Font(family="Lucida Grande", size=24)
        header = tk.Label(topborder, text=clicked_mod.upper(), fg='white', font=self.fontStyle, bg=CHAMPAGNE)

        header.place(relx=0.05, rely=0.2)
        instructions = tk.Label(self.main_frame,
                                text="On the left is the example character.\nPractice writing it on the right.",
                                fg=DESSERT_SAND)
        instructions.place(relx=0.4, rely=0.1)
        back = tk.Button(self.main_frame, text="<-", command=self.go_back)
        back.place(relx=0.05, rely=0.1)

        self.current_char = tk.StringVar()
        self.current_char.set(str(self.training_set[0]) + " [" + get_pronunciation(self.training_set[0]) + "]")

        self.character_frame = tk.Frame(self.main_frame, bg=MING, highlightthickness=6, highlightbackground="black")
        self.character_frame.place(relx=0.25, rely=0.2, width=400, height=190, anchor='n')
        char_font = tkFont.Font(family="Lucida Grande", size=90)
        self.char_label = tk.Label(self.character_frame, textvariable=self.current_char, font=char_font, bg=MING,
                                   fg='white')
        self.char_label.place(relx=0.5, rely=0.5, anchor='center')
        hear_char = Button(self.character_frame, text="Hear", bg=MING, fg='white', command=self.get_char_sound,
                           borderless=1)
        hear_char.place(relx=0.5, rely=0.1, anchor='n')

        self.canvas_frame = tk.Frame(self.main_frame, bg=DARK_CYAN, width=420, height=190, highlightthickness=6,
                                     highlightbackground="black")
        self.canvas_frame.place(relx=0.75, rely=0.2, anchor='n')
        self.practice_canvas = tk.Canvas(self.canvas_frame, bg=CHAMPAGNE, width=275, height=150)
        self.practice_canvas.place(relx=0.05, rely=0.08)
        self.image1 = Image.new('RGB', (275, 150), 'white')
        self.draw = ImageDraw.Draw(self.image1)
        self.practice_canvas.bind('<1>', self.activate_paint)
        self.old_x = None
        self.old_y = None

        clear_btn = Button(self.canvas_frame, text='Clear', command=self.clear, borderless=1)
        clear_btn.place(relx=0.85, rely=0.3, anchor='n')
        btn_save = Button(self.canvas_frame, text='Save', command=self.save, borderless=1)
        btn_save.place(relx=0.85, rely=0.5, anchor='n')

        self.example_frame = tk.Frame(self.main_frame, bg=LIGHT_GRAY)
        self.example_frame.place(relx=0.05, rely=0.6, relheight=0.25, relwidth=0.92)
        self.current_word = tk.StringVar()
        self.return_val = get_word_with_same_char(self.training_set[0])
        print(self.return_val)
        if self.return_val != "No Example Available":
            try:
                self.current_word.set(
                    self.return_val[0] + " : " + self.return_val[1] + "\n" + get_pronunciation(self.return_val[0]))
            except TypeError:
                self.current_word.set(
                    self.return_val[0][0] + " : " + self.return_val[0][1] + "\n" + get_pronunciation(
                        self.return_val[0][0]))
        else:
            self.current_word.set(self.return_val)
        word_example_font = tkFont.Font(family="Lucida Grande", size=30)
        self.current_word_label = tk.Label(self.example_frame, textvariable=self.current_word, font=word_example_font,
                                           bg=LIGHT_GRAY, fg='white')
        self.current_word_label.place(relx=0.5, rely=0.5, anchor='center')
        hear_word = Button(self.example_frame, text="Listen Word", bg=LIGHT_GRAY, fg='white',
                           command=self.get_word_sound)
        hear_word.place(relx=0.1, rely=0.7, anchor='center')

        bottomborder = tk.Frame(self.main_frame, bg=CHAMPAGNE)
        bottomborder.place(relx=0, rely=0.93, relwidth=1, relheight=0.07)
        self.back_btn = Button(bottomborder, text="Previous", bg='white', fg='black', borderless=1, command=self.prev)
        self.back_btn.place(relx=0.05, rely=0.2)
        self.next_btn = Button(bottomborder, text="Next", bg='white', fg='black', borderless=1, command=self.next)
        self.next_btn.place(relx=0.9, rely=0.2)

        self.index = 0

    def clear(self):
        self.practice_canvas.delete("line")
        self.image1 = Image.new('RGB', (250, 150), 'white')
        self.draw = ImageDraw.Draw(self.image1)

    def save(self):
        filename = "image_trial.png"
        self.image1.save(filename)
        print("Image got saved")

    def activate_paint(self, e):
        self.practice_canvas.bind('<B1-Motion>', self.paint)
        self.old_x = e.x
        self.old_y = e.y

    def paint(self, event):
        self.practice_canvas.create_line(self.old_x, self.old_y, event.x, event.y, width=5, tag='line')

        self.draw.line((self.old_x, self.old_y, event.x, event.y), fill='black', width=5)
        self.old_x = event.x
        self.old_y = event.y

    def next(self):
        if self.index == (len(self.training_set) - 1):
            self.index = 0
        else:
            self.index = self.index + 1
        self.current_char.set(
            str(self.training_set[self.index]) + " [" + get_pronunciation(self.training_set[self.index]) + "]")
        self.clear()
        self.return_val = get_word_with_same_char(self.training_set[self.index])

        if self.return_val != "No Example Available":
            try:
                self.current_word.set(
                    self.return_val[0] + " : " + self.return_val[1] + "\n" + get_pronunciation(self.return_val[0]))
            except TypeError:
                self.current_word.set(
                    self.return_val[0][0] + " : " + self.return_val[0][1] + "\n" + get_pronunciation(self.return_val[0][0]))
        else:
            self.current_word.set(self.return_val)

    def prev(self):
        if self.index == 0:
            self.index = (len(self.training_set) - 1)
        else:
            self.index = self.index - 1
        self.current_char.set(
            str(self.training_set[self.index]) + " [" + get_pronunciation(self.training_set[self.index]) + "]")
        self.clear()
        self.return_val = get_word_with_same_char(self.training_set[self.index])

        if self.return_val != "No Example Available":
            self.current_word.set(
                self.return_val[0] + " : " + self.return_val[1] + "\n" + get_pronunciation(self.return_val[0]))
        else:
            self.current_word.set(self.return_val)

    def get_word_sound(self):
        try:
            get_sound(self.return_val[0])
        except AttributeError:
            get_sound(self.return_val[0][0])

    def get_char_sound(self):
        get_sound(self.training_set[self.index])

    def go_back(self):
        self.main_frame.destroy()
        Dashboard(self.master, "Dashboard Window")


class Review_Characters:
    def __init__(self, master, clicked_mod):
        self.master = master
        master.title("Review Characters")
        self.main_frame = tk.Frame(self.master, height=HEIGHT, width=WIDTH, bg='white', borderwidth=1)
        self.main_frame.pack()
        self.clicked = clicked_mod

        topborder = tk.Frame(self.main_frame, bg=LIGHT_GRAY)
        topborder.place(relx=0, rely=0, relwidth=1, relheight=0.07)
        header_font = tkFont.Font(family="Lucida Grande", size=24)
        header_label = tk.Label(topborder, text="Review Characters".upper(), font=header_font, fg='white', bg=LIGHT_GRAY)
        header_label.place(relx=0.05, rely=0.2)

        instructions = tk.Label(self.main_frame,
                                text="Click the button below to see the answer.\nWhen you think you have memorized it, hit confirm",
                                fg=LIGHT_GRAY)
        instructions.place(relx=0.5, rely=0.2, anchor='center')

        self.current_char = tk.StringVar()
        self.answer = tk.StringVar()

        self.index = 0
        self.training_set = []
        if self.clicked == "Review Vowels":
            self.training_set = VOWELS
        elif self.clicked == "Review Consonants":
            self.training_set = CONSONANTS
        else:
            self.training_set = MODIFIERS

        self.learned_array = []

        self.card_frame = tk.Frame(self.main_frame, bg=CHAMPAGNE, highlightbackground=MING, highlightthickness=6)
        self.card_frame.place(relx=0.5, rely=0.5, anchor='center', relheight=0.4, relwidth=0.45)

        self.current_char.set(self.training_set[self.index])
        char_font = tkFont.Font(family="Lucida Grande", size=100)
        self.char_label = tk.Label(self.card_frame, textvariable=self.current_char, font=char_font, bg=CHAMPAGNE, fg='black')
        self.char_label.place(relx=0.5, rely=0.4, anchor='center')

        self.show_answer_btn = Button(self.card_frame, text="Show Answer", bg='white', fg='black', borderless=1, command=self.show_answer)
        self.show_answer_btn.place(relx=0.5, rely=0.8, anchor='center')

        # Buttons that will control the flow of cards seen
        self.prev_btn = Button(self.main_frame, text="Previous", bg=DARK_CYAN, fg='white', borderless=1, command=self.prev)
        self.prev_btn.place(relx=0.2, rely=0.5, anchor='center')
        self.next_btn = Button(self.main_frame, text="Next", bg=DARK_CYAN, fg='white', borderless=1, command=self.next)
        self.next_btn.place(relx=0.8, rely=0.5, anchor='center')

        bottomborder = tk.Frame(self.main_frame, bg=LIGHT_GRAY)
        bottomborder.place(relx=0, rely=0.93, relwidth=1, relheight=0.07)

        back = tk.Button(self.main_frame, text="Dashboard", command=self.go_back)
        back.place(relx=0.05, rely=0.1)

        # When card if flipped
        self.confirm_btn = Button(self.card_frame, text="Confirm", command=self.confirm)
        self.confirm_btn.place_forget()
        self.not_yet_btn = Button(self.card_frame, text="Not yet")
        self.not_yet_btn.place_forget()


    def show_answer(self):
        self.current_char.set(get_pronunciation(self.training_set[self.index]))
        self.show_answer_btn.place_forget()
        self.confirm_btn.place(relx=0.2, rely=0.8)
        self.not_yet_btn.place(relx=0.6, rely=0.8)

    def prev(self):
        if self.index == 0:
            self.index = (len(self.training_set) - 1)
        else:
            self.index = self.index - 1
        self.current_char.set(self.training_set[self.index])

        self.confirm_btn.place_forget()
        self.not_yet_btn.place_forget()
        self.show_answer_btn.place(relx=0.5, rely=0.8, anchor='center')



    def next(self):
        if self.index == (len(self.training_set) - 1):
            self.index = 0
        else:
            self.index = self.index + 1
        self.current_char.set(self.training_set[self.index])

        self.confirm_btn.place_forget()
        self.not_yet_btn.place_forget()
        self.show_answer_btn.place(relx=0.5, rely=0.8, anchor='center')


    def go_back(self):
        review_write(G_USERNAME, self.clicked, self.learned_array)
        self.main_frame.destroy()
        Dashboard(self.master, "Dashboard Window")

    def confirm(self):
        if self.training_set[self.index] not in self.learned_array:
            self.learned_array.append(self.training_set[self.index])


class Quiz:
    def __init__(self, master):
        self.master = master
        master.title("Quiz")
        self.main_frame = tk.Frame(self.master, height=HEIGHT, width=WIDTH, bg='white', borderwidth=1)
        self.main_frame.pack()
        self.module_list_frame = tk.Frame(self.main_frame, bg=LIGHT_GRAY)
        self.module_list_frame.place(relx=0.1, rely=0, relwidth=0.2, relheight=1, anchor='n')
        scrollbar = tk.Scrollbar(self.module_list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        question_list_font = tkFont.Font(family="Lucida Grande", size=16)

        self.mylist = tk.Listbox(self.module_list_frame, borderwidth=0, yscrollcommand=scrollbar.set, width=WIDTH,
                                 height=HEIGHT, font=question_list_font, bg=LIGHT_GRAY, fg='white')
        question_header_font = tkFont.Font(family="Lucida Grande", size=18)

        question_label = tk.Label(self.module_list_frame, text="Question List".upper(), font=question_header_font, bg=LIGHT_GRAY, fg='white')
        question_label.pack()
        i = 1
        while i <= 20:
            self.mylist.insert(tk.END, "Question: " + str(i))
            i = i + 1
        self.mylist.pack(padx=10, pady=10, fill="both", expand=True)
        scrollbar.config(command=self.mylist.yview)
        self.current_question = ""
        self.mylist.bind('<<ListboxSelect>>', self.click_button)  # basically list box on click listener

        self.header_font = tkFont.Font(family="Lucida Grande", size=48)
        self.header = tk.Label(self.main_frame, text="Quiz", fg=MING, font=self.header_font)
        self.header.place(relx=0.55, rely=0.1, anchor='center')

        self.inst_frame = tk.Frame(self.main_frame, bg=CHAMPAGNE, highlightbackground='black', highlightthickness=6)
        self.inst_frame.place(relx=0.25, rely=0.25, relheight=0.5, relwidth=0.65)
        instructions_font = tkFont.Font(family="Lucida Grande", size=18)
        instructions = tk.Label(self.inst_frame, text="There are 20 questions on this quiz.\nYou will be given a word which you will have to "
                                                      "\nspeak out loud to be graded", font=instructions_font, fg=DARK_PURPLE, bg=CHAMPAGNE)
        instructions.place(relx=0.5, rely=0.5, anchor='center')

        self.start_quiz = Button(self.inst_frame, text="Start Quiz", bg=MING, fg='white', borderless=1, command=self.start_quiz)
        self.start_quiz.place(relx=0.5, rely=0.8, anchor='center')

        filename = G_USERNAME + ".txt"
        self.question_bank = get_vowel_quiz(get_value_from_line(filename, 5))
        self.question_var = tk.StringVar()

        for i in self.question_bank:
            print(i[2])




    # display the clicked location
    def click_button(self, event):
        w = event.widget
        index = int(w.curselection()[0])
        self.current_question = w.get(index)
        self.current_question = self.current_question.split(": ")[1]
        string = self.question_bank[int(self.current_question)][2]
        self.question_var.set(string)

    def start_quiz(self):
        self.inst_frame.destroy()
        self.header.destroy()
        self.question_frame = tk.Frame(self.main_frame, bg=MING)
        self.question_frame.place(relx=0.55, rely=0.3, anchor='center', relheight=0.3, relwidth=0.55)
        self.current_question = 1
        self.question_var.set((self.question_bank[self.current_question][2]))
        self.user_question = tk.Label(self.question_frame, textvariable=self.question_var, bg=MING, fg='white', font=self.header_font)
        self.user_question.place(relx=0.5, rely=0.3, anchor='center')

        self.user_answer_txt = tk.StringVar()
        self.user_answer_txt.set("You said: ")
        self.answer_frame = tk.Frame(self.main_frame, bg=CHAMPAGNE)
        self.answer_frame.place(relx=0.55, rely=0.6, anchor='center', relheight=0.3, relwidth=0.55)
        self.user_answer_label = tk.Label(self.answer_frame, textvariable=self.user_answer_txt, bg=CHAMPAGNE, fg=DARK_PURPLE)
        self.user_answer_label.place(relx=0.5, rely=0.5, anchor='center')

        self.record_btn = tk.Button(self.main_frame, text="Record", bg=DARK_CYAN, fg='white', command=self.record)
        self.record_btn.place(relx=0.4, rely=0.8)
        self.listen_btn = tk.Button(self.main_frame, text="Listen", command=self.listen)
        self.listen_btn.place(relx=0.6, rely=0.8)

    def record(self):
        try:
            self.captured_text = capture().lower()
            self.user_answer_txt.set("You said: " + self.captured_text)
        except Exception:
            print("Error")

    def listen(self):
        speak(self.user_answer_txt.get())