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
    
    if card not in dealer and card not in player:
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
            ace = get_ace()
            player_total += int(ace)
        elif card[1].isdigit() == True:
            player_total += int(card[1])
        elif card[1] == 'King':
            player_total += 13 
        elif card[1] == 'Queen':
            player_total += 12
        elif card[1] == 'Jack':
            player_total += 11


def get_ace():
    """
    selects and checks the ace value
    """
    ace = input("please select 1 or 11 for ace value")
    if ace == str(1) or ace == str(11):
        return ace
    return get_ace()


def get_command():
    command = input("please choose HIT or HOLD: ").lower()
    if command == "hit" or command == 'hold':
        return command
    return get_command()


def hit_or_hold(user, end_game = False):
    """
    docstring
    """
    global player,dealer, dealer_total,player_total,D,P

    if user == player:
        if player_total < 21:
            command = get_command()
            if command == 'hit':
                new_card = draw_card()
                player.append(new_card)
                player_total = count(player)
                print(player)
                print(str(player_total))
                return hit_or_hold(player)
        end_game = True        
        return end_game

    elif user == dealer:
        print(dealer)
        while dealer_total < 16:
            print("dealer hits")
            new_card = draw_card()
            dealer.append(new_card)
            dealer_total = count(dealer)
            print(dealer)
            print(dealer_total)
        print("dealer holds")
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

    if (p_total == 21 and d_total == 21) or p_total == d_total\
        or (p_total > 21 and d_total > 21):
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

    end_turn = False
    start_game()
    while True:
        end_turn = hit_or_hold(player)
        if end_turn == True:
            end_turn = False
            break
    while True:
        end_turn = hit_or_hold(dealer)
        if end_turn == True:
            break
    check(player_total,dealer_total)


if __name__ == '__main__':
    run_game()