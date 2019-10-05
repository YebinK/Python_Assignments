print("20161089 김예빈")

monthString = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
day_30 = [4, 6, 9, 11]  #30일로 끝나는 달
day_28 = [2]            #28일로 끝나는 달

while True:

    month = input("월을 입력하세요. (종료 시 엔터키 입력) : ", ) #입력

    if month == '':
        break

    if isinstance(month, str) : #입력한 month 값이 string type이면 int type으로 변환
        for i in range(12) :
            if monthString[i] == month :
                month = i + 1
                break

    month = int(month)

    if month in day_30 :
        day = 30
    elif month in day_28 :
        day = 28
    else :
        day = 31

    if month in (4, 7) : #월요일로 시작하는 달
        space = 1
        cut = 6
    elif month in (1, 10) : #화요일로 시작하는 달
        space = 2
        cut = 5
    elif month == 5 :
        space = 3
        cut = 4
    elif month == 8 :
        space = 4
        cut = 3
    elif month in (2, 3, 11) :
        space = 5
        cut = 2
    elif month == 6 :
        space = 6
        cut = 1
    else :
        space = 0
        cut = 7

    print("\n", " "*5, "2019 년", month, "월", "\n")
    print(" 일\t 월\t 화\t 수\t 목\t 금\t 토")

    j = 0

    for i in range(day):
        print('\t' * space, i+1, end='\t')
        j += 1
        if (j == cut) :
            print("\n")
            j = 0
            cut = 7
        space = 0

    print("\n")
