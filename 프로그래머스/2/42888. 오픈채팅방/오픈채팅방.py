def solution(record):
    answer = []
    dic = {}
    for i in record:
        i = i.split(' ')
        if i[0] == 'Enter':
            answer.append(i[1] + "님이 들어왔습니다.")
            dic[i[1]] = i[2]
        elif i[0] == 'Leave':
            answer.append(i[1] + "님이 나갔습니다.")
        else:
            dic[i[1]] = i[2]
    for i in range(len(answer)):
        ID = answer[i].split('님')[0]
        answer[i] = answer[i].replace(ID, dic[ID])
    return answer