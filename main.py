from Classes.Deck import Deck
from Classes.Players import Players
from Functions import display_rules
import random

flag = True
print("Welcome to polish version of Blackjack game")
c = input("\nDo you want to check the rules?")
display_rules() if c[0].upper() == "Y" else None

while flag: #Start of each game / idle loop
    deck = Deck() #create and shuffle deck
    deck.shuffle()

    n_players_human = int(input("\nEnter number of human players"))
    n_players_si = int(input("\nEnter numbers of SI players"))
    players = Players(n_players_human, n_players_si)
    n_players = n_players_si + n_players_human

    n_start = random.randint(0, n_players) #n_start is index of player not its number (number of player equal index+1)
    players.toss_cards(deck, n = 1) #Give each player n cards, default  1
    print(f"\nPlayer number {n_start+1} start")

    while not players.pass_check() and n_players != 1: #Round loop with players decieding
        if n_start >= n_players:
            n_start = 0

        player = players.chose_player(n_start)
        print(f"\nPlayer {player.player_index} is making a decision")

        player.make_a_move(deck)
        player_score = player.get_value()

        if player_score == 21:
            break
        elif player_score > 21:
            n_players -= 1
            players.remove_player(player)
            print(f"\nPlayer {player.player_index} loose by exceeding the point threshold")
        else:
            n_start += 1

    players.check_score()
    cont = input("\nDo You want to play another round?")[0].upper()
    flag = True if cont == "Y" else False
    