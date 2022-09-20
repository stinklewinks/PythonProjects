import random
coin = ['heads', 'tails']
flip = random.randint(0, 1)

def coin_flip(coin, flip):
    return coin[flip]

print(coin_flip(coin, flip))