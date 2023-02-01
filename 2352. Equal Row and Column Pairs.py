from collections import defaultdict
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = defaultdict(int)
        for row in grid:
            rows[tuple(row)] += 1

        columns = defaultdict(int)
        for col in range(len(grid[0])):
            current_col = []
            for row in range(len(grid)):
                current_col.append(grid[row][col])

            columns[tuple(current_col)] += 1

        answer = 0
        for elem in rows:
            answer += rows[elem] * columns[elem]

        return answer


sol = Solution()
print(sol.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))

