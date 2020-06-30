#201901881_컴퓨터전자시스템공학부_설희관
n = int(input("구입한 콜라의 수를 입력하시오"))
price = 0
if n >= 11 and n <= 20:
    price = n* 800*(0.97)
elif n >= 21:
    price = n* 800*(0.95)
else:
    price = n* 800

print("콜라 %d병은 %d입니다." %(n, price))

