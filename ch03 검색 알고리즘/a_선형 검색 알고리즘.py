# 선형 검색 알고리즘
"""
선형 검색의 종료 조건
1) 검색할 값을 찾지 못하고 배열의 맨 끝을 지나는 경우 
2) 검색할 값과 같은 원소를 찾은 경우
"""
from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    i = 0
    while True:
        if i == len(a): # 종료 조건1
            return -1
        if a[i] == key: # 종료 조건2
            return i
        i += 1

if __name__ == "__main__":
    num = int(input("원소 수를 입력하세요.: "))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f"x[{i}]: "))

    ky = int(input("검색할 값을 입력하세요.: "))

    idx = seq_search(x, ky)

    if idx == -1:
        print("검색값을 갖는 원소가 존재하지 않습니다.")
    else:
        print(f"검색값은 x[{idx}]에 있습니다.")
