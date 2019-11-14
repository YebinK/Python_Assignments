from tkinter import *
from korean_lunar_calendar import KoreanLunarCalendar
import calendar

window = Tk()
weekList = ('월', '화', '수', '목', '금', '토', '일')

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
    global yearInput
    global monthInput
    if monthInput < 12:
        monthInput += 1
    else:                   #monthInput == 12
        yearInput += 1
        monthInput = 1
    makeCalendar(yearInput, monthInput)

leftBtn = Button(window, text="<", command=leftBtn)
rightBtn = Button(window, text=">", command=rightBtn)

leftBtn.pack(side=LEFT)
rightBtn.pack(side=RIGHT)            
    
def makeCalendar(yearInput, monthInput):
    global dateFrame
    global c
    for child in dateFrame.winfo_children():
        child.destroy()

    print(yearInput, monthInput)

    title["text"] = "{}년 {}월".format(yearInput, monthInput)
    c = calendar.month(yearInput, monthInput)
    lunar_c = KoreanLunarCalendar()
   # lunar.setSolarDate(2017, 6, 24)
    #print(lunar.LunarIsoFormat())
    dateIndex = c.find('Su')
    c = c[dateIndex + 2:]
    index = 0
    for i in range(6):
        for j in range(7):
            day = c[index:index+3]
            day = day.replace('\n', '')
            if day.strip() != '':               #day가 비어있지 않으면 음력 추가
                lunar_day = day.strip()
                lunar_day = int(lunar_day)
                lunar_c.setSolarDate(yearInput, monthInput, lunar_day)
                lunar_day = lunar_c.LunarIsoFormat()
                lunar_index = lunar_day.find('-')
                lunar_day = lunar_day[lunar_index+1:]
                lunar_day = lunar_day.replace('-', '.')
                day = day + '\n' + lunar_day
            name = Button(dateFrame, text = day)
            name.grid(row=i, column=j)
            if index + 3 <= len(c): index += 3
        if index >= len(c): break
    return c

yearInput = int(input("년도를 입력하세요: "))
monthInput = int(input("월을 입력하세요: "))

title = Label(window, text="{}년 {}월".format(yearInput, monthInput))
week = Label(window, text=weekList)
dateFrame = Frame(window, width=3000, height=1000)

c = makeCalendar(yearInput, monthInput)

title.pack()
week.pack()
dateFrame.pack()

window.mainloop()
