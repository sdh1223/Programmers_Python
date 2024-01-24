def solution(n):
    answer = 0
    for i in range(1, n+1):
        sum = 0
        for j in range(i, n+1):
            sum += j
            if sum == n:
                answer += 1
                break
            elif sum > n: # n을 넘기면 표현 불가능
                break
    return answer