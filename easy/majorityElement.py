import math

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}

        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
        

        for k, v in d.items():
            if v > math.floor(len(nums) / 2):
                return k
        