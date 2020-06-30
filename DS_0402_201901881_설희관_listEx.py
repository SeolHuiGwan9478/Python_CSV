#201901881_컴퓨터전자시스템공학부_설희관

#1. 숫자 리스트
numberList = [10, 20, 30]
print(numberList)
print(numberList[0] + numberList[1])
print(numberList[-1])
print(numberList[0] + numberList[2])

#2. 복합 리스트(리스트 안의 리스트 => 문자열도 리스트와 같은 역할 but, 수정불가
listOfList = ['apple', 'banana', [100,200]]
print(listOfList)
print(listOfList[2])
print(listOfList[2][0])
print(listOfList[2][1])

#3. 리스트 슬라이싱
list = ['apple', 100, 'banana', 200] 
print(list[2:]) #Prints elements starting from 3rd element
print(list[1:3]) #Prints elements starting from 2nd till 3rd
print(list[-3:]) #Reverse indexing한 slicing

#4 리스트 연산
numberList = [10, 20, 30]
n2 = [40, 50, 60]
print(numberList + n2)
print(len(n2)) #list 길이 구하는 함수 len()
n3 = numberList + n2
print(n3)
print(len(n3))

#5. 리스트 수정/삭제/추가 etc
list1 = ['apple', 100, 'banana', 200]
list1[1] = 300
print(list1)
del list1[1]
print(list1)
list1.append(100)
print(list1)
list1.insert(1, 100)
print(list1)

#6. 리스트 packing, unpacking
num = [1,2,3]
a, b, c, = num
print(num, a, b, c)

#7. 리스트 sort
'''
list1 = ['apple', 100, 'banana', 200]
print(list1.sort()) #문자와 숫자가 혼합된 리스는 sort불가능해서 오류가 뜬다.
'''
list2 = [2, 25, 3, 4, 1, 32, 4, 19, 99, 54]
list2.sort()
print(list2)
list2.sort(reverse = True)
print(list2)
