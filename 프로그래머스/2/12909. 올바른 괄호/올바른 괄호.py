def solution(s):
    answer = True
    p = list(s)
    stack = []
    for i in range(len(p)):
        if p[i] == '(':
            stack.append(p[i])
        else:
            if stack:
                stack.pop()
            else:
                answer = False
    if stack:
        answer = False
    return answer