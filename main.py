from tkinter import *

# --------------- CONSTANTS ---------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# --------------- UI SETUP ---------------- #

window = Tk()
window.title("Pomodoro")


canvas = Canvas(width=1000, height=666)
bg = PhotoImage(file="bg.png")
canvas.create_image(500, 333, image=bg)
canvas.pack()


window.mainloop()
