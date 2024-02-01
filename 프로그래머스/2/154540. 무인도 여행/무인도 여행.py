import sys 

def solution(maps):
    sys.setrecursionlimit(10000) # 재귀한도 제한을 늘려주지 않으면 오류가 난다
    answer = []
    rows = len(maps)
    cols = len(maps[0])
    maps =  [list(i) for i in maps]
    # 문자열을 하나씩 쪼개서 2차원 배열을 만든다
    # [['X','5','9','1','X'], ['X','1','X','5','X'], ['X','2','3','1','X'], ['1','X','X','X','1']]
    visited = [[0 for j in range(cols)] for i in range(rows)]
    # 각 노드에 방문했는지 확인하기 위해 maps와 같은 크기의 배열을 만든다
    # 0으로 초기화한 뒤 방문했다면 1로 변경
    def dfs(x, y):
        if x < 0 or y < 0 or x >= rows or y >= cols:
            return 0
            # 지도 범위를 벗어나면 0을 반환
        if visited[x][y] == 0 and maps[x][y] != 'X':
            visited[x][y] = 1
            return int(maps[x][y]) + dfs(x-1, y) + dfs(x, y-1) + dfs(x+1, y) + dfs(x, y+1)
            # 아직 방문하지 않았고 바다가 아니라면
            # 방문했음을 표기하고
            # 식량 숫자를 재귀적으로 더해준다
        return 0
        # if문을 통과하지 못했다면
        # 즉, 이미 방문했거나 바다라면 0을 반환해서 아무것도 더해지지 않게 한다
    for i in range(rows):
        for j in range(cols):
            island = dfs(i, j) # 각 노드마다 dfs를 확인
            if island != 0:
                answer.append(island)
                # 값이 0이 아니라면 정답 list에 추가
    if answer:
        answer.sort()
        return answer
    else:
        return [-1]