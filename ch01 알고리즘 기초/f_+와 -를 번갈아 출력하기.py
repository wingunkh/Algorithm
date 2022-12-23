# +와 -를 번갈아 출력하기

print("+와 -를 번갈아 출력합니다,")
n = int(input("몇개를 출력할까요?: "))

for _ in range(n // 2): # 파이썬에서는 무시하고 싶은 값을 언더스코어로 표현
    print("+-", end='')

if n % 2: # 홀수일 때
    print("+", end='')

print()
