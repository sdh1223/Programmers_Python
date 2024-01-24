from collections import Counter

def solution(want, number, discount):
    answer = 0
    dic = {}
    for w, n in zip(want, number):
        dic[w] = n # dictionary를 만들어 입력값 정리
    for i in range(len(discount)-9):
        count = Counter(discount[i:i+10])
        # Counter는 dictionary 형태로 원소 개수를 반환한다
        # 때문에 앞서 만든 dic과 같은지 확인하면 됨
        if count == dic:
            answer += 1
    return answer