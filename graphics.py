import os

from players import Player


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class Graphics:
    def __init__(self, players: list[Player]):
        clear()
        self.moves = ["" for i in range(9)]
        self.players = players
        self.turn = 0
        self.draw_axes()
        self.draw_score(self.players)

    def draw_axes(self):
        i = 0
        for row in range(3):
            for column in range(3):
                mark = "   "
                if self.moves[i]:
                    mark = f" {self.moves[i]} "
                if column == 2:
                    print(f"{mark}", end="\n")
                else:
                    print(f"{mark}|", end="")
                i += 1
            if row != 2:
                print("---|---|---")

    def draw_score(self, players: list):
        print(
            f"""+----------------------------\nScore: {self.players[0].name} {self.players[0].score}  {self.players[1].name} {self.players[1].score}\n+----------------------------""")

    def _change_turn(self):
        if not self.turn:
            self.turn = 1
        else:
            self.turn = 0

    def update_move(self, place):
        clear()
        try:
            place = int(place)
            current_place = self.moves[place]
        except IndexError:
            print("You chose a place that doesnt exist choose again")
        except ValueError:
            print("That's not a number try again")
        else:
            if not current_place:
                self.moves[place] = f"{self.players[self.turn].mark}"
                self._change_turn()
            else:
                print("You can't choose this place, choose again")

    def get_turn(self) -> Player:
        return self.players[self.turn]
