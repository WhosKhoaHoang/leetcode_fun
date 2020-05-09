import datetime

# ===== Problem Statement =====
# Given a date, return the corresponding day of the week for that date.
# The input is given as three integers representing the day, month and
# year respectively.
# Return the answer as one of the following values
# {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

class Solution:

    # Runtime: 24 ms
    # Memory Usage: 14 MB
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days = ["Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday", "Sunday"]
        return days[datetime.datetime(year, month, day).weekday()]



if __name__ == "__main__":
    s = Solution()
    day = 31
    month = 8
    year = 2019
    print(s.dayOfTheWeek(day, month, year))
