def solution(progresses, speeds):
    answer = []
    queue = []
    for p, s in zip(progresses, speeds):
        n = (100-p) // s
        if (100-p) % s != 0:
            n += 1
        # 남은 작업 일수 계산
        if not queue or queue[0] >= n: # queue의 맨
            queue.append(n)
            # queue의 맨 앞 값이 현재 값보다 크거나 같으면 현재 값을 append
            # queue에 7이 있는데 3이 들어오면 7이 나갈 때까지 기다려야 함
        else:
            answer.append(len(queue))
            queue = [n]
            # queue의 맨 앞 값이 현재 값보다 작으면 queue의 모든 요소를 다 꺼냄
            # 현재 값은 넣어서 다음 계산에 활용되도록 함
    answer.append(len(queue))
    # for문을 다 돌려도 마지막 값이 남아있으므로 한 번 더 처리해주어야 한다
    return answer