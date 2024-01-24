def solution(n, words):
    answer = [0,0]
    stack = [words[0]] # stack에 첫번째 단어 넣고 시작
    for i in range(1, len(words)):
        if stack[-1][-1] == words[i][0] and words[i] not in stack:
        # 끝말잇기가 성립하고 한 번 썼던 단어가 아닐 때
            stack.append(words[i])
        else:
            answer[0] = i % n + 1 # 번호 : 8 % 3 + 1 = 3
            answer[1] = i // n + 1 # 차례 : 8 // 3 + 1 = 3
            break
    return answer