
#-------------PROCEDURAL PROGRAMMING PARADIGM-------------------


# # Write a program to greet a customer.
# name = input("Enter your name: ")
# print(f"Hello {name}")


# # Write a program to print table of 5
# for i in range(1, 11):
#     print(5*i)


# # Write a program to add to numbers.
# num1 = eval(input("Enter first number: "))
# num2 = eval(input("Enter second number: "))
# print(num1 + num2)



#------------------- Functional Programming Paradigm ------------

# def greet(name):
#     print(f"Hello {name}")

# def table_of_5():
#     for i in range(1, 11):
#         print(5*i)

# def addition(num1, num2):
#     print(num1 + num2)


# greet("Sonu")
# greet("Chandu")
# greet("Namratha")
# greet("Mallesh")

# greet("Vaibhav")
# table_of_5()
# addition(6, 7)

#-----------------------What is Function:

# Functions are Block of code written in the scope of them.
# Functions are Building Blocks of Classes.
# Functions define the behavour of an Object
# Functions are also called methods

# Functions needs to be called in order to excute them
# Functions can be reused N number of times in file
# or  across the project folder.

# Functional code is isolated from global.

# Functions are defined using:
    # Header: def keyword, name of function, parenthesis, collan
        # def fuction_name():

    # Body: after 4 empty spaces we start writing body
    #       We can write complte program here.


# def function_name():
#     print("My First function.")

# function_name()

#---------------- Types of Functions: -----------------------

# 1) No Argument Function:
    # A function which doesnt take an argument

# Write a function to print "Jai India"
# def slogan():
#     print('Jai India')

# slogan()

# 2) Single Argument Function:
    # A function takes single argument

# def slogan(slo):
#     print(slo)

# slogan("Jai India")

# 3) Positional Argument Function:
    # A function takes multiple arguments

# def slogans(slo1, slo2, slo3, slo4):
#     print(slo1)
#     print(slo2)
#     print(slo3)
#     print(slo4)

# slogans("Jai INdia", "Jai BHarat", "Jai Matha di", "Jai Jawan")

# def student_info(firstname, lastname, roll, standard, marks):
#     print(f'''
#         Firstname: {firstname}
#         Lastname:  {lastname}
#         Roll No:   {roll}
#         Standard:  {standard}
#         Marks:     {marks}
#     ''')


# student_info(56, 7, "Ajith", "Reddy", "9th")
# student_info("Vijaya", "Pothineni", 9, "10th", 78)


# 4) Default Argument Fucntion
    # A Function with argument and its default value

# def greet(name="Friend"):
#     print(f"Hello Dear {name}")

# greet()
# greet("Sanjana")

# 5) Keyword Argument Function  
    # A function with key and value

# def product(pid, pname, supplier, price, address):
#     print(f'''
#         Product ID:    {pid}
#         Product Name:  {pname}
#         Supplier:      {supplier}
#         Price:         {price}
#         Address:       {address}
#     ''')


# product(price=67, supplier="Royalsima Mangoes Co.", pid=12, pname="Mangoes", address="Kadappa, AP, 500023")


# 6) Variable Length Argument Function
# def addition(*args):
#     print(sum(args))

# addition(4, 5)

# def students(*name):
#     for i in name:
#         print(i)

# students("Kirthi", "Rajesh", "Sandhya", "Pushpa", "Daya")

# 7) Variable Length Keyword Argument Function

def item_prices(**kwargs):
    total = 0
    for key, value in kwargs.items():
        print(f"{key} ---> {value}")
        total+= value
    print(f"Total: {total}")
    

item_prices(mango=50, apple=20, grapes=80, pineapple=70)

# Find total price
