from itertools import product

def solution(word):
    words = []
    for i in range(1, 6):
        for j in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            words.append(''.join(list(j)))
            # product는 list 안의 요소를 활용해 순열을 만드는데,
            # 이때 요소 하나를 여러번 사용하는 것이 가능하다
            # 모든 중복 순열을 구해 words에 추가
    words.sort() # 정렬하면 문제에서 원하는 순서대로 바뀜
    return words.index(word) + 1 # 원하는 word의 index를 구해서 1을 더해줌