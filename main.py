from tkinter import *

# --------------- CONSTANTS ---------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
PRIMARY_DARKEST = "#000000"
FONT_NAME = "Courier"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# --------------- UI SETUP ---------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=PRIMARY_DARKEST)

title = Label(text="Timer", fg=GREEN, bg=PRIMARY_DARKEST,
              font=(FONT_NAME, 50, "bold"))
title.grid(column=1, row=0)


canvas = Canvas(width=300, height=150, highlightthickness=0)
bg = PhotoImage(file="bg.png")
canvas.create_image(150, 75, image=bg)
canvas.create_text(150, 70, text="00:00", fill="white",
                   font=(FONT_NAME, 50, "bold")
                   )
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

check_marks = Label(text="✔", fg=GREEN, bg=PRIMARY_DARKEST)
check_marks.grid(column=1, row=3)


window.mainloop()
