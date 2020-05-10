from typing import List

# ===== Problem Statement =====
# Write a function to find the longest common prefix string
# amongst an array of strings.
# If there is no common prefix, return an empty string "".

# TODO: Consider playing around with this solution a bit more


class Solution:

    # Helper method
    def _get_prefixes(self, s):
        result = set()
        for i in range(1, len(s)+1):
            result.add(s[:i])

        return result


    # Runtime: 44 ms, faster than 12.33%
    # Memory Usage: 15.4 MB, less than 6.67%
    def approach1(self, strs: List[str]) -> str:
        # Time Complexity: O(n*len(longest_str))?
        # Space Complexity: O(n*len(prefix_sets))?
        if strs:
            # This is an example of a great time to use list
            # comprehensions since you would need to make a
            # for loop to iterate through all elements of
            # strs to get the prefixes no matter what.
            prefixes = [self._get_prefixes(s) for s in strs]
            result = set.intersection(*prefixes)
            if result:
                return max(result, key=len)
        return ""


    longestCommonPrefix = approach1



if __name__ == "__main__":
    sol = Solution()
    strs = ["flower","flow","flight"]
    #strs = ["dog","racecar","car"]
    #strs = []
    print(sol.longestCommonPrefix(strs))
