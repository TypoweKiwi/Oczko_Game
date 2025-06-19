class Card:
    values = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":2, "Q":3, "K":4, "A":11}
    def __init__(self, c, s):
        self.color = c
        self.symbol = s

    def get_value(self):
        return Card.values[self.symbol]

    def __str__(self):
        return self.symbol + self.color
    
    def __repr__(self):
        return self.symbol + self.color