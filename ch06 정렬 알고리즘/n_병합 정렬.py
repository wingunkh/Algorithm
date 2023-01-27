# 병합 정렬 알고리즘 구현하기

from typing import MutableSequence

def merge_sort(a: MutableSequence) -> None:
    def _merge_sort(a: MutableSequence, left: int, right: int) -> None:
        if left < right:
            center = (left + right) // 2

            _merge_sort(a, left, center) # 배열 앞부분을 병합 정렬
            _merge_sort(a, center + 1, right) # 배열 뒷부분을 병합 정렬

            p = j = 0 # 배열 buff의 커서
            i = k = left # 배열 a의 커서

            while i <= center: # 배열 a의 앞부분을 배열 buff로 복사
                buff[p] = a[i]
                p += 1
                i += 1

            while i <= right and j < p: # 배열 a의 뒷부분과 배열 buff를 배열 a에 병합
                if buff[j] <= a[i]:
                    a[k] = buff[j]
                    j += 1
                else:
                    a[k] = a[i]
                    i += 1
                k += 1

            while j < p: # 배열 buff의 나머지 원소를 배열 a에 복사
                a[k] = buff[j]
                k += 1
                j += 1

    n = len(a)
    buff = [None] * n # 작업용 배열을 생성
    _merge_sort(a, 0 , n - 1) # 배열 전체를 병합
    del buff # 작업용 배열을 소멸

if __name__ == "__main__":
    print("병합 정렬을 수행합니다.")
    num = int(input("원소 수를 입력하세요.: "))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f"x[{i}]: "))

    merge_sort(x)

    print("오름차순으로 정렬했습니다.")
    for i in range(num):
        print(f"x[{i}] = {x[i]}")
