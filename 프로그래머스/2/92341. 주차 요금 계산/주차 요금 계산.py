import math

def solution(fees, records):
    dic = {}
    for i in records:
        record = i.split(' ')
        # 공백으로 구분해서 시간, 차량번호, IN/OUT의 list를 생성
        time = record[0].split(':')
        minute = int(time[0]) * 60 + int(time[1])
        # 입차, 출차 시간을 모두 분 단위로 변환
        p_time = dic.get(int(record[1]), 0)
        # 차량번호를 key로 갖는 value를 반환
        # 만약 해당 key가 없다면 0을 반환 (초기값을 0으로 하기 위해)
        if record[2] == 'IN':
            dic[int(record[1])] = p_time - minute
            # IN이라면 분 단위 시간을 빼준다
        else:
            dic[int(record[1])] = p_time + minute
            # OUT이라면 더해줌
    for i in dic.items():
        if i[1] <= 0:
            dic[i[0]] += 1439
            # 23:59에 출차하는 경우
            # value 값이 음수로 남아있다면 23 * 60 + 59를 더해준다
    total_fees = sorted(dic.items())
    total_fees = list(i[1] for i in total_fees)
    # list를 반환해야 하므로 dictionary를 정렬해서 value 값만 넣은 list를 만듬
    # 현재는 누적 주차 시간 값이 저장되어 있다
    for i in range(len(total_fees)):
        if total_fees[i] <= fees[0]:
            total_fees[i] = fees[1]
            # 기본 시간보다 작다면 기본 요금을 청구
        else:
            total_fees[i] = fees[1] + math.ceil((total_fees[i]-fees[0])/fees[2]) * fees[3]
            # 아니라면 요금을 계산
    return total_fees