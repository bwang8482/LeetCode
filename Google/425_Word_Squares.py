"""
Given a set of words (without duplicates), find all word squares you can build from them.

A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.

b a l l
a r e a
l e a d
l a d y
Note:
There are at least 1 and at most 1000 words.
All words will have the exact same length.
Word length is at least 1 and at most 5.
Each word contains only lowercase English alphabet a-z.
Example 1:

Input:
["area","lead","wall","lady","ball"]

Output:
[
  [ "wall",
    "area",
    "lead",
    "lady"
  ],
  [ "ball",
    "area",
    "lead",
    "lady"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
Example 2:

Input:
["abat","baba","atan","atal"]

Output:
[
  [ "baba",
    "abat",
    "baba",
    "atan"
  ],
  [ "baba",
    "abat",
    "baba",
    "atal"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
"""


"""Solution:
    1. using trie or dictionary to store prefix
    2. for each line only try the word with particular prefix
"""


class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        length = len(words[0])
        # Tip: using defaultdict to set default value type as list
        diction = collections.defaultdict(list)
        for word in words:
            for i in range(length):
                # Error 1: append the word not =
                diction[word[:i]].append(word)
        def construct(square):
            if len(square) == length:
                ans.append(square)
                return
            # Tip: using zip(*square) to transpose the list
            for word in diction[''.join([list(x) for x in zip(*square)][len(square)])]:
                # Tip: using square + [word] to copy the element to new list
                construct(square + [word])
        ans = []
        for word in words:
            # Error 2: the type of input should be [word], transform the string to list
            construct([word])
        return ans










