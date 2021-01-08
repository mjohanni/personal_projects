import cards
import random
dealer = []
player = []

score = [0,0]

def draw_card():
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


def blackjack(amount,user=False):
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
                    pass
    pass


def count(cards,player=False):
    """
    gets the total of all cards
    """

    total = 0
    for card in cards:
        card  = card.split()
        if card[1].isdigit() == True:
            total += int(card[1])
        elif card[1] == 'ace':
            if player == False:
                total += 1
            else:
                ace = input("Should ace be 1 or 11?")
                while ace != '1' or ace != '11':
                    ace = input("Please enter correct number: ")
                total += int(ace)
        else:
            if card[1] == 'Jack':
                total += 11
            elif card[1] == 'Queen':
                total += 12
            elif card[1] == 'King':
                total += 13
    return total

if __name__ == '__main__':
    start_game()
    my_turn = True
    my_total = count(dealer)
    print(my_total)
    