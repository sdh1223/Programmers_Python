def solution(n):
    # 달팽이 채우기의 구조를 자세히 보면,
    # 처음 n 값에서 하나씩 줄어들며
    # 아래쪽, 오른쪽, 위쪽 순으로 계속 움직이는 것을 알 수 있다
    # n = 4일 경우의 예를 들면,
    # 아래쪽으로 4칸, 오른쪽으로 3칸, 위로 2칸, 그리고 다시 아래로 1칸 이동한다
    # 이 규칙성을 이용해 코드를 작성한다
    snail = [[0] * n for _ in range(n)] # n*n 사이즈의 list 생성
    answer = []
    x, y = -1, 0
    # 이 좌표는 snail list의 index로, 이를 이용해 이동을 구현한다
    # 달팽이 채우기는 1부터 시작하고, 기본적인 for문은 0부터 시작하기 때문에
    # 이 차이를 염두에 두고 초기값을 설정한다
    # x와 y 중 x를 -1로 설정한 까닭은, 맨처음에는 무조건 아래로 이동하여
    # x가 1 증가할 것이기 때문이다
    num = 1 # 칸 안에 채울 숫자
    for i in range(n):
        for j in range(i, n):
        # snail list는 [i][j]의 index를 가진다
        # 피라미드 구조를 가지기 때문에 j의 범위는 i부터 시작하게 한다
            if i % 3 == 0: # 아래쪽으로 이동하는 경우
                x += 1
            elif i % 3 == 1: # 오른쪽으로 이동하는 경우
                y += 1
            elif i % 3 == 2: # 위쪽으로 이동하는 경우 (엄밀히 말하면 왼쪽 위)
                x -= 1
                y -= 1
            snail[x][y] = num
            num += 1
            # num 값을 계속 증가시키며 넣는다
    for i in range(n):
        for j in range(i+1):
            answer.append(snail[i][j])
            # 최종 결과값은 1차원 list이므로 2차원 list의 값들을 추가한다
            # snail list 내부에는 0도 들어있지만,
            # 범위 자체가 수정한 값들만 순환하게 되어 있어 상관이 없다
    return answer