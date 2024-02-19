import heapq

def solution(operations):
    heap = []
    max_heap = []
    # 최솟값, 최댓값을 모두 확인하기 위해 heap과 max_heap을 둘다 만든다
    for i in operations:
        i = i.split(' ')
        op, num = i[0], i[1]
        if op == 'I':
            heapq.heappush(heap, int(num))
            heapq.heappush(max_heap, -int(num))
            # max의 경우 -를 붙이면 구현 가능
        if heap and op == 'D':
            if num == '-1':
                minimum = heapq.heappop(heap)
                max_heap.remove(-minimum)
            else:
                maximum = heapq.heappop(max_heap)
                heap.remove(-maximum)
                # 최댓값, 최솟값을 제거할 때 다른 한쪽 heap에서도 똑같이 제거해준다
    if heap:
        minimum = heapq.heappop(heap)
        maximum = -heapq.heappop(max_heap)
        return [maximum, minimum]
    else:
        return [0, 0]
        