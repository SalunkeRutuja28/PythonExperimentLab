#Libraries modules import
#random random.choice(seq)
#from
#random.randint
#random.shuffle(x)
import random #imports everything from random 
# from random import choice

coin = random.choice(["heads", "tails"])
print(coin)

number = random.randint(1,10)
print(number)

cards = ["jack", "king", "queen"]
random.shuffle(cards)
print(cards)