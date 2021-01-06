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
    print("the dealer's hand: hidden_card " + str(dealer[1::]))


def blackjack(amount):
    """
    docstring
    """
    
    pass


def count(cards):
    """
    docstring
    """
    pass

if __name__ == '__main__':
    start_game()
    