num = 3

# if문
result = '짝수' if num%2==0 else '홀수'

print(f'{num}은 {result} 입니다')

# for문
a_list = [1,2,3,4,5]

b_list = [i*2 for i in a_list]

print(b_list)