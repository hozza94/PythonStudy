def solution(numbers, k):
    answer = ''
    npass = 0

    for i in range(len(numbers) - 1):

        if (k - npass) == 0:
            if i == len(numbers) - 1:
                answer += numbers[i:]
            break
        now = int(numbers[i])
        next = int(numbers[i + 1])
        if next > now:
            npass += 1
        else:
            k -= npass
            npass = 0
            answer += numbers[i]

    return answer


numbers = "1231234"
k = 3
print(solution(numbers, k))
