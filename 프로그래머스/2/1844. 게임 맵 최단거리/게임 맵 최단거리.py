from collections import deque

def solution(maps):
    n = len(maps) # n: 세로 길이
    m = len(maps[0]) # m: 가로 길이
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # dx, dy를 list로 구성해서 상하좌우 이동 구현
    queue = deque()
    queue.append((0,0)) # 시작 지점을 queue에 추가
    while queue:
        x, y = queue.popleft() # bfs이므로 맨 왼쪽 요소를 꺼냄
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 각각 좌, 우, 하, 상을 구현할 수 있음
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
                # 맵을 벗어나는 경우 아무것도 하지 않고 건너뜀
            if maps[nx][ny] == 0:
                continue
                # 막혀 있는 경우 아무것도 하지 않고 건너뜀
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
                # 이동할 수 있는 경우
                # 한 칸 이동했으므로 해당 칸에 거리를 하나 더해주고
                # queue에 추가해 해당 위치에서의 연산을 추가로 하도록 함
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]
        # n-1, m-1의 목적지 칸의 수를 반환하면 되지만
        # 이 값이 업데이트되지 않고 1로 남았다면 도달할 수 없다는 뜻이므로 -1을 반환