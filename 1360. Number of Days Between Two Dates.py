from datetime import datetime

# ===== Problem Statement =====
# Write a program to count the number of days between two dates.
# The two dates are given as strings, their format is YYYY-MM-DD

class Solution:


    # Runtime: 32 ms, faster than 53.72%
    # Memory Usage: 13.9 MB, less than 100.00%
    def approach1(self, date1: str, date2: str) -> int:
        return abs((datetime.strptime(date2, "%Y-%m-%d")-
                    datetime.strptime(date1, "%Y-%m-%d")).days)


    daysBetweenDates = approach1



if __name__ == "__main__":
    sol = Solution()
    date1 = "2020-01-15"
    date2 = "2019-12-31"

    print(sol.daysBetweenDates(date1, date2))
