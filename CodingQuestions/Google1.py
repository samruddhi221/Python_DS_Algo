"""
Question: In a nxn chessboard, the position of king and queen is specied as K->(kx, ky) and Q->(qx, qy).
Other pieces are denoted by '1's and blank spaces are denoted by '0'. The king can move one step in any
direction. There are j jumps, i.e. the king can share the space with a piece j times.

Write an algorithm to calculate the shorted distance the king has to travel to reach the queen.
chessboard = [[K, 1, 0, 0, 0],
              [0, 1, 0, 0, 0],
              [0, 1, 0, 0, 0],
              [0, 0 ,0, 0, 1],
              [1, 0, 0, 1, Q]]
kx=ky=0, qx=qy=4, j=1

answer = 4 (K->(1,1)->(2,2)->(3,3)->Q)
"""
import collections


def shortestDistance(chessboard, kx, ky, qx, qy):

    pass

def bfs(chessboard, kx, ky, qx, qy):
    n = len(chessboard)
    queue = collections.deque([])
    queue.append((kx, ky, 0))   #x, y, distance
    # next move = {up, up_right_diag, right, down_right_diag, down, down_left, left, up_left}
    nextRow = [-1,-1,0,1,1,1,0,-1]
    nextCol = [0,1,1,1,0,-1,-1,-1]
    visited = [[0 for i in range(n)] for j in range(n)]

    while queue:
        node_x, node_y, distance = queue.popleft()
        if node_x==qx and node_y==qy:
            return distance
        for i in range(8):
            nextX = node_x+nextRow[i]
            nextY = node_y+nextCol[i]
            if 0 <= nextX <= n and 0 <= nextY <= n:
                if chessboard[nextX][nextY] == 0:
                    if visited[nextX][nextY] == 0:
                        queue.append((nextX, nextY, distance+1))
                        visited[nextX][nextY] = distance
                    else:
                        visited[nextX][nextY] = min(visited[nextX][nextY], distance+1)



    pass

if __name__ == '__main__':


