import math
from typing import List

# ===== Problem Statement =====
# Given an array nums of integers,
# return how many of them contain an even number of digits.

# THINK:
# We can use math.log10 to determine the
# length of an integer. Idea is that 10^n
# will be 0.something if n is 1 digit,
# 1.something if n is 2 digits, etc. In
# general, math.log10 evaluates to
# [digit_len-1].something for some digit_len.
# Therefore, to convert [digit_len-1].something
# to digit_len, we'd need to add 1 to it and
# cast it to int.



class Solution:

    # Runtime: 52 ms
    # Memory: 14.1 MB
    def findNumbers(self, nums: List[int]) -> int:
        # Problem verified that nums is
        # a list of integers only
        result = 0
        for e in nums:
            if int(math.log10(e)+1) % 2 == 0:
                result += 1

        return result


if __name__ == "__main__":
    sol = Solution()
    nums = [12,345,2,6,7896]

    result = sol.findNumbers(nums)
    print(result)
