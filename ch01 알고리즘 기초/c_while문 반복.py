# while문

print("1부터 n까지 정수의 합을 구합니다.")
n = int(input("n값을 입력하세요.: "))

i = 1
sum = 0

while i <= n:
    sum+=i
    i+=1

print(f"1부터 {n}까지 정수의 합은 {sum}입니다.")
