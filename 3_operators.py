# Operators:

    # Expressions
        # x + 7 = 12   
            # Operands  # x, 7, 12
            # Operators #  +, =

#--------------------------
    # Aritmetic Operators:
# x = 5
# y = 3

#         # Addition +
# print(x+y)
#         # Substraction -
# print(x-y)
#         # Multiplication *
# print(x*y)
#         # True Division /
# print(x/y)
#         # Floor Division //
# print(x//y)
#         # Exponentiation (Power)  **
# print(x ** y)

#         # Modulus (Mod) %
# print(x % y)


    # Assignment Operators:
        # Assign =
# p = 9
#         # Add and Assign +=
# # p = p+2
# p+=2
# print(p)
#         # Substract and Assign -=
# # p = p - 4
# p-=4
# print(p)
#         # Multiply and Assign *=
# # p = p * 3
# p *=3
# print(p)

#         # True Divide and assign /=
# # p = p / 8
# p/=8
# print(p)

#         # Floor Divide and assign //=
# # print(14 // 4)

#         # Exponentiation and assign **=
# # p = p ** 3
# p **=3
# print(p)
#         # Modulus and assign %=
# # p = p % 7
# p %=7
# print(p)

    # Comparision Operators:
        # Equal to ==
x = 7
y = 3
# print(x == y)

        # Not Equal to !=
# print(x != y)

        # Greater than >
# print(x > y)

        # Lesser than <
# print( x < y)

        # Greater than or equal to >=
# print(x >= y)
# print(y >= x)

        # Lesser than or Equal to <=
# print(x <= y)

    # Identity Operators:
# References
# x = [1, 2, 3, [10, 20, 30]]
# y = x
# print(id(x))
# print(id(y))
# x[0] = 100

# print(x)
# print(y)
#--------------------------
# x = [1, 2, 3, [10, 20, 30]]
# y = x.copy()    # Shallow Copy

# x[3][0] = 100

# print(x)
# print(y)
# print(id(x))
# print(id(y))

#------------------------------------------
from copy import deepcopy

x = [1, 2, 3, [10, 20, 30]]
y = deepcopy(x)   # Deep copy

# x[3][0] = 100
# print(x)
# print(y)
# print(id(x))
# print(id(y))

        # is
# print(x is y)  #True

        # is not
# print(x is not y)

    # Membership Operators:
# s1 = {12, 34, 56, 7, 8,  8, 9, False}

        # in 
# print(0 in s1)
# print(111 in s1)

        # not in
# print(False not in s1)
# print(111 not in s1)

    # Logical Operators:
        # To check on multiple conditions we use logical operators.

# students = {
#     "1": {"Result": "Failed", "Gender": "Male", "name":"Avi"},
#     "2": {"Result": "Passed", "Gender": "Female", "name": "Karuna"},
#     "3": {"Result": "Passed", "Gender": "Male", "name": "David"},
#     "4": {"Result": "Failed", "Gender": "Female", "name": "Sara"},
#     "5": {"Result": "Passed", "Gender": "Male", "name": "Daya"},
#     "6": {"Result": "Failed", "Gender": "Female", "name": "Pooja"},
#     "7": {"Result": "Failed", "Gender": "Male", "name": "Vijay"},
#     "8": {"Result": "Passed", "Gender": "Female", "name": "Shabana"},
#     "9": {"Result": "Failed", "Gender": "Female", "name": "Divya"}
# }

# Loops:
        # 1) while loop:
                # More Maual
                # Gives more Control

        # 2) for loop:
                # More Automatic
                # Gives less control


# for student in students:
#     if students[student]["Gender"] == "Female" and students[student]["Result"]=="Failed":
#         print(students[student]["name"])
        
        # and
number = 9
# Check if number is even and also greater than 10

# if number % 2 == 0 and number > 10:  # True and False => False
#     print("Ok")

# if number % 2 == 0 and number > 10:   # False and True => False
#     print(number)

        # or
# if number > 10 or number % 2 == 0:   # True or False => True
#     print(number)

        # not
# if not(number > 10):
#     print(number)

# and ==> True and True and True and False => False
# or => True or False or False or False => True
# or => False or False or False => False
# and => False and False and False => False
# and => True and True and True => True

# print(not(True and True or False) and False or True or not (False))

# print(True * True and True*(not(False)) 
#       and False or False 
#       and True * (not(True and False)))

# x = 23
# if x % 2 == 0 and x % 3 == 0 or x % 1 == 0:
#     print(x)

    # Ternary Operators:

# Write a program to print the meaning of color after
# user enters his/her fav primary color:

# color = input("Enter your favourate primary color: ")
# Blue => Peace, Red => Sacrifice, Green=> Nature

# result = "Peace" if color == "Blue" else "Sacrifice" if color == "Red" else "Nature" if color == "Green" else "Invalid Color"
# print(result)
#---------------------------------------------------

# ask user to enter his or her age 
# and as per indian law is she eligible to vot or not print.

# age = int(input("Enter your age: "))

# eligibility = "Eligible to vote" if age >= 18 else "Not Eligible to vote"
# print(eligibility)

#------------------------------------------
# Write a program where you ask user to enter a number
# and you check wether it is even or odd and print it.
# using ternary operator.

# num = int(input("Enter a number: "))

# result = "Even" if num % 2 == 0 else "Odd"
# print(result)


    # Bitwise Operators:
        # &  (AND)
# print(23 & 8)   # 0

# Function to convert a number into binary:
# print(bin(23))  # 10111
# print(bin(8))   # 1000

# print(int("00000000", 2))
        # |  (OR)
# print(23 | 10)

# print(bin(23))
# print(bin(10))

# print(int("11111", 2))

        # ^  (XOR)

# print(23 ^ 10)  # 29
# print(int("11101", 2))

