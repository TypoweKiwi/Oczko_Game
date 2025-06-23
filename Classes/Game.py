from Classes.Deck import Deck
from Classes.Players import Players
from Functions.display_rules import display_rules
import random
from enum import Enum

class GameState(Enum):
    INIT = 1
    RUNNING = 2
    END = 3


class Game:
    def __init__(self):
        self.state = GameState.INIT 
        self.deck = None
        self.players = None
        self.n_players = None
        self.present_player_index = None

        print("Welcome to polish version of Blackjack game")
        decision = input("\nDo you want to check the rules?")
        display_rules() if decision[0].upper() == "Y" else None

    def create_new_game(self):
        self.state = GameState.RUNNING
        self.deck = Deck()
        self.deck.shuffle()
        
        n_players_human = int(input("\nEnter number of human players"))
        n_players_si = int(input("\nEnter numbers of SI players"))
        self.n_players = n_players_human + n_players_si
        self.present_player_index = random.randint(0, self.n_players-1)
        print(f"\nGame starts from player {self.present_player_index+1}")

        self.players = Players(n_players_human, n_players_si)
        self.players.toss_cards(self.deck)

    def player_turn(self):
        if self.present_player_index >= self.n_players:
            self.present_player_index = 0

        player = self.players.chose_player(self.present_player_index)
        print(f"\nPlayer {player.player_index} is making a decision")
        player.make_a_move(self.deck)
    
    def check_player_score(self):
        player = self.players.chose_player(self.present_player_index)
        player_score = player.get_value()
        if player_score == 21:
            self.state = GameState.INIT
        elif player_score > 21:
            self.n_players -= 1
            self.players.remove_player(player)
            print(f"\nPlayer {player.player_index} loose by exceeding the point threshold")
        else:
            self.present_player_index += 1


    def check_players_status(self):
        if self.players.pass_check():
            self.state = GameState.INIT

    def score_board(self):
        self.players.check_score()

        decision = input("Do you wish to continue game?")
        if decision[0].upper() != "Y":
            self.state = GameState.END