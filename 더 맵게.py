scoville = [1, 2, 3, 9, 10, 12]
k = 7

import heapq


def solution(scoville, k):
    answer = 0
    # scoville.sort()
    #
    # if scoville[0] > k:
    #     return answer
    #
    # while len(scoville) > 1:
    #     small = scoville.pop(0)
    #     ssmall = scoville.pop(0)
    #     newscoville = small + (ssmall * 2)

    heapq.heapify(scoville)
    while True:
        min1 = heapq.heappop(scoville)
        if min1 >= k:
            break
        elif len(scoville) == 0:
            answer = -1
            break
        min2 = heapq.heappop(scoville)
        new_scoville = min1 + 2 * min2
        heapq.heappush(scoville, new_scoville)
        answer += 1

    return answer


print(solution(scoville, k))
