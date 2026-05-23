class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        if not numSet:
            return 0
        longest = 1
        for num in numSet:
            if num - 1 not in numSet:
                length = 1
                while num + 1 in numSet:
                    length += 1
                    longest = max(longest, length)
                    num += 1
        return longest