from Classes.Card import Card
import random

class Deck:
    colors = "♥♦♣♠"
    symbols = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self):
        self.cards = []

        for i in range(len(Deck.colors)):
            for j in range(len(Deck.symbols)):
                self.cards.append(Card(Deck.colors[i], Deck.symbols[j]))
    
    def get_card(self):
        return self.cards.pop()
    
    def shuffle(self):
        random.shuffle(self.cards)