# 시퀀스 원소의 최댓값 출력하기

from typing import Any, Sequence

def max_of(a: Sequence) -> Any:
    maximum = a[0]
    for i in range(1,len(a)):
        if a[i] > maximum:
            maximum =a[i]

    return maximum

if __name__ == "__main__":
    # 파이썬에서는 하나의 스크립트 프로그램을 모듈이라고 한다.
    # __name__은 모듈 이름을 나타내는 변수이다.
    # 1. 스크립트 프로그램이 직접 실행될 때 변수 __name__은 "__main__"이다.
    # 2. 스크립트 프로그램이 import될 때 변수 __name__은 원래 모듈 이름이다.
    print("배열의 최댓값을 구합니다.")
    num = int(input("원소 수를 입력하세요.: "))
    x = [None] * num # 원소 수가 num인 리스트를 생성

    for i in range(num):
        x[i] = int(input(f"x[{i}] 값을 입력하세요.: "))


    print(f"최댓값은 {max_of(x)} 입니다.")
