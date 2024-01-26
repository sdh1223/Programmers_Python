def solution(m, n, board):
    answer = 0
    board = [list(x) for x in board]
    # [['C', 'C', 'B', 'D', 'E'], ['A', 'A', 'A', 'D', 'E']]
    # 이러한 형태의 2차원 리스트가 만들어짐
    while True: # while
        twotwo = set() # 블록이 겹치는 부분이 생기기 때문에 set을 사용한다
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == 0:
                    continue
                    # 후에 사라진 블록을 0으로 처리할 것이기 때문에,
                    # 0을 확인하면 건너뛴다
                if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                    twotwo.update([(i,j),(i,j+1),(i+1,j),(i+1,j+1)])
                    # 2*2칸의 블록이 모두 같다면 set에 좌표를 추가한다
        if twotwo:
        # 같은 블록이 없다면 set에 좌표가 추가되지 않을 것이다
        # 때문에 set에 요소가 있다면 좌표가 추가 되었다는 뜻
            answer += len(twotwo) # 지워진 블록의 갯수를 세고
            for i, j in twotwo:
                board[i][j] = 0
                # 사라진 블록을 0으로 처리한다
        else:
            return answer # 없앨 블록이 없다면 실행이 모두 끝났다는 뜻
        while True:
            end = True # 빈 칸 채우기가 다 끝났는지 확인
            for i in range(m-1): # m-1
                for j in range(n):
                    if board[i][j] != 0 and board[i+1][j] == 0:
                    # 현재 블록이 존재하고 바로 아래 블록이 지워져 있다면
                        board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                        # 두 값을 교환해 블록을 아래로 떨어뜨려 빈 공간을 채운다
                        end = False
                        # 블록을 바꿨다면 end가 False가 되고 while문을 다시 실행해서 또 확인
            if end: # end가 True로 남아 있다면 빈 칸 채우기가 모두 완료되었음을 의미
                break