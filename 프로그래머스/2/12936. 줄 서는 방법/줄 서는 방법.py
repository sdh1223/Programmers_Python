import math

def solution(n, k):
    # 첫번째 자리가 1일 때의 경우의 수는 (n-1)!이 되고,
    # 마찬가지로 2일 때의 경우의 수도 (n-1)!이 된다
    # 따라서, (n-1)!로 나눈 몫만큼 첫번째 자리 수가 1, 2, ...와 같이 증가함을 알 수 있다
    # 때문에 k를 (n-1)!로 나눈 몫에 1을 더해주면 첫번째 자리 숫자를 구할 수 있다
    # (몫만큼의 경우의 수는 이미 시행했으므로 그 다음 수가 필요함)
    # 나머지 자리도 n을 1씩 감소시키며 같은 방식으로 진행하면 된다
    answer = []
    num = [i for i in range(1, n+1)]
    # 1부터 n+1까지의 값을 가지는 list를 생성하여 필요한 번호를 꺼낸다
    # 1부터 시작하는 점이 중요함
    fac = 1
    factorial = [1]
    for i in range(1, n):
        fac *= i
        factorial.append(fac)
        # factorial을 항상 계산하면 시간이 너무 오래 걸리므로
        # factorial 값들을 꺼내쓸 수 있는 list를 생성한다
        # 0!인 1이 하나 더 포함되어 있어야 오류가 발생하지 않음
    while num:
        fac = factorial.pop()
        # factorial list는 [1, 1, 2, 6, 24]와 같은 형태로 되어 있다
        # 때문에 뒤에서부터 값을 꺼내준다
        i = (k-1) // fac
        # factorial로 (k-1)을 나눠준다
        # i번째 값을 num에서 꺼낼 예정인데, list는 0부터 시작하므로 k에서 1을 빼준다
        answer.append(num.pop(i))
        # num list는 1부터 시작하기 때문에, index 0에는 1이, index 1에는 2가 들어있다
        # index보다 1이 더 큰 값이 들어있기 때문에,
        # 앞서 말한 1을 더해주는 과정을 구현할 수 있게 된다
        k = k % fac
        # 두번째 자리부터는 factorial로 나눈 나머지를 가지고 다시 똑같이 시행하면 된다
    return answer