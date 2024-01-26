def solution(sequence, k):
    # 투 포인터를 활용
    answer = []
    interval_sum = 0
    end = 0
    for start in range(len(sequence)): # start는 for문에서 증가시킨다
        while interval_sum < k and end < len(sequence):
        # sum이 k보다 작고 end가 list 범위를 넘지 않을 때
            interval_sum += sequence[end]
            end += 1
            # end를 하나씩 움직이며 sum을 증가시킴
        if interval_sum == k:
            answer.append([start, end-1])
            # sum 값이 k가 되면 answer에 추가한다
            # end 값을 위에서 하나 증가시킨 상태이기 때문에 -1을 해줘야 올바른 값이 됨
        interval_sum -= sequence[start]
        # for문이 한번 종료되면 start가 한 칸 증가할 것이기 때문에
        # sum에서 그 값만큼을 제거해준다
    answer.sort(key=lambda x: (x[1]-x[0], x[0]))
    # 구간의 길이가 짧은 정도(x[1]-x[0])를 1순위로,
    # 구간 시작점이 빠른 정도(x[1])를 2순위로 해서 정렬
    return answer[0] # 제일 앞에 오는 원소를 반환