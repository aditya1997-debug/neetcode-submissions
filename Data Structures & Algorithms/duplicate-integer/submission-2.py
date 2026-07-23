class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = set(nums)
        print(result)
        if len(result) < len(nums):
            return True
        return False