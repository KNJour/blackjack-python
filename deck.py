import random
import card

class Deck:
    def __init__(self):
        self.all_cards = []
        # loop through all possible suit and rank combinations to create a ful deck of cards. 
        for x in card.suits:
            for y in card.ranks:
                one_card = card.Card(y, x)
                self.all_cards.append(one_card)

    def shuffle_the_deck(self):
        self.all_cards.clear()
        for x in card.suits:
            for y in card.ranks:
                one_card = card.Card(y, x)
                self.all_cards.append(one_card)
        random.shuffle(self.all_cards)
    def deal(self):
        return self.all_cards.pop()

    def __str__(self):
        return f'the deck has {len(self.all_cards)} cards remaining'
    
    
