inputs = list(map(int,input().split()))
n , k = inputs[0], inputs[1]
allScores = list(map(int,input().split()))
count = 0
for i in range(n):
    if allScores[i] >= allScores[k-1] and allScores[i]>0:
        count += 1
print(count)