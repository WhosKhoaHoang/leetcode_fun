from typing import List

# ===== Problem Statement =====
# There are n soldiers standing in a line. Each
# soldier is assigned a unique rating value.

# You have to form a team of 3 soldiers amongst them under the following rules:
#  * Choose 3 soldiers with index (i, j, k) with
#      rating (rating[i], rating[j], rating[k]).
#  * A team is valid if:
#    (rating[i] < rating[j] < rating[k]) or
#    (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).

# Return the number of teams you can form given the conditions.
# (soldiers can be part of multiple teams).

# TODO: Consider playing around with this solution a bit more


class Solution:

    # Basically, the indices i,j,k must be *ALWAYS BE* in
    # ascending order while the values AT the indices
    # can be in ASCENDING order *OR* DESCENDING order

    # Consider both ascending and descending case?

    # Consider a sliding window of length 3?

    # Goal is to pick 3 and ONLY 3 soldiers...


    # ===== Helper methods =====
    def _triple_loop(self, lst):
        result = 0
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                for k in range(j+1, len(lst)):
                    if lst[i][0] < lst[j][0] < lst[k][0]:
                        result += 1
        return result


    # Brute force approach
    # Runtime: 1820 ms, faster than 20.57%
    # Memory Usage: 13.6 MB, less than 100.00%
    def approach1(self, rating: List[int]) -> int:
        result = 0
        if rating:
            enum = list(enumerate(rating))
            # CAUTION:
            # - You're not only looking at neighbors...
            #   you need to at EACH element with res-
            #   pect to the current one! I.e., every
            #   every possible combination...

            # Acscedning case
            enum.sort(key = lambda x: x[1])
            result += self._triple_loop(enum)

            # Descending case
            enum.sort(key = lambda x: -x[1])
            result += self._triple_loop(enum)

        return result


    numTeams = approach1



if __name__ == "__main__":
    rating = [2,5,3,4,1]  # Expected: (2,3,4), (5,4,1), (5,3,1)
    #rating = [2,1,3]  # Expected: Can't form any teams
    sol = Solution()
    print(sol.numTeams(rating))

    # THINK:
    # . What are the edge cases (empty list...)
    # . Sort list, will that help?
    # . Use enumerate to get original indices
