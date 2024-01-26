def solution(prices):
    answer = [i for i in range(len(prices))][::-1]
    # 1씩 감소하는 list를 만든다
    # ex) [4, 3, 2, 1, 0]
    stack = []
    for i in range(len(prices)):
            while stack and prices[stack[-1]] > prices[i]:
            # 가격이 떨어진다면 원하는 가격이 
                index = stack.pop()
                answer[index] = i - index
            stack.append(i)
            # stack에 기간을 찾을 index를 저장한다
            # 마지막으로 저장된 index를 확인해서
            # i번째 값이 이 값보다 작다면 가격이 떨어짐을 의미한다
            # 그러면 마지막 index를 빼내고 answer에 그 사이의 기간을 저장한다
            # while문으로 설정되어 있기 때문에
            # stack을 다 비우거나, 큰 수가 없어 다음 i를 확인해야 할 때까지 반복한다
            # 만약 for문이 끝날 때까지 특정 index의 값이 떨어지지 않았다면
            # 기간은 len(prices) - index가 된다
            # 때문에 초기에 1씩 감소하는 list를 만들었다
    return answer