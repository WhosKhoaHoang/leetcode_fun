from typing import List

# ===== Problem Statement =====
# Given the array candies and the integer extraCandies, where candies[i]
# represents the number of candies that the ith kid has. For each kid check
# if there is a way to distribute extraCandies among the kids such that he
# or she can have the greatest number of candies among them. Notice that
# multiple kids can have the greatest number of candies.

class Solution:

    # Runtime: 24 ms
    # Memory: 14 MB
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [c+extraCandies >= max(candies) for c in candies]



if __name__ == "__main__":
    sol = Solution()
    candies = [2,3,5,1,3]
    extraCandies = 3
    print(sol.kidsWithCandies(candies, extraCandies))
