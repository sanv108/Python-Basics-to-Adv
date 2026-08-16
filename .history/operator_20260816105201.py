a = 10
b = 3

print(a + b)   # Addition → 13
print(a - b)   # Subtraction → 7
print(a * b)   # Multiplication → 30
print(a / b)   # Division → 3.3333333333333335
print(a // b)  # Floor Division → 3
print(a % b)   # Modulus (Remainder) → 1
print(a ** b)  # Exponent/Power → 1000

# Comparison operators
a = 10
b = 3

print(a == b)   # Equal to → False
print(a != b)   # Not equal to → True
print(a > b)    # Greater than → True
print(a < b)    # Less than → False
print(a >= b)   # Greater than or equal to → True
print(a <= b)   # Less than or equal to → False


#Logical operators  
a = 10
b = 3

print(a > 5 and b < 5)    # True and True → True
print(a > 5 and b > 5)    # True and False → False


a = 10

print(not(a > 5))    # not True → False
print(not(a < 5))    # not False → True


# ==========================================
#       SHORT-CIRCUIT EVALUATION
# ==========================================

# Short-circuit means:
# Python stops checking conditions when
# the final result is already known.


# ==========================================
# 1. AND (and)
# ==========================================

# AND → Stops when it finds FALSE

a = 10
b = 3

print(a > 5 and b > 5)
# True and False → False
# Second condition is checked because first is True.


print(a < 5 and b > 5)
# False and anything → False
# Python stops after the first condition.
# No need to check the second condition.


# ==========================================
# 2. OR (or)
# ==========================================

# OR → Stops when it finds TRUE

print(a > 5 or b > 5)
# True or False → True
# Python stops after the first condition.


print(a < 5 or b > 5)
# False or False → False
# Python checks both conditions because
# it needs to find at least one True.


# ==========================================
# 3. NOT (not)
# ==========================================

# NOT → Reverses the result
# It does NOT perform short-circuiting by itself.

print(not(a > 5))
# not True → False

print(not(a < 5))
# not False → True


# ==========================================
# QUICK RULE
# ==========================================

# AND → Stop at FALSE
# OR  → Stop at TRUE
# NOT → Reverse the result

# ==========================================
#       BITWISE OPERATORS
# ==========================================

a = 5
b = 3

# Binary:
# 5 = 101
# 3 = 011


# ==========================================
# 1. Bitwise AND (&)
# ==========================================

print(a & b)

#    101   → 5
# &  011   → 3
# --------
#    001   → 1

# Output: 1


# ==========================================
# 2. Bitwise OR (|)
# ==========================================

print(a | b)

#    101   → 5
# |  011   → 3
# --------
#    111   → 7

# Output: 7


# ==========================================
# 3. Bitwise XOR (^)
# ==========================================

print(a ^ b)

#    101   → 5
# ^  011   → 3
# --------
#    110   → 6

# Output: 6

# XOR Rule:
# Same bits  → 0
# Different  → 1


# ==========================================
# 4. Left Shift (<<)
# ==========================================

print(a << 1)

# 5 = 101
# 101 << 1 = 1010
# 1010 = 10

# Output: 10


# ==========================================
# 5. Right Shift (>>)
# ==========================================

print(a >> 1)

# 5 = 101
# 101 >> 1 = 10
# 10 = 2

# Output: 2


# ==========================================
# QUICK REVISION
# ==========================================

# &   → Bitwise AND
# |   → Bitwise OR
# ^   → Bitwise XOR
# <<  → Left Shift
# >>  → Right Shift
