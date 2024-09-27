"""
time complexity: O(nlogn);
space complexity: O(n);
"""

import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 == str2 + str1:
            str_len = math.gcd(len(str1), len(str2))
            return (str2[:str_len])
        return ""