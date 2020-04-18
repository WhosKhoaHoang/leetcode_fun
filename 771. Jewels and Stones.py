from collections import Counter



class Solution:

    # Runtime: 24 ms
    # Memory Usage: 13.8 MB
    def numJewelsInStones(self, J: str, S: str) -> int:
        # J: The target stones
        # S: Stones you have an inventory

        # THINK: Get the count of each stone
        #        contained in J
        # - Make a counter dict of S
        # - Iterate through J
        # - Use the elements of J as keys
        #   to access the counter dict for
        #   the count values
        counts = Counter(S)
        result = 0
        for jewel in J:
            result += counts[jewel]

        return result


    # NOTE: Although there are fewer lines of code in this method,
    #       it takes longer to execute than numJewelsInStones(). Interesting...
    # - Storing Counter(S) in a separate variable shaved several
    #   ms from the runtime.
    # Runtime: 40 ms
    # Memory Usage: 13.6 MB
    def numJewelsInStonesOneLine(self, J: str, S: str) -> int:
        return sum([Counter(S)[jewel] for jewel in J if jewel in Counter(S)])


if __name__ == "__main__":
    sol = Solution()
    J = "aA"
    S = "aAAbbbb"
    # Output: 3

    #result = sol.numJewelsInStones(J, S)
    result = sol.numJewelsInStonesOneLine(J, S)
    print(result)
