# ===== Problem Statement =====
# Given the array nums, for each nums[i] find out
# how many numbers in the array are smaller than it.
# That is, for each nums[i] you have to count the number
# of valid j's such that j != i and nums[j] < nums[i].
#
# Return the answer in an array.



class Solution:

    # Runtime: 280 ms
    # Memory: 14.1 MB
    def smallerNumbersThanCurrentBrute(self, nums):
        result = []
        for i in nums:
            count = 0
            for j in nums:
                # No need to check if j != i because
                # j < i already implies !=
                if j < i:
                    count += 1
            result.append(count)

        return result


    # Runtime: 56 ms
    # Memory: 14 MB
    def smallerNumbersThanCurrent(self, nums):
        nums_s = sorted(nums)
        result = []
        # Store a dict that keeps the count
        # of elements less than an i'th
        # element in nums
        d = {}
        for i in range(len(nums_s)):
            # say "not in d" to prevent from
            # looking at the same element
            if nums_s[i] not in d:
                d[nums_s[i]] = i
        for e in nums:
            result.append(d[e])

        return result



if __name__ == "__main__":
    x = Solution()
    nums = [8,1,2,2,3]
    result = x.smallerNumbersThanCurrentBrute(nums)
    #result = x.smallerNumbersThanCurrent(nums)
    print(result)
