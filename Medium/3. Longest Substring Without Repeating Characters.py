# Brute Force
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        maxi = 1

        for i in range(len(s)):
            arr = [0] * 128
            for j in range(i, len(s)):
                char_index = ord(s[j]) - ord('a')

                if arr[char_index] != 1:
                    arr[char_index] = 1
                    maxi = max(maxi, j - i + 1)
                else:
                    break
        return maxi

# Optimized
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        maxi, left, right = 0, 0, 0

        while right < len(s):
            if s[right] in map:
                left = max(left, map[s[right]]+1)
            map[s[right]] = right

            maxi = max(maxi, right-left+1)
            right += 1

        return maxi