class Solution:
    def maxArea(self, height: List[int]) -> int:
        # BRUTE FORCE METHOD O(n^2)
        # res = 0

        # for l in range(len(height)):
        #     for r in range(l + 1, len(height)):
        #         area = (r - l) * min(height[l], height[r])
        #         res = max(res, area)
        
        # return res

        # O(N) METHOD
        l = 0
        r = len(height) - 1
        largest = 0

        while l <= r:
            area = (r - l) * min(height[l], height[r])

            largest = max(largest, area)

            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return largest