
# ask customer name
name = input("What is your name? ").strip().title()

firstName, lastName = name.split("   ")
# print on screen
print(f"Hello, {firstName} {lastName}")