def solution(N, number):
    s = [set() for x in range(8)]
    print(s)
    for i, x in enumerate(s, start=1):
        x.add(int(str(N) * i))  # 5, 55, 555, 5555 를 담고있음
    print(s)
    for i in range(len(s)):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i - j - 1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)
        print(s[i])
        print(s)
        if number in s[i]:
            answer = i + 1
            break
    else:
        answer = -1

    return answer


N = 5
number = 12

print(solution(N, number))
