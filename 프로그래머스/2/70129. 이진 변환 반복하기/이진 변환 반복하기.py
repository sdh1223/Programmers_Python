def solution(s):
    answer = [0, 0]
    while True:
        one = s.count('1')
        zero = s.count('0')
        answer[0] += 1 # 이진 변환 횟수
        answer[1] += zero # 제거된 0의 갯수
        s = bin(one)[2:] # 이진 변환
        if s == '1':
            break
    return answer