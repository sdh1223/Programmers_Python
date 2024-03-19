from collections import Counter

def solution(picks, minerals):
    # minerals를 5개씩 슬라이싱한 묶음을 여러 개 만든 뒤,
    # 다이아몬드, 철이 많은 순대로 정렬하여 좋은 곡괭이부터 사용하면 된다
    answer = 0
    m_count = [] # 광물 묶음 정보를 저장할 리스트
    pick_num = picks[0] + picks[1] + picks[2] # 전체 곡괭이 갯수
    for i in range(0, len(minerals), 5): # 5씩 증가시키며 순회
        mineral = minerals[i:i+5]
        dic = Counter(mineral)
        m_count.append([dic.get('diamond', 0), dic.get('iron', 0), dic.get('stone', 0)])
        # 다이아몬드, 철, 돌 갯수의 리스트를 생성한 뒤 m_count에 계속해서 추가
        pick_num -= 1
        if pick_num == 0:
            break
        # 왼쪽의 두번째 예시를 보면,
        # 곡괭이 수가 2개, 광물 수가 11개로 마지막 다이아몬드 한 개는 캐지 못하는 것을 알 수 있다
        # 이런 경우를 판단하기 위해 전체 곡괭이 개수를 감소시켜 0이 되면 종료한다
    m_count.sort(key=lambda x: (-x[0], -x[1]))
    # 다이아몬드 수를 1순위, 철 수를 2순위로 하여 정렬
    for mineral in m_count:
        d, i, s = mineral
        if picks[0] != 0: # 다이아몬드 곡괭이가 있는 경우
            picks[0] -= 1
            answer += d + i + s
        elif picks[1] != 0: # 다이아몬드 곡괭이는 다 썼지만 철 곡괭이가 있는 경우
            picks[1] -= 1
            answer += 5 * d + i + s
        else: # 돌 곡괭이만 남은 경우
            picks[2] -= 1
            answer += 25 * d + 5 * i + s
    return answer