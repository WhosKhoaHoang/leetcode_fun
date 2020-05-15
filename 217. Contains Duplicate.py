from collections import Counter
from typing import List

# ===== Problem Statement =====
# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in
# the array, and it should return false if every element is distinct.


class Solution:

    # Runtime: 128 ms, faster than 57.17%
    # Memory Usage: 20.8 MB, less than 7.55%
    def approach1(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        for num in counts:
            if counts[num] > 1:
                return True
        return False


    # Runtime: 120 ms, faster than 90.61%
    # Memory Usage: 19.1 MB, less than 16.98%
    def approach2(self, nums: List[int]) -> bool:
        nums.sort()
        if len(nums) > 1:
            for i in range(len(nums)-1):
                if nums[i] == nums[i+1]:
                    return True
        return False


    #containsDuplicate = approach1
    containsDuplicate = approach2



if __name__ == "__main__":
    #nums = [1,2,3,1]
    #nums = [1,2,3,4]
    nums = [1,1,1,3,3,4,3,2,4,2]
    sol = Solution()
    print(sol.containsDuplicate(nums))
