def solution(order):
    count = 0
    stack = []
    i = 1
    while i < len(order) + 1: # while문으로 order를 전부 순환
        stack.append(i) # stack에 순서를 계속 추가
        while stack and stack[-1] == order[count]:
            count += 1
            stack.pop()
            # 원하는 순서가 나온 경우 count를 세고 해당 순서를 빼낸다
            # while문을 사용하는 것을 볼 수 있는데
            # 만약 왼쪽 첫번째 예시의 [4, 3]처럼 숫자가 내림차순으로 되어 있는 경우
            # while문을 사용하지 않으면 4를 뺀 뒤 5부터 다시 append를 시작하게 되어
            # 3을 빼내지 못하게 된다
            # 때문에 while문을 사용해야 함
        i += 1
    return count # count가 얼마나 증가했는지 센다