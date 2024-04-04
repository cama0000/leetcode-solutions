class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # BRUTE FORCE SOLUTION
        # ans = []

        # for i in range(len(nums)):
        #     val = 1
        #     for j in range(len(nums)):
        #         if j != i:
        #             val *= nums[j]
        #     ans.append(val)
        
        # return ans

        # PREFIX AND POSTFIX SOLUTION O(n)
        res = [1] * (len(nums))

        pre = 1
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post
            post *= nums[i]
        return res