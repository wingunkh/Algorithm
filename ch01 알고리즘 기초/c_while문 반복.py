# while문

print("1부터 n까지 정수의 합을 구합니다.")

while True: # 무한 루프
    n = int(input("n값을 입력하세요.: "))
    if n > 0:
        break # 파이썬은 사후 판단 반복문을 제공하지 않는다.

i = 1
sum = 0

while i <= n:
    sum+=i
    i+=1

print(f"1부터 {n}까지 정수의 합은 {sum}입니다.")
