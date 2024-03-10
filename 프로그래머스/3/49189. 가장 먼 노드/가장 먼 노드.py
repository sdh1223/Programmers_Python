from collections import deque

def solution(n, edge):
    # bfs를 이용한다
    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    visited, distance = [0] * (n + 1), [0] * (n + 1)
    visited[1] = 1
    queue = deque([1])
    while queue:
        index = queue.popleft()
        for i in graph[index]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                distance[i] = distance[index] + 1
    distance.sort(reverse=True)
    answer = distance.count(distance[0])
    return answer