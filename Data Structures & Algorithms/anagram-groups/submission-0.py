class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic_t = {}
        for i in strs:
            if tuple(sorted(i)) in dic_t:
                dic_t[tuple(sorted(i))].append(i)
            else:
                dic_t[tuple(sorted(i))] = [i]
        return list(dic_t.values())