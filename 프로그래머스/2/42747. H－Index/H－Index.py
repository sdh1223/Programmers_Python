def solution(citations):
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i] < i+1: # n번째 값이 n보다 작아질 때
            return i # n-1이 H-Index가 된다
    return len(citations) # 리스트 값이 모두 같을 때는 리스트 전체가 포함됨
        # [6, 5, 4, 2, 1]
        #  1  2  3  4
        # 3번 이상 인용된 논문이 3편 이상일 때가 최댓값이 된다
        # [5, 5, 5, 5, 5, 5]
        #  1  2  3  4  5  6
        # 이 경우 h = 6 - 1 = 5인데, 5는 총 6개 있으므로 h = 6이어야 한다
        # 따라서 이때는 len(citations)를 반환하게 함