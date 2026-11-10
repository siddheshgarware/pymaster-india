# divmod()
hours,minutes=divmod(135,60)
print(hours,minutes)

# 3 Operator Precedence — PEMDAS
# Priority Operator Description
# 1    (Highest)    **    Exponentiation
# 2               +x -x   Unary plus/minus
# 3               * / // %   Multiply, Divide, Floor, Modulus  
# 4     (Lowest)   + -    Add, Subtract

print(2 + 3 * 4 ** 2)

#input() function is used to take input from the user. It always returns a string.
t=input("Enter my collage name :")
print("i study in collage named",t)


#int function is used to convert a string or float into an integer. It can also be used to convert a string in a different base to an integer.
#Q. Write a program to take two numbers from the user and print their sum
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
f=a+b
print(f"sum of {a} and {b} is {f}")

#nested function:- function inside a function is called nested function. It is used to break a complex problem into smaller sub-problems. It is also used to avoid code duplication.
  

# 5 Type Conversion — Casting
# Function What it does Example Result
# int()      Converts to integer   int("25") 25
# float()    Converts to float     float("3.14") 3.14
# str()      Converts to string    str(100) "100"
# bool()     Converts to boolean   bool(0) False

a=float(input("Enter the number:"))
print(f"the number is {a} and its type is {type(a)}")

a=str(input("Enter the number:"))
print(f"the number is {a} and its type is {type(a)}")

a=bool(input("Enter the number:"))
print(f"the number is {a} and its type is {type(a)}")



# Function What it does Example Result
# math.sqrt(x) Square root math.sqrt(144) 12.0
# math.ceil(x) Round UP math.ceil(3.2) 4
# math.floor(x) Round DOWN math.floor(3.9) 3
# math.pi Value of pi math.pi 3.14159...
# math.factorial(x) Factorial (n!) math.factorial(5) 120
# math.pow(x, y) Power (float) math.pow(2, 10) 1024.0
# math.isclose(a,b) Compare floats isclose(0.1+0.2, 0.3) True

# firstly we have to import math module to use its functions.

import math
print("sqaure root of 225 is" ,math.sqrt(225))

