a = 3
b = 4

if a > b:
    print("true")
else:
    print("false")

# set은 순서가 바뀐다.
for i in set([1, 3, 54, 23]):
    print(i)
print('\n')

# for문은 조건을 평가하는 대신 순서열을 순회하며 반복적으로 코드를 실행
'''
for 반복변수 in 순서열:
    코드블록
    
ex)
for i in [1,2,3,4,]:
    print(i)
'''

# 순서열에 들어갈 수 있는 데이터 형식에는 list, tuple, 문자열 등이 있고,
# 순서열은 아니지만 set이나 dict도 사실은 들어갈 수 있다.


for i in range(1, 20):
    print(i)
    
for i in range(1, 20, 2):
    print(i)