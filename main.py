"""
Tile matching game tutorial: https://www.youtube.com/watch?v=tlMPVGSEEDw&
"""

from tkinter import *
from tkinter import messagebox
from random import shuffle
from time import sleep

root = Tk()
root.title("Mamory game")
root.geometry("600x350")

global winner
winner = 0


matches = [
    1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6,
]

shuffle(matches)
# print(matches)

# define some variables
count = 0
answer_list = []
answer_dict = {}

# reset game
def reset():
    global matches
    global winner

    shuffle(matches)
    
    my_label.config(text="")
    
    


def win():
    my_label.config(text="Congratulations! You win!")
    button_list = [b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, ]
    for button in button_list:
        button.config(text=" ")


def button_click(b, number):  # fun to click buitttons
    global count
    global answer_dict
    global answer_list
    global winner

    if (b["text"] == ' ') and (count < 2):
        b["text"] = matches[number]
        answer_list.append(number)  # add number to answer_list, to keep track
        answer_dict[b] = matches[number]  # add number to answer_dict, to keep track
        count += 1  # increment counter
        # print(answer_list, answer_dict)

    # check if the tiles numbers are same
    if len(answer_list) == 2:
        if matches[answer_list[0]] == matches[answer_list[1]]:
            my_label.config(text="MATCH!")
            for key in answer_dict:
                key["state"] = "disabled"
            count = 0
            answer_dict = {}
            answer_list = []
            # increment winner counter
            winner += 1
            if winner == 6:
                win()
        else:
            my_label.config(text="DOH!")

            count = 0
            answer_list = []
            messagebox.showinfo("inc!", "inc!")
            for key in answer_dict:
                key["text"] = " "

            answer_dict = {}


# create button frame
my_frame = Frame(root)
my_frame.pack(pady=10)

# buttons def
b0 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3,
            width=6, command=lambda: button_click(b0, 0), relief="groove", )
b1 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3,
            width=6, command=lambda: button_click(b1, 1), relief="groove", )
b2 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3,
            width=6, command=lambda: button_click(b2, 2), relief="groove", )
b3 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3,
            width=6, command=lambda: button_click(b3, 3), relief="groove", )
b4 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3,
            width=6, command=lambda: button_click(b4, 4), relief="groove", )
b5 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3,
            width=6, command=lambda: button_click(b5, 5), relief="groove", )
b6 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3,
            width=6, command=lambda: button_click(b6, 6), relief="groove", )
b7 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3,
            width=6, command=lambda: button_click(b7, 7), relief="groove", )
b8 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3,
            width=6, command=lambda: button_click(b8, 8), relief="groove", )
b9 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3,
            width=6, command=lambda: button_click(b9, 9), relief="groove", )
b10 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3,
             width=6, command=lambda: button_click(b10, 10), relief="groove", )
b11 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3,
             width=6, command=lambda: button_click(b11, 11), relief="groove", )

# grid buttons
b0.grid(row=0, column=0)
b1.grid(row=0, column=1)
b2.grid(row=0, column=2)
b3.grid(row=0, column=3)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=1, column=3)

b8.grid(row=2, column=0)
b9.grid(row=2, column=1)
b10.grid(row=2, column=2)
b11.grid(row=2, column=3)

my_label = Label(root, text="")
my_label.pack(pady=20)

root.mainloop()
