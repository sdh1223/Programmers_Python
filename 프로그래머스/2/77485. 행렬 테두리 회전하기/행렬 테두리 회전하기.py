def solution(rows, columns, queries):
    answer = []
    matrix = [[0 for col in range(columns)] for row in range(rows)]
    n = 1
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = n
            n += 1
    # 1부터 순서대로 값이 오도록 행렬을 먼저 만들어준다
    for r1, c1, r2, c2 in queries:
        r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1
        first = matrix[r1][c1]
        minimum = first
        for i in range(r1, r2):
        # 왼쪽 세로에서 위로 올라가는 부분
            temp = matrix[i+1][c1]
            matrix[i][c1] = temp
            minimum = min(minimum, temp)
            # 회전 방향과 for문의 진행 방향은 반대가 된다
            # 옆의 큰 그림을 예시로 들어보자
            # 맨 처음은 14부터 시작하게 될 것이다
            # temp는 14의 아래에 있는 20이 되고
            # 14는 20(temp)으로 교체된다
            # 그 다음은 20의 경우를 시행하게 되는데
            # temp -> 20의 아래에 있는 26
            # 20 -> 26(temp)으로 교체된다
            # 즉, 값들이 한 칸씩 위로 당겨지고 있지만
            # 여기서 주목해야할 점은 row의 index는 증가하고 있다는 점이다
            # 회전 방향의 반대로 index를 증가시킴으로써 회전을 구현했음을 알 수 있다 
            # 교체가 끝나면 최솟값을 계속해서 업데이트한다
        for j in range(c1, c2):
        # 아래에서 왼쪽으로 이동하는 부분
            temp = matrix[r2][j+1]
            matrix[r2][j] = temp
            minimum = min(minimum, temp)
            # 총 4가지의 for문을 시행하게 될 텐데,
            # 시행 순서는 실제 테두리의 회전 방향이 아닌 for문의 이동 방향을 따라야 한다
            # 앞선 경우에서 값들이 위로 당겨졌지만 index 자체는 r1에서 r2로 바뀌며 아래로 이동했다
            # 때문에 c1에서 c2로 이동하는 for문을 선택해야 한다
        for i in range(r2, r1, -1):
            temp = matrix[i-1][c2]
            matrix[i][c2] = temp
            minimum = min(minimum, temp)
        for j in range(c2, c1, -1):
            temp = matrix[r1][j-1]
            matrix[r1][j] = temp
            minimum = min(minimum, temp)
        matrix[r1][c1+1] = first
        answer.append(minimum)
    return answer