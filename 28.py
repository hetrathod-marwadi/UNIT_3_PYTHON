''' 28. Write a program to demonstrate basic regular 
expression pattern matching.'''

import re

num = input("Enter mobile number: ")

regular_expression = re.compile(r'\d{10}')

ans  = regular_expression.search(num)

if ans == None:
    print("Invalid Mobile number")
else:
    print("mobile number is: ",num)
