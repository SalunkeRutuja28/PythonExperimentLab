emoticon = "v.v"

def main():
    global emoticon
    say("Is anyone there?")
    emoticon = ":D"
    say("Oh, Hi!")


def say(phrase):
    print(phrase + " " + emoticon)


main()