name = input("What's your name ? ")
# if name == "Harry":
#     print("Gryffindor")
# elif name == "Hermoine":
#     print("Gryffindor")
# elif name == "Ron":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who? ")
match name:
    case "Harry" | "Hermoine" | "Ron":
        print("Gryffindor")
    # case "Hermoine":
    #     print("Gryffindor")
    # case "Ron":
    #     print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who? ")