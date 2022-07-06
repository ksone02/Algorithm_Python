t = int(input())
for _ in range(t):
    n, location = map(int, input().split(" "))
    priorities = list(map(int, input().split(" ")))
    answer = 0

    while len(priorities) > 0:
        shift = priorities.pop(0)
        if len(list(filter(lambda u: u > shift , priorities))) > 0:
            priorities.append(shift)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
        else:
            answer += 1
            if location == 0:
                break
            else:
                location -= 1

    print(answer)