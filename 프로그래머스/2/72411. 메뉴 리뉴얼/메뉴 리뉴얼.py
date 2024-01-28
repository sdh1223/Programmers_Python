from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for n in course:
    # 코스 개수마다의 최댓값을 바로 구하면 연산 과정을 줄일 수 있다
        combi = []
        for i in orders:
            for c in combinations(i, n):
                combi.append(''.join(sorted(c)))
                # 빈 리스트를 생성하여 orders 원소들의 모든 조합을 추가한다
                # 알파벳 순서가 다를 수도 있으므로 정렬
        combi_count = Counter(combi).most_common()
        # most_common()은 가장 빈도수가 큰 순서부터 먼저 오도록 정렬해서 반환해준다
        answer += [menu for menu, count in combi_count if count > 1 and count == combi_count[0][1]]
        # 최소 2명 이상의 손님으로부터 주문되었어야 하므로 count > 1이어야 하고
        # count 값이 같은 메뉴가 있는지도 확인한다
        # 사실 count가 가장 큰 값을 확인하려면 0번 index를 확인해도 되지만
        # 이 경우 dictionary가 비어 있으면 index out of range 오류가 발생한다
        # 되도록이면 0번 index를 확인하는 코드는 작성하지 말자
        # 맨날 여기서 오류남
    return sorted(answer) # 마지막으로 한번 더 정렬 (문제에서 오름차순 요구)