people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby', 'age': 57},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

# def check_adult(person):
#     if person['age'] > 20:
#         return '성인'
#     else:
#         return '청소년'
#
# result = map(check_adult, people)

# map - 리스트를 지정한 함수로 처리
# result = map(lambda  person: ('성인' if person['age'] > 20 else '청소년'),people)

# filter - true인 경우 실행
result = filter(lambda  x:x['age'] > 20,people)

print(list(result))