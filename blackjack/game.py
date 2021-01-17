import cards
import random
dealer = []
player = []
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
            player_total += int(card[1])
        elif card[1] == 'King':
            player_total += 13 
        elif card[1] == 'Queen':
            player_total += 12
        elif card[1] == 'Jack':
            player_total += 11


def hit_or_hold(amount, end_game = False):
    """
    docstring
    """
    global player,dealer, dealer_total,player_total,D,P

    if amount == player_total:
        if amount < 21:
            command = ''
            while command.lower() != 'hold' or command.lower() != 'hit':
                command = input("hold or hit? :")
            if command.lower() == 'hit':
                new_card = draw_card()
                player.append(new_card)
                player_total = count(player)

            else:
                #skip all turns
                end_game = True
                return end_game

    elif amount == dealer_total:
        while amount < 16:
            new_card = draw_card()
            dealer.append(new_card)
            dealer_total = count(dealer)
        end_game = True
        return end_game


def count(user):
    global player_total,dealer_total
    """
    gets the total of all cards
    """
    total = 0
    if user == player:
        last_card = player[len(player) -1]
        total = player_total
        last_card = last_card.split()
        if last_card[1].isdigit() == True:
            total += int(last_card[1])
        elif last_card[1] == 'King':
            total += 13 
        elif last_card[1] == 'Queen':
            total += 12
        elif last_card[1] == 'Jack':
            total += 11
        elif last_card[1] == 'Ace':
            user_input = input("please select 1 or 11")
            while user_input != '1' or '11':
                user_input = input("please select 1 or 11")
        return total

    elif user == dealer:
        last_card = dealer[len(dealer) -1]
        total = dealer_total
        last_card = last_card.split()
        if last_card[1].isdigit() == True:
            total += int(last_card[1])
        elif last_card[1] == 'King':
            total += 13 
        elif last_card[1] == 'Queen':
            total += 12
        elif last_card[1] == 'Jack':
            total += 11
        elif last_card[1] == 'Ace':
            if (total + 11) == 21:
                total += 11
            else:
                total += 1
        return total


def check(p_total,d_total):
    global score
    """
    checks the end values of all cards drawn and changes the score accordingly
    """


    if (p_total == 21 and d_total == 21) or p_total == d_total:
        print("draw")
    elif p_total == 21 and d_total != 21:
        print("Player wins round with BLACKJACK!")
    elif d_total == 21 and p_total != 21:
        print("Dealer wins round with BLACKJACK!")
    
    if p_total != 21 and d_total != 21:
        if p_total > 21 and d_total < 21:
            print("bust!")
            print("dealer wins the round!")
        elif d_total > 21 and p_total < 21:
            print("bust!")
            print("player wins the round!")
        elif d_total < 21 and p_total < 21:
            if p_total > d_total:
                print("player wins the round!")
            else:
                print("dealer wins the round!")


def keep_score():
    pass


def run_game():
    """
    calls all functions and runs to game
    """
    global score, player, dealer

    dealer_turn = False
    start_game()
    print(str(player_total)+"   "+ str(dealer_total))
    dealer_turn = hit_or_hold(player_total)
    if dealer_turn == True:
        dealer_turn = False
        dealer_turn = hit_or_hold(dealer_total)
    check(player_total,dealer_total)


if __name__ == '__main__':
    run_game()