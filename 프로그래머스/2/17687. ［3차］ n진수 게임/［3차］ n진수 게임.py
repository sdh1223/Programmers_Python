def convert(num, base):
        temp = "0123456789ABCDEF"
        q, r = divmod(num, base)
        if q == 0:
            return temp[r]
        else:
            return convert(q, base) + temp[r]

def solution(n, t, m, p):
    # n : 진법 / t : 준비할 정답 개수 / m : 총인원 / p : 본인 순서
    answer = ''
    answer_sheet = ''
    for i in range(m*t):
    # 총인원 수 * 정답 개수만큼의 수를 미리 저장해두면
    # 차례에 맞는 숫자를 뽑아서 쓰면 된다
        answer_sheet += str(convert(i, n))
        # 변환해서 string으로 계속 붙임
    while len(answer) < t: # 정답 개수만큼 뽑을 때까지
        answer += answer_sheet[p-1] # 본인 순서에 해당하는 정답을 붙인다
        p += m # 총인원 수를 더해주면 본인 차례가 다시 돌아옴
    return answer