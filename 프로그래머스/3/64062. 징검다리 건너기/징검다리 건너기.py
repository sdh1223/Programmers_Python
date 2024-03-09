import heapq

def solution(stones, k):
    # k 크기만큼의 구간 내의 최댓값을 구해서, 그 최댓값들 중 최솟값을 구한다
    # 이때 연산을 빨리 하기 위해 max heap을 활용
    heap = []
    answer = 200000001
    for i in range(k - 1):
        heapq.heappush(heap, [-stones[i], i])
    # k-1번째 돌까지 (돌 위의 숫자, 인덱스)를 heap에 삽입한다 (인덱스 상으로는 k-2)
    for i in range(k - 1, len(stones)): # k번째 돌부터 최댓값을 확인한다
        heapq.heappush(heap, [-stones[i], i]) # 현재 돌의 정보도 heap에 삽입
        while heap[0][1] <= i - k:
            heapq.heappop(heap)
        # 최댓값을 찾았다고 해도 현재 구간 내에 포함되지 않는다면 사용할 수 없다
        # 현재 i번째 돌에서의 최댓값을 확인하고 싶은 것이므로,
        # 최댓값의 인덱스를 계속 확인하여 i보다 k번째 이전에 있다면 꺼내서 없앤다
        answer = min(answer, -heap[0][0])
        # 구간 내에 포함되는 최댓값을 찾았다면 이들 중에서 최솟값을 answer에 저장한다
    return answer