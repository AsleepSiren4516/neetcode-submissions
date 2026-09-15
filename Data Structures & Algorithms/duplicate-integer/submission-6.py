class Solution:
    def hasDuplicate (self, nums:list[int]) -> bool:
        n = set(nums)
        if len(nums) != len(n):
            return True
        return False

