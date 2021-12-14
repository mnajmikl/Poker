# -*- coding: utf-8 -*-
"""
pokerhands-v2.py
@author: Mohammad Najmi
@version 0.0.1
"""

# Suits and faces of a deck of cards
# suitchars: list = "♠ ♣ ♥ ♦".split()
suitnames: list = "Clubs Spades Hearts Diamonds".split()
facechars: list = "A 2 3 4 5 6 7 8 9 10 J Q K".split()

# Card values
cardsvalues: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Sample hand
cards = [('10', 'Diamonds'), ('A', 'Diamonds'), ('K', 'Diamonds'),
             ('Q', 'Diamonds'), ('J', 'Diamonds')]

def hasflush(hand: list):
    """
    hasflush(hand: list)
    parameter: hand (list)
        Check for player hand for flush (all cards are in the same suit)
    """
    if len(hand) == 5:
        cardfaces = []
        checksuit = hand[0][1]
        for card in hand:
            cardfaces.append(suitnames[suitnames.index(card[1])])
        cardfaces.sort()
        if cardfaces.count(checksuit) == 5:
            return True
        else:
            return False
    else:
        return False

def hasstraight(hand: list):
    """
    hasstraight(hand: list)
    parameter: hand (list)
        Check for player hand for straight
        e.g. {3, 4, 5, 6, 7} or {9, 10, J, Q, K}
    """
    if len(hand) == 5:
        cardincrementone = 0
        cardval = [cardsvalues[facechars.index(card[0])]\
                       for i, card in enumerate(hand)]
        cardval.sort()
        hasAce = False
        if cardval[0] == 1:
            hasAce = True 
        checkstart = 0
        checkend = len(cardval) - 1
        if hasAce:
            checkstart = 1
            if cardval[1] != 2 and cardval[1] != 10:
                return False
        for i in range(checkstart, checkend):
            if cardval[i] == cardval[i+1] - 1:
                cardincrementone += 1
        if hasAce and cardincrementone == 3:
            return True
        elif cardincrementone == 4:
            return True
        else:
            return False
    else:
        return False

def hasstraightflush(hand: list):
    """
    hasstraightflush(hand: list)
    parameter: hand (list)
        Check if hand for straight flush
        Straight Flush is the second highest possible rank
        if we do not include Royal Flush in the game
    """
    return hasflush(hand) and hasstraight(hand)

def hasroyalflush(hand: list):
    """
    hasroyalflush(hand: list)
    parameter: hand (list)
        Check if hand has royal flush
        Royal Flush is a straight flush consists of A, 10, J, Q, K
    """
    if len(hand) == 5:
        isroyal = False
        cardval = [cardsvalues[facechars.index(card[0])]\
                       for i, card in enumerate(hand)]
        cardval.sort()
        # Royal if hand conists of A, 10, J, Q, K (1, 10, 11, 12, 13)
        if (cardval[0] == 1 and cardval[1] == 10 and cardval[2] == 11
                and cardval[3] == 12 and cardval[4] == 13):
            isroyal = True
            
    return hasflush(hand) and hasstraight(hand) and isroyal

def handscore(hand: list):
    """
    handscore(hand: list)
    parameter: hand (list)
        Count the hand score
    """
    handvalue = 0
    if len(hand) == 5:
        for card in hand:
            val = facechars.index(card[0])
            handvalue += cardsvalues[val]
            # If the card value is 1 (Ace), add another 13
            if cardsvalues[val] == 1:
                handvalue += 13
    return handvalue

def hasfourofakind(hand: list):
    """
    hasfourofakind(hand: list)
    parameter: hand (list)
        Check for player hand for four of a kind
    """
    if len(hand) == 5:
        cardval = [cardsvalues[facechars.index(card[0])]\
                       for i, card in enumerate(hand)]
        if cardval.count(cardval[0]) == 4 or cardval.count(cardval[1]) == 4:
            return True
        return False
    else:
        return False
    
def hasthreeofakind(hand: list):
    """
    hasthreeofakind(hand: list)
    parameter: hand (list)
        Check for player hand for three of a kind
    """
    if len(hand) == 5:
        cardval = [cardsvalues[facechars.index(card[0])]\
                       for i, card in enumerate(hand)]
        cardval.sort()
        if (cardval.count(cardval[0]) == 3 or cardval.count(cardval[1]) == 3 
                or cardval.count(cardval[2]) == 3):
            return True
        return False
    else:
        return False

def hasonepair(hand: list):
    """
    hasonepair(hand: list)
    parameter: hand (list)
        Check for player hand for one pair
    """
    # Return False if hand has two pairs
    if hastwopairs(hand):
        return False
    
    if len(hand) == 5:
        cardval = [cardsvalues[facechars.index(card[0])]\
                       for i, card in enumerate(hand)]
        cardval.sort()
        if (cardval.count(cardval[0]) == 2 or cardval.count(cardval[1]) == 2 
                or cardval.count(cardval[2]) == 2 or 
                    cardval.count(cardval[3]) == 2):
            return True
        return False
    else:
        return False
    
def hastwopairs(hand: list):
    """
    hastwopairs(hand: list)
    parameter: hand (list)
        Check for player hand for two pairs
    """
    if len(hand) == 5:
        cardval = [cardsvalues[facechars.index(card[0])]\
                       for i, card in enumerate(hand)]
    cardval.sort()
    if (cardval.count(cardval[0]) == 2 and 
        (cardval.count(cardval[2]) == 2 or cardval.count(cardval[3]) == 2)):
        return True
    elif (cardval.count(cardval[1]) == 2 and cardval.count(cardval[3]) == 2):
        return True
    else:
        return False

def hasfullhouse(hand: list):
    """
    hasfullhouse(hand: list)
    parameter: hand (list)
        Check for player hand for full house (one pair and three of a kind)
    """
    return hasonepair(hand) and hasthreeofakind(hand)

print(f"hasflush(cards) is: {hasflush(cards)}")
print(f"hasstraight(cards) is {hasstraight(cards)}")
print(f"hasstraightflush(cards) is {hasstraightflush(cards)}")
print(f"hasroyalflush(cards) is {hasroyalflush(cards)}")
print(f"hasonepair(cards) is {hasonepair(cards)}")
print(f"hastwopairs(cards) is {hastwopairs(cards)}")
print(f"hasfourofakind(cards) is {hasfourofakind(cards)}")
print(f"hasthreeofakind(cards) is {hasthreeofakind(cards)}")
print(f"hasfullhouse(cards) is {hasfullhouse(cards)}")
print(f"Hand value is {handscore(cards)}")
