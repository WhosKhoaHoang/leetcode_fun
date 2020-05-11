from typing import List

# ===== Problem Statement =====
# Given an array containing n distinct numbers
# taken from 0, 1, 2, ..., n, find the one that
# is missing from the array.

class Solution:

    # Runtime: 5772 ms, faster than 5.14%
    # Memory Usage: 14.9 MB, less than 6.45%
    def approach1(self, nums: List[int]) -> int:
        for i in range(len(nums)+1):
            if i not in nums:
                return i


    # Using set difference to get elements in the
    # first set that aren't in the secodn set. Call
    # max() to retrieve the element from the set so
    # that you don't return a set.
    # Runtime: 316 ms, faster than 10.24%
    # Memory Usage: 15.9 MB, less than 6.45%
    def approach2(self, nums: List[int]) -> int:
        return max(set(range(len(nums)+1)) - set(nums))


    #missingNumber = approach1
    missingNumber = approach2


if __name__ == "__main__":
    #nums = [1]
    nums = [3,0,1]
    sol = Solution()
    print(sol.missingNumber(nums))
