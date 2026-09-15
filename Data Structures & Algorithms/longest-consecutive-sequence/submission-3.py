class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Remove duplicates and sort
        nums = sorted(list(set(nums)))

        longest = 1
        current_streak = 1

        # Single loop to compare adjacent elements
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                current_streak += 1
            else:
                # Sequence broken by a gap -> update max and reset streak
                longest = max(longest, current_streak)
                current_streak = 1

        return max(longest, current_streak)