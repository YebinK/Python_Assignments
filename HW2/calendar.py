from tkinter import *
import calendar

def makeCalendar(yearInput, monthInput):
    print(yearInput, monthInput)
    global c
    c = calendar.month(yearInput, monthInput)
    dateIndex = c.find('Su')
    c = c[dateIndex + 2:]
    return c

def leftBtn():
    global yearInput
    global monthInput
    if monthInput > 1:
        monthInput -= 1
    else:                   #monthInput == 1
        yearInput -= 1
        monthInput = 12
    makeCalendar(yearInput, monthInput)
    
def rightBtn():
    print("RIGHT")
    global yearInput
    global monthInput
    if monthInput < 12:
        monthInput += 1
    else:                   #monthInput == 12
        yearInput += 1
        monthInput = 1
    makeCalendar(yearInput, monthInput)

yearInput = int(input("년도를 입력하세요: "))
monthInput = int(input("월을 입력하세요: "))

c = makeCalendar(yearInput, monthInput)
print("START", c, "END")

weekList = ['월', '화', '수', '목', '금', '토', '일']

window = Tk()

title = Label(window, text="{}년 {}월".format(yearInput, monthInput))
week = Label(window, text=weekList)
dateFrame = Frame(window, width=1600, height=500)

index = 0
for i in range(5):
    for j in range(7):
        day = c[index:index+3]
        name = Button(dateFrame, text = day)
        name.grid(row=i, column=j)
        if index + 3 <= len(c): index += 3
        

leftBtn = Button(window, text="<", command=leftBtn)
rightBtn = Button(window, text=">", command=rightBtn)

leftBtn.pack(side=LEFT)
title.pack()
rightBtn.pack(side=RIGHT)
week.pack()
dateFrame.pack()



window.mainloop()
