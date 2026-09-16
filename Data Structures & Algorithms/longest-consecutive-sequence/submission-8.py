class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(list(set(nums)))
        current_streak = 1
        max_streak = 0

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                current_streak += 1
            else:
                max_streak = max(max_streak, current_streak)
                current_streak = 1
        return max(max_streak, current_streak)