import turtle

def ans_1():
    josh = turtle.Turtle()
    FONTSIZE = 18
    FONT = ('Arial', FONTSIZE, 'normal')
    turtle.write('1', font=FONT)
    turtle.mainloop()
    done()

def ans_2():
    josh = turtle.Turtle()
    FONTSIZE = 18
    FONT = ('Arial', FONTSIZE, 'normal')
    turtle.write('2', font=FONT)
    turtle.mainloop()
    done()

def ans_3():
    josh = turtle.Turtle()
    FONTSIZE = 18
    FONT = ('Arial', FONTSIZE, 'normal')
    turtle.write('3', font=FONT)
    turtle.mainloop()
    done()

def ans_4():
    josh = turtle.Turtle()
    FONTSIZE = 18
    FONT = ('Arial', FONTSIZE, 'normal')
    turtle.write('4', font=FONT)
    turtle.mainloop()
    done()

def ans_5():
    josh = turtle.Turtle()
    FONTSIZE = 18
    FONT = ('Arial', FONTSIZE, 'normal')
    turtle.write('5', font=FONT)
    turtle.mainloop()
    done()

def ans_6():
    josh = turtle.Turtle()
    FONTSIZE = 18
    FONT = ('Arial', FONTSIZE, 'normal')
    turtle.write('6', font=FONT)
    turtle.mainloop()
    done()

def ans_7():
    josh = turtle.Turtle()
    FONTSIZE = 18
    FONT = ('Arial', FONTSIZE, 'normal')
    turtle.write('7', font=FONT)
    turtle.mainloop()
    done()

def ans_8():
    josh = turtle.Turtle()
    FONTSIZE = 18
    FONT = ('Arial', FONTSIZE, 'normal')
    turtle.write('8', font=FONT)
    turtle.mainloop()
    done()

def ans_9():
    josh = turtle.Turtle()
    FONTSIZE = 18
    FONT = ('Arial', FONTSIZE, 'normal')
    turtle.write('9', font=FONT)
    turtle.mainloop()
    done()

def ans_10():
    josh = turtle.Turtle()
    FONTSIZE = 18
    FONT = ('Arial', FONTSIZE, 'normal')
    turtle.write('10', font=FONT)
    turtle.mainloop()
    done()

answer = input('pick a number 1-10  ==============>>>> ')
print("You Entered", answer)
if answer == "1":
    ans_1()
elif answer == "2":
    ans_2()
elif answer == "3":
    ans_3()
elif answer == "4":
    ans_4()
elif answer == "5":
    ans_5()
elif answer == "6":
    ans_6()
elif answer == "7":
    ans_7()
elif answer == "8":
    ans_8()
elif answer == "9":
    ans_9()
elif answer == "10":
    ans_10()
else:
    print("Invalid Input")
  
    




   
def nine(d):
    point = pos()
    fd(d)
    rt(90)
    fd(d*2)
    bk(d)
    rt(90)
    fd(d)
    rt(90)
    fd(d)
    pu()
    goto(point)
    pd()
    setheading(0)

def eight(d):
    point = pos()
    fd(d)
    rt(90)
    fd(d*2)
    for i in range(3):
        rt(90)
        fd(d)
    bk(d)
    lt(90)
    fd(d)
    pu()
    goto(point)
    pd()
    setheading(0)

def seven(d):
    point = pos()
    fd(d)
    rt(90)
    fd(d*2)
    bk(d*2)
    lt(90)
    bk(d)
    pu()
    goto(point)
    pd()
    setheading(0)

def six(d):
    point = pos()
    fd(d)
    bk(d)
    rt(90)
    fd(d*2)
    for i in range(3):
        lt(90)
        fd(d)
    rt(90)
    fd(d)
    pu()
    goto(point)
    pd()
    setheading(0)

def five(d):
    point = pos()
    fd(d)
    bk(d)
    rt(90)
    fd(d)
    lt(90)
    fd(d)
    for i in range(2):
        rt(90)
        fd(d)
    pu()
    goto(point)
    pd()
    setheading(0)

def four(d):
    point = pos()
    rt(90)
    fd(d)
    for i in range(2):
        lt(90)
        fd(d)
    bk(d * 2)
    pu()
    goto(point)
    pd()
    setheading(0)

def three(d):
    point = pos()
    for i in range(2):
        fd(d)
        rt(90)
    fd(d)
    for i in range(2):
        bk(d)
        rt(90)
    bk(d)
    pu()
    goto(point)
    pd()
    setheading(0)

def two(d):
    point = pos()
    fd(d)
    rt(90)
    fd(d)
    lt(90)
    for i in range(2):
        bk(d)
        lt(90)
    bk(d)
    pu()
    goto(point)
    pd()
    setheading(0)

def one(d):
    point = pos()
    pu()
    fd(d)
    pd()
    rt(90)
    fd(d*2)
    pu()
    goto(point)
    pd()
    setheading(0)

def zero(d):
    point = pos()
    fd(d)
    rt(90)
    fd(d*2)
    rt(90)
    fd(d)
    rt(90)
    fd(d*2)
    pu()
    goto(point)
    pd()
    setheading(0)

def drawnum(n):
    d=100
    if (n == 1):
        one(d)
    if (n ==2):
        two(d)
    if (n==3):
        three(d)
    if (n==4):
       four(d)
    if (n==5):
        five(d)
    if (n==6):
        six(d)
    if (n==7):
        seven(d)
    if (n==8):
        eight(d)
    if (n==9):
        nine(d)
    if (n==0):
        zero(d)
    pu()
    fd(1.5*d)
    pd()