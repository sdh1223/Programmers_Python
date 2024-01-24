def solution(s):
    stack = []
    for i in s:
        if not stack: # stack이 비어 있으면 문자 넣기
            stack.append(i)
        elif i == stack[-1]: # 같은 문자 만나면 제거
            stack.pop()
        else: # stack에 문자가 있는데 같은 문자가 아니면 문자 넣기
            stack.append(i)
    if stack: # stack에 문자가 남아 있으면 짝짓기 실패
        answer = 0
    else: # stack이 모두 비워지면 짝짓기 성공
        answer = 1
    return answer