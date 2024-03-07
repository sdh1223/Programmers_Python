from itertools import permutations

def check(user, ban):
    if len(user) != len(ban): # 글자 수 체크
        return False
    else:
        for i, j in zip(user, ban):
        # zip은 ("frodo", "fr*d*")의 형태로 묶어줌
        # i, j = "f", "f"와 같이 한 글자씩 확인하게 된다
            if j == '*':
                continue
            if i != j:
                return False
        return True # *을 제외한 부분이 모두 같으면 True
        
def solution(user_id, banned_id):
    answer = []
    for i in permutations(user_id, len(banned_id)):
    # user_id에서 banned_id 길이만큼의 수열 조합을 모두 생성한다
        count = 0
        for a, b in zip(i, banned_id):
        # a, b = "frodo", "fr*d*"의 형태가 된다
            if check(a, b):
                count += 1
        if count == len(banned_id):
        # check는 아이디 하나씩을 확인하기 때문에
        # count가 banned_id 길이와 같다는 것은 같은 아이디 목록을 하나 찾은 것을 의미
            if set(i) not in answer:
                answer.append(set(i)) # 중복 제거를 위해 set을 활용해서 추가
    return len(answer)