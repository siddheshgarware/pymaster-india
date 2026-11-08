# a=8
# if 4<a<13:
#     print ("yes")
# else:
#     print ("no")


# #if else program to check voting eligibility of a person
age=int(input("enter your age:"))
if age >=18:
    print("eligible for vote")
else:
    print("not eligible for vote")

# #WAP to check the number is positive negative or zero 
if a==0 :
    print("the number is is zero")
elif a>0:
    print("number is positive")
elif a<0:
    print("number is negative")

#WAP to read a number and display the even or odd

b=int(input("enter the number:"))
if b%2==0:
    print("number is even")
else:
    print("it is odd")# 


# #Nested if_else
age = int(input("Enter age: "))
citizen_score = int(input("Enter citizen score: "))
national_score = int(input("Enter national score: "))

if age >= 18:
   if citizen_score >= 40:
       if national_score >= 60:
           print("Congrats, you can vote")
       else:
           print("Not eligible, improve your national score")
   else:
        print("Improve your citizen score")
else:
  print (f"you are eligble after{18-age}years")
 

# # #PS1
marks=int(input("enter your marks:"))
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 40:
    print("Promoted")
elif marks<40:
    print("fail")

# #PS2
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))

if a>b:
    if a>c:
        print("a is greater")
    else: 
        print("c is greater")
else:
    if b>c:
        print("b is greater")
    else:
        print("c is greater")


#one line if else
marks=int(input("enter your marks:"))
print("pass"if marks>=40 else "fail")

#Match case
letter = input("Enter the letter :")

match letter :
    case "a":
        print(f"{letter} is vowel") 
    case "e":
        print(f"{letter} is vowel") 
    case "i":
        print(f"{letter} is vowel") 
    case "o":
        print(f"{letter} is vowel")     
    case "u":
        print(f"{letter} is vowel")             
    
    
        
        


    

  
