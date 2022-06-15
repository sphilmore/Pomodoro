import math
from tkinter import *
from PIL import ImageTk, Image

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
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(1000)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_marks.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN *60
    short_break_sec = SHORT_BREAK_MIN *60
    long_break_sec = LONG_BREAK_MIN * 60
    add=0
    if reps %8 ==0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)

    elif reps %2==0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)

    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)












# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count %60

    if count_sec<10:
        count_sec =f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >0:
        window.after(1000, count_down, count-1)
    else:
        start_timer()
        reps = 4
        marks =""
        work_sessions =math.floor(reps/2)
        for _ in range(work_sessions):
          marks +="✔"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------
#
window= Tk()
window.title("Pomdoro")
window.config(padx=100,pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0 )
tomato_img = ImageTk.PhotoImage(Image.open("tomato.png"))
canvas.create_image(100, 112, image=tomato_img)
timer_text=canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
timer_label = Label(text="Timer", fg=GREEN, font=("Arial", 30,"bold"), bg=YELLOW, highlightthickness=0 )
timer_label.grid(column=1, row=0)
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text='Reset', command=reset_timer)
reset_button.grid(column=3, row=2)
check_marks = Label( fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()





