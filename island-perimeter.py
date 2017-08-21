class Solution(object):
    def inBounds(self, grid, point):
        return point[0] >= 0 and point[0] < len(grid) and point[1] >= 0 and point[1] < len(grid[point[0]])

    def compute_neighbors(self, grid, current_point, row_increment, col_increment):

        neighbors = []

        for index in range(len(row_increment)):

            new_point = (current_point[0] + row_increment[index], current_point[1] + col_increment[index])

            if self.inBounds(grid, new_point) and grid[new_point[0]][new_point[1]] == 1:
                neighbors.append(new_point)

        return neighbors

    def compute_perimeter(self, grid, current_point, row_increment, col_increment):

        perimeter = 0

        for index in range(len(row_increment)):

            new_point = (current_point[0] + row_increment[index], current_point[1] + col_increment[index])

            if not self.inBounds(grid, new_point) or grid[new_point[0]][new_point[1]] == 0:
                perimeter = perimeter + 1

        return perimeter

    def islandPerimeter(self, grid):

        row_increment = [-1, 0, 1, 0]
        col_increment = [0, 1, 0, -1]

        if len(grid) == 0:
            return 0

        starting_row = 0
        starting_col = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    starting_row = i
                    starting_col = j
                    break

        if grid[starting_row][starting_col] == 0:
            return 0

        stack = [(starting_row, starting_col)]

        perimeter = 0
        seen = set()

        while stack:
            current_point = stack.pop()

            perimeter += self.compute_perimeter(grid, current_point, row_increment, col_increment)

            seen.add(current_point)

            for neighbor in self.compute_neighbors(grid, current_point, row_increment, col_increment):
                if neighbor not in seen:
                    stack.append(neighbor)
                    seen.add(neighbor)

        return perimeter