def solution(files):
    answer = []
    for i in files:
        head, number, tail = '', '', '' # 빈 문자열 선언
        tail_start = False # number 전후로 head와 tail을 구분한다
        for j in range(len(i)):
            if i[j].isdigit(): # number인지 판별
                number += i[j]
                tail_start = True # number가 나왔다면 그 후의 문자열은 tail이 됨
            elif not tail_start: # 아직 number가 나오지 않은 경우는 head로 판단
                head += i[j]
            else: # number가 나온 뒤 tail_start가 된 경우 => tail
                tail = i[j:] # 뒷부분을 전부 추가한 뒤 break
                break
        answer.append((head, number, tail)) # 세가지를 모두 묶어 tuple로 저장
    answer.sort(key=lambda x: (x[0].lower(), int(x[1])))
    # 이렇게 작성하면 head를 1순위, number를 2순위로 해서 정렬할 수 있음
    return [''.join(i) for i in answer] # 다시 이어서 반환