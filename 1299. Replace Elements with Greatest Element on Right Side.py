from typing import List

# Given an array arr, replace every element in that array
# with the greatest element among the elements to its right,
# and replace the last element with -1.
# After doing so, return the array.

class Solution:

    # Runtime: 124 ms
    # Memory: 14.9 MB
    def replaceElements(self, arr: List[int]) -> List[int]:
        cur_max = arr[-1]
        prev_max = cur_max
        # Loop from the back and keep a running max to
        # replace the guys along the way to the front
        for i in range(len(arr)-1, -1, -1):
            if arr[i] > cur_max:
                cur_max = arr[i]
                arr[i] = prev_max
                prev_max = cur_max
            else:
                arr[i] = cur_max

        arr[-1] = -1
        return arr



if __name__ == "__main__":
    sol = Solution()
    arr = [17,18,5,4,6,1]
    print(sol.replaceElements(arr))
