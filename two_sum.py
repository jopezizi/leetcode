class Solution:
    def twoSum(self, nums: list[int], target: int):
        seen = {}
        for i, num in enumerate(nums):
            if target - num not in seen:
                seen[num] = i
            else:
                return [seen[target-num], i]

b = Solution()
print(b.twoSum([3,3],6))