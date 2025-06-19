from Classes.Deck import Deck
from Classes.Player import Player, Player_human, Player_SI

class Players:
    def __init__(self, n_human: int, n_si: int):
        if (n_human + n_si) > 5 or (n_human + n_si) < 1:
            raise ValueError("The number of players is incorrect")
        
        self.players = []
        for i in range(n_human):
            self.players.append(Player_human(i+1))
        
        for i in range(n_si):
            self.players.append(Player_SI(n_human+i+1))

    def toss_cards(self, d: "Deck", n = 1): 
        for i in range(n): 
            for i in range(len(self.players)): 
                self.players[i].add_card(d.get_card())
            
    def chose_player(self, n: int) -> Player: 
        return self.players[n]

    def pass_check(self):
        return all(self.players[i].pass_flag for i in range(len(self.players)))
    
    def remove_player(self, player : "Player"):
        self.players.remove(player)

    def check_score(self):
        score_dict = {self.players[i].player_index: self.players[i].get_value() for i in range(len(self.players))}
        winner = max(score_dict, key=score_dict.get)
        print(f"\nThe winner is player {winner} with score {score_dict[winner]}")