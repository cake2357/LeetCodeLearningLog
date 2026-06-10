'''
## Problem Description
Given an integer x, return true if x is a palindrome, and false otherwise.

An integer is a palindrome when it reads the same forward and backward.
For example, 121 is a palindrome while 123 is not.

Difficulty: Easy

Link : https://leetcode.com/problems/palindrome-number/submissions/2028625051
'''

# submit
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        reverse_s = s[::-1]
        result = s==reverse_s
        return result

'''
Runtime 2ms Beats 90.81%
I could have aimed for an even better score if I had optimized the code I submitted.
'''

class Solution:
    def isPalindrome(self, x):
        number = str(x)
        return number == number[::-1]