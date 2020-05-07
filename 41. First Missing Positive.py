from typing import List

# ===== Problem Statement =====
# Given an unsorted integer array, find the smallest missing positive integer.

class Solution:

    # Nah, this is quite ineffective:
    def attempt1(self, nums: List[int]) -> int:
        # This seems legit:
        if all(e < 0 for e in nums):
            return 1

        small = min(nums)
        big = max(nums)
        non_occur = [e for e in range(small, big+1)
                     if e not in nums and e != 0]

        if non_occur:
            return min(non_occur)
        else:
            return max(nums)+1


    # Correctness seems OK, but performance is not
    # (results in a MemoryError due to construction of roi)
    def attempt2(self, nums: List[int]) -> int:
        # not nums to handle empty list
        if all(e <= 0 for e in nums) or not nums:
            return 1

        # Note how the singleton list case is
        # handled for each of the following blocks
        if all(e >= 0 for e in nums):
            # Only positive and 0
            small, big = min(nums), max(nums)
            roi = list(range(small, big+1))
            if 1 not in roi:
                return 1
            non_occur = [e for e in roi if e not in nums]
            if non_occur:
                return min(non_occur)
            return big+1
        else:
            # There's a mix of pos and neg. Get rid of negatives.
            pos = [e for e in nums if e > 0]  # Don't care about 0
            small, big = min(pos), max(pos)
            roi = list(range(small, big+1))
            if 1 not in roi:
                return 1
            non_occur = [e for e in roi if e not in pos]
            if non_occur:
                return min(non_occur)
            return big+1


    # NOTE: attempt3 is attempt but refactored
    # Correctness seems OK, but performance is not
    # (results in a MemoryError due to construction of roi)
    def attempt3(self, nums: List[int]) -> int:
        # not nums to handle empty list
        if all(e <= 0 for e in nums) or not nums:
            return 1

        if not all(e >= 0 for e in nums):
            # There's a mix of pos and neg. Get rid of negatives.
            nums = [e for e in nums if e > 0]  # Don't care about 0

        small, big = min(nums), max(nums)
        roi = list(range(small, big+1))
        if 1 not in roi:
            return 1
        non_occur = [e for e in roi if e not in nums]
        if non_occur:
            return min(non_occur)
        return big+1


    # NOTE: It's still possible to get MemoryErrors on
    #       values even larger than, say, 2147483647
    # Runtime: 28 ms
    # Memory: 13.8 MB
    def attempt4(self, nums: List[int]) -> int:
        # How MemoryError was avoided:
        #  Loop through (min, max) from a range instead
        #  of building a big ol' list from it!!
        if nums:
            if all(e <= 0 for e in nums):
                return 1

            small = min([e for e in nums if e > 0])
            big = max(nums)

            # Check left side of roi
            for e in range(1, small):
                return e

            # Check inside roi
            for e in range(small+1, big):
                if e not in nums:
                    return e

            # Check right side of roi
            for e in range(big+1, big+2):
                return e
        return 1

    #firstMissingPositive = attempt1
    #firstMissingPositive = attempt2
    #firstMissingPositive = attempt3
    firstMissingPositive = attempt4



if __name__ == "__main__":
    # Good general strategy:
    # - Come up with good test inputs

    sol = Solution()

    lst = [1,2,0]  # Expected: 3
    assert sol.firstMissingPositive(lst) == 3
    lst = [3,4,-1,1]  # Expected: 2
    assert sol.firstMissingPositive(lst) == 2
    lst = [7,8,9,11,12]  # Expected: 1
    assert sol.firstMissingPositive(lst) == 1
    lst = [2]  # Expected: 1
    assert sol.firstMissingPositive(lst) == 1
    lst = [-999999, 1]  # Expected: 2
    assert sol.firstMissingPositive(lst) == 2
    lst = [1000,-1]  # Expected: 1
    assert sol.firstMissingPositive(lst) == 1
    lst = [1,2,3,10,2147483647,9]
    assert sol.firstMissingPositive(lst) == 4
