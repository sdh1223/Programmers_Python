# https://daeun-computer-uneasy.tistory.com/69

def solution(numbers, target):
    answer = 0
    nodes = [0]
    # bfs 형식으로 가능한 수의 합을 nodes에 전부 저장한다
    # 첫번째 숫자도 더하기, 빼기 연산을 할 값이 필요하기 때문에 초기값은 0이 된다
    for i in numbers:
        temp = []
        # numbers의 숫자 모두를 더했을 때의 경우를 세기 때문에,
        # nodes에는 그 전 단계의 연산 결과가 남아 있으면 안 된다
        # (numbers 수가 총 5개인데 4개를 더한 결과가 남아 있으면 안 됨)
        # 때문에 연산 값을 nodes에 직접 추가하지 않고 temp를 활용한다
        for j in nodes:
            temp.append(j + i)
            temp.append(j - i)
            # 현재 nodes list에 들어 있는 전 단계 연산값들에
            # 추가로 이번 숫자를 더하고 뺀다
            # 이 값을 temp의 저장한 뒤
        nodes = temp # nodes를 이 temp로 업데이트한다
        # [4, 1, 2, 1]의 경우
        # 처음 nodes : [4, -4] (0에 4를 더하고 4를 뺌)
        # 두번째 nodes : [4+1, 4-1, -4+1, -4-1] (1을 더하고 뺀 값들로 업데이트)
        # 이런 식으로 계속 진행해서 네번째 nodes까지 업데이트한다
    for i in nodes:
        if i == target: # 그 후에 target에 맞는 경우의 수를 센다
            answer += 1
    return answer