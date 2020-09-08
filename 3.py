class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # print(s)
        isRepeat = True
        currentChar = ''
        startNum = 0

        strList = []

        for i in range(0, len(s)):
            if isRepeat:
                startNum = i
            else:
                strList.append(s[startNum: i - 1])

            if currentChar == s[i]:
                isRepeat = True
            else:
                isRepeat = False

            currentChar = s[i]

        print(strList)

Ans = Solution()
print(Ans.lengthOfLongestSubstring('pwwkew1233sda22ddd'))