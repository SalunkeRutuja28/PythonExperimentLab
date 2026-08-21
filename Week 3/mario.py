# Debugging
def main():
    height = int(input("Height: "))
    pyramid(height)



def pyramid(n):
    for i in range(n):
        print("#"*(i+1)) # can be replaced with print_row(width)


if __name__ == "__main__":
    main()