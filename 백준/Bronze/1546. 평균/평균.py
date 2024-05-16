n = int(input())
grade = list(map(int, input().split()))
max_score = max(grade)

score = []
for i in grade:
    score.append(i/max_score*100)

score_avg = sum(score)/n
print(score_avg)