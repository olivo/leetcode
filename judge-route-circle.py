class Solution(object):
    def judgeCircle(self, moves):
        current_move = (0, 0)

        move_map = {"U": [0, 1], "R": [1, 0], "D": [0, -1], "L": [-1, 0]}

        for move in moves:
            move_tuple = move_map[move]

            next_move = (current_move[0] + move_tuple[0], current_move[1] + move_tuple[1])

            current_move = next_move

        return current_move == (0, 0)