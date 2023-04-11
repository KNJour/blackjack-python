import random, hand

class Dealer:
    def __init__(self):
        self.name = "Dealer"
        self.player_hand = hand.Hand()

    def hit_or_stay(self, deck, isDealer=True):
        if self.player_hand.count < 17:
            print("DEALER HITS")
            self.player_hand.add_cards(deck, isDealer)
            return False
        else:
            print("DEALER STAYS")
            return True
            
    def __str__(self):
        if len(self.player_hand.cards) < 2:
            print("DEALER HAS ONE FACE DOWN CARD")
        else:
            print("DEALER HAS ONE FACE DOWN CARD")
            for i in range(1, len(self.player_hand.cards)):
                print(f'{self.player_hand.cards[i].rank} of {self.player_hand.cards[i].suit} -- {self.player_hand.cards[i].value} points')
        return f'total visible dealer points = {self.player_hand.count - self.player_hand.cards[0].value}'