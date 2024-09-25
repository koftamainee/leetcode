"""
time complexity: O(n);
space complexity: O(n);
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            add = target - nums[i]
            if (add in hashmap):
                return [hashmap[add], i]
            hashmap[nums[i]]= i