def solution(n, lost, reserve):
    uniform = [1] * (n + 2)
    for i in reserve:  # 체육복을 더 가져온 사람 O(n)
        uniform[i] += 1

    for i in lost:  # 체육복을 잃어버린 사람 O(n)
        uniform[i] -= 1

    for i in range(1, n + 1):
        if uniform[i - 1] == 0 and uniform[i] == 2:
            uniform[i - 1: i + 1] = [1, 1]
        elif uniform[i] == 2 and uniform[i + 1] == 0:
            uniform[i:i + 2] = [1, 1]

    return len([x for x in uniform[1:-1] if x > 0])

# n은 매우 크지만 reverse는 작을떼 효율적
def solution2(n, lost, reserve):
    s = set(lost) & set(reserve)  # 교집합
    l = set(lost) - s  # 도난당했으며, 여벌의 체육복이 없는 학생
    r = set(reserve) - s  # 여벌의 체육복을 가져와서 도난 당하지 않은 학생

    for x in sorted(r):
        if x - 1 in l:
            l.remove(x - 1)
        elif x + 1 in l:
            l.remove(x + 1)

    return n - len(l)


n = 5
lost = [2, 4]
reverse = [1, 3, 5]

solution(n, lost, reverse)
solution2(n, lost, reverse)
