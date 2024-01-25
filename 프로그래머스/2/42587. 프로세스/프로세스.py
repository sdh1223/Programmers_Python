def solution(priorities, location):
    answer = 0
    queue =  [(i,p) for i,p in enumerate(priorities)]
    # location 정보를 저장하기 위해 tuple로 list를 생성
    while True:
        process = queue.pop(0)
        # 맨 앞 process를 꺼냄
        if any(process[1] < i[1] for i in queue):
            queue.append(process)
            # any : 하나라도 True라면 True
            # queue 안에 자신보다 높은 우선순위가 하나라도 있다면 맨 뒤에 넣음
        else:
            answer += 1
            if process[0] == location:
                return answer
                # 우선순위가 가장 높다면 count를 세고
                # location이라면 반환