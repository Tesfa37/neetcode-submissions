class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        for word in strs:
            if tuple(sorted(word)) in words:
                words[tuple(sorted(word))].append(word)
            else:
                words[tuple(sorted(word))] = [word]
        return list(words.values()) if words else [""]