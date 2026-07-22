# Datatypes in python:

    # Numeric:
        # 1) Integer:-
            # Any Number without decimal point, including 0.
            # Integers can be +ve and -ve
            # Ex: 8, 34, -12, -90, 0, 
# num1 = 56
# print(num1)
# print(type(num1))   #<class 'int'>

# num2 = -12
# print(num2)
# print(type(num2))  #<class 'int'>

# num3 = 0
# print(num3)
# print(type(num3))  #<class 'int'>


        # 2) Float:-
            # Any number with decimal point is float.
            # Floats also can be +ve and -ve
            # Ex: -0.0, 90.567, 12.0, -100.000
# n1 = 67.34
# print(n1)
# print(type(n1))   #<class 'float'>

# n2 = -12.00
# print(n2)
# print(type(n2))  #<class 'float'>

# n3 = 0.0
# print(n3)
# print(type(n3))  #<class 'float'>

        # 3) Complex
            # It is a combination of Real number and imaginary number.
                # Real Numbers:
                    # All Integers and Floats are real numbers
                    # Ex: 0.0, 67.5, 4, -6, -0.12344

            # Imaginary Number:
                    # Any number with j suffix is imaginary number.
                    # j value is underroot of -1
                    # Ex: 9j, -23j, -0.45j, -12j

            # Ex: 7+6j, -9-5j, -12.5+56j, 23-5.6j
# number1 = 5-8j
# print(number1)
# print(type(number1))  #<class 'complex'>
# print(number1.real) #5.0
# print(number1.imag) #-8.0

    # Boolean
        # True  => 1
        # False => 0
# x = 56
# print(x == (100-44))
# print(x == 120)

# print(True + True)
# print(True / True - False * True +True)


    # String
        # It is a sequence of charecters enclosed using quotes:
        # Ex: "Apple", "Alpha@123", '12344', '!@#$%^'

        # Types of quotes can be used for string making:
            # ''   Single quotes
            # ""   Double quotes
            # ''' ''' Tripple Single quotes
            # """ """ Tripple Double quotes
# str1 = 'Apple'
# print(str1, type(str1))

# str2 = "Pineapple"
# print(str2, type(str2))

# str3 = '''Banana'''
# print(str3, type(str3))

# str4 = """Grapes"""
# print(str4, type(str4))

# str5 = "Uma is the 'Tallest' among all girls"
# str6 = 'Hari is the most "handsome" person in his town.'

# print(str5, type(str5))
# print(str6, type(str6))

# Hari Asked "Vijay where are you going ?"
# Vijay replied "I am going to school."
# str7 = '''Sara is calling Ajay for help, 
# but Ajay didnt "lift" the call. 'Sara' went 
# to his """place and shouted""" on him for not 
# lifting her calls.'''


# str1 = "123456"
# print(str1, type(str1))

# str2 = "@#$%^"
# print(str2, type(str2))

# str3 = "Apple"
# print(str3, type(str3))

# Indexing on String:

# str4 = "Ajay@123"

# print(str4)

# Print "A" from str4
# print(str4[0])
# print(str4[-8])

# print(str4[4])
# print(str4[-4])

# Slicing:
# print(str4[0:4:1])
# print(str4[4:8:1])
# print(str4[0:8:2])
# print(str4[2:8:3])
# print(str4[7:0:-2])
# print(str4[-4:-9:-4])
# print(str4[4::-4])
# print(str4[-4::-4])

# In built Methods of String:
str5 = "apple"

    # Case Conversion Methods:
    # .upper()  => Convert all lowercase letters into uppercase letters
# print(str5.upper())  #APPLE

# str6 = "GRAPES"
#     # .lower()
# print(str6.lower())  #grapes

# str7 = "india is my country."
#      # .title() 
# print(str7.title())  #India Is My Country.

# str8 = "python is awesome."
#     # .capitalize()
# print(str8.capitalize())   #Python is awesome.

# str9 = "aJKol"
#     # .swapcase()
# print(str9.swapcase())  #AjkOL

# str10 = "123Laila"

# print(str10.lower())  #123laila

# str11 = "1kiran 2shabana 3sameer"
# print(str11.title())   #1Kiran 2Shabana 3Sameer

# str12 = "sTRING is Good"
# print(str12.capitalize())   #String is good

#-------------------------------
# Search Methods:
    # .index()
    # .rindex()
    # .find()
    # .rfind()
# str13 = "Halleluih"
# print(str13.index("l"))
# print(str13.rindex("l"))

# print(str13.index("Z"))   #ValueError: substring not found

# print(str13.find("l"))
# print(str13.rfind("l"))

# print(str13.find("Z"))
# print(str13.rfind("A"))


#------------------------

    # is methods:
        # .isdigit() => True if all charecters in string are digits
# str15 ="1234"
# print(str15.isdigit())

# str16 = "78.2334"
# print(str16.isdigit())

# str17 = "0987"
# print(str17.isdigit())


        # .isalpha() True if all charecters are alphabetic
# st18 = "Apple@123"
# print(st18.isalpha())

# str19 = "sameer"
# print(str19.isalpha())

# str20 = "Kishan Ishan"
# print(str20.isalpha())

    # .isalnum()  True if charecters are alphbetic or numeric or alphabetic and numeric
# str21 = "Amit123"
# print(str21.isalnum())


# str22 = "Sanjay Dutt"
# print(str22.isalnum())


# str23 = "kiranrao"
# print(str23.isalnum())

# str24 = "123.90"
# print(str24.isalnum())

# str25 = "2345"
# print(str25.isalnum())

    # .isspace()  True is all charecters are empty spaces

# str26 = ""
# print(str26.isspace())


# str27 = "  "
# print(str27.isspace())

# str28 = "     ."
# print(str28.isspace())

# Some Other string operations:

# st1 = "apple"
# st2 = "fruit"

# Concatination:
# print(st1 + st2)  #applefruit

# print((st1 + " " + st2).title()[0::2][::-1])

# Repetation:

# print(st1*5)
#-------------------------------------------------------------
#-------------------------------------------------------------

    # Collection:
        # 1) List
        # 2) Tuple
        # 3) Set

    # Range

    # Dictionary

