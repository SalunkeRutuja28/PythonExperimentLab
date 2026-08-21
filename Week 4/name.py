#command-line arguements in python code
#sys
#sys.argv
#sys.exit()

import sys

# print("hello, my name is", sys.argv[1]) 
# python name.py David
# Output: hello, my name is David
# sys.argv[0] is name of the python file that is name.py
# therefore, sys.argv[1] is David


# try:
#     print("hello, my name is", sys.argv[1]) 
# except IndexError:
#     print("Too few arguements")


# if len(sys.argv) < 2:
#     print("Too few arguements")
# elif len(sys.argv) > 2:
#     print("Too many arguements")
# else:
#     print("hello, my name is", sys.argv[1])

# if len(sys.argv) < 2:
#     sys.exit("Too few arguements")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguements")

# print("hello, my name is", sys.argv[1])

# if len(sys.argv) < 2:
#     sys.exit("Too few arguements")
# for arg in sys.argv:
#     print("hello, my name is", arg)

#slice

if len(sys.argv) < 2:
    sys.exit("Too few arguements")
for arg in sys.argv[1:]:
    print("hello, my name is", arg)