# 1,000 이하의 소수를 나열하기

counter = 0 # 곱셈과 나눗셈 횟수를 카운트
ptr = 0 # 이미 찾은 소수의 개수
prime = [None] * 500 # 소수를 저장할 배열

prime[ptr] = 2 # 2는 소수
ptr += 1

prime[ptr] = 3 # 3은 소수
ptr += 1

for n in range(5, 1001, 2): # 홀수만을 대상으로 선정
    i = 1
    while prime[i] * prime[i] <= n: # 소수란? n의 제곱근 이하의 어떤 소수로도 나누어 떨어지지 않는 수
        counter += 2
        if n % prime[i] == 0: # n이 합성수일 때
            break
        i += 1
    else: # n이 소수일 때
        prime[ptr] = n
        ptr += 1
        counter += 1

for i in range(ptr):
    print(prime[i])
print(f"곱셈과 나눗셈을 실행한 횟수: {counter}")
