from itertools import permutations

def split(index, operator, expression):
# operator : 연산자 3개가 들어있는 tuple
# 예시 : ('*', '+', '-')
# index : operator에서 연산자를 꺼내기 위해 사용
# operator[index]로 연산자를 꺼낸다
# expression : 숫자와 수식이 적혀 있는 문자열
# 예시 : "100-200*300-500+20"
    expression = expression.split(operator[index])
    # operator[index]을 기준으로 문자열을 쪼개 list로 만들어준다
    # index의 초기값은 0이고, 재귀를 사용할 예정이기 때문에 이런 식으로 설정했다
    for i in range(len(expression)):
        if expression[i].isdigit(): # 숫자라면 그냥 놔둔다
            continue
        else: # 연산자가 섞여있다면
            expression[i] = split(index+1, operator, expression[i])
            # 해당 문자열에 대해 split을 다시 시행한다
            # index를 1 증가시켜서 다음 연산자를 사용할 수 있도록 한다
    result = str(eval(operator[index].join(expression)))
    # 이 시점에는 연산자가 모두 사라지고 숫자만이 남아있을 것이다
    # eval은 문자열 식을 입력받아 결과를 계산해주는 함수이다
    # 다만 재귀를 이용하기 때문에 재귀문을 시행하는 도중에 정수 값이 생성되면 오류가 발생한다
    # 때문에 다시 문자열로 바꿔줌
    return result

def solution(expression):
    answer = []
    operator = ['*', '+', '-']
    for op in permutations(operator, 3): # 모든 operator들의 조합을 반환
        answer.append(abs(int(split(0, op, expression))))
        # 문자열 형태로 반환했기 때문에 다시 정수로 바꿔주고,
        # 다시 절댓값을 구해서 answer에 추가해준다
    return max(answer) # 최댓값을 반환