#201901881_컴퓨터전자시스템공학부_설희관
total = 0
scoreList = [70, 55, 75, 95, 85, 90, 60, 85, 70, 90]

for i in scoreList:
    total = total + i

avg = total/len(scoreList)

print("원본 데이터")
print(scoreList)

print("total: %d" %total)
print("average: %.2f" %avg)
