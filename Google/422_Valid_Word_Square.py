"""
Given a sequence of words, check whether it forms a valid word square.

A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

Note:
The number of words given is at least 1 and does not exceed 500.
Word length will be at least 1 and does not exceed 500.
Each word contains only lowercase English alphabet a-z.
Example 1:

Input:
[
  "abcd",
  "bnrt",
  "crmy",
  "dtye"
]

Output:
true

Explanation:
The first row and first column both read "abcd".
The second row and second column both read "bnrt".
The third row and third column both read "crmy".
The fourth row and fourth column both read "dtye".

Therefore, it is a valid word square.
Example 2:

Input:
[
  "abcd",
  "bnrt",
  "crm",
  "dt"
]

Output:
true

Explanation:
The first row and first column both read "abcd".
The second row and second column both read "bnrt".
The third row and third column both read "crm".
The fourth row and fourth column both read "dt".

Therefore, it is a valid word square.
Example 3:

Input:
[
  "ball",
  "area",
  "read",
  "lady"
]

Output:
false

Explanation:
The third row reads "read" while the third column reads "lead".

Therefore, it is NOT a valid word square.
"""


"""Solution
    1. check the words by flip index i and j
    2. check the len and index
    3. remember to check every element
"""

class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        if not words:
            return True
        size = len(words)
        for i in range(size):
            # Error 2: the left boundary should be 0 otherwise the left bottom part would be checked
            for j in range(0, len(words[i])):
                # Error 1: the boundary should be i >= len(words[j])
                if j >= size or i >= len(words[j]) or words[i][j] != words[j][i]:
                    return False
        return True





