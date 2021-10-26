import random

#generating deck of cards
nums = [1, 2, 3, 4, 5, 6, 7, 7, 9, 10, 11, 12, 13]
suit = ['hearts', 'spades', 'clubs','diamonds']
deck = []
for i in nums:
    for j in suit:
        deck.append((i, j))

#deck is a list of tuples
#consider an arbitrary 3 player heads-up variant
#consider 100 arbitrary games and initial call is say $5

c1, c2, c3 = 100, 100, 100

for _ in range(100):

    #assigning init cash & cards to players
    c1 -= 5
    c2 -= 5
    c3 -= 5

    cards = random.sample(deck, 3)
    p1, p2, p3 = cards[0], cards[1], cards[2]

    if max(p1[0], p2[0], p3[0]) == p1[0]:
        c1+=15
    if max(p1[0], p2[0], p3[0]) == p2[0]:
        c2+=15
    if max(p1[0], p2[0], p3[0]) == p3[0]:
        c3+=15

    print (c1,c2, c3)

    if c1 == 0 or c2 == 0 or c3 == 0:
        break

#if a naive 'always bet' strat is utilized by all 3 players, cash distributions is trinomial . . .
#interesting question - how many rounds until the game is over? expected value
