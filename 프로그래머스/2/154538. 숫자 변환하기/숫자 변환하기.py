def solution(x, y, n):
    yx = [(y,0)] # (연산을 적용한 계산 결과, 연산 횟수)
    while True:
        temp = []
        for i, j in yx:
            if i == x: # 목표값이 생겼다면 바로 최솟값을 반환
                return max(yx, key = lambda x:x[1])[1]
            if i % 3 == 0: # 3으로 나눌 수 있으면 나눈 값을 추가하고 연산 횟수 + 1
                temp.append((i//3,j+1))
            if i % 2 == 0: # 2로 나눌 수 있으면 나눈 값을 추가하고 연산 횟수 + 1
                temp.append((i//2,j+1))
            if i - n >= x: # n을 뺐을 때 x 이상이라면 뺀 값을 추가하고 연산 횟수 + 1
                temp.append((i-n,j+1))
        if temp: # temp에 값이 추가 되었다면
            yx = temp
            # yx에 모든 중간 결과를 업데이트한다
            # 그냥 추가한다면 그 전 결과가 남아있게 되므로 temp를 활용한다
        else: # temp가 비어있다면 더 업데이트할 값이 없다는 뜻
            return -1 # 이 경우 y에 연산을 취해 x를 만들 수 없다