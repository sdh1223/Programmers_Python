def solution(triangle):
    for i in range(len(triangle)-2, -1, -1): # 맨 아래 왼쪽에서부터 위로 올라감
        for j in range(i+1):
            triangle[i][j] = max(triangle[i+1][j], triangle[i+1][j+1]) + triangle[i][j] # 왼쪽, 오른쪽 아래 두 가지 중 큰 수 + 현재 위치의 수
    return triangle[0][0]