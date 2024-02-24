from collections import deque

def solution(begin, target, words):
    # bfs를 이용한다
    if target not in words:
        return 0 # target word가 존재하지 않으면 바로 0을 반환
    else:
        n = len(words)
        visited, count = [0] * n, [0] * n
        queue = deque([])
        for i in range(n):
            diff = 0
            for j in range(len(begin)):
                if begin[j] != words[i][j]:
                    diff += 1
            if diff < 2:
                queue.append((i, words[i]))
                visited[i] = 1
                count[i] = 1
                # begin과 words의 단어들을 한 글자씩 비교한 뒤
                # 변환이 가능하다면 queue에 추가하고
                # 방문 여부와 단계 횟수까지 업데이트 한다
                # queue에 begin을 넣은 채로 시작하지 않고
                # 이 과정을 한 번 수행하는 이유는 count 때문이다
                # 아래 코드를 확인하면
                # count[i] = count[index] + 1를 발견할 수 있는데,
                # 이렇듯 count 값을 증가시키려면 words에서의 index가 필요하지만
                # begin은 words 내부에 없기 때문에 오류가 발생한다
                # 때문에 이런 식으로 코드를 작성했다
        while queue:
            index, word = queue.popleft()
            for i in range(n):
                if visited[i] == 0:
                    diff = 0
                    for j in range(len(word)):
                        if word[j] != words[i][j]:
                            diff += 1
                    if diff < 2:
                        queue.append((i, words[i]))
                        visited[i] = 1
                        count[i] = count[index] + 1
                        # 앞서 말한 내용과 거의 같다
        if count[words.index(target)] == 0:
            return 0
        else:
            return count[words.index(target)]
            # 이 문제의 경우 while문 내에서 target count에 접근하면 안된다
            # queue에서 값을 하나 꺼낼 때마다 words list를 한 번 순회하기 때문에
            # target word의 count 값이 업데이트 되지 않았음에도 그 값을 반환할 수 있다
            # 때문에 while문이 종료된 후에 count 값을 확인한다