def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1]) # 마지막 지점 값을 기준으로 작은 수부터 정렬
    camera = -30001 # 가장 최근의 카메라 위치
    for i in routes:
        if camera < i[0]: # 카메라 위치가 처음 지점보다 앞에 있다면
            answer += 1 # 카메라가 필요하므로 마지막 지점에 하나 추가
            camera = i[1] # 가장 최근 카메라 위치를 업데이트
    return answer