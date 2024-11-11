# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# https://leetcode.com/problems/valid-anagram/description/

from collections import Counter


def isAnagram(s, t):
    return Counter(s) == Counter(t)


s = "car"
t = "rat"

print(isAnagram(s, t))
