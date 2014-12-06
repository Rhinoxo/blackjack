# Blackjack program
# Started December 5, 2014
# by Justin Orner and Lance Orner

import random

def setupDeck ():
    deck=[]
    for rank in range(0,13):
        for suit in range(0,4):
            card=[rank,suit]
            deck.append(card)
    random.shuffle(deck);
    return deck

def printCard(card):
    rank = card[0]
    ranknames = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]   
    rankname = ranknames[rank]
        
    suit = card[1]
    suitnames = ["Diamonds", "Clubs", "Hearts", "Spades"]
    suitname = suitnames[suit]

    print (rankname + " of " + suitname)

def printHand(deck):
    for card in deck:
        printCard(card)

# Testing functions
def testDeck():
    deck=setupDeck()
    # Check the deck size
    decksize = len(deck)
    assert decksize == 52
    print("Cards: "+str(decksize))

def scoreHand(hand):
    score=0
    for card in hand:
        rank = card[0]
        if rank == 0:
            score+=11
        elif rank == 10 or rank == 11 or rank == 12:
            score+=10
        else:
            score += rank + 1
    return score


# Main
#test_deck()

# Deal two cards
phand=[]
dhand=[]

deck=setupDeck()

phand.append(deck.pop())
dhand.append(deck.pop())
phand.append(deck.pop())
dhand.append(deck.pop())

print ("\nPlayers hand:")
printHand(phand)
print ("Score: "+str(scoreHand(phand)))
print ("\nDealers hand:")
printHand(dhand)
print ("Score: "+str(scoreHand(dhand)))

