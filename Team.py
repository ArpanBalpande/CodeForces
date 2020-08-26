n = int(input())
knowsolution = 0
for i in range(n):
    problem = input()
    count = 0
    for p in problem:
        if p == "1":
            count += 1
            if count == 2:
                knowsolution += 1
print(knowsolution)