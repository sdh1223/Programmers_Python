from collections import Counter

def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    s1 = []
    s2 = []
    for i in range(len(str1)-1):
        s =''.join(str1[i:i+2])
        if s.isalpha():
            s1.append(s)
    for i in range(len(str2)-1):
        s =''.join(str2[i:i+2])
        if s.isalpha():
            s2.append(s)
            # 문자 두 개씩 끊어서 알파벳으로 이루어진 것만 추가
            # 'a1', 'm*' 이런 거 거름
    counter1 = Counter(s1)
    counter2 = Counter(s2)
    intersection = list((counter1 & counter2).elements())
    union = list((counter1 | counter2).elements())
    # 합집합과 교집합을 구할 때 보통 set을 이용하지만,
    # 이 문제에서는 중복값을 허용해야 하기 때문에 set은 이용할 수 없다
    # 때문에 counter를 이용한다
    if not s1 and not s2:
        answer = 65536
    else:
        answer = int(len(intersection) / len(union) * 65536)    
    return answer