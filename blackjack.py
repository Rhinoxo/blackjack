# Blackjack program
# Started December 5, 2014
# by Justin Orner and Lance Orner

import random

# TODO:
# Finish win/loss logic
# Be able to play multiple games
# Handle Ace correctly
# Cleanup display
# Ability to bet
# Splitting hands
# Double down

def setupDeck ():
    deck=[]
    for rank in range(0,13):
        for suit in range(0,4):
            card=[rank,suit]
            deck.append(card)
    random.shuffle(deck)
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

def printStatus(score,hand):
    print ("Hand:")
    printHand(hand)
    print (" Score: "+str(score))


# Main
#test_deck()

# Deal two cards
phand=[]
dhand=[]
play=True
deck=setupDeck()

phand.append(deck.pop())
dhand.append(deck.pop())
phand.append(deck.pop())
dhand.append(deck.pop())
pscore = scoreHand(phand)
dscore = scoreHand(dhand)

print("\nPlayer ")
printStatus(pscore, phand)
print("\nDealer ")
printStatus(dscore, dhand)
if pscore == 21:
    print("You Win!")
    play=False
elif dscore == 21:
    print("You Lose!")
    play=False
while play:
    if pscore < 21:
        while pscore < 21:
            answer=input("Hit or Stand?")
            if answer.lower() == "hit":
                phand.append(deck.pop())
            elif answer.lower() == "stand":
                break
            else:
                answer=input("Answer Not Valid! Try Again!")
            pscore=scoreHand(phand)
            dscore=scoreHand(dhand)
            print("\nPlayer ")
            printStatus(pscore, phand)
            print("\nDealer ")
            printStatus(dscore, dhand)
    elif pscore == 21:
        break
    else:
        print("You Lost!")
        play=False
        break
    if dscore <=16:
        while dscore <= 16:
            dhand.append(deck.pop())
            pscore=scoreHand(phand)
            dscore=scoreHand(dhand)
            print("\nPlayer ")
            printStatus(pscore, phand)
            print("\nDealer ")
            printStatus(dscore, dhand)
    if pscore > dscore:
        print("You Win "+str(pscore)+" to "+str(dscore))
        play=False
    elif pscore < dscore:
        print("You Lost "+str(pscore)+" to "+str(dscore))
        play=False



