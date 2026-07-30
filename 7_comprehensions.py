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

str1 = "12@#fgGH"
