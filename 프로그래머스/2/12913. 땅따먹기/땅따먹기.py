def solution(land):
    n = len(land)
    for i in range(1,n):
        land[i][0] = max(land[i-1][1], land[i-1][2], land[i-1][3]) + land[i][0]
        land[i][1] = max(land[i-1][0], land[i-1][2], land[i-1][3]) + land[i][1]
        land[i][2] = max(land[i-1][0], land[i-1][1], land[i-1][3]) + land[i][2]
        land[i][3] = max(land[i-1][0], land[i-1][1], land[i-1][2]) + land[i][3]
        # 내려올 수 있는 칸에서 가장 큰 값 + 현재 위치 값
        # dp로 계속 계산
    answer = max(land[n-1][0], land[n-1][1], land[n-1][2],land[n-1][3])
    # 마지막 행에서 가장 큰 값이 정답이 된다
    return answer