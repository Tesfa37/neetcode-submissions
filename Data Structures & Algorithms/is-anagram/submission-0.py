class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Dict_T, Dict_S = {}, {}
        if len(s) != len(t): 
            return False
        for i in range(len(s)):
            if s[i] not in Dict_S:
                Dict_S[s[i]] = 1
            else:
                Dict_S[s[i]] += 1
            if t[i] not in Dict_T:
                Dict_T[t[i]] = 1
            else:
                Dict_T[t[i]] += 1
        return Dict_T == Dict_S