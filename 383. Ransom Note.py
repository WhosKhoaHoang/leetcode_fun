from collections import Counter

# ===== Problem Statement =====
# Given an arbitrary ransom note string and another string containing
# letters from all the magazines, write a function that will return true
# if the ransom note can be constructed from the magazines ; otherwise,
# it will return false.
# Each letter in the magazine string can only be used once in your ransom note.

class Solution:

    # Runtime: 44 ms, faster than 83.18%
    # Memory Usage: 13.9 MB, less than 25.00%
    def approach1(self, ransom_note: str, magazine: str) -> bool:
        ransom_note_c = Counter(ransom_note)
        magazine_c = Counter(magazine)
        for char in ransom_note_c:
            if char not in magazine_c or\
               magazine_c[char] < ransom_note_c[char]:
               return False
        return True


    canConstruct = approach1



if __name__ == "__main__":
    sol = Solution()
    ransom_note = "aa"
    magazine = "ab"
    print(sol.canConstruct(ransom_note, magazine))
