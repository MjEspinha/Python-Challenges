# Step 1
age = 25

# Step 2
name = "Alice"

# Step 3
price = 19.99

# Step 4
print("Name:", name)
print("Age:", age)
print("Price:", price)
print()

# Step 5
a = 10
b = 3
print("Addition:", a + b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print()

# Step 6
x = True
y = False
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)
print()

# Step 7
number = 7
if number > 10:
    print("The number is greater than 10.")
elif number == 10:
    print("The number is exactly 10.")
else:
    print("The number is less than 10.")
print()

# Step 8
count = 3
while count > 0:
    print("Counting down:", count)
    count -= 1
print("Lift off!")
print()

# Step 9
for i in range(5):
    print("Number:", i)
print()

# Step 10
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
print()

# Step 11
colors = ("red", "green", "blue")
for color in colors:
    print(color)
print()

# Step 12
def greet():
    message = "Hello from the function!"
    return message

# Step 13
result = greet()
print(result)
