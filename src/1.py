class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_map = {}
        n = len(nums)
        for i in range(n):
            add = target - nums[i]
            if add in nums_map:
                return [nums_map[add], i]
            nums_map[nums[i]] = i
            
        return []

main = Solution()

print(main.twoSum([3, 2, 4], 6))