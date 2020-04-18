from typing import List

# ===== Problem Statement =====
# Given two arrays of integers nums and index. Your
# task is to create target array under the following rules:
#
#  . Initially target array is empty.
#  . From left to right read nums[i] and index[i], inser
#    at index index[i] the value nums[i] in target array.
#  . Repeat the previous step until there are no elements
#    to read in nums and index.
#
# Return the target array.
#
# It is guaranteed that the insertion operations will be valid.



class Solution:

    # Runtime: 32 ms
    # Memory Usage: 13.8 MB
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        for idx, num in zip(index, nums):
            res.insert(idx, num)

        return res



if __name__ == "__main__":
    sol = Solution()
    nums, index = [0,1,2,3,4], [0,1,2,2,1]
    #nums, index = [1,2,3,4,0], [0,1,2,3,0]
    #nums, index = [1], [0]

    result = sol.createTargetArray(nums, index)
    print(result)
