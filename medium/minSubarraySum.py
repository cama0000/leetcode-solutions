class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # FIRST ATTEMPT
        # l = 0
        # r = 1
        # shortest = len(nums) + 1
        # found = False

        # sum = 0

        # while r <= len(nums):
        #     sum = 0
        #     for i in range(l, r):
        #         sum += nums[i]
            
        #     if sum == target:
        #         found = True
        #         shortest = min(r - l, shortest)
        #         r += 1
        #     elif sum < target:
        #         r += 1
        #     else:
        #         shortest = min(r - l, shortest)
        #         l += 1

        # if not found and shortest == len(nums) + 1:
        #     return 0
        
        # return shortest

        # O(n)
        l = 0
        shortest = len(nums) + 1
        sum = 0

        for r in range(len(nums)):
            sum += nums[r]
            while sum >= target:
                shortest = min(shortest, r - l + 1)
                sum -= nums[l]
                l += 1
        return 0 if shortest == len(nums) + 1 else shortest