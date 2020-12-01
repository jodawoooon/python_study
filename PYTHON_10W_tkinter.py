# -*- coding: utf-8 -*-
"""
Created on Mon May 18 21:30:45 2020

@author: DaunJO
"""


## 1. Tic-Tac-Toc 게임

from tkinter import *

def checked(i): #i번째버튼 검사
    global player
    button = list[i]
    
    
    if button["text"] != "          ":
        return
    
    button["text"] = "     " +player+"     "
    button["bg"] = "yellow"
    
    if player == "X":
        player = "O"
        button["bg"] = "yellow"
    else:
        player = "X"
        button["bg"] = "lightgreen"
        

window = Tk()
player = "X"
list = []



for i in range(0,9):
    b = Button(window, text = "          ", command = lambda k=1: checked(k))
    b.grid(row = i//3, column = i%3)
    list.append(b)
    
window.mainloop()
    

## 2. 레이블과 버튼 배치

from tkinter import *

window = Tk()
colors = ['green', 'red', 'orange', 'white', 'yellow', 'blue']

r = 0

for c in colors:
    Label(window, text=c, relief=RIDGE, width=20).grid(row=r, column=0)
    Button(window, bg=c, width=15).grid(row=r, column=1)
    r=r+1
    
window.mainloop()

## 3. 스톱워치

from tkinter import *

def Timer():
    if(running):
        global timer

        timer += 1
        timeTxt.configure(text=str(timer))
    window.after(10, Timer)
    
def start():
    global running
    running = True
    
def stop():
    global running
    running = False
    

running = False
window = Tk()
timer = 0
timeTxt = Label(window, text="0", font=("Helvetica", 80))
timeTxt.pack()

startButton= Button(window, text="시작", bg="yellow", command = start)
startButton.pack(fill=BOTH)

stopButton= Button(window, text="중지", bg="yellow", command = stop)
stopButton.pack(fill=BOTH)

Timer()
window.mainloop()


## 4. 계산기

from tkinter import *

def click(key):
    if key == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, END)
            entry.insert(END, str(result))
        except:
            entry.insert(END, "오류")
    elif key == "C":
        entry.delete(0, END)
    else:
        entry.insert(END, key)

window = Tk()
window.title("간단한 계산기")


button = [
    '7', '8', '9', '+', 'C',
    '4', '5', '6', '-', '  '
    '1', '2', '3', '*', '  '
    '0', '.', '=', '/', '  ']


i=0
for b in button:
    cmd = lambda x=b: click(x)
    bt = Button(window, text=b, width=5, relief='ridge', command =cmd)
    bt.grid(row=i//5+1, column=i%5)
    i +=1
    
entry = Entry(window, width = 30, bg="yellow")
entry.grid(row=0, column = 0, columnspan=5)

window.mainloop()


## 5. 숫자 추측게임

from tkinter import *
import random



answer = random.randint(1, 100)

def guessing():
    guess = int(guessField.get())
    
    if guess > answer:
        msg = "높다"
    elif guess < answer:
        msg = "낮다"
    else:
        msg = "정답"
        
    resultLabel["text"] = msg
    guessField.delete(0,5)
    
def reset():
    global answer
    answer = random.randint(1, 100)
    resultLabel["text"] = "다시 한번"


window = Tk()
window.configure(bg="white")
window.title("숫자를 맞춰보세요")
window.geometry("500x80")

titleLabel = Label(window, text="숫자 게임에 오신걸 환영합니다", bg="white")
titleLabel.pack()

guessField = Entry(window)
guessField.pack(side="left")

tryButton = Button(window, text= "시도", fg="green", bg="white", command=guessing)
tryButton.pack(side="left")

resetButton = Button(window, text= "초기화", fg="red", bg="white", command=reset)
resetButton.pack(side="left")

resultLabel = Label(window, text="1부터 100 사이의 숫자를 입력", bg="white")

resultLabel.pack(side="left")


window.mainloop()
