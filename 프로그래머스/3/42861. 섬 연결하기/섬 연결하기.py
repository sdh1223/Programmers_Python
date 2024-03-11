# Kruskal 알고리즘을 활용
# 가장 적은 비용으로 모든 노드를 연결하는 경우를 찾을 수 있다

def find_parent(parent, x):
    # 알고리즘을 진행하면서 노드를 하나씩 연결하게 되는데,
    # 이를 표현하기 위해 부모 노드 개념을 이용한다
    # 두 노드의 부모 노드가 같다면 해당 노드들은 연결되어 있다고 판단할 수 있다
    # find_parent는 노드 x의 부모 노드를 찾아주는 함수이다
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    # union_parent는 노드 a와 노드 b를 연결해주는 함수이다
    # 두 노드의 부모 노드를 같게 만들어 서로 연결한다
    # 두 부모 노드 중 번호가 더 작은 것을 최종 부모 노드로 삼는다
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    answer = 0
    v, e = n, len(costs) # 노드, 간선 수
    parent = [0] * v
    for i in range(v):
        parent[i] = i
    # 부모 노드의 정보를 담을 list를 생성한다
    # 자기 자신을 부모 노드로 갖도록 초기화
    for i in range(e):
        costs[i][0], costs[i][1], costs[i][2] = costs[i][2], costs[i][0], costs[i][1]
    # 현재 costs는 [섬1, 섬2, 비용]의 형태로 되어 있다
    # Kruskal 알고리즘을 활용하기 위해서는 비용이 작은 순대로 정렬해야 하기 때문에
    # 정렬을 위해 [비용, 섬1, 섬2]의 형태로 바꾸어 준다
    costs.sort() # 비용이 작은 순대로 정렬
    for edge in costs:
        cost, a, b = edge
        # 이미 정렬을 했기 때문에 비용이 작은 순대로 꺼낼 수 있게 되고, 때문에 최소 비용을 얻을 수 있게 된다
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += cost
        # 노드 a와 b의 부모 노드가 같다는 것은 이미 두 노드가 연결되어 있음을 의미한다
        # 이 상태로 a와 b를 연결한다면 사이클이 발생하게 되므로,
        # a와 b의 부모 노드가 같을 때에만 두 노드를 연결한다
        # 비용 합도 계속해서 업데이트 한다
    return answer