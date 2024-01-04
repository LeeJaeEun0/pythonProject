fist_name= 'jaeeun'
last_name = 'lee'

print(fist_name+last_name)

# a= 2
# b= 'hello'
# print(a+b) # 문자열 + 숫자는 불가능

a='2'
b = str(2)
print(a+b)

# 문자열 슬라이싱
text = 'abcdefghijk'
result = len(text)
result2 = text[:3]
result3 = text[3:8]

print(result, result2, result3)

# 문자열 자르기
myemail = 'abc@sparta.co'
result = myemail.split('@')[1].split('.')[0]
print(result)

# 퀴즈
text = 'sparta'
result = text[0:3]
print(result)

# 퀴즈
phone='02-1234-1234'
result = phone.split('-')[0]
print(result)