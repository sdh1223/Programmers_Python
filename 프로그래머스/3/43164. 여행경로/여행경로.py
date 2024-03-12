def solution(tickets):
    answer = []
    visited = [0] * len(tickets)
    def dfs(departure, path):
    # tickets를 순환하면서 티켓 자체에 방문 표시를 한다
    # dfs 실행 종료 후 path가 하나의 경로가 된다
        if len(path) == len(tickets) + 1:
            answer.append(path)
            return
        # path의 길이가 ticket의 길이 + 1일 경우에만 해당 경로를 answer에 추가하고 dfs를 종료한다
        # 모든 티켓을 사용하지 못하는 경로 또한 존재하기 때문
        # 길이 조건을 만족할 경우에만 올바른 경로가 된다 (길이가 충족되지 않으면 티켓을 모두 사용하지 못했음을 의미)
        for index, airport in enumerate(tickets):
            if airport[0] == departure and visited[index] == 0:
            # 출발 도시가 일치하고 아직 사용하지 않은 티켓일 경우에만
                visited[index] = 1
                # 방문 표시를 하고
                dfs(airport[1], path + [airport[1]])
                # 도착 도시를 출발 도시로 하여 다시 dfs를 실행한다
                # path에도 도착 도시를 추가하여 경로를 업데이트 한다
                visited[index] = 0
                # 재귀 종료 후에는 방문 표시를 없애주어야 한다
                # 그래야 다른 경로를 탐색할 때 활용할 수 있음
    dfs('ICN', ['ICN']) # 출발 도시는 ICN이고, 경로 또한 ICN으로 시작해야 한다
    answer.sort() # 알파벳 순서가 앞서는 경로를 반환하기 위해 정렬
    return answer[0] # 맨 앞 원소 반환