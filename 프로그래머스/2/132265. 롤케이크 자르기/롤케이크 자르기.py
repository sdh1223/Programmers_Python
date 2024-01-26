from collections import Counter

def solution(topping):
    answer = 0
    p1 = Counter(topping) # 철수에게 토핑을 몰아주고
    p2 = set() # 동생은 아무 것도 주지 않음
    for i in topping:
        p1[i] -= 1 # 철수의 토핑을 하나씩 빼서
        p2.add(i) # 동생의 케이크로 옮김
        if p1[i] == 0:
            p1.pop(i)
            # 갯수가 0이 된 토핑은 제거
            # value가 0이어도 key가 남아있으므로 len 계산할 때 걸림
        if len(p1) == len(p2):
            answer += 1
    return answer