class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {} # {string, liststring}
        res = []

        for word in strs:
            srt = ''.join(sorted(word))

            if srt not in d:
                d[srt] = []

            d[srt].append(word)

        return d.values()
        
        # for key in d:
        #     res.append(d[key])

        # return res