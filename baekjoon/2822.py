
scores = []
for i in range(8):
    scores.append((i, int(input())))

scores = sorted(scores, key=lambda d: d[1], reverse=True)[:5]
print(sum(map(lambda x: x[1], scores)))
print(*sorted(map(lambda x: x[0]+1, scores)), sep=" ")