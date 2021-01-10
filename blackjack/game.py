import cards
import random
dealer = []
player = []
dealer_total = 0
player_total = 0
score = [0,0]


def draw_card():
    """
    selects a card from the deck and checks if that card
    already exists in player or dealer's hand if it does 
    exist it redraws a new card
    """

    card = cards.cards_type[random.randint(0,len(cards.cards_type)-1)]\
        + cards.card_number[random.randint(0,len(cards.card_number)-1)]
    
    if card not in dealer or card not in player:
        return card
    return draw_card()


def start_game():
    """
    at the start this runs and draws 2 
    cards for both the player and the Dealer
    """
    while len(dealer) < 2:
        dealer.append(draw_card())
    while len(player) < 2:
        player.append(draw_card())
    print("my cards: " + str(player))
    print("the dealer's hand: [hidden_card] " + str(dealer[1::]))
    

def blackjack(amount,user=False, end_game = False):
    """
    docstring
    """
    global player,dealer
    if user == True:
        if amount < 21:
            command = ''
            while command.lower() != 'hold' or command.lower() != 'hit':
                command = input("hold or hit? :")
                if command.lower() == 'hit':
                    new_card = draw_card()
                    player.append(new_card)
                elif command.lower() == "hold":
                    #skip all turns
                    end_game = True
                    return end_game
    elif amount == 21:
        if user == True:
            print("BLACKJACK!!! PLAYER WINS THE ROUND!")
            return
        print("BLACKJACK!!! DEALER WINS THE ROUND!")
        return
    elif amount > 21:
        print("BUST")
        if user == True:
            print("DEALER WINS THE ROUND!")
            return
        print("PLAYER WINS THE ROUND!")
        return
    pass


def count():
    """
    gets the total of all cards
    """
    pass


def run_game():
    """
    calls all functions and runs to game
    """
    global score, player, dealer


    hold = False
    score[0] = score[0] +1
    start_game()
    my_turn = True
    my_total = count(dealer)
    print(my_total)


if __name__ == '__main__':
    run_game()
    