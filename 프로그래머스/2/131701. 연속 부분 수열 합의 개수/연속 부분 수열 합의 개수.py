def solution(elements):
    answer = set() # set은 중복 값을 제거해주는 역할을 함
    n = len(elements)
    elements = elements * 2 # 원형 계산을 위해 리스트를 두 배로 확장
    for i in range(n):
        for j in range(n):
            answer.add(sum(elements[j:j+i+1])) # 모든 경우의 수 계산
    return len(answer)