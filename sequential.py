a = [1,2,3,4,5]
print(a)

#리스트 관련 함수들
#요소 추가 : 리스트.append(값)
#정렬 : 리스트.sort()
#뒤집기 : 리스트.reverse()
#위치 반환 : 리스트.index(값)
#삭제 : del 리스트[위치]

#기타 : insert, remove, pop, extend

a = [1,2,3,4,5]
a.append(8)
print(a)

b = [3,2,1,3,2,5,4]
b.sort()
del b[1]
print(b)

c = [1,5,9,4,5,6]
print(c.index(9))   #9가 2번째 자리에 있다.