# https://velog.io/@ju_h2/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level2-%EA%B0%80%EC%9E%A5-%ED%81%B0-%EC%A0%95%EC%82%AC%EA%B0%81%ED%98%95-%EC%B0%BE%EA%B8%B0-%EB%8F%99%EC%A0%81-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-dp

def solution(board):
    # 동적 계획법을 이용한다
    # 왼쪽 대각선 위 칸, 왼쪽 옆 칸, 바로 위 칸 중 최솟값 + 1로 점화식을 세운다
    # 정사각형 구조를 찾기 때문에 이런 식이 성립함
    rows = len(board)
    cols = len(board[0])
    max_length = 0
    for i in range(1, rows):
        for j in range(1, cols):
            if board[i][j] == 1: # 다만 값이 1일 때만 시행해야 한다
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
    for i in range(rows):
        row_max = max(board[i])
        max_length = max(max_length, row_max)
        # 시행 종료 후 가장 큰 정사각형 구하기
        # 2차원 배열은 max 값을 바로 구할 수 없으므로
        # row마다 max 값을 구해야 한다
        # 정사각형이 없는 경우 0이 나와야 하므로
        # max_length의 초기값은 0으로 한다 (윗부분에 있음)
        # 또한 dp를 시행할 때마다 최댓값을 구하지 않고
        # 모두 끝난 뒤 최댓값을 구해야 값에 오류가 발생하지 않는다
    answer = max_length ** 2 # 넓이니까 제곱
    return answer