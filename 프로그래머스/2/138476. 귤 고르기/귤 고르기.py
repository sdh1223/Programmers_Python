def solution(k, tangerine):
    answer = 0
    count = [0] * (max(tangerine)+1)
    for i in tangerine:
        count[i] += 1 # 같은 크기의 귤이 몇 개 있는지 셈
    count.sort(reverse=True) # 같은 크기가 많은 순대로 정렬
    sum = 0
    while True: # 가장 큰 갯수부터 k개를 넘을 때까지 더해서 최솟값을 구함
        for i in count:
            sum += i
            answer += 1
            if sum >= k:
                return answer