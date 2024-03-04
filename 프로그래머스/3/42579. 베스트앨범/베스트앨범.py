def solution(genres, plays):
    answer = []
    dic1, dic2 = {}, {}
    for i in range(len(genres)):
        dic1[genres[i]] = dic1.get(genres[i], 0) + plays[i]
        dic2[genres[i]] = dic2.get(genres[i], []) + [(i, plays[i])]
        # dictionary 두 개를 준비해
        # dic1에는 장르 별 재생 횟수의 총합을,
        # dic2에는 장르 별 (인덱스, 재생횟수)를 모두 담은 list를 저장한다
        # dic1 = {'classic': 1450, 'pop': 3100}
        # dic2 = {'classic': [(0, 500), (2, 150), (3, 800)],
        # 'pop': [(1, 600), (4, 2500)]}
    dic1 = sorted(dic1.items(), key=lambda x: x[1], reverse=True)
    # dic1만 총합이 가장 큰 순서부터 오도록 정렬한다
    # dic1.items()는 (key, value) 쌍을 반환하므로 x[0]가 key, x[1]이 value가 된다
    # 다만 정렬된 결과는 (key, value) 쌍이 담긴 list가 됨에 주의
    for genre, _ in dic1:
    # dic1에서 key 값, 즉 장르 이름만을 꺼낸다
        play = dic2[genre]
        # 해당 장르 이름을 가지고 dic2에서 (인덱스, 재생횟수)가 담긴 list를 찾는다
        # dic1은 정렬되어 있으므로 많이 재생된 장르부터 찾을 수 있게 됨
        play.sort(key=lambda x: (x[1], -x[0]), reverse=True)
        # 재생횟수가 얼마나 큰 지를 1순위,
        # 인덱스가 얼마나 작은 지를 2순위로 하여 정렬한다
        if len(play) >= 2:
            n = 2
        else:
            n = len(play)
        # 정렬이 완료되었다면 list에서 원소 2개의 인덱스를 꺼낼 것이다
        # 다만 list 자체의 길이가 2보다 작을 수 있으므로, 이를 고려하여 n 값을 정한다
        for i in range(n):
            answer.append(play[i][0])
            # n만큼 인덱스를 추가
    return answer