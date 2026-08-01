class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for i in strs:
            word = ''.join(sorted(i))
            result[word].append(i)
        return list(result.values())
