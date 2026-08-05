# Errors:-

# x  = 5
# y = "Helllo"
# print(x+y)  #TypeError: unsupported operand type(s) for +: 'int' and 'str'

# l1 = [1, 2, 3, 4, 5, 6]
# print(l1[10])    #IndexError: list index out of range

# print(23 / 0)   # ZeroDivisionError: division by zero


#  print("Hello")  #IndentationError: unexpected indent

# print(type(z))    #NameError: name 'z' is not defined
#--------------------------------------------

# write a program which will ask for numerator and denominator
# and then performs division and return answer.

def division(numerator, denominator):
    return numerator /denominator

# print(division(78, 4))
# print(division(98, 0))


# try:
#     ans = division(23, 7)

# except ZeroDivisionError:
#     print("Can not be divided by zero.")

# else:
#     print(ans)

# finally:
#     print("Program executed successfully..!")


# try:
#     ans = division(23, 0)

# except ZeroDivisionError:
#     print("Can not be divided by zero.")

# else:
#     print(ans)

# finally:
#     print("Program executed successfully..!")


# try:
#     ans = division("Hello", 5)

# except ZeroDivisionError:
#     print("Can not be divide by zero")

# except TypeError:
#     print("Only Numeric values are allowed.")

# else:
#     print(ans)

# finally:
#     print("Program executed successfully..!")





# try:
#     ans = division(89, 0)

# except ZeroDivisionError:
#     print("Can not be divide by zero")
    
# except TypeError:
#     print("Only Numeric values are allowed.")

# else:
#     print(ans)

# finally:
#     print("Program executed successfully..!")


# In case of Error:
    # try, except, finally

# In case of No Error:
    # try, else, finally


list1 = ["Hello", 23, 89, 1.2, 90, True]

# Write a program in the form of function where it takes 
# input paramenter as index number. 
# then it returns the value from list1's provided index.

def get_element_from_list1(index):
    return list1[index]


# value = get_element_from_list1(12)
# print(value)


# try:
#     value = get_element_from_list1(4)
    
# except IndexError:
#     print(f"Enter index less than {len(list1)}")

# else:
#     print(value)

# finally:
#     print("Program executed successfully.")



# try:
#     value = get_element_from_list1(12)
    
# except IndexError:
#     print("Index is wrong")

# else:
#     print(value)

# finally:
#     print("Program executed successfully.")


# def get_voter_card(fullname, age, citizenship):
#     if fullname and citizenship.lower() == 'indian' and age >= 18:
#         print("Voter card assigned")
#     else:
#         print("Not eligible to get voter card.")
    

# get_voter_card("Ajay Banga", 34, 'American')
# get_voter_card("Ajay Banga", 5, 'Indian')



#------------------------------------

class SmallAgeError(Exception):
    pass

class NonIndianError(Exception):
    pass


def get_voter_card(fullname, age, citizenship):
    if fullname and age < 18 and citizenship.lower() == "indian":
        raise SmallAgeError("Age is less than 18")
    
    elif fullname and age > 18 and citizenship.lower() != "indian":
        raise NonIndianError("You are not Indian Citizen")

    else:
        return "You will recieve voter card soon."


# get_voter_card("Vijay Chauhan", 34, 'Indian')
# get_voter_card("Rina Sharma", 12, 'Indian')
# get_voter_card('Diya Mirza', 45, 'British')

# try:
#     ans = get_voter_card("Kumar reddy", 7, 'Indian')

# except SmallAgeError:
#     print("You are too young to get voter card. Sorry")

# except NonIndianError:
#     print("Please be Indian First")

# else:
#     print(ans)

# finally:
#     print("Program executed successfully.")



# try:
#     ans = get_voter_card("Kumar reddy", 27, 'Canadian')

# except SmallAgeError:
#     print("You are too young to get voter card. Sorry")

# except NonIndianError:
#     print("Please be Indian First")

# else:
#     print(ans)

# finally:
#     print("Program executed successfully.")



# try:
#     ans = get_voter_card("Kumar reddy", 27, 'INDIAN')

# except SmallAgeError:
#     print("You are too young to get voter card. Sorry")

# except NonIndianError:
#     print("Please be Indian First")

# else:
#     print(ans)

# finally:
#     print("Program executed successfully.")

