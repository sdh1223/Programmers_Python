def solution(data, col, row_begin, row_end):
    answer = 0
    col, row_begin, row_end = col-1, row_begin-1, row_end-1
    # list의 index는 0부터 시작하므로 1을 빼준다
    data.sort(key=lambda x: (x[col], -x[0]))
    # x[col]을 기준으로 오름차순 정렬을 한 뒤,
    # 값이 같다면 x[0]를 기준으로 내림차순 정렬을 한다
    for i in range(row_begin, row_end+1):
        modulo_sum = 0 # sum 초기화해줘야 함
        for j in range(len(data[0])):
            modulo_sum += data[i][j] % (i+1)
        answer ^= modulo_sum
        # sum을 구해서 바로 bitwise xor 연산을 해준다
        # xor 연산은 두 개의 피연산자 중 하나만이 1일 때 1을 반환하므로
        # answer의 초기값은 0으로 설정한다 (1에 1 곱하는 것과 결이 같음)
    return answer