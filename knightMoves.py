import collections


def minMoves(n, startRow, startCol, endRow, endCol):
    # set variables
    visited = []

    directions = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]

    # traverse all possible moves from start pos
    q = collections.deque()
    q.append((startRow, startCol, 0))

    while q:
        r, c, move = q.popleft()
        if r == endRow and c == endCol:
            return move
        candidates = [(r + dr, c + dc, move + 1) for dr, dc in directions \
                      if r+dr in range(n) and c+dc in range(n)]

        for e in candidates:
            if e not in visited:
                visited.append(e)
                q.append(e)


        if candidates:
            move = move + 1

    return -1

if __name__ == '__main__':
    a = minMoves(9, 4, 4, 4, 8)

    print(a)


