def solution(n,a,b):
    answer = 0 
    while a != b:
        a = (a+1) // 2 # 계속해서 2로 나눈 몫을 계산하되 1을 더한 뒤에 한다
        b = (b+1) // 2 # 그러면 1 1 2 2 3 3 4 4 와 같이 값이 균등해짐
        answer += 1 # a, b가 같아질 때까지, 즉 1 1 이 나와서 만나게 될 때까지 반복
    return answer