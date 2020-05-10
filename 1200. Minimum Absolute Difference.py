from typing import List

# ===== Problem Statement =====
# Given an array of distinct integers arr, find all pairs of
# elements with the minimum absolute difference of any two elements.
# Return a list of pairs in ascending order(with respect to pairs),
# each pair [a, b] follows
#  . a, b are from arr
#  . a < b
#  . b - a equals to the minimum absolute difference of any two elements in arr


class Solution:

    # Brute force
    # Solution fails
    def approach1(self, arr: List[int]) -> List[List[int]]:
        min_abs = float("inf")
        result = []

        # First for loop to get the min abs
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                cur_min_abs = abs(arr[i]-arr[j])
                if cur_min_abs < min_abs:
                    min_abs = cur_min_abs

        # Second for loop to get the min abs diffs that
        # equal the min abs
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                if abs(arr[i]-arr[j]) == min_abs:
                    result.append(sorted([arr[i], arr[j]]))

        return sorted(result)


    # Runtime: 388 ms
    # Memory: 27.7 MB
    def approach2(self, arr: List[int]) -> List[List[int]]:
        # Always think: Will sorting the input give me
        #               any sort of advantage?
        arr.sort()
        result = []
        min_diff = float("inf")
        for i in range(len(arr)-1):
            abs_diff = abs(arr[i]-arr[i+1])
            if abs_diff < min_diff:
                min_diff = abs_diff

        for i in range(len(arr)-1):
            abs_diff = abs(arr[i]-arr[i+1])
            # No, trying to keep track of the
            # abs min diff within the same loop
            # as finding the pair of numbers that
            # evaluate to the min diff produces
            # the wrong result because the min_diff
            # isn't stable throughout the iteration,
            # which is what you need to have.
            #if abs_diff < min_diff:
            #    min_diff = abs_diff
            if abs_diff == min_diff:
                result.append([arr[i], arr[i+1]])

        # This solution takes O(1) space and O(n) time
        return result


    # Runtime: 344 ms
    # Memory: 27.7 MB
    def approach3(self, arr: List[int]) -> List[List[int]]:
        # Always think: Will sorting the input give me
        #               any sort of advantage?
        arr.sort()

        # Consider making a dict whose keys are pairs of
        # adjacent neighbors and whose values are their diffs
        #diffs_d = {}
        result = []
        min_diff = float("inf")
        for i in range(len(arr)-1):
            # If list is already sorted, then we don't need to use abs
            #abs_diff = abs(arr[i]-arr[i+1])
            abs_diff = arr[i+1] - arr[i]
            #diffs_d[(arr[i], arr[i+1])] = abs_diff
            if abs_diff < min_diff:
                # RESET result to the pair with the smallest diff!
                result = [[arr[i], arr[i+1]]]
                min_diff = abs_diff
            elif abs_diff == min_diff:
                result.append([arr[i], arr[i+1]])

        # Nooo, you're still making another loop here then. How
        # can we just make one loop?...Ah, consider resetting result!
        #return [pair for (pair,diff) in diffs_d.items() if diff == min_diff]

        return result


    #minimumAbsDifference = approach1
    #minimumAbsDifference = approach2
    minimumAbsDifference = approach3



if __name__ == "__main__":
    # Consider making a dict whose keys are arr's
    # elements and whose values are a complement...
    # Nah, this approach would probably involve a
    # a nested for loop

    # Somehow find the minimum abs difference...

    # Consider finding the minimum and the second minimum

    #arr = [1,3,6,10,15]
    arr = [40,11,26,27,-20]
    #arr = [4,2,1,3]
    sol = Solution()
    print(sol.minimumAbsDifference(arr))
