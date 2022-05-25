# while 문과 for 문은 굉장히 비슷하며 대부분의 경우 서로 호환 가능하다.

'''
while 조건:
    코드블록
    
-> 조건이 참인 동안에 계속 코드블록을 반복한다.

ex)
i = 0
while i <= 100:
    print(i)
    i += 1
''' 
i = 0
while i <= 10:
    print(i)
    i += 1
    
# pass, break, continue
# 제어문 안에서 쓸 수 있는 특수 명령어로 pass, break, continue가 있다.
# pass: 아무 일 없이 그냥 통과
# break : for 문이나 while 문에서 loop 끝냄
# continue : while문에서 현재 loop를 중단하고 다음 loop로 넘어감