#random.choice
#random.choices
#random.sample
import random

cards = ["jack", "queen", "king"]

def main():
    # print(random.choice(cards))
    # print(random.choices(cards, k=2)) #might answer ['queen', 'queen']
    # print(random.sample(cards, k=2))
    # print(random.choices(cards, weights=[100,0,0], k=2)) #['jack', 'jack']
    # print(random.choices(cards, weights=[75,20,5], k=2))
    random.seed(2)
    print(random.choices(cards, k=2))

main()