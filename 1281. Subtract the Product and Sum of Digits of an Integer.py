# ===== Problem Statement =====
# Given an integer number n, return the
# difference between the product of its
# digits and the sum of its digits.



class Solution:

    # Runtime: 24 ms
    # Memory: 13.8 MB
    def subtractProductAndSum(self, n: int) -> int:
        mult = 1
        add = 0
        while n > 0:
            mult *= n % 10
            add += n % 10
            n //= 10

        return (mult-add)


if __name__ == "__main__":
    # THINK:
    # . How to get the count of digits? Use a while loop that "shaves" n
    # . How to get the actual digits themselves? With integer division (//)
    sol = Solution()
    n = 234
    result = sol.subtractProductAndSum(n)
    print(result)
