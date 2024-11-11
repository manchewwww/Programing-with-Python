# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# https://leetcode.com/problems/valid-anagram/description/


def isAnagram(s, t):
    s_list = list(s)
    s_list.sort()
    t_list = list(t)
    t_list.sort()
    return s_list == t_list


s = "car"
t = "rat"

print(isAnagram(s, t))
