class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for s in strs:
            s_sorted = "".join(sorted(s))
            if s_sorted in dict:
                dict[s_sorted].append(s)
            else:
                dict[s_sorted] = [s]

        return dict.values()
