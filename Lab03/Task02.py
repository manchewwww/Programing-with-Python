# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of
#  American keyboard like the image below.

# In the American keyboard:
# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".

# https://leetcode.com/problems/keyboard-row/description/


def findWords(words):
    american_keyboard_rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
    finded_words = [
        word
        for word in words
        if set(word.lower()).issubset(american_keyboard_rows[0])
        or set(word.lower()).issubset(american_keyboard_rows[1])
        or set(word.lower()).issubset(american_keyboard_rows[2])
    ]  # if any(set(word.lower()).issubset(row) for row in american_keyboard_rows)]
    return finded_words


print(findWords(["Hello", "Alaska", "Dad", "Peace"]))
