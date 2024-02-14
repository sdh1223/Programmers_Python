from collections import deque

def solution(board):
    answer = 0
    n = len(board) # n: 세로 길이
    m = len(board[0]) # m: 가로 길이
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start = (i,j)
    # 시작 지점 찾기
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([start])
    visited = [[0] * m for i in range(n)]
    count = [[0] * m for i in range(n)]
    visited[start[0]][start[1]] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x, y
            while True:
                nx += dx[i]
                ny += dy[i]
                # 벽이나 D에 부딪힐 때까지 전진해야 하므로
                # while문을 이용해 dx[i], dy[i]를 계속 더해준다
                if nx < 0 or ny < 0 or nx >= n or ny >= m or board[nx][ny] == 'D':
                    # 벽을 넘게 되거나 D에 도달하게 되는 경우
                    new_x, new_y = nx - dx[i], ny - dy[i]
                    # 그 바로 전 지점이 멈춰야 하는 지점이 된다
                    # 때문에 dx[i], dy[i]를 한 번 빼줌
                    if visited[new_x][new_y] == 0:
                        count[new_x][new_y] = count[x][y] + 1
                        # 방문한 적이 없다면 이동 횟수를 세고
                        if board[new_x][new_y] == 'G':
                            return count[new_x][new_y]
                            # 목표지점에 도달했다면 바로 횟수를 반환
                        visited[new_x][new_y] = 1
                        queue.append((new_x, new_y))
                    break
    return -1