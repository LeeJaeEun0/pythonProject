num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]

# 리스트에서 짝수만 출력하는 함수 출력
for i in num_list:
    if i % 2 == 0:
        print(i)

# 리스트에서 짝수의 개수 출력
counter = 0
for i in num_list:
    if i % 2 == 0:
        counter=counter+1
print(counter)

# 리스트 안의 모든 숫자 더하기
total = 0
for i in num_list:
   total += i
print(total)

# 리스트 안에 있는 자연수 중 가장 큰 수 구하기
max=-1
for i in num_list:
   if max < i:
       max = i
print(max)