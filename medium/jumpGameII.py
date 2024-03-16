class Solution:
    def jump(self, nums: List[int]) -> int:
        # will always make it to last index
        # return minimum jumps to do so

        # 1st attempt
        # minJumps = 0
        # curr = 0

        # for i in range(len(nums)):
        #     if curr >= len(nums) - 1:
        #         return minJumps
        #     else:
        #         curr = i + nums[i]
        #         minJumps += 1

        # return minJumps


        # greedy solution

        minJumps = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, nums[i] + i)
            l = r + 1
            r = farthest
            minJumps += 1
        return minJumps