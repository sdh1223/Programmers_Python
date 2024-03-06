def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    d1 = [0] * len(sticker)
    d2 = [0] * len(sticker)
    d1[0] = sticker[0] # 첫번째 스티커를 고르는 경우
    d1[1] = sticker[0] # 두번째는 못 고르므로 d1[0]과 같다
    d2[0] = 0 # 첫번째 스티커를 고르지 않는 경우
    d2[1] = sticker[1] # 이번에는 두번째를 고를 수 있게 됨
    for i in range(2, len(sticker)-1):
        # 첫번째를 골랐으므로 그 옆에 있는 마지막 스티커는 고를 수 없음
        # 따라서 len(sticker)-1까지
        d1[i] = max(d1[i-2] + sticker[i], d1[i-1])
        # 두 칸 전 스티커 + 현재 스티커를 고르는 경우
        # 한 칸 전 스티커를 고르는 경우
        # 둘 중에 더 큰 경우를 선택한다
    for i in range(2, len(sticker)):
        # 이번에는 고를 수 있으므로 len(sticker)까지
        d2[i] = max(d2[i-2] + sticker[i], d2[i-1])
    answer = max(max(d1), max(d2))
    # d1, d2 중에 더 큰 경우를 고른다
    return answer