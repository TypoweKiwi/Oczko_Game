from Classes.Deck import Deck
from Classes.Card import Card
from Functions.hand_to_data_dict import hand_to_data_dict
import joblib
import pandas as pd

class Player: 
    def __init__(self, player_number: int):
        self.cards = []
        self.present_value = 0
        self.player_index = player_number
        self.pass_flag = False 

    def add_card(self, card: "Card"):
        self.cards.append(card)
        self.present_value += card.get_value()
        self.pass_flag = False

    def get_cards(self):
        return self.cards
    
    def get_value(self):
        return self.present_value
    
    def passes(self):
        self.pass_flag = True
    
    def is_human(self):
        return self.human
    
    def make_a_move(self, deck: "Deck"):
        raise Exception("Base class use")

class Player_human(Player):
    def make_a_move(self, deck: "Deck"):
        print(f"Your hand: {self.get_cards()}")
        print(f"Your hand value {self.get_value()}")

        decision = input("Do you want to draw another card?")[0].upper()
        if decision == "Y":
            card = deck.get_card()
            self.add_card(card)
            print(f"You draw {card}")
        else:
            self.passes()
            print("You decided to pass")
        
class Player_SI(Player):
    model = joblib.load("model.pkl")
    def make_a_move(self, deck: "Deck"):
        hand_df = pd.DataFrame([hand_to_data_dict(self.get_cards())])
        pred = (Player_SI.model.predict(hand_df) >= 0.5)
        if pred == True:
            card = deck.get_card()
            self.add_card(card)
            print(f"Player {self.player_index} decided to draw card")
        else:
            self.passes()
            print(f"Player {self.player_index} decided to pass")