def cal(a,b):
    return a+2+b

result=cal(b=2, a=1) # 변수의 순서와 상관 없음
print(result)

def cal(a,b=2): # 기본값
    return a+2+b

result=cal(b=2, a=1)
print(result)

