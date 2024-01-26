def solution(numbers):
    # 맨 뒤에서부터 판단했을 때 0이 나오기 전까지의 1의 갯수를 센다
    # 3 = 0b10 : 0개
    # 7 = 0b111 : 3개
    # 이 갯수를 n이라고 하면
    # input 숫자에 (1 + 2진수 1을 (n-1)개만큼 반복한 값을 10진수로 변환한 값)
    # 을 더하여 구할 수 있다
    # 7의 경우 3개이므로
    # 7 + (1 + (2 + 1)) = 11이 된다 (2진수 11을 10진수 3으로 변환)
    # 직접 생각한 내용이므로 충분히 다시 할 수 있음
    answer = []
    for i in numbers:
        binomial = bin(i)
        if binomial[-1] == '0':
            f = i + 1
            # 1이 없으면 그냥 1을 더해주면 된다
            # 맨 뒤 '01'이 '10'으로 바뀌므로 비트가 2개 차이 나게 된다
        else:
            count = 0
            index = len(binomial) - 1
            while binomial[index] == '1':
                count += 1
                index -= 1
                # 뒤에서부터 index를 줄여가며 1의 개수를 셈
            if count == 1:
                f = i + 1
                # count = 1 이면 count - 1 = 0이므로
                # '0b' + '1' * 0 = '0b'가 되어서 int 변환이 되지 않는다
                # 때문에 케이스를 따로 작성해서 1만 더해줌
            else:
                f = i + 1 + int('0b' + '1' * (count - 1), 2)
                # 2진수 1을 10진수로 변환해서 더해줌
        answer.append(f)
    return answer