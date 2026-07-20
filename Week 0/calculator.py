# x = input("What's x? ")
# y = input("What's y? ")

# z = x + y
# z = int(x) + int(y)
# print(z)

# x = int(input("What's x? "))
# y = int(input("What's y? "))
# print(x + y)

# x = float(input("What's x? "))
# y = float(input("What's y? "))
# print(round(x + y))
# z = round(x + y)
# print(f"{z:,}")

# a = round( x / y, 2)
# a = x / y
# print(a)
# print(f"{a:.2f}")

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n*n
    # return n ** 2
    # return pow(n, 2)


main()