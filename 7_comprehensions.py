# Comprehensions:

    # List Comprehension:
# Give a list of table of 2

# table_of_2 = []
# for num in range(1, 11):
#     table_of_2.append(num*2)
# print(table_of_2)

# table_of_2 = [num*2 for num in range(1, 11)]
# print(table_of_2)


#---------------------------------------------

# Write a program which ll create a list
# of consonents from str1

# str1 = "ASDFGHJKLOIUYTREWQ"

# consonents = []

# for char in str1:
#     if char not in "AEIOU":
#         consonents.append(char)

# print(consonents)

# consonents = [char for char in str1 if char not in "AEIOU"]
# print(consonents)


# ---------------------------------------

# Write a program where you ll have a list of 
# all those numbers which are greater than
# 5 from str1

str1 = "D*3961M7@5"

# nums_greater_than_5 = []

# for char in str1:
#     if char.isdigit():
#         if int(char) > 5:
#             nums_greater_than_5.append(char)

# print(nums_greater_than_5)

# nums_greater_than_5 = [char for char in str1 if char.isdigit() and int(char) > 5]
# print(nums_greater_than_5)

#-----------------------------------------

# create a list comprehension where you get 
# all odd numbers in the range of 1 to 11

# odds = [num for num in range(1, 11) if num % 2 != 0]
# print(odds)

#----------------------------------------------

# Tuple Comprehension

# Create a tuple comprehension for a table of 5

# table_of_5 = (num*5 for num in range(1, 11))
# print(table_of_5)   #<generator object <genexpr> at 0x000001D7738F9490>

# for i in table_of_5:
#     print(i)


# Write a Tuple Complrehension with all the 
# special charecters from string bellow

# str1 = "12@#fgGH"

#-----------------------------------------

# Set Comprehension 

# Create a set comprehension using bellow string
# where all the charecters from it will be available.
# No duplicates, even lower or upper charecters.

# str2 = "123@#$asdfASDF"

# set1 = {char.lower() for char in str2}
# print(set1)


# Write a set comprehension where all the numbers from
# 0 to 10 will be available.

# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}  Statically

# set2 = {num for num in range(0, 10)}
# print(set2)


# Write a set comprehension where you get 
# all odd numbers from 0 to 20

# set3 = {num for num in range(0, 20) if num % 2 != 0}
# print(set3)


# Write a set comprehension to have all those numbers
# which are greater than 5 or less than 0 from bellow list

# l1 = [9, 3, 7, -1, -4, 0, 5, 2]

# set4 = {num for num in l1 if num > 5 or num < 0}
# print(set4)


#--------------------------

# Dictionary Comprehension:

# Write a program to create a dictionary of 
# numbers from 1 to 10 with there squares
# {1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:49, 8:64, 9:81}

# d1 = {num: num**2 for num in range(1, 10)}
# print(d1)

# Write a dictionary comprehension where you use bellow string
# need each charecter with its ascii number
# charecter as a key and ascii as a value

# st1 ="apple@123😭"
# {"a": 97, }

# d2 = {char: ord(char) for char in st1}
# print(d2)


#----------------------

