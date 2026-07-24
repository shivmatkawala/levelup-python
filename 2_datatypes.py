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
# list1 = []
# print(list1, type(list1))

# list2 = [1, 2, 3, 4, 5]
# print(list2, type(list2))

# list3 = [1, 2.2, 3+6j, True, "Banna", [100, 200, 300]]
# print(list3, type(list3))

# Indexing upon list:

# l1 = [12, 23, 34, 45, 56, 67]
# print(l1)
# print(type(l1))
# print(len(l1))

# Positive Indexing:
# print(l1[0])  #12
# print(l1[1])  #23
# print(l1[4])  #56

# Negative Indexing
# print(l1[-6])
# print(l1[-5])
# print(l1[-2])

#---- Slicing:
# print(l1[0:3:1])
# print(l1[3::1])
# print(l1[0::2])
# print(l1[-1::-2])

# In built methods fo list:
# l2 = [1, 34.5, 8-9j, False, [1, 2, 3], "CAKE"]

# Insertion Methods
    # .append()  # takes only 1 argument and adds it at last of list
# l2.append(100)
# l2.append("sanju")

    # .extend() # takes only 1 argument as acollection and adds it at last
# l2.extend([1.1, 2.2, 3.3, 4.4])

    # .insert() # takes two arguments first index number and second element
# l2.insert(0, 10000)

# print(l2)

#---- Deletion of elements methods
# l2 = [1, 34.5, 8-9j, False, [1, 2, 3], "CAKE", 34.5]

#     # .pop() # deletes last element from list
# l2.pop()
#     # .remove()  # deletes specified element from list
# l2.remove(34.5)
#     # .clear() # it deletes all elements from list and makes list empty
# l2.clear()

# print(l2)

# Search methods:

# l3 = [11, 22, 33, 22, 44, 55, 66, 22, 77]
# print(l3.index(33))

# count the appearances of particular element

# print(l3.count(22))

# Sort and reverse methods

l4 = [4, 2, 3, 9, 0, 1, 8, 6]

# l4.sort()   # when sorting do not print
# print(l4)   #[0, 1, 2, 3, 4, 6, 8, 9]

# l4.sort(reverse=True)
# print(l4)  #[9, 8, 6, 4, 3, 2, 1, 0]

# l4.reverse()   # while performing reverse ops do not print
# print(l4)  #[6, 8, 1, 0, 9, 3, 2, 4]

# .copy()

# l5 = l4.copy()

# print(l5)

# Some other operations:
    # Concatination

l1 = [1, 2, 3, 4]
l2 = [4, 5, 6]

# print(l1 + l2)

    # repetation of list

# print(l1 * 5)

    # Packing and unpacking

# x, y, z = l1   #ValueError: too many values to unpack (expected 3)
# print(x)
# print(y)
# print(z)
#-----------------------------------------------------------
#-----------------------------------------------------------

        # 2) Tuple

# tup1 = ()
# print(tup1, type(tup1))

# tup2 = (1, 2, 3, 4, 5, 6)
# print(tup2, type(tup2))

# tup3 = (1, 2.2, 3+4j, True, [100, 200, 300], (9, 8, 7), "Appple")
# print(tup3, type(tup3))

# Positive Indexing

tup4 = (12, 23, 34, 4, 5, 5, 6, 6, 7, 23, 1, 4, 5, 23)
# print(tup4[2])
# print(tup4[6])
# print(tup4[7])

# Negative Indexing
# print(tup4[-6])
# print(tup4[-9])

# Slicing:
# print(tup4[-2::-3])

# In built methods of tuple
    # .index()  # it gets you the index of element

# print(tup4.index(4))

    # .count() 
# print(tup4.count(23))

# Some other methods of tuple
# t1 = (1, 2 , 3)
# t2 = (4, 5, 6)

    # Concatination
# print(t1 + t2)

    # repetaion
# print(t1 * 3)

    # Packing and unpacking
# m, n, o = t2
# print(m)
# print(n)
# print(o)

# print(tup4[tup4.index(12)])
#----------------------------------------------------
#----------------------------------------------------


        # 3) Set

# set1 = {1}
# print(set1, type(set1))


# set2 = set()
# print(set2, type(set2))

# set3 = {1, 2, 3, 4}
# print(set3, type(set3))

