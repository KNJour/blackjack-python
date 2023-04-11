import card, hand

class Player:
    def __init__(self, name, chips):
        self.name = name
        self.player_hand = hand.Hand()
        try: 
            amount = float(chips)
        except:
            print("not a valid number for chips, starting chips set to 500")
            amount = 500
        finally: 
            self.chips = amount
        self.bet_amount = "none"
    
    def bet(self):
        the_bet = "none"
        while type(the_bet) != float :
            the_bet = input(f"You have ${self.chips} chips, how much would you like to bet?")
            
            try:
                the_bet = float(the_bet)
            except:
                print("that is not a valid betting amount)")
            finally:
                if (self.chips - the_bet) < 0:
                    print("You don't have enough chips to bet that")
                    the_bet = "none"
                else:
                    self.chips -= the_bet
                    self.bet_amount = the_bet
    
    def get_chips(self, bet):
        winnings = bet * 2
        self.chips += winnings
        print(f"{self.name} wins {winnings} chips.")

    def hit(self, card, isDealer=False):
        print(f'{self.name} chose to HIT')
        self.player_hand.add_cards(card, isDealer)
    
    def stay(self):
        print(f'{self.name} chose to STAY')
    
    def __str__(self):
        return f'{self.name} has {self.chips} total chips.'
        