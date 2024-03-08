from collections import deque

def solution(gems):
    # 투 포인터를 이용한다
    minimum = [1, 100001]
    my_gems = {}
    # 리스트를 이용하면 효율성 테스트를 통과할 수 없으니 딕셔너리를 이용해야 한다
    g_kind = len(set(gems)) # 전체 보석 종류 갯수
    end = 0 # end 값은 for문 밖에서 초기화한다
    for start in range(len(gems)):
        while len(my_gems) < g_kind and end < len(gems):
        # end가 범위를 벗어나거나 딕셔너리의 길이가 전체 보석 종류 갯수와 같아지면 종료
            my_gems[gems[end]] = my_gems.get(gems[end], 0) + 1
            # 딕셔너리에는 각 보석의 갯수를 저장한다
            # 투 포인터이기 때문에 후에 start 값을 증가시켜야 하는데,
            # 이때 start에 해당하는 값도 없애줘야 한다
            # set으로 퉁쳐버리면 이를 확인하기 곤란하기 때문에 딕셔너리로 값을 센다
            # 딕셔너리에서 해당 보석의 갯수 값을 꺼낸 뒤 1을 증가시켜서 다시 저장한다
            # 만약 보석이 존재하지 않는다면 0을 반환해서 1을 다시 삽입해준다
            end += 1 # end 증가
        if len(my_gems) == g_kind:
        # 만약 딕셔너리의 길이가 전체 보석 종류 갯수와 같아져 종료되었다면
            if end - (start + 1) < minimum[1] - minimum[0]:
                minimum = [start+1, end]
                # 더 작은 구간의 길이로 업데이트한다
                # 딕셔너리의 길이가 전체 보석 종류 갯수와 같아졌다는 것은
                # 각 보석이 적어도 하나씩 딕셔너리에 포함되었음을 의미한다
        if my_gems[gems[start]] == 1:
            del my_gems[gems[start]]
        else:
            my_gems[gems[start]] -= 1
            # start 값을 딕셔너리에서 제거해준다
            # 2개 이상 있다면 값을 1 감소시키고, 1개 있다면 딕셔너리에서 제거한다
    return minimum