# 보초법


from typing import Any, Sequence
import copy

def seq_search(seq :Sequence, key: Any) -> int:
    a = copy.deepcopy(seq) # seq를 복사
    a.append(key) # 보초를 추가 (보초란 배열의 맨 끝에 저장되는 검색하고자 하는 키값이다.)

    i = 0
    while True:
        if a[i] == key:
            break
        i += 1
    # 선형 검색은 반복할 때 마다 2가지 종료 조건을 체크하지만 보초법을 사용할 경우 이 비용이 절반으로 감소한다.
        
    return -1 if i == len(seq) else i # 조건 연산자인 if~else 문은 파이썬의 유일한 삼항 연산자이다. 참이면 -1을, 거짓이면 i를 반환한다.

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
