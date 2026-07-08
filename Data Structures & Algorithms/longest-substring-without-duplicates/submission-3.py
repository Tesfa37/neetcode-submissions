class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, count, maximum = 0, 0, 0, 0
        seen = set()
        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
                count -= 1
            seen.add(s[right])
            right += 1
            count += 1
            maximum = max(count, maximum)
        return maximum