def solution(cpr):
    answer = []
    basic_order = ["check", "call", "pressure", "respiration", "repeat"]
    for action in cpr:
        for i in range(len(basic_order)):
            if action == basic_order[i]:
                answer.append(i+1)
    return answer


# cpr	result
# ["call", "respiration", "repeat", "check", "pressure"]	[2, 4, 5, 1, 3]
# ["respiration", "repeat", "check", "pressure", "call"]	[4, 5, 1, 3, 2]

