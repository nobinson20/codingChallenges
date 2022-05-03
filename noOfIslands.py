import collections


class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        if not grid:
            return 0

        count = 0
        rows, cols = len(grid), len(grid[0])
        v = set()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def bfs(cur):
            q = collections.deque()
            q.append(cur)
            v.add(cur)

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c]=='1' and
                        (r,c) not in v):
                        q.append((r,c))
                        v.add((r,c))



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and  (r,c) not in v:
                    bfs((r,c))
                    count+=1

        return count









