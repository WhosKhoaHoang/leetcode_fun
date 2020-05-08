from collections import Counter
from typing import List

# ===== Problem Statement =====
# Given an array of integers arr, write a function that returns
# true if and only if the number of occurrences of each value
# in the array is unique.

class Solution:

    # Runtime: 32 ms
    # Memory: 14 MB
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len(Counter(arr).values()) == len(set(Counter(arr).values()))



if __name__ == "__main__":
    lst = [1,2,2,1,1,3]
    sol = Solution()
    print(sol.uniqueOccurrences(lst))
