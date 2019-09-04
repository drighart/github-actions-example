import unittest

from app.routers.blackjack.controller import BlackJackController


class BlackjactTestSuite(unittest.TestCase):

    def test_show_deck(self):
        retrieved_deck = BlackJackController().show_deck()

        expected_result = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
        self.assertEqual(expected_result, retrieved_deck)

    def test_when_draw_hand_then_two_cards_returned(self):
        cards_drawn = BlackJackController().draw_hand()

        self.assertTrue(len(cards_drawn) == 2)

    def test_when_draw_hand_then_different_cards_returned_each_time(self):
        cards_drawn_first = BlackJackController().draw_hand()
        cards_drawn_second = BlackJackController().draw_hand()
        cards_drawn_third = BlackJackController().draw_hand()

        self.assertNotEqual(cards_drawn_first[0], cards_drawn_first[1])
        self.assertNotEqual(cards_drawn_second[0], cards_drawn_second[1])
        self.assertNotEqual(cards_drawn_third[0], cards_drawn_third[1])

    def test_save_the_world(self):
        print("Hello World!")
