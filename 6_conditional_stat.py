# Conditional Statements:

    # if : only for first condition
    # elif : rest of the all conditions
    # else : its is a default condition (when all conditions fail to satisfy)

# write a program to where you ask user to provide a favourate
# primary color. and as per color theory print the meaning of 
# users favourate color.

# "Red" => Sacrifice
# "Blue" => Peace
# "Green" => Nature

# fav_prim_color = input("Enter your favourate primary color: ")

# if fav_prim_color == "Blue":
#     print("Peace")

# elif fav_prim_color == "Green":
#     print("Nature")

# elif fav_prim_color == "Red":
#     print("Sacrifice")

# else:
#     print("Invalid Color")

#------------------------------------

# if fav_prim_color == "Blue":
#     print("Peace")

# if fav_prim_color == "Green":
#     print("Nature")

# if fav_prim_color == "Red":
#     print("Sacrifice")

# if fav_prim_color != "Blue" and fav_prim_color != "Green" and fav_prim_color != "Red":
#     print("Invalid Color")

#--------------------------------------------
# Write a program to check marriage eleligibily as per
# Indian Marriage Act:

# Male => Age >= 21 ==> Eligible
# Female => Age >= 18 ==> Eligible

# gender = input("Enter your gender: ")
# age = int(input("Enter your age: "))

# if gender == "Male" and age >= 21:
#     print("Eligible")

# elif gender == "Female" and age >= 18:
#     print("Eligible")

# else:
#     print("Not Eligible")


#------------------------------------
# Write a program to check wether you are
# eligible to pay the income tax 
# if employee and ctc >= 12L but expenditure > 5L => No need
# if farmer and income >= 20 but expenditure > 10L => No need
# if businessman and income >= 500000 but expenditure > 20L => No need

# domain = input("Enter your domain: ")
# ctc = eval(input("Enter your ctc: "))
# expend = eval(input("Enter your expenditure: "))

# if domain == "emp":
#     if ctc >= 12:
#         if expend >= 5:
#             print("Eligible")
#         else:
#             print("Not eligible")
#     else:
#         print("Not Eligible")

# elif domain == "farm":
#     if ctc >= 20:
#         if expend >= 10:
#             print("Eligible")
#         else:
#             print("Not eligible")
#     else:
#         print("Not Eligible")

# if domain == "business":
#     if ctc >= 50:
#         if expend >= 20:
#             print("Eligible")
#         else:
#             print("Not eligible")
#     else:
#         print("Not Eligible")

#--------------------------------

# Second Largest Number in list

# l1 =[-23, -7, -45, -98, -1, -65, -100, -10]

# first = second = float('-inf')

# for i in range(0, len(l1)):
#     if l1[i] > first:
#         first = l1[i]

# for i in range(0, len(l1)):
#     if l1[i] > second and first != l1[i]:
#         second = l1[i]

# print(second)

#-----------------------------------------
# l1 = [34, 12, 66, 90, 3, 55, 88, 200]

# first = None  # 34, 66, 90, 200
# second = None # None, 12, 34, 66, 88, 90

# for i in l1:
#     if isinstance(i, (int, float)):   
#         if first is None or i > first:
#             second = first
#             first = i
#         elif (second is None or i > second) and i != first:
#             second = i

# print("Second largest:", second)

#-----------------------------------------------------------

# Write a program to print all odd numbers
# which are divisible by 3 and 5 from l1

# l1 = ["Apple", 30, True, 15, 45, 60, 75, '90', 105]

# index = 0

# while index < len(l1):
#     if isinstance(l1[index], int):
#         if l1[index] % 2 != 0:
#             if l1[index] % 3 == 0 and l1[index] % 5 == 0:
#                 print(l1[index]) 
#     index +=1


# Write a program to print all vowels from each string 
# of l1, make sure no duplicates

# l1 = ["Apple", True, 67, 89.2, "USA", "eat", "12345ae$"]

# vowels = []
# for i in l1:
#     if type(i) == str:
#         for char in i:
#             if char.lower() in 'aeiou':
#                 if char not in vowels:
#                     if char.upper() not in vowels:
#                         vowels.append(char)

# print(vowels)

#------------------------------------

# Write a program to print those charecters
# from string whose ascii are greater than 60

# str1 = "25!-Gkw0# "

# for char in str1:
#     if ord(char) > 60:
#         print(char)

    