'''
## Problem
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.

'''

# submit
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> tuple[int, int]:
            # left, right を中心として、回文である限り左右に広げる
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            # whileを抜けた時点では1つ外側に出ているので戻す
            return left + 1, right

        start = 0
        end = 1

        for i in range(len(s)):
            # 奇数長の回文
            l1, r1 = expand(i, i)

            # 偶数長の回文
            l2, r2 = expand(i, i + 1)

            # 最長なら更新
            if r1 - l1 > end - start:
                start, end = l1, r1

            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end]

'''
Link: https://leetcode.com/problems/longest-palindromic-substring/submissions/2047416497
## 中央から始めるという発想はよかった。
発想はよかったが、そこからの処理の実装に時間がかかってしまった。
'''