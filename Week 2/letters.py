#for loop
def main():
    # print(write_letters("Mario","Princess Peach"))
    # print(write_letters("Luigi","Princess Peach"))
    # print(write_letters("Daisy","Princess Peach"))
    # print(write_letters("Yoshi","Princess Peach"))
    
    names = ["Mario", "Luigi", "Daisy", "Yoshi"]
    # for i in range(len(names)):
    for name in names:
        print(write_letters(name, "Princess Peach"))


def write_letters(receiver, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    Dear {receiver},

    You are cordially invited to a ball at 
    Peach's castle this evening at 7:00 PM.

    Sincerely,
    {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+    
    """

main()