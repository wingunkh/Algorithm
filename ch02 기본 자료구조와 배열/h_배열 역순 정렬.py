# 뮤터블 시퀀스 원소를 역순으로 정렬

from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n // 2): # 원소의 수가 홀수인 경우 가운데 원소는 교환할 필요가 없다.
        a[i], a[n-1-i] = a[n-1-i], a[i]

if __name__ == "__main__":
    print("배열 원소를 역순으로 정렬합니다.")
    nx = int(input("원소 수를 입력하세요.: "))
    x = [None] * nx

    for i in range(nx):
        x[i] = int(input(f"x[{i}]값을 입력하세요.: "))

    reverse_array(x)
    # x.reverse() # list 타입에서 제공하는 함수 / 역순 정렬 기능 제공 / 반환값이 없음
    # y = list(reversed(x)) # 파이썬의 내장 함수 / 역순 정렬 기능 제공 / 이터러블 객체 반환

    print("배열을 역순으로 정렬했습니다.")
    for i in range(nx):
        print(f"x[{i}] = {x[i]}")
