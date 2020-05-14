from collections import Counter
from typing import List


class Solution:

    # Runtime: 44 ms, faster than 76.34%
    # Memory Usage: 13.9 MB, less than 5.88%
    def approach1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(nums2))


    # Runtime: 48 ms, faster than 51.03%
    # Memory Usage: 14.1 MB, less than 5.88%
    def approach2(nums1, nums2):
        result = []
        for num in nums1:
            if num in nums2 and num not in result:
                result.append(num)

        return result


    #intersection = approach1
    intersection = approach1



if __name__ == "__main__":
    #nums1, nums2 = [1,2,2,1], [2,2]
    nums1, nums2 = [4,9,5], [9,4,9,8,4]
    sol = Solution()
    print(sol.intersection(nums1, nums2))
