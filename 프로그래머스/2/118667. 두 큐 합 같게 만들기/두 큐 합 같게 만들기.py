from collections import deque

def solution(queue1, queue2):
    answer = 0
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    half = (sum1 + sum2) // 2
    max_count = len(queue1) * 3
    # 작업의 최대 횟수는 queue의 길이 * 3이다
    # queue 하나를 다른 queue에 전부 몰아넣고
    # 이 상태로 다시 비어있는 queue에 하나씩 옮긴다고 해보자
    # 이때 원소들을 전부 옮겼음에도 합이 같아지지 않는다면 해가 없다고 할 수 있다
    # queue 1개 길이 + queue 2개를 합친 길이 = queue 3개 길이이므로
    # 이 횟수가 작업의 최대 횟수가 된다
    dq1 = deque(queue1)
    dq2 = deque(queue2)
    while True:
        # 합이 더 큰 queue에서 원소를 꺼낸 뒤 다른 queue에 넣어준다
        # 이에 따라 합과 실행 횟수도 업데이트한다
        if sum1 > sum2:
            n = dq1.popleft()
            dq2.append(n)
            sum1 -= n
            sum2 += n
            answer += 1
        elif sum1 < sum2:
            n = dq2.popleft()
            dq1.append(n)
            sum1 += n
            sum2 -= n
            answer += 1
        else:
            break
        if answer == max_count: # 최대 횟수에 도달했다면 합을 같게 만들 수 없다
            return -1
    return answer