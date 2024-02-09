import heapq

def solution(N, road, K):
    # Dijkstra 알고리즘을 활용한다
    # Dijkstra 알고리즘은 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하고,
    # 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 기존 비용보다 적다면 갱신하는 구조를 가지고 있다
    INF = int(1e9) # 무한대를 표기하기 위해 사용
    graph = [[] for i in range(N + 1)] # 연결된 노드와 거리를 저장하는 그래프
    distance = [INF] * (N + 1) # 최단 거리를 저장하는 테이블 (초기값은 무한대)
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
        # a: 출발 노드 / b: 도착 노드 / c: 두 노드 사이의 거리
        # 도로의 정보는 중복되지 않으므로 a와 b 모두에 서로의 정보를 입력해주어야 한다
    def dijkstra(start):
        queue = []
        # queue에는 (출발 노드에서 현재 노드까지의 거리, 현재 노드 번호)의 tuple이 추가된다
        # heap을 이용하므로 항상 출발 노드에서 현재 노드까지의 거리가 짧은 원소를 꺼낼 수 있게 된다
        heapq.heappush(queue, (0, start))
        distance[start] = 0
        # 출발 노드의 정보를 입력하고 시작
        while queue: # queue에 원소가 존재하는 동안
            dist, node = heapq.heappop(queue)
            # heappop을 통해 최단 거리가 가장 짧은 노드의 정보를 꺼낸다
            # dist: 출발 노드에서 현재 노드까지의 거리
            # node: 현재 노드 번호
            if distance[node] < dist: # 기존의 최단 거리가 현재 거리보다 짧다면 업데이트할 필요가 없다
                continue # 아래 for문을 시행하지 않고 넘어감
            for i in graph[node]:
                cost = dist + i[1]
                # 현재 거리가 더 짧다면 현재 노드를 거쳐 다른 노드로 가는 거리를 계산한다
                # dist: 출발 노드에서 현재 노드까지의 거리
                # i[1]: 현재 노드에서 i번째 노드까지의 거리
                # 즉, cost는 출발 노드에서 현재 노드를 거쳐 i번째 노드로 가는 새로운 거리를 의미한다
                if cost < distance[i[0]]: # i[0] : 다음 노드의 번호
                    distance[i[0]] = cost
                    heapq.heappush(queue, (cost, i[0]))
                    # i[0]: i번째 노드의 번호
                    # i[0] 노드의 최단 거리를 확인하여 cost가 더 적은 비용을 가진다면 최단 거리를 cost로 업데이트 한다
                    # 새로운 거리가 생겼으므로 queue에 (거리, 노드 번호) 순으로 삽입한다
    dijkstra(1) # 시작 지점이 1이므로 1을 넣고 알고리즘 시행
    count = 0
    for i in range(1, N+1):
        if distance[i] <= K:
            count += 1
            # 최단 거리가 K보다 작은 노드의 개수를 센다
    return count