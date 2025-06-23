from Classes.Game import Game, GameState

game = Game()
while game.state == GameState.INIT:
    game.create_new_game()
    while game.state == GameState.RUNNING:
        game.player_turn()
        game.check_player_score()
        game.check_players_status()
    game.score_board()