# create tuples for suit and rank combinations. create key value pairs for values where keys are ranks, so value can be grabbed from rank
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {
    'Two': 2,
    'Three': 3,
    'Four' : 4,
    'Five' : 5,
    'Six' : 6,
    'Seven' : 7,
    'Eight' : 8,
    'Nine' : 9,
    'Ten' : 10,
    'Jack' : 10,
    'Queen' : 10,
    'King' : 10,
    'Ace' : 11
}

class Card:
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    # create a str version to announce the card
    def __str__(self):
        return f'{self.rank} of {self.suit}'