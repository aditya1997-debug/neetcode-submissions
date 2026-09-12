class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        max_count = 0
        for x in num_set:
            if x - 1 not in num_set:
                curr = x
                count = 1
                while curr + 1 in num_set:
                    curr += 1
                    count += 1
                if count > max_count:
                    max_count = count
        return max_count