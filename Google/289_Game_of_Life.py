"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.

Follow up: 
Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
"""

"""Solution
    1. using two bits to represent current state and next state
    2. after calculation, move the state from current to next
"""

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) is 0 or len(board[0]) is 0:
            return
        self.height = len(board)
        self.width = len(board[0])
        for i in range(self.height):
            for j in range(self.width):
                count = 0
                for x in range(max(i-1,0),min(i+2,self.height)):
                    for y in range(max(j-1,0),min(j+2,self.width)):
                        if x == i and y == j:
                            continue
                        # Error 1: only check the last bit
                        if board[x][y] & 0b01:
                            count += 1
                # Error 1: only check the last bit
                if board[i][j] & 0b01:
                    # Tip: put the next state one bit before the last bit
                    if count < 2 or count > 3:
                        board[i][j] = board[i][j] & 0b01
                    else:
                        board[i][j] = board[i][j] | 0b10
                else:
                    if count == 3:
                        board[i][j] = board[i][j] | 0b10
        for i in range(self.height):
            for j in range(self.width):
                board[i][j] = board[i][j] >> 1












