import random

def create_deck(suites=4, type_cards=13):
    #creates deck of cards with 4 suites and 13 different types
    cards = []
    for suite in range(suites):
        for type_card in range(1, type_cards+1):
            cards.append(type_card)
    random.shuffle(cards)
    return cards