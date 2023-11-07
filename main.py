import os

from graphics import Graphics
from players import Player
from brain import Brain

print("Hello to tic tac toe game")
brain = Brain()
player1 = Player("O", name=input("Give name for player 1 > "))
player2 = Player("X", name=input("Give name for player 2 > "))
initial_order = [player1, player2]
turn = None
while True:
    graphics = Graphics(initial_order)
    for i in range(9):
        turn = graphics.get_turn()
        choice = input(f"{turn.name} set the place > ")
        graphics.update_move(choice)
        brain.update_moves(graphics.moves)
        graphics.draw_axes()

        if brain.game_over():
            print(f"{turn.name} won")
            turn.score += 1
            graphics.draw_score(initial_order)
            break

    # check if player want to continue
    if input("Continue? Y/N") == "N":
        break
    # change order for the next game
    initial_order[0], initial_order[1] = initial_order[1], initial_order[0]
print("Have a nice day")
