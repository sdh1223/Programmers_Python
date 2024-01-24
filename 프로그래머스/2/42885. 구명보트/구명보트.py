def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    stack = [people[0]]
    for i in range(1, len(people)):
        if stack: # stack이 비어있으면 pop 시에 error가 생김
            if stack[-1] + people[i] > limit:
                stack.append(people[i])
            else:
                stack.pop()
                answer += 1
        else:
            stack.append(people[i])
    answer += len(stack)
    return answer