def solution(s):
    l = list(map(int, s.split()))
    m = str(max(l))
    n = str(min(l))
    answer = n + ' ' + m
    return answer