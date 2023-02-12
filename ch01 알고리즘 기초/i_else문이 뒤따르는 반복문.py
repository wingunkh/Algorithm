# 10~99 사이의 난수 n개 생성하기 (13이 나오면 중단)

import random

n = int(input("난수의 갯수를 입력하세요.: "))

for i in range(1, n+1):
    r = random.randint(10,99)
    print(r, end=' ')
    if r==13:
        print("\n프로그램을 중단합니다.")
        break
else: # 반복문의 끝 부분에 else문을 둘 수 있으며 조건식에 의해 반복문이 종료되는 경우 실행됩니다.
    print("\n난수 생성을 종료합니다.")
