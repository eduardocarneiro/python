"""
Official Python documentation explain how is the print() function behavior
https://docs.python.org/3/library/functions.html#print
"""
name = input("What is your name? ")
print("Hello, " + name)

print("Hello,", name)

print("Hello,", name, end="___")

print("Hello, ", name, sep="AAA")

print("Hello, \"World\"")

print(f"Hello, {name}")