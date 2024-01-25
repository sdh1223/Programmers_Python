from collections import Counter

def solution(s):
    answer = []
    s = s.replace('{', '') # s에서 { 제거
    s = s.replace('}', '') # s에서 } 제거
    s_list = list(map(int, s.split(','))) # ,로 구분해서 int로 변환한 뒤 list에 저장
    count = Counter(s_list) # 각 요소를 count
    sorted_count = sorted(count.items(), key=lambda item:item[1], reverse=True)
    # value 값에 따라 큰 순서대로 정렬
    # 앞쪽에 있는 숫자일수록 많이 등장하게 됨
    for i in sorted_count:
        answer.append(i[0])
    return answer