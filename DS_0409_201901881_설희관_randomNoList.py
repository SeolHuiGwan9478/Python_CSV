#201901881_컴퓨터전자시스템공학부_설희관
import random
myList = []
for i in range(10):
    myList.append(random.randint(1,5))

print("리스트 한 번에 출력")
print(myList)
print("리스트의 element를 한 개씩 출력")
for i in myList:
    print(i, end = " ")
print()
print("홀수 인덱스 출력")
for i in range(1, len(myList), 2):
    print(myList[i], end = " ")
print()
print("짝수 인덱스 출력")
for i in range(0, len(myList), 2):
    print(myList[i], end = " ")
print()
    
