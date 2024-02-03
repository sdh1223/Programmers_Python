def seperation(paren): # 괄호 문자열을 u와 v로 분리하는 과정
    u, v = '', ''
    left, right = 0, 0
    for i, p in enumerate(paren):
        if p == '(':
            left += 1
        else:
            right += 1
        u += p
        if left == right:
            v = paren[i+1:]
            break
    return u, v

def check(paren): # 올바른 괄호 문자열인지 확인하는 과정
    p = list(paren)
    stack = []
    for i in p:
        if i == '(':
            stack.append(p)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True

def reverse(paren): # u가 올바른 괄호 문자열이 아닐 경우 시행하는 4번 과정
    result = ''
    p = list(paren)
    p.pop(0)
    p.pop(-1)
    for i in p:
        if i == '(':
            result += ')'
        else:
            result += '('
    return result
    
def change(paren): # 전체 괄호 변환 과정
    result = ''
    if paren:
        u, v = seperation(paren)
        if check(u):
            result += u
            result += change(v)
            # "문자열 v에 대해 1단계부터 다시 수행합니다."
            # change(v)로 재귀의 형식으로 다시 작성하면 된다
        else:
            temp = '('
            temp += change(v)
            temp += ')'
            temp += reverse(u)
            result += temp
    return result

def solution(p):
    return change(p)