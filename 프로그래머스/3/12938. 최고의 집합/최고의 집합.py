def solution(n, s):
    if n > s:
        return [-1]
    answer = [s//n] * n # 몫만큼 똑같이 분배한 list 생성
    index = n - 1
    for _ in range(s%n): # 나머지를 균등하게 1씩 분배하면 곱이 최대가 된다
        answer[index] += 1 # 오름차순 정렬이어야 하므로 뒤에서부터
        index -= 1
    return answer