class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(list(set(nums)))
        curr = 1
        max_ = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                curr += 1
            else:
                max_ = max(curr, max_)
                curr = 1
        return max(curr, max_)