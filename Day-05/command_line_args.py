import sys

def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
operation = sys.argv[3]
if operation == "add":
    print(f"The addition of {num1} and {num2} is {add(num1, num2)}")
elif operation == "subtract":
    print(f"The subtraction of {num1} and {num2} is {subtract(num1, num2)}")    
elif operation == "multiply":
    print(f"The multiplication of {num1} and {num2} is {multiply(num1, num2)}")
else:
    print("Invalid operation. Please use add, subtract, or multiply.")  
