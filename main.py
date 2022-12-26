from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

# --------------------- UI SETUP ------------------------ #
# Creating a window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Creating a Canvas
canvas = Canvas(height=526, width=800,
                bg=BACKGROUND_COLOR, highlightthickness=0)
# Importing card image
card_white_img = PhotoImage(file='./images/card_front.png')
canvas.create_image(400, 263, image=card_white_img)
canvas.grid(row=0, column=0, columnspan=2)

# Texts on canvas
heading = canvas.create_text(
    400, 150, text='Title', fill="black", font=("Ariel", 40, "italic"))
word = canvas.create_text(
    400, 263, text='word', fill="black", font=("Ariel", 60, "bold"))

# Creating the btns
wrong = PhotoImage(file="./images/wrong.png")
button_w = Button(image=wrong, highlightthickness=0, borderwidth=0)
button_w.grid(row=1, column=0)

correct = PhotoImage(file="./images/right.png")
button_c = Button(image=correct, highlightthickness=0, borderwidth=0)
button_c.grid(row=1, column=1)

window.mainloop()
