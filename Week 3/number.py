# x = int(input("What's x? "))
# print(f"x is {x}")
# """What's x? cat
# Traceback (most recent call last):
#   File "D:\PythonExperimentLab\Week 3\number.py", line 1, in <module>
#     x = int(input("What's x? "))
#         ^^^^^^^^^^^^^^^^^^^^^^^^
# ValueError: invalid literal for int() with base 10: 'cat'"""


# try:
#     x = int(input("What's x? "))
#     # print(f"x is {x}")
# except ValueError:
#     print("x is not an integer")

# print(f"x is {x}")
# What's x? cat
# x is not an integer
# Traceback (most recent call last):
#   File "D:\PythonExperimentLab\Week 3\number.py", line 15, in <module>
#     print(f"x is {x}")
#                   ^
# NameError: name 'x' is not defined


# try:
#     x = int(input("What's x? "))
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}")

# while True:
#     try:
#         x = int(input("What's x? "))
#         break
#     except ValueError:
#         print("x is not an integer")
#     # else:
#     #     break

# print(f"x is {x}")

def main():
    x = get_int()
    print(f"x ix {x}")

def get_int():
    while True:
        try:
            return int(input("What's x? "))
            # break
        except ValueError:
            # print("x is not an integer")
            pass
        # else:
        #     break

main()