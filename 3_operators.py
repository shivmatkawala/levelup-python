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
s1 = {12, 34, 56, 7, 8,  8, 9, False}

        # in 
# print(0 in s1)
# print(111 in s1)

        # not in
print(False not in s1)
print(111 not in s1)

    # Logical Operators:
        # and
        # or
        # not

    # Ternary Operators:

    # Bitwise Operators:
        # &  (AND)
        # |  (OR)
        # ^  (XOR)
