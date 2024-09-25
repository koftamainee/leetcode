"""
time complexity: O(n);
space complexity: O(n);
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1, p2 = len(word1), len(word2)
        new_word = ""

        for i in range(min(p1, p2)):
            new_word += word1[i]
            new_word += word2[i]
        
        if p1 > p2:
            new_word += word1[p2:]
        else:
            new_word += word2[p1:]
        return new_word