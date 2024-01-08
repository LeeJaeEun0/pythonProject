def hello():
    print('안녕!')
hello()

#return 값이 있는 경우
def sum(a,b):
    return a+b

result = sum(1,2)
print(result)

def bus_rate(age):
    if age > 65:
        return 0
    elif age > 20:
        return 1200
    else:
        return 750

myrate = bus_rate(60)
print('버스비: ',myrate)

# 퀴즈 - 주민등록번호를 입력받아 성별을 출력하는 함수 만들기
def check_gender(pin):
    index = pin.split('-')[1][0]
    if int(index)%2 == 0:
        print("여자")
    else:
        print("남자")

check_gender('150101-1012345')
check_gender('150101-2012345')
check_gender('150101-4012345')