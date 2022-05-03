import collections


def moves(n, startRow, startCol, endRow, endCol, bishopRow, bishopCol):
    # set variables
    visited = []
    directions = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
    threatened = []
    smaller = bishopRow if bishopRow <= bishopCol else bishopCol
    threatened.append((bishopRow - smaller, bishopCol - smaller))
    while 1:
        t = (threatened[-1][0] + 1, threatened[-1][1] + 1)
        if t[0] in range(n) and t[1] in range(n):
            threatened.append(t)
        else:
            break
    print(threatened)
    visited.extend(threatened)
    if (endRow, endCol) in threatened:
        visited.remove((endRow, endCol))
    visited.remove((bishopRow, bishopCol))

    # do bfs
    q = collections.deque()
    q.append((startRow, startCol, 0))

    while len(q) > 0:

        r, c, move = q.popleft()
        if r == endRow and c == endCol:
            return move
        elif r == bishopRow and c == bishopCol:
            visited = list(set(visited) - set(threatened))

        candidates = [(r + dr, c + dc, move + 1) for dr, dc in directions \
                      if r + dr in range(n) and c + dc in range(n)]

        for e in candidates:
            if e not in visited:
                visited.append(e)
                q.append(e)

    return -1

if __name__ == '__main__':
    a = moves(5,0,0,4,3,3,0)
    print(a)