class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        count = 0
        seen = set()
        left = 0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left += 1
                count -= 1
            seen.add(s[i])
            count += 1
            res = max(res, count)
        return res 