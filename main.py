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

reps = 0

# --------------- TIMER MECHANISM ---------------- #


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        # title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        # title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        # title_label.config(text="Work", fg=GREEN)

# --------------- COUNTDOWN MECHANISM ---------------- #


def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()


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
timer_text = canvas.create_text(150, 70, text="00:00", fill="white",
                                font=(FONT_NAME, 50, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

check_marks = Label(text="✔", fg=GREEN, bg=PRIMARY_DARKEST)
check_marks.grid(column=1, row=3)


window.mainloop()
