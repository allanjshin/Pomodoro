
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_id = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer_id)
    title_label.config(text=f"Timer", fg=GREEN)
    canvas.itemconfigure(canvas_text, text="00:00")
    check_mark.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def count_down(count):
    marks = ""
    # print(count)
    count_min = math.floor(count / 60)
    count_sec = count % 60
    global timer_id

    canvas.itemconfigure(canvas_text, text=f"{count_min:02}:{count_sec:02}")
    if count > 0:
        timer_id = window.after(1000, count_down, count-1)
    else:
        start_timer()
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✔"
            check_mark.config(text=marks)

def start_timer():
    global reps
    reps += 1


    if reps % 8 in (1, 3, 5, 7):
        count_down(WORK_MIN * 60)
        title_label.config(text=f"{reps}:WORK", fg=GREEN)
    elif reps % 8 in (2, 4, 6):
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text=f"{reps}:Break", fg=PINK)

    else:
        count_down(LONG_BREAK_MIN * 60, fg=RED)
        title_label.config(text=f"{reps}:Break", fg=RED)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.minsize(width=300, height=300)
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
title_label.grid(row=0, column = 1)

start_button = Button(text="Start")
start_button.config(font=FONT_NAME, width=5, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.config(font=FONT_NAME, width=5)
reset_button.grid(row=2, column=2)

check_mark = Label(text="")
check_mark.config(fg=GREEN, bg=YELLOW)
check_mark.grid(row=3, column = 1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas_text = canvas.create_text(100, 138, text = "00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)




window.mainloop()