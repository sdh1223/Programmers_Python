from collections import Counter

def solution(clothes):
    answer = 1
    count = Counter([type for clothe, type in clothes])
    # 의상의 종류만을 꺼내 갯수를 세서 곱해주는 것으로 경우의 수를 센다
    for i in count.values():
        answer *= i+1
        # 1을 더해주는 이유는 입지 않는 경우를 포함하기 위해서
    answer -= 1 # 아무것도 입지 않는 경우를 제거하기 위해 1을 뺀다
    return answer