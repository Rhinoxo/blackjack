# Blackjack program
# Started December 5, 2014
# by Justin Orner and Lance Orner

# Last Updated: April 13,2025

# This is a simple blackjack program that allows the user to play against the dealer.
# The user can hit or stand, and the dealer will hit until they reach a score of 17 or higher.
# The program will check for blackjack and busts, and will display the final scores.
# The program will also check for a push (tie) and will display the result of the game.

import random

# TODO:
# Finish win/loss logic
# Be able to play multiple games
# Handle Ace correctly
# Cleanup display
# Ability to bet
# Splitting hands
# Double down

def setupDeck():
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
        # Ace is 1 or 11
        if rank == 0:
            if score + 11 > 21:
                score += 1
            else:
                score += 11
        # Face cards are 10
        elif rank == 10 or rank == 11 or rank == 12:
            score += 10
        else:
            score += rank + 1
    return score

def printStatus(score,hand):
    print ("Hand:")
    printHand(hand)
    print (" Score: "+str(score))

def dealCard(hand):
    card=deck.pop()
    hand.append(card)
    return card


# Main
#test_deck()

# Deal two cards
phand=[]
dhand=[]
play=True
deck=setupDeck()

dealCard(phand)
dealCard(dhand)
dealCard(phand)
dealCard(dhand)
pscore = scoreHand(phand)
dscore = scoreHand(dhand)

print("\nPlayer ")
printStatus(pscore, phand)
print("\nDealer ")
printStatus(dscore, dhand)

#Check for blackjack
if pscore == 21 and dscore == 21:
    print("Push!")
    play=False
if pscore == 21:
    print("You Win!")
    play=False
elif dscore == 21:
    print("You Lose!")
    play=False
while play:
    # Player turn
    while pscore < 21:
        answer=input("Hit or Stand?")
        if answer.lower() == "hit":
            dealCard(phand)
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
    if pscore == 21:
        print("You Win!")
        play=False
        break
    elif pscore > 21:
        print("You Lost!")
        play=False
        break

    # Dealer turn
    while dscore <= 16:
        dealCard(dhand)
        pscore=scoreHand(phand)
        dscore=scoreHand(dhand)
        print("\nPlayer ")
        printStatus(pscore, phand)
        print("\nDealer ")
        printStatus(dscore, dhand)

    # Final scoring
    if pscore > dscore or dscore > 21:
        if dscore > 21:
            print("Dealer Bust!")
        print("You Win "+str(pscore)+" to "+str(dscore))
        play=False
    elif pscore < dscore:
        print("You Lost "+str(pscore)+" to "+str(dscore))
        play=False
    elif pscore == dscore:
        print("Push!")
        play=False



