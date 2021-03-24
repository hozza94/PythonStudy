def solution(numbers):
    numbers = [str(x) for x in numbers]
    print(numbers)

    numbers.sort(key=lambda x: (x * 4)[:4], reverse=True)

    for ch in numbers:
        ch1 = (ch * 4)[:4]
        print(ch1)

    # numbers = sorted([str(x) for x in numbers],
    #                  key=lambda x: (x*4)[:4], reverse=True)
    if numbers[0] == '0':
        answer = '0'
    else:
        answer = ''.join(numbers)

    return answer


numbers = [3, 30, 34, 90, 9]

solution(numbers)
