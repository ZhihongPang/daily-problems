"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

A knight's tour is a sequence of moves by a knight on a chessboard such that all squares are visited once.

Given N, write a function to return the number of knight's tours on an N by N chessboard.
"""
# research for the problem
# notes: knights tour moves in a sequence on the chess board, hitting every tile on the board
#        if the knight ends one move from the initial move, then it's closed, else it's open
# rules: Schwenk proved that for any m x n board where m <= n, a closed knight's tour is possible unless
#        1. m and n are both odd
#        2. m = 1, 2, or 4
#        3. m = 3, and n = 4, 6, or 8
# tours: N = 1 : 1
#        N = 2, 3, or 4 : 0
#        N = 5 : 1,728
#        N = 6 : 6,637,920
#        N = 7 : 165,575,218,320
#        N = 8 : 19,591,828,170,979,904

import unittest

# problem was pretty hard
# not my solution, credit to https://www.dailycodingproblem.com/blog/knights-tour/
def safe_move(board, move, n):
    x, y = move
    return 0 <= x < n and 0 <= y < n and board[x][y] is None

def valid_moves(board, x, y, n):
    moves = [(2, 1), (2, -1), (1, 2), (1, -2), (-2, 1), (-2, -1), (-1, 2), (-1, -2)]
    all_moves = [(x + x_moves, y + y_moves) for x_moves, y_moves in moves]
    return [move for move in all_moves if safe_move(board, move, n)]

def solveKT(n):
    count = 0
    for i in range(n):
        for j in range(n):
            board = [[None for _ in range(n)] for _ in range(n)]
            board[i][j] = 0
            count += helperKT(board, [(i, j)], n)
    return count

def helperKT(board, tour, n):
    if len(tour) == n * n:
        return 1
    else:
        count = 0
        last_x, last_y = tour[-1]
        for x, y in valid_moves(board, last_x, last_y, n):
            tour.append((x, y))
            board[x][y] = len(tour)
            count += helperKT(board, tour, n)
            tour.pop()
            board[x][y] = None
        return count
    
class Test(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(solveKT(1), 1)
    def test_one(self):
        self.assertEqual(solveKT(2), 0)
    def test_two(self):
        self.assertEqual(solveKT(3), 0)
    def test_three(self):
        self.assertEqual(solveKT(4), 0)
    def test_four(self):
        self.assertEqual(solveKT(5), 1728)
    # not testing above N=5 since it would take too long

if __name__ == "__main__":
    unittest.main()