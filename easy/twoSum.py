class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # METHOD 1: BRUTE FORCE O(n^2)
        # ans = []

        # for i in range(len(nums)):
        #     for j in range(1, len(nums)):
        #         if (nums[i] + nums[j] == target) and i != j:
        #             ans.append(i)
        #             ans.append(j)
        #             return ans
        # return ans

        # METHOD 2: Single Pass Hash Map

        # have the map to remember which index it was at
        m = {}

        for i in range(len(nums)):
            comp = target - nums[i]

            if comp in m:
                return [m[comp], i]
            
            m[nums[i]] = i