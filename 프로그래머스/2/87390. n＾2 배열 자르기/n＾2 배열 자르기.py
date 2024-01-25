def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        answer.append(max(i//n, i%n) + 1)
        # 1차원 배열에서의 현재 위치를 n으로 나눴을 때
        # 몫과 나머지 중 더 큰 값에 1을 더하면 해당 위치의 값이 나온다
    return answer