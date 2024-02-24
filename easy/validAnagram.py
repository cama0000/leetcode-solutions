class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # METHOD 1: Sorting
        # s = sorted(s)
        # t = sorted(t)

        # if s == t:
        #     return True
        # else:
        #     return False

        # METHOD 2: Hash Map
        d = defaultdict(int)

        for c in s:
            d[c] += 1
        
        for c in t:
            d[c] -= 1
        
        for v in d.values():
            if v != 0:
                return False
            
        return True