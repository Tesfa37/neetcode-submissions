class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """ Given two strings s1 and s2, return true if a permutation of s1 exists 
        as a substring """
        freq = {}
        freq2 = {}
        for i in s1:
            freq[i] = 1 + freq.get(i, 0)
        left = 0
        length = len(s1)
        for r in range(len(s2)):
            freq2[s2[r]] = 1 + freq2.get(s2[r],0)
            if (r - left + 1) > length:
                freq2[s2[left]] -= 1
                if freq2[s2[left]] == 0:
                    del freq2[s2[left]]
                left += 1
            if freq == freq2:
                return True
        return False