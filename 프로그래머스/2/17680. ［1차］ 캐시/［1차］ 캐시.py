def solution(cacheSize, cities):
# LRU : 가장 오랫동안 참조되지 않은 페이지를 교체한다
# cache hit : cache 안에 원하는 도시 이름이 있는 경우
# cache miss : cache 안에 원하는 도시 이름이 없는 경우
    time = 0
    cache = []
    if cacheSize == 0:
        return 5 * len(cities)
        # cachesize가 0이면 무조건 cache miss이므로 5 * 도시이름 갯수를 반환
    for i in cities:
        i = i.lower() # 대소문자 구분이 없으므로
        if i in cache:
            cache.remove(i)
            cache.append(i)
            time += 1
            # cache hit인 경우 (+1)
            # cache에서 뺀 뒤에 맨 뒤에 넣어줌으로써,
            # 가장 최근에 참조되었다는 마킹을 한다
            # append를 하면 가장 오래된 요소는 맨 앞에 있을 것이므로
        else:
            if len(cache) == cacheSize:
                cache.pop(0)
            cache.append(i)
            time += 5
            # cache miss인 경우 (+5)
            # 만약에 cache가 다 찼다면
            # 가장 오랫동안 참조되지 않은 cache[0]를 꺼낸다
            # cache hit인 경우는 해당 요소를 꺼낼 것이므로 cache가 다 차있어도 상관 없음
    return time