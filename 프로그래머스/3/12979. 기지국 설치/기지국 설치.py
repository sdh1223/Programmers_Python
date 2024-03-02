def solution(n, stations, w):
    answer = 0
    wave = w * 2 + 1 # 전파가 닿는 범위
    left = 1
    index = 0
    while index <= len(stations):
        if index == len(stations):
            right = n # 맨 마지막 케이스
        else:
            right = stations[index] - w - 1
            new_left = stations[index] + w + 1 # 여기서 계산 안 하면 range 오류 남
        length = right - left + 1 # 현 기지국의 왼쪽, 전 기지국의 오른쪽 거리
        answer += length // wave # 몫만큼 기지국 수 추가
        if length % wave != 0:
            answer += 1
            # 6, 7, 8을 채워도 9가 남기 때문에 이를 위해 기지국이 하나 더 필요함
        left = new_left
        index += 1
    return answer