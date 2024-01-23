def solution(s):
    s = s.lower()
    l = s.split(' ') # ['3people', 'unfollowed', 'me']
    for i in range(len(l)):
        l[i] = l[i].capitalize() # 앞글자만 대문자로 / l을 바꿔야 하므로 무조건 len(l)
    answer = ' '.join(l) # 공백 넣어서 다시 합치기
    return answer