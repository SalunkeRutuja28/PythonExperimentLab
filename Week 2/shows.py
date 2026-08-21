#String methods

SHOWS = [
    " Avatar: the last airbender",
    "Ben 10",
    "Arthur",
    " Spongebob Squarepants",
    "Phineas and ferb",
    "Kim possible",
    "Jimmy neutron"
    "the Proud family"
]

def main():
    cleaned_shows = []
    for show in SHOWS:
        # print(show.capitalize())
        cleaned_shows.append(show.title().strip())

    # print(cleaned_shows)
    print(', '.join(cleaned_shows))

main()