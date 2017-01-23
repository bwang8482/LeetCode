"""
Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Example:
Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

TicTacToe toe = new TicTacToe(3);

toe.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

toe.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

toe.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

toe.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

toe.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

toe.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
Follow up:
Could you do better than O(n2) per move() operation?
"""


"""Solution:
    1. using dictionary to track each row and col and two diagonals.
    2. only update the row and col the player move to.
    3. if one row or col or diagonal filled with one value (1 or -1), return the winner
"""

class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.size = n
        self.rows = collections.defaultdict(int)
        self.cols = collections.defaultdict(int)
        self.diagonals = collections.defaultdict(int)
        

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        # player 1: -1, player 2: 1
        weight = -1 + 2*(player-1)
        self.rows[row] += weight
        self.cols[col] += weight
        if row == col:
            self.diagonals['\\'] += weight
        if row == self.size - 1 - col:
            self.diagonals['/'] += weight
        return player if abs(self.rows[row]) == self.size 
                        or abs(self.cols[col]) == self.size 
                        or abs(self.diagonals['\\']) == self.size 
                        or abs(self.diagonals['/']) == self.size else 0

        
"""Summary:
    this solution only use N(1) time to check the status and need at most O(2n^2+2n) space
    this solution can be optimized if we prunning the row or col has move from both players
"""
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)






