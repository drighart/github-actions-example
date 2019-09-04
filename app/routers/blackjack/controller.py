"""Deze class bevat de logica om the bepalen of iets blackjack is."""
import random

#from app.routers.blackjack.api_model import Card


class BlackJackController:
    """BlackJack controller.
    Provides the linking layer between the view (REST API interface) and blackjack job.
    """

    def show_deck(self): #pylint: disable=R0201
        """Show what cards are in a deck"""
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
        return deck

    def draw_hand(self): #pylint: disable=R0201
        """Draw a hand of 2 random cards. Why is this not correct!?"""
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
        random.shuffle(deck)
        card = deck.pop()
        card2 = deck.pop()
        return [card, card2]

    def check_blackjack(self, card1, card2): #pylint: disable=R0201
        """Return the blackjack score after a small pause"""
        return card1.get_value() + card2.get_value()
