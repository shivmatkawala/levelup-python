# Lambda:

    # Lambdas are single line expressions
    # Lambdas can be stored using varibale
    # Lambdas are anonymous / Nameless functions
    # Lambdas are popular because they are easy and concise
    # though they are faster.
    # Using Lambda we can enhance the code reusibility

# Create a lambda for adding two numbers

# total = lambda num1, num2: num1+num2
# print(total(4, 5))

# Create a lambda function to get the square of a number

# square = lambda num: num**2
# print(square(8))
# print(square(123))
# print(square(25))


# Write a lambda function to concatenate two different strings
# strings must be separated by space

# concat = lambda str1, str2: str1 + " " + str2
# print(concat("Hello", "World"))

# Write a lambda function to check a highest number
# between two numbers.

# greater = lambda num1, num2: num1 if num1 > num2 else num2
# print(greater(3, 9))
# print(greater(7, 7))

# Write a lambda function to get the largest number 
# from list

# l1 = [1, 7.2, "A", True, 89, "Apple"]

# great_num = lambda list1: max([num for num in l1 if isinstance(num, (float, int))])
# print(great_num(l1))

#--------

# map()

# l1 = [1, 2, 3, 4, 5]

# l1_squares = list(map(lambda num: num**2, l1))
# print(l1_squares)


# Use map with lambda and convert each charecter
# from str1 into capital

# str1 = "watermelon"
# capitals = "".join(list(map(lambda char: char.upper(), str1)))
# print(capitals)

#----------------------------
# Write a lambda function with map
# to get the ascii numbers of each charecter from str1
# str1 = "Banana@143"

# asciis = list(map(lambda char: ord(char), str1))
# print(asciis)

# str2 = "AHil$Z"

# just_string = "".join(list(map(lambda char: chr(ord(char)-2), str2)))
# print(just_string)

#------------------------

# Filter

# Write a program using lambda with filter to get only 
# those charecters which are alphabetic from str1

# str1 = "a^L0Bn@ft"

# alphabets = list(filter(lambda char: char if char.isalpha() else None, str1))
# print(alphabets)


# l1 = [7, 2, 0, 5, 15, -12, -4, 6]

# using filter and lambda get the lsit of those numbers from
# l1 which are greater than 5 and less than 10

# nums_filtered = list(filter(lambda num: num if 5<num<10 else None, l1))
# print(nums_filtered)

#--------------------------

from functools import reduce

# l1 = [1, 2, 3, 4, 5, 6]

# total = reduce(lambda num1, num2: num1+num2, l1)
# print(total)

# l2 = ["a", "G", '7', "m", '1.1', "P"]

# str2 = reduce(lambda x, y: x+y, l2)
# print(str2)

#--------------------
# Write a program to print a highest number from l3
# using reduce with lambda

l3 = ["2", "6", "@", "A", "90", "101.1", "%"]

# output = reduce(lambda x, y: x if eval(x) > eval(y) else y,filter(lambda char: char if char.isdigit() else None, l3))
# print(output)
l4 = []
for k in l3:
    flag = False
    for i in k:
        if i in "0123456789.":
            pass
        else:
            break
        flag = True
    if flag == True:
        l4.append(eval(k))

print(l4)


    