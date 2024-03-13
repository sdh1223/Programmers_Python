import heapq

def solution(jobs):
    # 이미 한 작업이 시행되고 있는 시점을 가정해서,
    # 해당 작업의 시작 시간 start, 해당 작업이 종료된 뒤 다음 작업을 처리할 수 있는 시간 free를 설정한다
    # 이때 나머지 작업들의 요청 시간을 확인하여 만약 요청 시간이 이 구간 사이에 있다면 heap에 삽입한다
    # 소요 시간이 적은 작업을 처리하는 것도 중요하지만 요청 시간이 얼마나 빠른지 역시 판단해야 하기 때문에,
    # 요청 시간이 빠른 작업들을 먼저 모으고 그 안에서 heap을 통해 소요 시간이 적은 작업을 찾는 것이다
    # 왼쪽 문제를 예시로 들어보자
    # 만약 현재 A 작업이 시행되고 있다고 하면, 시작 시간(start)은 0, 종료 시간(free)은 3이 될 것이다
    # B와 C 모두 요청 시간이 이 구간 내에 있으므로 heap에 삽입될 것이고, 그 후엔 소요 시간이 적은 C를 꺼내 수행하게 된다
    # C의 작업이 시작됨에 따라 start는 C의 시작 시간 3, free는 C의 종료 시간 9로 업데이트 된다
    # 왼쪽 문제에는 존재하지 않지만, 만약 이 구간 내에 존재하는 작업 D가 있다면 heap에 새로 추가될 것이다
    # 이때는 heap에 이미 존재하던 B와 소요 시간을 비교하여 소요 시간이 적은 것이 먼저 시행되게 된다
    # 만약 현재 구간에 시행할 수 있는 작업이 없다면, free를 1 증가시킨 뒤 다시 찾도록 한다
    total_time, start, free = 0, -1, 0
    # total_time: 각 작업의 요청부터 종료까지 걸린 시간의 총합
    # start: 현재 시행되고 있는 작업의 시작 시간
    # free: 현재 작업이 종료된 뒤 다음 작업을 처리할 수 있는 시간
    job_left = len(jobs)
    # job_left: 아직 처리되지 않은 남은 작업의 수
    heap = []
    while job_left != 0: # 남은 작업이 0이 되면 종료
        for time in jobs: # jobs를 순회하면서
            request, work = time # 요청 시간, 소요 시간을 꺼낸다
            if start < request <= free:
                heapq.heappush(heap, (work, request))
            # 요청 시간이 (start, free) 구간 내에 존재한다면 heap에 삽입
            # 소요 시간의 최솟값을 구해야 하므로 순서를 바꿔준다
        if heap: # heap에 원소가 존재한다는 것은 현재 처리할 수 있는 작업이 있음을 의미한다
            time = heapq.heappop(heap)
            work, request = time
            # 소요 시간이 가장 적은 작업을 찾아 소요 시간, 요청 시간을 꺼낸 뒤
            start = free
            free += work
            # 새로운 작업이 시행될 것이므로 start, free를 각각 새로운 시작 시간과 종료 시간으로 업데이트 해준다
            # start는 새로운 작업이 시작된 시간, 즉 free하여 작업을 시작한 시간이 되고
            # 새로운 작업을 끝낸 뒤에야 free해질 것이므로 free에는 소요 시간을 더해준다
            total_time += free - request
            # 종료 시간 - 요청 시간을 total_time에 더해주어 총합을 업데이트하고
            job_left -= 1
            # 작업을 하나 처리했으므로 남은 작업 수를 줄여준다
        else:
            free += 1 # 처리할 수 없는 작업이 없으면 free 1 증가
    return total_time // len(jobs) # 평균을 구하기 위해 총 작업 수로 나누어 주어 반환