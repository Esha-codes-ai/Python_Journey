# ==========================================================
# Assignment Operators in Python
# Assignment operators are used to assign values to variables.
# They can also update the existing value of a variable.
# ==========================================================

# Taking input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# += (Addition Assignment)
a = num1          # Store the original value of num1
a += num2         # Same as: a = a + num2
print("+= :", a)

# -= (Subtraction Assignment)
a = num1
a -= num2         # Same as: a = a - num2
print("-= :", a)

# *= (Multiplication Assignment)
a = num1
a *= num2         # Same as: a = a * num2
print("*= :", a)

# /= (Division Assignment)
a = num1
a /= num2         # Same as: a = a / num2
print("/= :", a)

# //= (Floor Division Assignment)
a = num1
a //= num2        # Same as: a = a // num2
print("//= :", a)

# **= (Exponentiation Assignment)
a = num1
a **= num2        # Same as: a = a ** num2
print("**= :", a)

# %= (Modulus Assignment)
a = num1
a %= num2         # Same as: a = a % num2
print("%= :", a)

# &= (Bitwise AND Assignment)
a = num1
a &= num2         # Same as: a = a & num2
print("&= :", a)

# |= (Bitwise OR Assignment)
a = num1
a |= num2         # Same as: a = a | num2
print("|= :", a)

# ^= (Bitwise XOR Assignment)
a = num1
a ^= num2         # Same as: a = a ^ num2
print("^= :", a)

# >>= (Right Shift Assignment)
a = num1
a >>= num2        # Same as: a = a >> num2
print(">>= :", a)

# <<= (Left Shift Assignment)
a = num1
a <<= num2        # Same as: a = a << num2
print("<<= :", a)