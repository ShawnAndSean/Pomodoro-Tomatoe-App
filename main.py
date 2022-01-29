
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

from tkinter import*

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
	global timer
	window.after_cancel(timer) #CANCELING THE WINDOW AFTER SOME TIME
	#timer_text 00:00
	canvas.itemconfig(timer_text,text = "00:00")
	#title_label = "Timer"
	main_text.config(text = "Timer", fg = GREEN)
	#reset check
	check.config(text = "")
	global reps #ENABLES REPS TO BE GLOBAL EVEN INSIDE A FUNCTION
	reps = 0
	timer = None





# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
	global reps  # makes reps a global variable
	reps += 1
	work = WORK_MIN *60
	long_rest = LONG_BREAK_MIN *60
	rest = SHORT_BREAK_MIN * 60
	if reps %8 ==0:
		count_down(long_rest)
		main_text.config(text = "Long Rest", fg = GREEN)
	elif reps % 2 == 0 and reps%8==0:
		count_down(rest)
		main_text.config(text = "Short Rest", fg = PINK)
	else:
		count_down(work)
		main_text.config(text = "Work Time" ,  fg = RED)
	#in minutes
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

import math
def count_down(count_from):
	minute = math.floor(count_from/ 60)
	seconds = count_from % 60
	if count_from == 0:
		count_from = "00"
	if seconds<10:
		seconds= f"0{seconds}"
	canvas.itemconfig(timer_text , text=f"{minute}:{seconds}")
	if count_from > 0:
		global timer
		# call method, then pass count_from
		# 1000 millisecond for 1 second. Will wait for 1 second, call count_down, then it will count_from
		timer = window.after(1000 , count_down,count_from-1)
	else:
		start_timer()
		marks = ""
		work_sessions = math.floor(reps/2)
		for _ in range(work_sessions):
			marks+="✔"
		check.config(text = marks)

# ---------------------------- UI SETUP ------------------------------- #fr
# fg for foreground or text colors. bg for background colors

window = Tk()
window.title("Pomodoro App for Productivity")
window.config(padx = 100,pady = 100, bg = YELLOW)

#timer title
main_text = Label(text = "TIMER", font =(FONT_NAME,35,"bold"),fg = GREEN, bg = YELLOW)
main_text.grid(column = 1, row = 0)
tomato_photo = PhotoImage(file = "tomato.png")

#checks
check = Label(text = "", font =(FONT_NAME,13,"bold"),fg = GREEN, bg = YELLOW)
check.grid(column = 1, row = 3)

#button
start = Button(text = "Start", font =(FONT_NAME,13,"bold"),bg = "white",command = start_timer,highlightthickness = 0)
start.grid(column = 0, row = 2)

reset = Button(text = "Reset", font =(FONT_NAME,13,"bold"),bg = "white",highlightthickness = 0, command = reset_timer)
reset.grid(column = 2, row = 2)

#highlightthickness is there to remove the highlight square of the image.
canvas = Canvas(width = 203, height = 224 , bg = YELLOW , highlightthickness = 0)
canvas.create_image(103, 112, image = tomato_photo)

#timer_text is the text inside the tomato.
timer_text = canvas.create_text(103,130, text = "00:00", fill = "white", font = (FONT_NAME,35,"bold"))

#website called color hunt for hexes
canvas.grid(column = 1, row = 1)



window.mainloop()