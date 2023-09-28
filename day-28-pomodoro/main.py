from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.1
REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global REPS
    REPS += 1
    work_sec = round(WORK_MIN * 60)
    short_break_sec = round(SHORT_BREAK_MIN * 60)
    long_break_sec = round(LONG_BREAK_MIN * 60)

    if REPS > 8:
        reset()
    elif REPS == 8:
        timer_title.config(text="Long break", fg=RED)
        # 8th rep
        count_down(long_break_sec)

    elif REPS % 2 == 0:
        timer_title.config(text="Break :)", fg=PINK)
        # 2nd, 4th, 6th rep
        count_down(short_break_sec)

    else:
        timer_title.config(text="Work bro", fg=GREEN)
        # 1st, 3rd, 5th, 7th rep
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="0:00")
    timer_title.config(text="Timer", fg=GREEN)
    checkmarks.config(text="")
    global REPS
    REPS = 0

def count_down(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60

    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    # can't directly edit timer_text because it's in a canvas
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global timer
        # after 1sec, call count_down (itself) again but with count minus 1
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmarks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodorooooo")
window.config(padx=100, pady=50, background=YELLOW)

timer_title = Label(text="Timer", font=(FONT_NAME, 36), bg=YELLOW, fg=GREEN)
timer_title.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomat = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomat)
timer_text = canvas.create_text(100, 130, text="0:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

button = Button(text="Start", command=start_timer, highlightbackground=YELLOW)
button.grid(column=0, row=2)

checkmarks = Label(text="", font=(FONT_NAME, 36), bg=YELLOW, fg=GREEN)
checkmarks.grid(column=1, row=3)

button = Button(text="Reset", command=reset, highlightbackground=YELLOW)
button.grid(column=2, row=2)


window.mainloop()