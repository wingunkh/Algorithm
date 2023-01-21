# 단순 삽입 정렬 알고리즘 구현하기

from typing import MutableSequence

def insertion_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(1, n): # 단순 삽입 정렬은 두번째 원소부터 주목하여 진행한다.
        j = i
        tmp = a[i] # 변수 tmp에 주목하는 원소의 값을 대입
        while j > 0 and a[j-1] > tmp:
            a[j] = a[j-1]
            j -= 1
        a[j] = tmp # 주목하는 원소의 값을 알맞은 위치에 삽입 즉, 아직 정렬되지 않은 부분의 맨 앞 원소를 정렬된 부분의 알맞은 위치에 삽입한다.

if __name__ == "__main__":
    print("단순 삽입 정렬을 수행합니다.")
    num = int(input("원소 수를 입력하세요.: "))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f"x[{i}]: "))

    insertion_sort(x)

    print("오름차순으로 정렬했습니다.")
    for i in range(num):
        print(f"x[{i}] = {x[i]}")
