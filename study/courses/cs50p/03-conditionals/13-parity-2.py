#!/usr/bin/env python3
def main():
    x = int(input("what is X? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return True if n % 2 == 0 else False

main()