def solution(n):
    answer = 0
    while n > 0: # 최대한 점프를 많이 쓰는 방향으로 구성
        answer += n % 2
        # 짝수면 점프, 홀수면 점프 + 1을 해서 구성할 수 있다
        # 때문에 짝수면 0을, 홀수면 1을 더해준다
        n //= 2 # 점프했으므로 반으로 줄임
    return answer