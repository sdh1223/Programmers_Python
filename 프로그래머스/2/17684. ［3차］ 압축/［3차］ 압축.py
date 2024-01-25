def solution(msg):
    answer = []
    dic = []
    while msg:
        exist = False
        for i in reversed(range(len(dic))):
        # 새로 추가된 긴 문자열은 뒤에 있을 것이므로 뒤부터 탐색
            if dic[i] == msg[0:len(dic[i])]:
            # msg의 앞에서부터 문자열의 길이만큼 슬라이스하여
            # w가 존재하는지 확인
                answer.append(i+27)
                # 사전의 색인 번호 추가
                dic.append(msg[0:len(dic[i])+1])
                # w+c에 해당하는 단어를 사전에 등록
                msg = msg[len(dic[i]):len(msg)]
                # msg에서 w를 제거
                exist = True
                break
        if not exist:
        # w가 존재하지 않는 경우
        # A, B, C, D, ...와 같은 길이가 1인 단어로 w를 설정
            answer.append(ord(msg[0])-64)
            # 아스키 코드를 활용
            # 64를 빼면 1부터 시작하게 됨
            dic.append(msg[0:2])
            # w+c에 해당하는 단어를 사전에 등록
            msg = msg[1:len(msg)]
            # msg에서 w를 제거
    return answer