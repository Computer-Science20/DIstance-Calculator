# Get the Input Values
x1 = float(input("Please enter a number: "))
y1 = float(input("Please enter another number: "))
x2 = float(input("Please enter another number: "))
y2 = float(input("Please enter another number: "))

# Process
d = ((x2 - x1) ** 2 (y2 - y1) ** 2) ** 0.5

# Output Results
print("The distance between the two points is" + str(d) + ".")
