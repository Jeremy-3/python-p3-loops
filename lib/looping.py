#!/usr/bin/env python3

def happy_new_year():
    counter = 10
    while counter > 0:
        print(counter)
        counter -= 1
        if counter == 0:
            print("Happy New Year!")
    # code goes here!
    

def square_integers(int_list):
    for num in int_list:
        print(num ** 2)
        
    return [num ** 2 for num in int_list]    
         
    # code goes here!
   

def fizzbuzz():
    i = 0
    while(i < 100):
        i += 1
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

    # code goes here!
    pass
