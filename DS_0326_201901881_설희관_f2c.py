#변환 함수
def convert_function(f):
    c = (f - 32) * (5/9)
    return c

#Fahrenheit's Temperature
fahrenheit = int(input("화씨 온도를 입력하세요: "))
celsius = convert_function(fahrenheit)
print("Fahrenheit: %d 도는 Celsius: %.2f도 입니다" %(fahrenheit, celsius))
