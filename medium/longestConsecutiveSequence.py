class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for n in nums:
            # if n is start of sequence
            if (n - 1) not in s:
                length = 0

                # keep checking incrememnts while updating length of this subsequence
                while (n + length) in s:
                    length += 1
                longest = max(longest, length)
        
        return longest