# set4 = {1, 2.2, 3+5j, True, "grapes", (11, 22, 33)}
# print(set4, type(set4))

#---------------------------------------

# In Built Methods of Set:

# s1 = {1, 2, 3, 4, 5, 6}
    # Insertion methods:
# s1.add(7)
# s1.update({9, 10, 11, 12})

    # Deletion Methods:
# s1.pop()  # deletes any random element from set

# s1.remove(3)  # deletes specified element

# s1.clear()   # removes all elements from set and makes set empty

# print(s1)

#-----------------------------------------
s1 = {1, 2, 3}
s2 = {3, 4, 5}

# Set Operations:
    # Union   |
# print(s1.union(s2))  #{1, 2, 3, 4, 5}
# print(s1 | s2)

    # Difference -
# print(s1.difference(s2))   # {1, 2}
# print(s1-s2)
# print(s2.difference(s1))   # {4, 5}
# print(s2-s1)
    # Intersection  &
# print(s1.intersection(s2))
# print(s1 & s2)


# Bellow methods make permanent changes in sets

# union update
# s1.update(s2)
# print(s1)

# intersection update
# s1.intersection_update(s2)
# print(s1)

# difference update
# s1.difference_update(s2)
# print(s1)
# print(s1.isdisjoint(s2))

# s3 = {8, 0}   #   Superset
# s4 = {8, 0}   # Subset
# print(s3.issuperset(s4))
# print(s4.issubset(s3))

# print(s4.issuperset(s3))
# print(s3.issubset(s4))


    # Range
        # It develops immutable sequence of numbers
        # Range develops numbers but never stores them in memory
        # Because of this range is memory friendly

    # [Start: End: Step]
# r1 = range(5)  # default start = 0, end =5, default step = 1
# print(r1)
# print(list(r1))


# r2 = range(7,16,2)
# print(r2)
# print(tuple(r2))

    # Dictionary

        # Dictionary is a collection of key and value pairs.

        # Dictionary is ordered datatype but it is indexed using its key.

        #  Dictionary is mutable
        #  Dictionary is also heterogeneous

# dict1 = {}
# print(dict1, type(dict1))   #<class 'dict'>

# dict2 = {1:1, 2:4, 3:9, 4:16, 5:25}
# print(dict2, type(dict2))

# dict3 = {1:"Masood", 2:"Vishal", 3:"Divya"}
# print(dict3, type(dict3))


# dict4 = {"Masood": 12, "Vishal": 34, "Divya": 1}
# print(dict4, type(dict4))

# dict5 = {"Masood": [89, 12, "Male", False], "Vishal": [78, 34, "Male", True]}
# print(dict5, type(dict5))


# dict6 = {"Masood": {"Roll_No": 12, "Marks": 89, "Gender": "Male"}, "Vishal": {"Roll_No": 34, "Marks": 89, "Gender": "Male"}}
# print(dict6, type(dict6))


#------------------------------------
# Indexing on Dict:

# d1 = {"A": 65, "D": 68, "a": 97, "b": 98, "@": 64}
# print(d1)
# print(d1["b"])
# print(d1["D"])

#------------------------------
# d1 = {"A": 65, "D": 68, "a": 97, "b": 98, "@": 64, "D": 100}
# d1["D"] = 100
# d1["Z"] = 23

# print(d1)

# Built in Methods of Dict:

d1 = {"A": 65, "D": 68, "a": 97, "b": 98, "@": 64, "D": 100}

# print(d1.items())
# print(d1.keys())
# print(d1.values())

# .get()
# print(d1.get("@"))

#.copy()
# d2 = d1.copy()
# print(d2)

# d1.pop('a')   # It deletes key value pair, using key
# print(d1)

# d1.popitem()   # It delets any last item
# print(d1)


# d1.clear()  # It deletes all elements
# print(d1)


#----- Some Other Operations:

# students = ["Masood", "Vishal", "Divya"]
# marks = [89, 78, 40]

# dict11 = dict(zip(students, marks))
# print(dict11)


# fruits = ["Apple", "Mango", "Pineapple", "Avocado"]

# dict12 = dict.fromkeys(fruits, "Sweet")
# print(dict12)


# dict13 = dict(mango="fruit", mobile="electronics", marks=34, city="Hyd")
# print(dict13)
