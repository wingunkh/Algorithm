# 버블 정렬 알고리즘 구현하기(알고리즘의 개선 2)

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    k = 0
    while k < n - 1:
        last = n - 1 # 각 패스에서 마지막으로 교환한 두 원소 가운데 오른쪽 원소인 a[j]의 인덱스를 저장한다.
        for j in range(n-1, k, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
                last = j
        k = last # 하나의 패스를 마친 시점에 last의 값을 k에 대입하여 다음에 수행할 패스의 스캔 범위를 a[k]로 제한한다.

if __name__ == "__main__":
    print("버블 정렬을 수행합니다.")
    num = int(input("원소 수를 입력하세요.: "))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f"x[{i}]: "))

    bubble_sort(x)

    print("오름차순으로 정렬했습니다.")
    for i in range(num):
        print(f"x[{i}] = {x[i]}")
