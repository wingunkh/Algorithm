# 힙 정렬 알고리즘 구현하기

from typing import MutableSequence

def heap_sort(a: MutableSequence) -> None:
    def down_heap(a: MutableSequence, left: int, right: int) -> None:
        temp = a[left] # 루트

        parent = left
        while parent < (right + 1) // 2:
            cl = parent * 2 + 1 # 왼쪽 자식
            cr = cl + 1 # 오른쪽 자식
            child = cr if cr <= right and a[cr] > a[cl] else cl # 더 큰 자식을 선택
            if temp >= a[child]:
                break
            a[parent] = a[child]
            parent = child
        a[parent] = temp

    n = len(a)

    for i in range((n - 1) // 2, -1, -1): # 배열 a를 힙으로 만드는 반복문
        down_heap(a, i, n - 1)

    for i in range(n - 1, 0, -1): # 루트를 꺼내 배열의 마지막 원소와 교환하고, 배열의 남은 부분을 다시 힙으로 만드는 반복문
        a[0], a[i] = a[i], a[0]
        down_heap(a, 0, i - 1)

if __name__ == "__main__":
    print("힙 정렬을 수행합니다.")
    num = int(input("원소 수를 입력하세요.: "))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f"x[{i}]: "))

    heap_sort(x)

    print("오름차순으로 정렬했습니다.")
    for i in range(num):
        print(f"x[{i}] = {x[i]}")
