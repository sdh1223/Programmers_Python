def solution(dirs):
    visit = set()
    # ((0,0),(-1,0))와 ((-1,0),(0,0))은 같은 길이므로
    # 이러한 중복을 제거하기 위해 set을 사용
    x = 0
    y = 0
    for i in dirs:
        if i == 'U' and y < 5:
            visit.add(((x,y), (x,y+1)))
            y += 1
        elif i == 'D' and y > -5:
            visit.add(((x,y-1), (x,y)))
            y -= 1
        elif i == 'R' and x < 5:
            visit.add(((x,y), (x+1,y)))
            x += 1
        elif i == 'L' and x > -5:
            visit.add(((x-1,y), (x,y)))
            x -= 1
    return len(visit)