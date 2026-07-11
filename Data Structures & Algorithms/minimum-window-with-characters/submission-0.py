class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        res = [-1, -1]
        length = float("infinity")
        left = 0
        count = {}
        freq = {}
        for i in t:
            count[i] = count.get(i,0) + 1
        need = len(count)
        have = 0
        
        for right in range(len(s)):
            freq[s[right]] = 1 + freq.get(s[right], 0)
            if s[right] in count and freq[s[right]] == count[s[right]]:
                have += 1
            while have == need:
                if (right - left + 1) < length:
                    res = [left, right]
                    length = (right - left + 1)
                freq[s[left]] -= 1
                if s[left] in count and freq[s[left]] < count[s[left]]:
                    have -= 1
                left += 1
        left, right = res
        return s[left:right+1] if length != float("infinity") else ""      