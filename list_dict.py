# 리스트 - 순서가 중요
# a_list = ['사과', '배', '감']
a_list = [1, '배', False, ['사과','감']]
print(a_list[3][1])

b_list = [1,5,6, 3, 2]
b_list.append(99)

print(b_list[5])

b_list = [1,5,6, 3, 2]
result = b_list[:3]
result2 = len(b_list)
print(result, result2)

c_list = [1,5,6, 3, 2]
c_list.sort()
# c_list.sort(reverse=True)

print(c_list)

c_list = [1,5,6, 3, 2]
result = (33 in c_list)
print(result)

# 삭제
del c_list[0] # 인덱스 위치의 값을 삭제
c_list.remove(2) # 2 삭제

# 딕셔너리
a_dict = {'name':'bob', 'age':27, 'friend' :['영희', '철수']}
result = a_dict['name']
result2 = a_dict['friend'][1]

print(result, result2)

a_dict['height'] = 180
print('height' in a_dict)

# 리스트와 딕셔너리
people=[{'name':'bob', 'age':27},{'name':'john', 'age':30}]
print(people[1]['age'])

# 퀴즈
people = [
    {'name': 'bob', 'age': 20, 'score':{'math':90,'science':70}},
    {'name': 'carry', 'age': 38, 'score':{'math':40,'science':72}},
    {'name': 'smith', 'age': 28, 'score':{'math':80,'science':90}},
    {'name': 'john', 'age': 34, 'score':{'math':75,'science':100}}
]
print(people[2]['score']['science'])