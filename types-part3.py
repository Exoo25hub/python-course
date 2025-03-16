#*******************************
#           Types              * 
#*******************************
# 1. Int
a = int(9)
print(a)  # Output: 9999999

# 2. Float
b = float(5.4)
print(b)  # Output: 5.4

# 3. String
c = str("Mehdi")
print(c)  # Output: 'Mehdi'

# 4. Boolean
d = bool(1)  # True because 1 is truthy
print(d)  # Output: True

# 5. List
e = list([1, 2, 3, 4, 5])
print(e)  # Output: [1, 2, 3, 4, 5]

# 6. Dictionary
f = dict(name="Mehdi", class_=5, age=9)  # Using `class_` since `class` is a keyword in Python
print(f)  # Output: {'name': 'Mehdi', 'class_': 5, 'age': 9}

# 7. Range
g = range(5)  # Generates numbers from 0 to 4
print(list(g))  # Output: [0, 1, 2, 3, 4]

# 8. Complex Number
h = complex(2, 3)  # 2 + 3j
print(h)  # Output: (2+3j)
