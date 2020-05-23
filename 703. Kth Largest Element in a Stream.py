import bisect
import heapq
from typing import List



class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._k = k
        #self._nums = nums
        # . Consider the idea of only slicing what
        #   you need from nums. Do you really need
        #   all the numbers? If k is given, then
        #   perhaps it can serve as a lower boundary
        #   that guarantees no other values below
        #   it will ever be considered...Shaving off
        #   all those lower values could save you space.
        # . Instead of saying reverse=True, you can just
        #   index the -kth element in self._nums
        #self._nums = sorted(nums, reverse=True)
        self._nums = sorted(nums)[-k:]


    # Runtime: 2720 ms, faster than 6.68%
    # Memory Usage: 18.1 MB, less than 8.70%
    def approach1(self, val: int) -> int:
        """
        This approach sorts val and returns
        the (k-1)th element in self._nums.
        """
        self._nums.append(val)
        # Sorting everytime this method is called
        # can be costly. Consider if there's an
        # efficient way to insert into self._nums
        # without having to sort each time...
        # - Ah, consider using something called
        #   the bisect module!
        self._nums.sort()
        return self._nums[-self._k]


    # Time Limit Exceeded
    # TODO: Come up with a cleaner solution using a heap that
    #       will not exceed the time limit during evaluation!
    def approach2(self, val: int) -> int:
        """
        This approach uses a max heap.
        """
        self._nums.append(val)
        cur_k = self._k
        res = None
        temp = self._nums.copy()  # Copying blows things up
        heapq._heapify_max(temp)
        while cur_k > 0:
            res = heapq._heappop_max(temp)
            cur_k -= 1

        return res


    # Runtime: 132 ms, faster than 40.66%
    # Memory Usage: 18 MB
    def approach3(self, val: int) -> int:
        """
        This approach uses the bisect module
        """
        bisect.insort(self._nums, val)
        return self._nums[-self._k]


    #add = approach1
    #add = approach2
    add = approach3



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
if __name__ == "__main__":
    k = 3
    arr = [4,5,8,2]
    kth_l = KthLargest(k, arr)
    print(kth_l.add(3))
    print(kth_l.add(5))
    print(kth_l.add(10))
    print(kth_l.add(9))
    print(kth_l.add(4))
