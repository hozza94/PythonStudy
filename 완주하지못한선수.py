### linear time algorithm
def solution(participant, completion):
    d = {}

    # list 각각에 대해서 key로 사전에 접근, update, 삽입 / hash로 구성되어있기 때문에 O(n)
    for x in participant:
        d[x] = d.get(x, 0) + 1  # d.get( key, '디폴드 값')

    # list 길이에 비례해 접근, update / hash로 구성되어있기 때문에 O(n-1)
    for x in completion:
        d[x] -= 1

    # 사전에 있는 모든 원소를 꺼내서 검사해야 하기 때문에 O(n)
    dnf = [k for k, v in d.items() if v > 0]

    answer = dnf[0]

    return answer


participant = []
completion = []
solution(participant, completion)
