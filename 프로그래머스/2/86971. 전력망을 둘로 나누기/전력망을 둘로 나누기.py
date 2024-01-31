import copy

def dfs(x, graph, visited): # x번 노드에 연결되어 있는 노드 개수 구하기
        count = 1
        if visited[x] == 0:
            visited[x] = 1
            for i in graph[x]:
                count += dfs(i, graph, visited)
            return count
        return 0

def solution(n, wires):
    # 노드를 연결하는 간선을 하나 끊어 전력망을 두 개 생성한다
    # dfs를 통해 두 전력망의 노드 개수를 구하고 그 차이까지 구한다
    # 이 과정을 모든 간선에 대해 반복해서 최솟값을 구함
    answer = []
    graph = [[] for _ in range(n+1)]
    # wires를 인접 리스트로 표현한다
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
        # list의 index를 노드 번호로 사용한다
        # 해당 노드 번호와 같은 index에 어떤 노드들이 연결되어 있는지를 저장한다
        # 노드 번호가 1번부터 시작하기 때문에 0번 index는 비우고 시작한다
        # 때문에 graph 크기가 n+1이 된다
        # 예시 1의 wires로 만든 graph는 다음과 같다
        # [[], [3], [3], [1, 2, 4], [3, 5, 6, 7], [4], [4], [4, 8, 9], [7], [7]]
    for a, b in wires:
        visited = [0] * (n+1)
        new_graph = copy.deepcopy(graph)
        new_graph[a].remove(b)
        new_graph[b].remove(a)
        # wires에는 연결 정보가 포함되어 있기 때문에 이를 확인하면서 graph에서 해당 연결을 지워준다
        # graph뿐만 아니라 visited도 계속 초기화해주어야 코드가 제대로 작동함
        answer.append(abs(dfs(a, new_graph, visited) - dfs(b, new_graph, visited)))
        # 노드 개수 차이 값을 answer에 추가한다
    return min(answer) # 최솟값 반환