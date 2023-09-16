
def main():
    name = int(input("Type X number: "))
    print("X squared is: ", square(name))

def square(n):
    return n * n
    #return n ** 2
    #return pow(n, 2)

main()