from typing import List

# Given n and m which are the dimensions of a matrix initialized by
# zeros and given an array indices where indices[i] = [ri, ci]. For
# each pair of [ri, ci] you have to increment all cells in row ri
# and column ci by 1.

# Return the number of cells with odd values in the matrix after
# applying the increment to all indices.

# Example:
#      [ 0 0 ]   n=2, m=2
#      [ 0 0 ]
# . indices = [[1,1], [0,0]]
# . For [1,1], increment all cells in row 1
#   and then all cells in column 1:
#      [ 0 1 ]
#      [ 1 2 ]
# . For [0, 0], increment all cells in row 0
#   and then all cells in column 0:
#     [ 2 2 ]
#     [ 2 2 ]
# - PROTIP: Don't think of the elements of indices as
#           cells in the matrix. Rather, think of them
#           as individual instructions for how to process
#           a row and a column (could help to think of a sudoku)

# Originally, you tried saying this to set the 0-matrix:
#   mat = [[0]*m]*n
# But this caused stranged behavior whenever you tried
# incrementing single -- you ended up incrementing a whole
# column instead! See this SO discussion that explains this
# weirdness:
# https://stackoverflow.com/questions/1959744/python-list-problem


class Solution:

    # Runtime: 44 ms
    # Memory: 13.9 MB
    def oddCellsNaive(self, n: int, m: int, indices: List[List[int]]) -> int:
        # THINK: There's probably a way to solve
        #        this problem WITHOUT the need
        #        for creating a 0 matrix since
        #        since all we're really asked
        #        for is the number of odd cells
        #        within some theoretical nxm matrix...
        mat = [[0]*m for i in range(n)]
        res = 0
        for r,c in indices:
            # Iterate through columns of mat[r]
            # to increment a whole row:
            for i in range(len(mat[r])):
                mat[r][i]+=1
            # Iterate through all rows of mat
            # to increment a whole column:
            for row in mat:
                row[c]+=1

        for row in mat:
            for col in row:
                if col % 2 != 0:
                    res += 1
        return res


    final = oddCellsNaive




if __name__ == "__main__":
    #n, m = 2, 2
    #indices = [[1,1],[0,0]]
    # Expected Result: 0

    n, m = 3, 3
    indices = [[0,1],[1,1]]
    # Expected Result: 6

    #indices = [[0, 0]]
    sol = Solution()
    res = sol.final(n,m,indices)
    print(res)
