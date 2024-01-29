import heapq

def minute(time):
    time = time.split(':')
    result = int(time[0]) * 60 + int(time[1])
    return result
    # 시간을 분 단위로 변경한다
    # 10분을 더하는 계산을 쉽게 하기 위해 필요

def solution(book_time):
    # 종료 시간의 최솟값을 추적해서
    # 예약 가능한 시간을 만나면 하나의 시간으로 합쳐준다
    # 모든 과정을 끝낸 후 원소의 개수를 세면 된다
    # 다만 ["14:20", "15:20"]과 ["18:20", "21:20"]이 합쳐지면 안되기 때문에
    # 맨처음에 list를 시작 시간을 기준으로 정렬한다
    book_time.sort(key=lambda x: x[0])
    # 시작 시간을 기준으로 정렬
    # 문자열 상태여도 정렬에 문제는 없음
    book_time = [[minute(j), minute(i)] for i, j in book_time]
    # 분 단위로 변경해서 시작 시간, 종료 시간을 뒤집어준다
    # 최솟값을 찾기 위해 heap을 사용할 예정인데,
    # heap 내부 원소의 값이 두개라면 앞에 오는 값을 기준으로 최솟값을 구하기 때문
    heap = [book_time[0]]
    # pop할 때 list가 비어있으면 오류남
    # 때문에 첫번째 원소를 넣어준다
    for i in range(1, len(book_time)):
        minimum = heapq.heappop(heap) # 최솟값 pop
        min_start = minimum[1]
        min_end = minimum[0]
        now_start = book_time[i][1]
        now_end = book_time[i][0]
        # 뒤집어놔서 헷갈리니 명칭을 따로 정리
        if min_end + 10 <= now_start:
            heapq.heappush(heap, [now_end, min_start])
            # 예약이 가능하다면
            # ["14:20", "15:20"] + ["16:40", "18:20"] = ["14:20", "18:20"]
            # 와 같은 방식으로 붙여준다
            # 다만 뒤집어서 넣어야 함
        else:
            heapq.heappush(heap, minimum)
            heapq.heappush(heap, book_time[i])
            # 예약 불가능하면 heap에 추가
            # 최솟값도 pop해서 없어졌으니 다시 넣어줌
    return len(heap)