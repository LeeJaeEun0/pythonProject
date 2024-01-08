# tuple - 불변형 자료
a = ('사과', '감', '배')
print(a[1])

# set
a = [1,2,3,4,2,3,4,6,4,5]
a_set = set(a)
print(a)

a=['사과', '감', '베', '수박', '딸기']
b=['배', '사과', '포도', '참외', '수박']

a_set = set(a)
b_set = set(b)

print(a_set & b_set)

# 퀴즈 -  a중에 b를 빼기
student_a = ['물리2','국어','수학1','음악','화학1','화학2','체육']
student_b = ['물리1','수학1','미술','화학2','체육']

a_set = set(student_a)
b_set = set(student_b)

print(a_set - b_set)