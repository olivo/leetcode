class Solution(object):
    def imageSmoother(self, M):
        N = [row[:] for row in M]

        diff_row = [-1, -1, 0, 1, 1, 1, 0, -1]
        diff_col = [0, 1, 1, 1, 0, -1, -1, -1]

        for i in range(len(M)):
            for j in range(len(M[0])):

                num_cells = 1
                val_sum = M[i][j]

                for diff_index in range(len(diff_row)):

                    adjacent_row = i + diff_row[diff_index]
                    adjacent_col = j + diff_col[diff_index]

                    if 0 <= adjacent_row and adjacent_row < len(M) and 0 <= adjacent_col and adjacent_col < len(
                            M[adjacent_row]):
                        num_cells += 1
                        val_sum += M[adjacent_row][adjacent_col]

                    N[i][j] = val_sum / num_cells

        return N