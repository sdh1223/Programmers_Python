def solution(phone_book):
    phone_book.sort()
    # 정렬을 하면 앞부분이 같은 수들은 바로 옆에 놓이게 됨
    for i in range(len(phone_book)-1):
        length = len(phone_book[i])
        if phone_book[i][:length] == phone_book[i+1][:length]:
        # 때문에 바로 옆의 수와 같은지만 비교하면 된다
            return False
    return True