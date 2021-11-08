# Suits and faces of a deck of cards
suitchars: list = "♠ ♣ ♥ ♦".split()
suitnames: list = "Clubs Spades Hearts Diamonds".split()
facechars: list = "A 2 3 4 5 6 7 8 9 10 J Q K".split()

# Card values
cardsvalues: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

cards = [('4', 'Diamonds'), ('3', 'Diamonds'), ('6', 'Diamonds'),
             ('2', 'Diamonds'), ('5', 'Diamonds')]

def hasflush(cards: list):
    if len(cards) == 5:
        checksuit = cards[0][1]
        cardswithchecksuit = 0
        for i, card in enumerate(cards):
            if cards[i][1] == checksuit:
                cardswithchecksuit += 1
        if cardswithchecksuit == 5:
            return True
    return False

def hasstraight(cards: list):
    if len(cards) == 5:
        cardincrementone = 0
        cardval = [cardsvalues[facechars.index(card[0])]\
                       for i, card in enumerate(cards)]
        cardval.sort()
        for i in range(len(cardval) - 1):
            if cardval[i] == cardval[i+1] - 1:
                cardincrementone += 1
        if cardincrementone == 4:
            return True
    return False

def hasstraightflush(cards: list):
    return hasflush(cards) and hasstraight(cards)

def handscore(cards: list):
    handvalue = 0
    if len(cards) == 5:
        for i, card in enumerate(cards):
            handvalue += cardsvalues[facechars.index(card[0])]
    return handvalue
        

print(f"hasflush(cards) is: {hasflush(cards)}")
print(f"hasstraight(cards) is {hasstraight(cards)}")
print(f"hasstraightflush(cards) is {hasstraightflush(cards)}")
print(f"Hand value is {handscore(cards)}")
