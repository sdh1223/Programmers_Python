import heapq

def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    # scoville로 heap 사용
    # scoville 자체는 list 형식이다
    # heap은 list에서 사용함
    while scoville[0] < K: # index 0에 항상 최솟값이 있으므로
        if len(scoville) == 1:
            count = -1
            break
            # 모든 음식을 K 이상 만들 수 없는 경우
            # scoville의 요소가 하나만 남아있을 것이다
            # 요소가 하나 남아도 이 값이 K보다 큰 값일 수도 있다
            # 다만 이때는 while문을 벗어났을 것이므로 해당이 되지 않음
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        new_scoville = min1 + (min2 * 2)
        heapq.heappush(scoville, new_scoville)
        # 스코빌 지수를 새로 계산해서 heap에 다시 추가
        count += 1
    return count