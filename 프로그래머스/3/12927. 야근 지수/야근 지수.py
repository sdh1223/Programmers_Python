import heapq

def solution(n, works):
    # max heap을 만들어서 최댓값을 꺼낸 뒤, 1을 빼주고 heap에 다시 넣어준다
    # 이 과정을 n번 반복
    answer = 0
    max_heap = []
    for i in works:
        heapq.heappush(max_heap, -i)
    while n > 0 and max_heap:
        maximum = -heapq.heappop(max_heap)
        if maximum != 0:
            maximum -= 1
            heapq.heappush(max_heap, -maximum)
        n -= 1
    return sum([i ** 2 for i in max_heap])