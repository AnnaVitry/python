#!/usr/bin/env python3
from tkinter import *
import math

window = Tk()
calc_input = ""
result = 0

def input_key(value):
    global calc_input
    if is_number(value) == False and float(result_text.get()) != 0:
        calc_input = result_text.get()
    calc_input += value
    calc_input_text.set(calc_input)

def equal(operator):
    global calc_input
    if operator == "√":
        result = str(eval("math.sqrt({})".format(calc_input)))
    elif operator == "²":
        float_calc_input = float(calc_input)
        result = float_calc_input*float_calc_input
    elif operator == "!" and calc_input.isnumeric():
        int_calc_input = int(calc_input)
        result = 1
        while(int_calc_input > 0):
            result *= int_calc_input
            int_calc_input-=1
    else:
        result = str(eval(calc_input))
    result_text.set(result)

def clear():
    global calc_input
    calc_input = ""
    result = 0
    result_text.set(result)
    calc_input = ""
    calc_input_text.set(calc_input)

def is_number(string):
   try:
       float(string)
       return True
   except ValueError:
       return False

Button(window, text=" clear ", command=lambda: clear()).grid(row=0, column=0) 
Button(window, text=" close ", command=window.quit).grid(row=0, column=4)

Button(window, text=" 0 ", command=lambda: input_key("0")).grid(row=6, column=0)
Button(window, text=" 1 ", command=lambda: input_key("1")).grid(row=5, column=0)
Button(window, text=" 2 ", command=lambda: input_key("2")).grid(row=5, column=1)
Button(window, text=" 3 ", command=lambda: input_key("3")).grid(row=5, column=2)
Button(window, text=" 4 ", command=lambda: input_key("4")).grid(row=4, column=0)
Button(window, text=" 5 ", command=lambda: input_key("5")).grid(row=4, column=1)
Button(window, text=" 6 ", command=lambda: input_key("6")).grid(row=4, column=2)
Button(window, text=" 7 ", command=lambda: input_key("7")).grid(row=3, column=0)
Button(window, text=" 8 ", command=lambda: input_key("8")).grid(row=3, column=1)
Button(window, text=" 9 ", command=lambda: input_key("9")).grid(row=3, column=2)

Button(window, text=" + ", command=lambda: input_key("+")).grid(row=3, column=3)
Button(window, text=" - ", command=lambda: input_key("-")).grid(row=4, column=3)
Button(window, text=" * ", command=lambda: input_key("*")).grid(row=5, column=3)
Button(window, text=" / ", command=lambda: input_key("/")).grid(row=6, column=3)
Button(window, text=" . ", command=lambda: input_key(".")).grid(row=6, column=1)
Button(window, text=" % ", command=lambda: input_key("%")).grid(row=3, column=4)
Button(window, text=" ! ", command=lambda: equal("!")).grid(row=4, column=4)
Button(window, text=" √ ", command=lambda: equal("√")).grid(row=5, column=4)
Button(window, text=" ² ", command=lambda: equal("²")).grid(row=6, column=4)

Button(window, text=" = ", command=lambda: equal("=")).grid(row=6, column=2)

calc_input_text = StringVar()
Label(window, textvariable=calc_input_text).grid(row=1, column=0)
result_text = StringVar()
Label(window, textvariable=result_text).grid(row=2, column=0)
result_text.set(result)
window.mainloop()