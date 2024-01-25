def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)
    # 뒷 큰수가 없는 경우를 위해 -1로 초기화
    for i in range(len(numbers)):
            while stack and numbers[stack[-1]] < numbers[i]:
                answer[stack.pop()] = numbers[i]
            stack.append(i)
            # stack에 뒷 큰수를 찾을 index를 저장한다
            # 마지막으로 저장된 index를 확인해서
            # i번째 값이 이 값보다 크다면 이것이 뒷 큰수가 된다
            # 그러면 마지막 index를 빼내고 answer에 뒷 큰수를 저장한다
            # while문으로 설정되어 있기 때문에
            # stack을 다 비우거나, 큰 수가 없어 다음 i를 확인해야 할 때까지 반복한다
    return answer