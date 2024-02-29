def solution(A, B):
    answer = 0
    A.sort(reverse=True) # A를 큰 수부터 오게 정렬
    B.sort(reverse=True) # B를 큰 수부터 오게 정렬
    while A:
        if B[0] > A[0]: # B가 큰 경우 가장 큰 수로 승리
            answer += 1
            A.pop(0)
            B.pop(0)
        else: # A가 큰 경우 절대 못 이기므로 가장 작은 수로 패배
            A.pop(0)
            B.pop(-1)
    return answer