for _ in range(int(input())):
    n = int(input())
    problems = input()

    res = 0
    solved = set()
    for problem in problems:
        if problem in solved:
            res += 1
        else:
            res += 2
            solved.add(problem)
    
    print(res)