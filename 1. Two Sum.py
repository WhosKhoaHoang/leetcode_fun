from typing import List

# ===== Problem Statement =====
# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.


class Solution:

    # . To solve this problem, consider the notion of some number's (call
    #   it nums[i]) complement for some other target number. The complement
    #   is the value that needs to be added to nums[i] to get the target.
    #   E.g., 7's complement for 9 is 2.
    # . To get a number's complement for, say, 9, subtract the number from 9.
    #   E.g., 7's complement for 9 is 2 because 9-7=2 and so 7+2=9.
    # . So the general strategy is to consider the complements for each
    #   element and check if it's in the given nums list. If it is, then we
    #   need to get the complement's index. We can actually use a dict to make
    #   a mapping of complements to corresponding indices rather than iterating
    #   through nums itself with a for i in range loop for geting the index i.
    # . Indices are the target values for the result, so make a dict where
    #   keys are nums' complements and values are the corresponding indices.
    #   If an element's complement for, say, 9 is in the dict's keys, then we
    #   have a result.

    # Brute force method
    # Runtime: 7308 ms, faster than 5.02%
    # Memory Usage: 15 MB, less than 9.53%
    def approach1(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    res = [i, j]
                    break

        return res


    # Using two passes through nums
    # Runtime: 40 ms, faster than 97.97%
    # Memory Usage: 15.8 MB, less than 5.11%
    def approach2(self, nums: List[int], target: int) -> List[int]:
        d = {}
        res = []
        for i in range(len(nums)):
            d[nums[i]] = i

        for i in range(len(nums)):
            complement = target-nums[i]
            if complement in d and d[complement] != i:
                res = [i, d[complement]]
                break

        return res


    # Using one pass through nums
    # Runtime: 36 ms, faster than 99.65%
    # Memory Usage: 15.4 MB, less than 5.11%
    def approach3(self, nums: List[int], target: int) -> List[int]:
        d = {}
        res = []

        # Difference between this approach and approach2:
        # - A complement for target can come from two different
        #   values. E.g., for x+y=target, the following complements
        #   (x and y) can exist: x=target-y & y=target-x
        # - The first time we get x=target-y, it may not exist. After
        #   checking for its existence in d, we put y in d. We then
        #   move on with our iteration and may eventually come across
        #   y=target-x. Since we had previous put y in d, we get a match
        #   and set our result.
        # - All of that^ in the second bullet point contrasts with what
        #   happens in approach 2 where we build all of d beforehand rather
        #   than on the fly. Therefore, the first time we come across x,
        #   we get a hit and set our result.

        for i in range(len(nums)):
            complement = target-nums[i]
            if complement in d and d[complement] != i:
                res = [i, d[complement]]
                break
            d[nums[i]] = i

        return res


    #twoSum = approach1
    #twoSum = approach2
    twoSum = approach3



if __name__ == "__main__":
    sol = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(sol.twoSum(nums, target))
