# 버블 정렬 알고리즘 구현하기

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n-1): # n-1개 원소의 정렬이 끝나면 마지막 원소는 이미 끝에 놓이기 때문에 수행하는 패스 횟수는 n-1번이다.
        for j in range(n-1, i, -1): # 패스를 한 번 수행할 때 마다 정렬할 대상은 1개씩 줄어든다.
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]

if __name__ == "__main__":
    print("버블 정렬을 수행합니다.")
    num =int(input("원소 수를 입력하세요.: "))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f"x[{i}]: "))

    bubble_sort(x)

    print("오름차순으로 정렬했습니다.")
    for i in range(num):
        print(f"x[{i}] = {x[i]}")
