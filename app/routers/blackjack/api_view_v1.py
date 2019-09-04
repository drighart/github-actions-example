"""Beschrijft v1 van de API."""
from fastapi import APIRouter

from app.routers.blackjack.controller import BlackJackController

app = APIRouter() # pylint: disable=C0103

controller = BlackJackController() # pylint: disable=C0103

@app.post("/")
def check_blackjack(card1, card2): # pylint: disable=E1121
    """
    Check of de twee opgegeven kaarten blackjack geven
    """
    return controller.check_blackjack(card1, card2)

@app.get("/deck")
def show_deck():
    """
    Geef alle kaarten uit een span terug
    """
    return controller.show_deck() # pylint: disable=E1121

@app.get("/draw")
def draw_hand():
    """
    Deel een hand met twee random kaarten uit het span
    """
    return controller.draw_hand() # pylint: disable=E1121
