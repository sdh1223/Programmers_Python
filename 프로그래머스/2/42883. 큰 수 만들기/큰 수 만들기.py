def solution(number, k):
    stack = []
    for num in number:
        while k > 0 and stack and stack[-1] < num:
        # 아직 k개를 전부 제거하지 않았어야 하고
        # stack이 비어있으면 안되고
        # stack의 맨 마지막 수가 현재 number보다 작아야 한다
            stack.pop()
            # 세가지를 모두 만족하면 stack에서 값을 꺼낸다
            # while문을 사용했으므로 작은 값이 있으면 계속 제거
            k -= 1
        stack.append(num) # 값을 꺼내던 안 꺼내던 값은 계속 추가
    answer = ''.join(stack[:len(stack)-k])
    # for문이 끝났음에도 k가 0이 되지 않았을 수 있다
    # 이때는 문자열의 뒤에서 k개만큼의 숫자를 제거해준다
    # 위 숫자 제거 과정을 끝마쳤다면, 문자열의 맨 앞에는 가장 큰 수가 들어있을 것이다
    # 때문에 뒤에서 제거하는 것이 값을 가장 크게 만드는 방법이 된다
    return answer