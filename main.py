from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"

# --------------------- FLASH CARD RANDOMIZATION ------------------------ #
df = pd.read_csv('./data/word_meanings.csv')
word_dict = df.to_dict('records')
rand_word = {}


def random_card():
    '''Generate random word for cards'''
    global rand_word, flip_timer
    window.after_cancel(flip_timer)
    rand_word = random.choice(word_dict)
    canvas.itemconfig(heading, text='Word', fill="black")
    canvas.itemconfig(
        word, text=rand_word['WORD'], fill="black", font=("Ariel", 60, "bold"))
    canvas.itemconfig(canvas_img, image=card_white_img)
    flip_timer = window.after(3000, func=flip_card)


# --------------------- FLIP CARD ------------------------ #
def flip_card():
    canvas.itemconfig(heading, text='Meaning', fill="white")
    canvas.itemconfig(
        word, text=rand_word['MEANING'], fill="white", font=("Ariel", 30, "bold"))
    canvas.itemconfig(canvas_img, image=card_green_img)


# --------------------- UI SETUP ------------------------ #
# Creating a window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Creating a Canvas
canvas = Canvas(height=526, width=800,
                bg=BACKGROUND_COLOR, highlightthickness=0)
# Importing card image
card_white_img = PhotoImage(file='./images/card_front.png')
card_green_img = PhotoImage(file='./images/card_back.png')
canvas_img = canvas.create_image(400, 263, image=card_white_img)
canvas.grid(row=0, column=0, columnspan=2)

# Texts on canvas
heading = canvas.create_text(
    400, 150, text='', fill="black", font=("Ariel", 40, "italic"))
word = canvas.create_text(
    400, 263, text='', fill="black", font=("Ariel", 60, "bold"))
random_card()

# Creating the btns
wrong = PhotoImage(file="./images/wrong.png")
button_w = Button(image=wrong, highlightthickness=0,
                  borderwidth=0, command=random_card)
button_w.grid(row=1, column=0)

correct = PhotoImage(file="./images/right.png")
button_c = Button(image=correct, highlightthickness=0,
                  borderwidth=0, command=random_card)
button_c.grid(row=1, column=1)

window.mainloop()
