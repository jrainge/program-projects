# Justin Rainge, CIS 345, iCourse, FinalProject
from tkinter import *
from tkinter import ttk
import random
import os
import difflib

list_data = []
question_list = []
points = (1,2,3)
point_value=random.choice(points)

def start_quiz():
    global question_index,question_list,quiz_button,window,right,number_of_questions,points,point_value
    class Question:
        def __init__(self, question_number, option, correct_answer):
            self.quest = question_number
            self.options = option
            self.correct_answer = correct_answer

        def check_answer(self, choice, quiz_view):
            global right,points
            if (choice == self.correct_answer):
                quiz_label = Label(quiz_view, text="That is the correct answer!")
                right += point_value
                points += point_value
            else:
                quiz_label = Label(quiz_view, text=f"Wrong Answer! the correct answer is {self.correct_answer}")
                points += point_value
            quiz_label.pack()
            quiz_view.after(1000, lambda *args: self.quiz_screen(quiz_view))

        def display_choices(self, window):
            global point_value
            quiz_view = Frame(window)
            Label(quiz_view, text= str(point_value) + " " + "Points").pack()
            Label(quiz_view, text=self.quest).pack()
            Button(quiz_view, text=self.options[0], command=lambda *args: self.check_answer("A", quiz_view),width =50).pack()
            Button(quiz_view, text=self.options[1], command=lambda *args: self.check_answer("B", quiz_view),width =50).pack()
            Button(quiz_view, text=self.options[2], command=lambda *args: self.check_answer("C", quiz_view),width =50).pack()
            Button(quiz_view, text=self.options[3], command=lambda *args: self.check_answer("D", quiz_view),width =50).pack()
            return quiz_view

        def quiz_screen(self, quiz_view):
            quiz_view.pack_forget()
            display_questions()

    def display_questions():
        global question_list, window, question_index, quiz_button, right, number_of_questions,points,point_value
        if (question_index==2):
            Label(window, text="Thank you for taking the quiz." + " You have earned " + str(right) + " out of " + str(points)).pack()
            return
        quiz_button.pack_forget()
        question_index += 1
        random.shuffle(question_list)
        question_list[question_index].display_choices(window).pack()

    question_list = []
    file = open("questions.txt", "r")
    question_line = file.readline()
    while (question_line != ""):
        question_item = question_line
        choices = []
        for i in range(4):
            choices.append(file.readline())
        correct_choice = file.readline()
        correct_choice = correct_choice[:-1]
        question_list.append(Question(question_item, choices, correct_choice))
        question_line = file.readline()
    file.close()
    question_index = -1
    right = 0
    points = 0
    number_of_questions = len(question_list)

    window = Tk()
    window.title("Quiz")
    window.geometry("400x400")
    quiz_button = Button(window, text="Thank you for choosing to take this quiz!!\n Please press here to continue",command=display_questions)
    quiz_button.pack()
    window.mainloop()


def display_data():
    global list_data
    list_data = []
    with open("questions.txt", "r") as file:
        for fp in file:
            listbox.insert(END, fp.strip())
            list_data.append(fp.strip())
        print(list_data)

def add_data():
    global list_data
    listbox.insert(END, item_entry.get())
    list_data.append(item_entry.get())

def delete_selected():
    global list_data
    selected = listbox.get(listbox.curselection())
    listbox.delete(ANCHOR)
    list_data.pop(list_data.index(selected))

def save():
    global root
    with open("questions.txt", "w",) as file:
        for d in list_data:
	        file.write(d + "\n")

def update():
    global list_data
    selected = listbox.curselection()[0]
    listbox.delete(ANCHOR)
    listbox.insert(selected, item_entry.get())
    list_data[selected]=item_entry.get()

def clear_form():
    global item_entry
    item_entry.set('')

def item_selected(event):
    global listbox, select_index
    select_index = listbox.curselection()[0]
    edit_question = list_data[select_index]
    item_entry.set(edit_question)


def search_question():
    global question_list , entry , answer , search_entry
    def search():
        global question_list
        question_list = []
        search_input = difflib.get_close_matches(entry.get(),question_list,6,0.5)
        with open('questions.txt', 'r') as fp:
            for line in fp:
                question_list = line.strip()
                listbox.insert(END, question_list)
            print(search_input)

    root = Tk()
    root.title("Search")
    root.geometry("400x400")
    search_entry = StringVar()
    entry = Entry(root, textvariable=search_entry, width=40)
    entry.pack()
    button = Button(root, text="Search", command=search)
    button.pack()
    listbox = Listbox(root, width=50)
    listbox.bind()
    listbox.pack()

   
def read_me():
    def retrievedata():
        global read_data
        read_data = []
        with open("README.txt", "r") as file:
            for f in file:
                listbox.insert(END, f.strip())
                read_data.append(f.strip())
            print(read_data)
    root = Tk()
    root.title("README")
    root.geometry("400x400")
    listbox = Listbox(root, width = 120)
    listbox.bind('<Double-Button-1>', item_selected)
    listbox.pack()
    retrievedata()
    root.mainloop()


root = Tk()
root.title("Quiz Management System")
root.geometry("400x400")
menu_bar=Menu(root)
root.config(menu=menu_bar)

item_entry = StringVar()
file_menu= Menu(tearoff=False)
menu_bar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Start Quiz', command = start_quiz)
file_menu.add_command(label='README', command = read_me)
file_menu.add_command(label='Search', command = search_question)

entry = Entry(root, textvariable=item_entry,width=30)
entry.pack()

button = Button(root, text="Add Item", command=add_data)
button.pack()

button_update = Button(text="Update", command=update)
button_update.pack()

button_save = Button(root, text="Save", command=save)
button_save.pack()

delete_item = Button(text="Delete Item", command=delete_selected)
delete_item.pack()

listbox = Listbox(root , width=50)
listbox.bind('<Double-Button-1>', item_selected)
listbox.pack()


display_data()
root.mainloop()
