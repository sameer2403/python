# Method 1: Using a temporary variable
a = 5
b = 10

temp = a
a = b
b = temp

print(f"a = {a}, b = {b}")

# Method 2: Taking user input and adding two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sum = num1 + num2
print(f"Sum of {num1} and {num2} is {sum}")