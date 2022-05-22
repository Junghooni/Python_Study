# key : value의 형태로 주어진 데이터들의 집합을 딕셔너리라고 한다.
# {key1:value1, key2:value2, key3:value3}
# key에는 변하지 않는 값을 사용하고, value에 있는 값은 변경 가능하다.
# key의 순서는 없으며 key는 중복될 수 없다.
# key는 자료형이 없지만 일반적으로 문자열을 쓴다.
# key에 대응되는 value를 가져오고 싶으면 dictionary[key]를 입력

a = {'1' : '강승현', '2' : '아무개'}
print(a)
print(a['2'])

b = dict()
b['3'] = '고길동'

b['7'] = 'alpha'
b['5'] = 'alphago'
print(b)

# dict 주요 함수
# 길이 반환 : len(딕셔너리) / 데이터 삭제 : del 딕셔너리[key]
# 키 값 모두 반환 : 딕셔너리.keys() / 밸류 값 모두 반환 : 딕셔너리.values()
# 기타 : clear, copy, get(key), update, popitem 등

print(len(b))
del b['3']
print(b)
print(b.keys())
print(b.values())

'''
a['100000']     # 에러가 발생하고
a.get('1000000')    # 아무런 값도 반환하지 않는다.
'''