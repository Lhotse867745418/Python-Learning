#-------------------------------------------------------------------------------
# Name:  factorial
# Purpose: calculate factorial of number(number!)
#
# Author:      lhotse
#
# Created:     04/02/2018
# Copyright:   (c) Administrator 2018
# Licence:
#-------------------------------------------------------------------------------

# define factorial
# input: number
# output:number!
# achieve by for loop statement

def factorial_1(number):
    product =  1
    for i in range(number):
        product = product * (i + 1)
    return product

# define factorial
# input: number
# output:number!
# achieve by Recursive call

def factorial_2(number):
    if number <= 1:
        return 1
    else:
        return number*factorial_2(number -1)



# get input  and print result

user_input = input("Enter:")

a = factorial_1(user_input)
print("Factorial_1 Result")
print a

b = factorial_2(user_input)
print("Factorial_2 Result")
print b



