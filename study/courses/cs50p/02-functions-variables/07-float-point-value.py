
# docs.python.org/3/library/functions.html#round
## round(number[, ndigits])
## use the number 999 for X and 1 for Y to understand the example

x = float(input("Type X number: "))
y = float(input("Type Y number: "))

z = round(x + y)

print(f"{z:,}")