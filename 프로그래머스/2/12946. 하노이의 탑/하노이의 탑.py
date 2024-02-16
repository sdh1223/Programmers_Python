def solution(n):
    # 세 가지 과정을 재귀를 이용해 표현하면 된다
    # 1. n-1개의 원판을 1번 기둥에서 3번 기둥을 거쳐 2번 기둥으로 이동
    # 2. n번째 원판을 1번 기둥에서 3번 기둥으로 이동
    # 3. 2번 기둥에 있던 n-1개의 원판을 1번 기둥을 거쳐 3번 기둥으로 이동
    answer = []
    def hanoi(n, one, two, three):
        if n == 1:
            answer.append([one, three])
            return
        hanoi(n-1, one, three, two) # 1번
        answer.append([one, three]) # 2번
        hanoi(n-1, two, one, three) # 3번
    hanoi(n, 1, 2, 3)
    return answer