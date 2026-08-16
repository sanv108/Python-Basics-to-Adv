# ============================================================
#                  PYTHON OPERATORS
# ============================================================
# This file contains examples of different operators in Python.
#
# Topics Covered:
# 1. Arithmetic Operators
# 2. Comparison Operators
# 3. Logical Operators
# 4. Short-Circuit Evaluation
# 5. Bitwise Operators
# 6. Membership Operators
# 7. Identity Operators
# ============================================================


# ============================================================
# 1. ARITHMETIC OPERATORS
# ============================================================
# Used to perform mathematical operations.

a = 10
b = 3

print(a + b)   # Addition: 13
print(a - b)   # Subtraction: 7
print(a * b)   # Multiplication: 30
print(a / b)   # Division: 3.3333333333333335
print(a // b)  # Floor Division: 3
print(a % b)   # Modulus (Remainder): 1
print(a ** b)  # Exponent/Power: 1000


# ============================================================
# 2. COMPARISON OPERATORS
# ============================================================
# Used to compare two values.
# The result is always True or False.

a = 10
b = 3

print(a == b)   # Equal to: False
print(a != b)   # Not equal to: True
print(a > b)    # Greater than: True
print(a < b)    # Less than: False
print(a >= b)   # Greater than or equal to: True
print(a <= b)   # Less than or equal to: False


# ============================================================
# 3. LOGICAL OPERATORS
# ============================================================
# Used to combine multiple conditions.
#
# and → Both conditions must be True
# or  → At least one condition must be True
# not → Reverses the result

a = 10
b = 3

print(a > 5 and b < 5)  # True and True → True
print(a > 5 and b > 5)  # True and False → False

print(a > 5 or b > 5)   # True or False → True
print(a < 5 or b > 5)   # False or False → False

print(not(a > 5))       # not True → False
print(not(a < 5))       # not False → True


# ============================================================
# 4. SHORT-CIRCUIT EVALUATION
# ============================================================
# Python stops evaluating conditions when the final result
# is already known.
#
# AND → Stops when it finds False
# OR  → Stops when it finds True
# NOT → Reverses the result


# ----- AND Short-Circuit -----

print(a < 5 and b > 5)
# First condition is False.
# Therefore, the result will be False.
# Python does not need to evaluate the second condition.


# ----- OR Short-Circuit -----

print(a > 5 or b > 5)
# First condition is True.
# Therefore, the result will be True.
# Python does not need to evaluate the second condition.


# ============================================================
# 5. BITWISE OPERATORS
# ============================================================
# Bitwise operators work on the binary representation of numbers.
#
# a = 5 → 101
# b = 3 → 011

a = 5
b = 3


# ----- Bitwise AND (&) -----
# 101
# 011
# ---
# 001 → 1

print(a & b)   # Bitwise AND: 1


# ----- Bitwise OR (|) -----
# 101
# 011
# ---
# 111 → 7

print(a | b)   # Bitwise OR: 7


# ----- Bitwise XOR (^) -----
# 101
# 011
# ---
# 110 → 6
#
# XOR Rule:
# Same bits → 0
# Different bits → 1

print(a ^ b)   # Bitwise XOR: 6


# ----- Left Shift (<<) -----
# 5 = 101
# 101 << 1 = 1010
# 1010 = 10

print(a << 1)  # Left Shift: 10


# ----- Right Shift (>>) -----
# 5 = 101
# 101 >> 1 = 10
# 10 = 2

print(a >> 1)  # Right Shift: 2


# ============================================================
# 6. MEMBERSHIP OPERATORS
# ============================================================
# Used to check whether a value exists in a sequence.
#
# in     → Checks if value exists
# not in → Checks if value does not exist


name = "Sandeep"

print("S" in name)       # True
print("x" in name)       # False
print("x" not in name)   # True


# Membership operators can also be used with lists.

numbers = [10, 20, 30, 40]

print(20 in numbers)       # True
print(50 not in numbers)   # True


# ============================================================
# 7. IDENTITY OPERATORS
# ============================================================
# Used to check whether two variables refer to the SAME object.
#
# is     → Same object
# is not → Different objects


a = [10, 20, 30]
b = a

print(a is b)       # True
# Both variables refer to the same list object.


c = [10, 20, 30]

print(a is not c)   # True
# a and c have the same values,
# but they are different objects.


# ============================================================
# == VS is
# ============================================================
# == checks whether the VALUES are equal.
# is checks whether the OBJECTS are the same.


a = [10, 20, 30]
b = [10, 20, 30]

print(a == b)   # True → Values are the same
print(a is b)   # False → Objects are different


# ============================================================
#                    QUICK REVISION
# ============================================================
#
# Arithmetic:
# +   → Addition
# -   → Subtraction
# *   → Multiplication
# /   → Division
# //  → Floor Division
# %   → Modulus
# **  → Power
#
# Comparison:
# ==  → Equal
# !=  → Not Equal
# >   → Greater Than
# <   → Less Than
# >=  → Greater Than or Equal
# <=  → Less Than or Equal
#
# Logical:
# and → Both conditions must be True
# or  → At least one condition must be True
# not → Reverse the result
#
# Bitwise:
# &   → AND
# |   → OR
# ^   → XOR
# <<  → Left Shift
# >>  → Right Shift
#
# Membership:
# in     → Value exists
# not in → Value does not exist
#
# Identity:
# is     → Same object
# is not → Different objects
#
# Important:
# == → Compares values
# is → Compares object identity
# ============================================================