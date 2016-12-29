"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.
"""

"""Solution
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        diction = {}
        for string in strs:
            key = ''.join(sorted(string))
            if key not in diction:
                diction[key] = [string]
            else:
                diction[key].append(string)
        ret = []
        for key in diction.keys():
            ret.append(diction[key])
        return ret
