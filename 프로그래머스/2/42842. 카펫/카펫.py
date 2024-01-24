def solution(brown, yellow):
    for i in range(1, int(yellow**(1/2))+1):
        if yellow % i == 0:
            x, y = i, yellow/i # yellow의 가로, 세로 길이 조합 찾기
            if (x+y)*2+4 == brown: # 현재 x,y로 brown 격자 수 생성이 가능한지 확인
                return [max(x,y)+2, min(x,y)+2] # 전체 카펫의 가로 세로 길이 반환