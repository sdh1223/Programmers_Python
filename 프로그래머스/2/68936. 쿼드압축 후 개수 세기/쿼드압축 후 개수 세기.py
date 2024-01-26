def solution(arr):
    answer = [0,0] # 0의 개수, 1의 개수를 저장할 list
    length = len(arr) # arr의 길이
    def compression(a, b, l): # solution 함수 안에 작성함으로써 answer을 활용할 수 있게 됨
        start = arr[a][b] # 시작 지점 index 안에 있는 값
        for i in range(a, a+l):
            for j in range(b, b+l):
                if arr[i][j] != start:
                # length 내에 값들이 start 지점의 값과 같은지 확인한다
                # 모두 같아야지만 압축을 할 수 있기 때문에,
                # 하나라도 같지 않다면 재귀 함수로 해당 부분을 다시 4등분한다
                    l = l // 2
                    compression(a, b, l)
                    compression(a, b+l, l)
                    compression(a+l, b, l)
                    compression(a+l, b+l, l)
                    return # 아무것도 반환하지 않음
        answer[start] += 1
        # 이곳에 도달하면 압축이 성공했음을 의미하므로 한 번만 갯수를 세면 된다
        # start는 시작 지점 index 안에 있는 값이므로 0 또는 1이다
        # 때문에 answer[0] 또는 answer[1]이 되므로 0인지 1인지 갯수를 셀 수 있게 됨
    compression(0, 0, length) # 함수 실행
    return answer