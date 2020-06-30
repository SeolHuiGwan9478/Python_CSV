#201901881_컴퓨터전자시스템공학부_설희관
date_count = 0
snail_distance = 0
while(True):
    date_count += 1
    snail_distance += 3
    if snail_distance == 30:
        break
    else:
        snail_distance -= 2

print("달팽이는 %d일만에 %d미터를 올라간다." %(date_count, snail_distance))
