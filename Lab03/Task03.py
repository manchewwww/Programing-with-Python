# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

# https://leetcode.com/problems/majority-element/description/

from collections import Counter
import math


def majorityElement(nums):
    count_nums = Counter(nums)
    majority_element = [
        num for num, value in count_nums.items() if value > (len(nums) // 2)
    ][0]
    return majority_element


print(majorityElement([3, 2, 3]))
