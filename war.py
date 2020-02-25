import random

def create_deck(suites=4, type_cards=13):
    #creates deck of cards with 4 suites and 13 different types
    cards = []
    for suite in range(suites):
        for type_card in range(1, type_cards+1):
            cards.append(type_card)
    random.shuffle(cards)
    return cards

def play_war(deck):
    p1_cards = deck[:len(deck)/2]
    p2_cards = deck[len(deck)/2:]
    p1_stash =[]
    p2_stash = []

    round = 1
    while p1_cards and p2_cards:
        p1_card = p1_cards.pop()
        p2_card = p1_cards.pop()

        if p1_card == p2_card:
            p1_stash.extend([p1_card]+p1_cards[-3:])
            p1_cards = p1_cards[:-3]
            p1_cards.append(p1_stash.pop())

            p2_stash.extend([p2_card]+p2_cards[-3:])
            p2_cards = p2_cards[:-3]
            p2_cards.append(p2_stash.pop())