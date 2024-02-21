def dfs(n, i, computers, visited):
    if not visited[i]:
        visited[i] = True # 방문 표시
        for j in range(n):
            if computers[i][j] == 1: # i와 j가 연결되어 있다면
                dfs(n, j, computers, visited) # j로 다시 dfs
        return True # 다른 컴퓨터가 연결되어 있다면 True
    return False # 더 이상 연결되어 있는 컴퓨터가 없으면 False

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if dfs(n, i, computers, visited) == True:
            answer += 1
            # 1, 2, 3이 연결되어 있다면,
            # i = 1일 때 1 = True, 2 = True, 3 = False로 나올 것이다
            # 2도 True로 반환되지만, 어짜피 i = 1일 때의 경우이므로
            # 1이 True인지만 확인하기 때문에 상관이 없다
            # i = 2일 때는 이전에 방문했기 때문에 false로 반환될 것이다
    return answer