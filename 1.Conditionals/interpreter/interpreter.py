# Prompt the user to enter an arithmetic expression
expression = input("Enter an arithmetic expression (in the format x y z): ")

# Split the expression into three variables
x, op, y = expression.split()

# Convert x and y to floats
x = float(x)
y = float(y)

# Perform the arithmetic operation specified by op
if op == "+":
    result = x + y
elif op == "-":
    result = x - y
elif op == "*":
    result = x * y
elif op == "/":
    result = x / y

# Output the result as a floating-point value formatted to one decimal place
print("{:.1f}".format(result))
