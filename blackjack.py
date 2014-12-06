# Blackjack program
# Started December 5, 2014
# by Justin Orner and Lance Orner

import random

def setup_deck ():
    deck=[]
    for rank in range(0,13):
        for suit in range(0,4):
            card=[rank,suit]
            deck.append(card)
    random.shuffle(deck);
    return deck

def print_card(card):
    rank = card[0]
    ranknames = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]   
    rankname = ranknames[rank]
        
    suit = card[1]
    suitnames = ["Diamonds", "Clubs", "Hearts", "Spades"]
    suitname = suitnames[suit]

    print (rankname + " of " + suitname)
    
# Testing functions
def test_deck():
    deck=setup_deck()
    for card in deck:
        print_card(card)

    # Check the deck size
    decksize = len(deck)
    assert decksize == 52
    print("Cards: "+str(decksize))

# Main
test_deck()
