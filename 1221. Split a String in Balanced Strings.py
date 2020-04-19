
# ===== Problem Statement ===== #
# Balanced strings are those who have equal quantity of 'L' and 'R' characters.

# Given a balanced string s split it in the maximum amount of balanced strings.

# Return the maximum amount of splitted balanced strings.


# THINK:
# - Scan from left to right. Somehow keep track of the
#   character being considered that can form a balanced string.
# - Would using some data structure help me solve the problem?
# - Note that the problem only asks you for a count, not the actual
#   balanced strings themselves...
# - Continuously pop from some container while keeping track of
#   of the current character. E.g., R - R - L (SWITCH TRACK) - L,
#   then check to see if the number of Rs and number of Ls is equal...
#    * May not be necessary to pop, can just loop through the string...


class Solution:

    # Runtime: 36 ms
    # Memory: 13.9 MB
    def balancedStringSplit(self, s: str) -> int:
        # Let the empty string indicate a transition
        # between balanced string cases.
        cur_char = ""
        cur_cnt = 0
        result = 0
        for char in s:
            if cur_char == "":
                cur_char = char
                cur_cnt +=1
            else:
                if cur_char != char:
                    cur_cnt -= 1
                    # When 0 is reached, then a balanced
                    # string case has been processed
                    if cur_cnt == 0:
                        result += 1
                        cur_char = ""
                else:
                    cur_cnt += 1

        return result


    def balancedStringSplitDUD(self, s: str) -> int:
        # THINK:
        # - Consider using some baseline counter
        #   that you not only increment but also
        #   decrement. Whenever it's 0, that indi-
        #   cates that equality in characters
        #   was reached...or rather, when a balanced
        #   string has been processed.

        # Ugh, I'm off by one with this code...
        prev_char = s[0]
        count_d = { "R": 0, "L": 0 }
        sw_count = 0
        result = 0
        for i in range(len(s)):
            print(s[i])
            if prev_char != s[i]:
                print("sw_count increment")
                sw_count += 1

            if sw_count == 2 or i == len(s)-1:
                print("SWITCH")
                print(count_d)
                if count_d["R"] == count_d["L"]:
                    result += 1
                count_d["R"] = 0
                count_d["L"] = 0
                sw_count = 0

            count_d[s[i]] += 1
            prev_char = s[i]
            print()

        return result



if __name__ == "__main__":
    sol = Solution()
    s = "RLRRLLRLRL"  # Output: 4 ("RL", "RRLL", "RL", "RL")
    #s = "RL"  # Output: 1 ("RL")

    result = sol.balancedStringSplit(s)
    print(result)
