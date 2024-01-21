#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
        if i == 0:
            print("Happy New Year!")
    pass

def square_integers(int_list):
    square_integers = [number ** 2 for number in int_list]
    return square_integers

def fizzbuzz():
    for num in range(1, 101):
        if (num % 3 == 0) and (num % 5 == 0):
            num = "FizzBuzz"
        elif num % 3 == 0:
            num = "Fizz"
        elif num % 5 == 0:
            num = "Buzz"
        print(num)

fizzbuzz()
