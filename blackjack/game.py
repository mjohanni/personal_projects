import cards
import random
dealer = []
player = [1,2,3,4,5,6]
dealer_total = 0
player_total = 0
score = [0,0]
D = 0
P = 0

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
    global dealer_total,player_total

    while len(dealer) < 2:
        dealer.append(draw_card())
    while len(player) < 2:
        player.append(draw_card())
    print("my cards: " + str(player))
    print("the dealer's hand: [hidden_card] " + str(dealer[1::]))
    
    for card in dealer:
    #adds up the dealer's cards
        card = card.split()
        if card[1] == "Ace":
            dealer_total += 1
        elif card[1].isdigit() == True:
            dealer_total += int(card[1])
        elif card[1] == 'King':
            dealer_total += 13 
        elif card[1] == 'Queen':
            dealer_total += 12
        elif card[1] == 'Jack':
            dealer_total += 11

    for card in player:
    #adds up the player's cards
        card = card.split()
        if card[1] == 'Ace':
            request = input("please select number '1' or '11' for ace: ")
            while int(request) != 1 or int(request) != 11:
                request = input("please select number '1' or '11' for ace: ")
            player_total += int(request)

        elif card[1].isdigit() == True:
            dealer_total += int(card[1])
        elif card[1] == 'King':
            dealer_total += 13 
        elif card[1] == 'Queen':
            dealer_total += 12
        elif card[1] == 'Jack':
            dealer_total += 11


def hit_or_hold(amount,user=False, end_game = False):
    """
    docstring
    """
    global player,dealer, dealer_total,player_total,D,P

    if user == True:
        if amount < 21:
            command = ''
            while command.lower() != 'hold' or command.lower() != 'hit':
                command = input("hold or hit? :")
                if command.lower() == 'hit':
                    new_card = draw_card()
                    player.append(new_card)
                    player_total = count(player)
                elif command.lower() == "hold":
                    #skip all turns
                    end_game = True
                    return end_game

    elif user == False:
        while amount < 16:
            new_card = draw_card()
            dealer.append(new_card)
            dealer_total = count(dealer)
        end_game = True
        return end_game



    # if amount == 21:
    #     if user == True:
    #         print("BLACKJACK!!! PLAYER WINS THE ROUND!")
    #         return
    #     print("BLACKJACK!!! DEALER WINS THE ROUND!")
    #     return

    # elif amount > 21:
    #     print("BUST")
    #     if user == True:
    #         print("DEALER WINS THE ROUND!")
    #         return
    #     print("PLAYER WINS THE ROUND!")
    #     return
    # pass


def count(user):
    global player_total,dealer_total
    """
    gets the total of all cards
    """
    total = 0
    if user == player_total:
        last_card = player[len(player) -1]
        total = player_total
        last_card = last_card.split()
        return total
    elif user == dealer_total:
        last_card = dealer[len(dealer) -1]
        total = dealer_total
        last_card = last_card.split()
        return total



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
    while my_turn == True:
        pass


if __name__ == '__main__':
    run_game()
    