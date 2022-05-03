class Solution:
    def orangesRotting(self, grid: [[int]]) -> int:

        # grid = [[2,1,1],[0,1,1],[1,0,1]]

        if len(grid) == 0:
            return -1

        a1 = []
        for row in grid:
            for e in row:
                if e == 1:
                    a1.append(e)
        if len(a1) < 1:
            return 0

        def find_rot(grid):

            start_rot = []
            rows, cols = len(grid), len(grid[0])

            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 2:
                        start_rot.append((r, c))


            return start_rot

        start_rot = find_rot(grid)  # (0,0)
        if len(start_rot)==0 : return -1

        print(start_rot)

        def bfs(start, grid) -> int:
            max_row = len(grid)
            max_col = len(grid[0])
            mins = 0
            # up, down, left, right
            directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

            q = []
            q.extend(start)
            if len(q) > 1: mins = mins - len(q) + 1

            while len(q) > 0:
                v = q.pop(0)  # (1,1)
                # mins += 1
                neighbors = []

                for direc in directions:
                    tmp = (v[0] + direc[0], v[1] - direc[1])
                    if 0 <= tmp[0] < max_row and \
                            0 <= tmp[1] < max_col and \
                            grid[tmp[0]][tmp[1]] == 1 and \
                            grid[v[0]][v[1]] == 2:
                        neighbors.append(tmp)
                        grid[tmp[0]][tmp[1]] = 2

                if len(neighbors) > 0:
                    mins += 1
                    q.extend(neighbors)

            for row in grid:
                if 1 in row:
                    return -1

            return mins

        return bfs(start_rot, grid)

        # print (str(find_rot(grid)))

if __name__ == '__main__':
    grid = [[2,1,1],[1,1,1],[0,1,2]]
    output = Solution.orangesRotting(Solution, grid)



    print(output)