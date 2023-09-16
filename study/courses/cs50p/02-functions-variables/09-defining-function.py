
from re import X


def hello(to="user"):
    print("hello", to)

hello()
name = input("What is your name: ")
hello(name)