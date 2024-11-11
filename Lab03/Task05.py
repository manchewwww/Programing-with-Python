# You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians).
# The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

# A row i is weaker than a row j if one of the following is true:

# The number of soldiers in row i is less than the number of soldiers in row j.
# Both rows have the same number of soldiers and i < j.
# Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/description/


def kWeakestRows(mat, k):
    """
    :type mat: List[List[int]]
    :type k: int
    :rtype: List[int]
    """
    strenghts = [(row.count(1), i) for i, row in enumerate(mat)]
    strenghts.sort()
    return [i for _, i in strenghts[:k]]

print(
    kWeakestRows(
        [
            [1, 1, 0, 0, 0],
            [1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [1, 1, 1, 1, 1],
        ],3
    )
)
