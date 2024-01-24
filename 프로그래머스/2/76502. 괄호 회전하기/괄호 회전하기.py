def solution(s):
    answer = 0
    l = len(s)
    s = s * 2 # 문자열을 두 배 늘려서
    for i in range(l):
        ss = s[i:i+l] # 원하는 부분을 잘라 활용
        stack = []
        for j in ss:
            if j == '[' or j == '{' or j == '(':
                stack.append(j)
            elif j == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(j)
                    break
            elif j == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(j)
                    break
            elif j == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(j)
                    break
        if not stack:
            answer += 1
    return answer