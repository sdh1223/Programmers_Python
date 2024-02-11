from collections import deque

def bfs(place):
    # 응시자가 앉아 있는 자리 P를 시작 지점으로 하여 P 지점들 모두에 대해 bfs를 시행한다
    # 거리두기를 지키지 않은 P가 발견되는 순간 바로 0을 반환하고
    # 모든 시행이 무사히 끝났다면 거리두기가 지켜진 것이므로 1을 반환한다
    start = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                start.append((i,j))
    # 시작 지점 P들을 모아 list를 만든다
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for s in start:
        queue = deque([s])
        visited = [[0] * 5 for i in range(5)]
        distance = [[0] * 5 for i in range(5)]
        visited[s[0]][s[1]] = 1
        # P 하나마다 visited와 distance를 초기화해주고
        # 시작 지점을 다시 방문하는 경우를 막기 위해 방문 처리를 해준다
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
                    continue
                if place[nx][ny] == 'X':
                    continue
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[x][y] + 1
                    # distance는 1씩 증가시키면 간단하게 구현이 가능하다
                    if place[nx][ny] == 'O':
                        queue.append((nx,ny))
                        # O일 경우에만 queue에 추가한다
                        # P를 만났을 경우에는 더 나아갈 필요가 없음
                    if place[nx][ny] == 'P' and distance[nx][ny] <= 2:
                        return 0
                        # P를 만났는데 맨해튼 거리가 2 이하라면 바로 0을 반환
    return 1 # 모든 시작 지점에 대해 0이 반환되지 않았다면 1을 반환

def solution(places):
    answer = []
    for place in places:
        # place = [list(x) for x in p]
        # 문자열을 리스트로 변환하지 않아도 문제 없이 시행된다
        answer.append(bfs(place))
    return answer