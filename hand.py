
class Hand:
    def __init__(self):
        self.cards = []
        self.count = 0
        self.aces = 0
        self.ace_used = False

    def add_cards(self, new_card, isDealer):
            # if dealer, does not reveal name of facedown card and does not include 1st card in count. 
        self.count += new_card.value
        self.cards.append(new_card)
        if isDealer:
            if len(self.cards) < 2:
                print("DEALER PLAYS FACE DOWN CARD")
            else:
                print(f'DEALER dealt {new_card.rank} of {new_card.suit} -- {new_card.value}')
        # player logic
        else:
            print(f'PLAYER dealt {new_card.rank} of {new_card.suit} -- {new_card.value}')
        if new_card.rank == "Ace":
                self.aces += 1

    def starting_deal(self, new_cards):
        for card in new_cards:
            self.cards.append(card)
            self.count += card.value
            if card.rank == "Ace":
                self.aces += 1
    

    def ace_check(self):
        if self.aces > 0 and self.count > 21 and not self.ace_used:
            self.count -= 10
            print(f'Ace reduced to, new amount: {self.count}')
            self.ace_used = True

    def __str__(self):
        print("PLAYER HAND")
        for card in self.cards:
            print(f'{card.rank} of {card.suit} -- {card.value} points')
        return f'total points = {self.count}'