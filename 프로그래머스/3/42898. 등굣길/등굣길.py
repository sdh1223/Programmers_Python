def solution(m, n, puddles):
    puddles = [[q,p] for [p,q] in puddles] # 좌표 거꾸로 돼있으니 뒤집기
    dp = [[0 for col in range(m+1)] for row in range(n+1)] # n+1, m+1 사이즈
    dp[1][1] = 1 # 1,1부터 시작 / 그 위쪽 값들은 0이라 계산에 문제 없음
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue # 1,1은 계산 안 하고 넘김
            if [i, j] in puddles:
                dp[i][j] = 0 # 물에 잠겼으면 0으로 변경
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1])
                # 왼쪽에서 오는 경우 + 위에서 오는 경우
    return dp[n][m] % 1000000007