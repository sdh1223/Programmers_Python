def fib(n):
    a, b = 0, 1
    for i in range(n): # 재귀 쓰면 시간 초과
        a, b = b, a+b
    return a

def solution(n):
    answer = fib(n) % 1234567
    return answer