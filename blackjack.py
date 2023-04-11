import dealer, player, deck, hand

player_one = player.Player(input("What's Your name?"),input("How many chips do you want to start with?"))
# player_one = player.Player('KEITH', 500)
the_dealer = dealer.Dealer()
game_deck = deck.Deck()
game_on = True
round = 0
def bust_check(player):
    player.player_hand.ace_check()
    if player.player_hand.count > 21:
        print(f"{player.name} has {player.player_hand.count} points and BUSTS!!")
        return True
    else: return False
    
def reset(player, dealer, game_deck):
    player.player_hand.count = 0
    player.player_hand.aces = 0
    player.player_hand.ace_used = False
    player.player_hand.cards.clear()
    dealer.player_hand.count = 0
    dealer.player_hand.aces = 0
    dealer.player_hand.ace_used = False
    dealer.player_hand.cards.clear()
    
# print(f'{player_one.name} has ${player_one.chips} chips.')
while game_on:
    round += 1
    round_on = True
    print(f'Round {round}... START!')
    game_deck.shuffle_the_deck()
    player_one.bet()
    print("DEALER HAND")
    the_dealer.player_hand.starting_deal([game_deck.deal(), game_deck.deal()])
    print(the_dealer)
    player_one.player_hand.starting_deal([game_deck.deal(), game_deck.deal()])
    print(player_one.player_hand)
    while round_on: 
        print("------------------------------")
        if player_one.player_hand.count == 21:
            print(f'{player_one.name} has 21 points and WINS! You collect {player_one.bet_amount * 2} Chips!!')
            player_one.chips += player_one.bet_amount * 2
            round_on = False
            break
        player_choice = input("Hit or Stay? H/S").lower()
        if player_choice == "h":
            player_one.hit(game_deck.deal())
            print(f'{player_one.name} has {player_one.player_hand.count} points')
        elif player_choice == "s":
            player_one.stay()
        if bust_check(player_one):
            round_on = False
            print("DEALER WINS")
            player_one.bet_amount = "none"
            break
        if bust_check(the_dealer):
            round_on = False
            print(f'{player_one.name} WINS! You collect {player_one.bet_amount * 2} Chips!!')
            player_one.chips += player_one.bet_amount * 2
            round_on = False
            break

        dealer_choice = the_dealer.hit_or_stay(game_deck.deal())
        print(the_dealer)
        if dealer_choice and player_choice == "s":
            if the_dealer.player_hand.count > player_one.player_hand.count:
                print(f'DEALER has {the_dealer.player_hand.count} points, {player_one.name} has {player_one.player_hand.count} points.')
                print("DEALER WINS")
                player_one.bet_amount = "none"
                break
            elif the_dealer.player_hand.count < player_one.player_hand.count:
                print(f'DEALER has {the_dealer.player_hand.count} points, {player_one.name} has {player_one.player_hand.count} points.')
                print(f'{player_one.name} WINS! You collect {player_one.bet_amount * 2} Chips!!')
                player_one.chips += player_one.bet_amount * 2
                round_on = False
                break
        round_on = True
    keep_playing = input("do you want to play another round?? Y/N").lower()
    if keep_playing != "y":
        print(f'You ended with {player_one.chips} Chips! Thanks for playing!')
        break
    else: 
        reset(player_one, the_dealer, game_deck)
        print("New Round -------------")



        
