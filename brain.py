class Brain:

    def __init__(self):
        self.moves = []

    def update_moves(self, moves):
        self.moves = moves

    def game_over(self):

        check_compinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for comp in check_compinations:
            first_mark = self.moves[comp[0]]
            if first_mark != "":
                checked = 0
                for place in comp[1:]:
                    if self.moves[place] != first_mark:
                        break
                    checked += 1
                if checked == 2:
                    # won
                    return True
        return False
