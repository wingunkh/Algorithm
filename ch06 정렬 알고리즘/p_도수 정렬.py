# 도수 정렬 알고리즘 구현하기

from typing import MutableSequence

def fsort(a: MutableSequence, max: int) -> None:
    n = len(a) # 정렬할 배열 a
    f = [0] * (max + 1) # 누적 도수 분포표 배열 f
    b = [0] * n # 작업용 배열 b

    for i in range(n): # 1단계) 도수 분포표 만들기
        f[a[i]] += 1
    for i in range(1, max + 1): # 2단계) 누적 도수 분포표 만들기
        f[i] += f[i - 1]
    for i in range(n - 1, -1, -1): # 3단계) 작업용 배열 만들기
        f[a[i]] -= 1
        b[f[a[i]]] = a[i]
    for i in range(n): # 4단계) 배열 복사하기
        a[i] = b[i]

def counting_sort(a: MutableSequence) -> None:
    fsort(a, max(a))

if __name__ == "__main__":
    print("도수 정렬을 수행합니다.")
    num = int(input("원소 수를 입력하세요.: "))
    x = [None] * num

    for i in range(num):
        while True: # 양수만 입력받도록 제한
            x[i] = int(input(f"x[{i}]: "))
            if x[i] >= 0: break

    counting_sort(x)

    print("오름차순으로 정렬했습니다.")
    for i in range(num):
        print(f"x[{i}] = {x[i]}")
