def solution(skill, skill_trees):
    answer = 0

    for this_skill in skill_trees:
        stack_str = ""
        for s in this_skill:
            if s in skill:
                stack_str += s
        if stack_str == skill[:len(stack_str)]:
            answer += 1

    return answer


if __name__ == "__main__":
    print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
