# Control Statements:
    # while loop:
        # More Manul
        # It gives more control

    # for loop
        # More Automatic
        # It gives less control

#------------------------------------------
# Print "Hello World" 
# print("Hello World")

# Print "Hello World" 5 times
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")

# Print "Hello World 10000 times"

# count = 0  # 1, 2, 3, 4, 5, 6, 6,   10000

# while count < 10000:   
#     print("Hello World", count)
#     count +=1


#-------------------------------------------
# Write a program using while loop to print 1 to 10
# table.

# count = 1
# while count < 11:
#     print(count)
#     count +=1

#-----------------------------------
# Write a program to print table of 7
# using while loop.

# count = 1

# while count <= 10:
#     print(count * 7)
#     count +=1

#---------------------------------------
# Write a program to print all even numbers in between
# 1 and 20 using while loop

# count = 1

# while count < 20:
#     if count % 2 == 0:
#         print(count)
#     count +=1

#---------------------------------------

# Write a program to print all numbers which are
# divisible by 3 and 7 in between 1 and 100 using while loop

# count = 1

# while count < 100:
#     if count % 3 == 0 and count % 7 == 0:
#         print(count)
#     count +=1

#-----------------------------------------

# write a program to print all integers from bellow list

# l1 = ["A", True, 2, 9.7, 4, "Apple", 8, 1.1, (1, 2, 3)]
# print(len(l1))

# indx = 0

# while indx < len(l1):
#     if type(l1[indx]) == int:
#         print(l1[indx])
#     indx +=1
#-----------------------------------------

# Write a program to print sum of all floats from 
# bellow tuple
# tup1 = ("9", 5, "Grapes", False, 9.1, 4.5, 1, '2.2', [1, 3.3, 6, 7.7])
# 9.1, 4.5 => 13.6

# index = 0
# total = 0
# while index < len(tup1):
#     if type(tup1[index]) == float:
#         total += tup1[index]
#     index +=1
# print(total)

#------------------------------------
# Write a program to fibonacci series upto users requirement
# using while loop

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

# num1 = 0
# num2 = 1
# num_of_nums = int(input("How many fibonacci numbers do you want: "))
# count = 0
# print(num1)
# print(num2)
# while count < num_of_nums-2:
#     new = num1 + num2
#     print(new)
#     num1, num2 = num2, new
#     count +=1

#-------------------------------------------
# Write a program to print all Armstrong 
# numbers in between 100 and 10000:

# 153 => 1**3 + 5**3 + 3**3
#     => 1 + 125 + 27
#     => 153

# start = 100
# end = 10000

# while start <= end:
#     power = len(str(start))  #3

#     total = 0  # 1
#     indx = 0
#     while indx < power:
#         total += int(str(start)[indx]) ** power
#         indx +=1

#     if start == total:
#         print(start)
#     start +=1