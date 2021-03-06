from typing import List
# ^For function annotations

# ===== Problem Statement =====
# We are given a list nums of integers representing a
# list compressed with run-length encoding.
#
# Consider each adjacent pair of elements
# [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).
# For each such pair, there are freq elements with value
# val concatenated in a sublist. Concatenate all the sub-
# lists from left to right to generate the decompressed list.
#
# Return the decompressed list.



class Solution:

    # Runtime: 64 ms
    # Memory: 13.8 MB
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0, len(nums)-1, 2):
            # Apparently, list addition is slightly
            # more efficient than extend(). An INPLACE_ADD
            # apparently less overhead than a method call.
            # - See: https://stackoverflow.com/questions/3653298
            result += nums[i]*[nums[i+1]]

        return result


    # Nahhh, more time would be eaten up from flattening the
    # result of this list comprehension...
    def decompressRLENoLoop(self, nums: List[int]) -> List[int]:
        return [nums[i]*[nums[i+1]] for i in range(0, len(nums)-1, 2)]



if __name__ == "__main__":
    nums = [1,2,3,4]
    sol = Solution()
    #result = sol.decompressRLElist(nums)
    result = sol.decompressRLENoLoop(nums)
    print(result)
