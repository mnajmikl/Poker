"""
pokerhands.py
@author: Mohammad Najmi
@version 0.0.1
"""
# Suits and faces of a deck of cards
suitchars: list = "♠ ♣ ♥ ♦".split()
suitnames: list = "Clubs Spades Hearts Diamonds".split()
facechars: list = "A 2 3 4 5 6 7 8 9 10 J Q K".split()

# Card values
cardsvalues: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Sample hand
cards = [('4', 'Diamonds'), ('3', 'Diamonds'), ('6', 'Diamonds'),
             ('2', 'Diamonds'), ('5', 'Diamonds')]

def hasflush(hands: list):
    """
    hasflush(cards: list)
    parameter: hands (list)
        Check for player hands with the same suits
    """
    if len(cards) == 5:
        checksuit = hands[0][1]
        cardswithchecksuit = 0
        for card in hands:
            if card[1] == checksuit:
                cardswithchecksuit += 1
        if cardswithchecksuit == 5:
            return True
    return False

def hasstraight(hands: list):
    """
    hasstraight(hands: list)
    parameter: hands (list)
        Check for player hands with incremental values
        e.g. {3, 4, 5, 6, 7} or {9, 10, J, Q, K}
        Conditional straights with Ace is to be implemented
    """
    if len(hands) == 5:
        cardincrementone = 0
        cardval = [cardsvalues[facechars.index(card[0])]\
                       for i, card in enumerate(hands)]
        cardval.sort()
        for i in range(len(cardval) - 1):
            if cardval[i] == cardval[i+1] - 1:
                cardincrementone += 1
        if cardincrementone == 4:
            return True
    return False

def hasstraightflush(hands: list):
    """
    hasstraightflush(hands: list)
    parameter: hands (list)
        Check if hands are both a straight and a flush
    """
    return hasflush(hands) and hasstraight(hands)

def handscore(hands: list):
    """
    handscore(hands: list)
    parameter: hands (list)
        Count the hand score
    """
    handvalue = 0
    if len(hands) == 5:
        for card in hands:
            handvalue += cardsvalues[facechars.index(card[0])]
    return handvalue

print(f"hasflush(cards) is: {hasflush(cards)}")
print(f"hasstraight(cards) is {hasstraight(cards)}")
print(f"hasstraightflush(cards) is {hasstraightflush(cards)}")
print(f"Hand value is {handscore(cards)}")
