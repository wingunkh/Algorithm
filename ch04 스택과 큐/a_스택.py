# 고정 길이 스택 클래스 FixedStack 구현하기

from typing import Any

class FixedStack:
    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity: int = 256) -> None:
        self.stk = [None] * capacity # 스택 본체
        self.capacity = capacity # 스택의 크기
        self.ptr = 0 # 스택 포인터(스택에 쌓여있는 데이터의 개수를 나타내는 정숫값)

    def __len__(self) -> int:
        return self.ptr

    def is_empty(self) -> bool:
        return self.ptr <= 0

    def is_full(self) -> bool:
        return self.ptr >= self.capacity

    def push(self, value: Any) -> None:
        if self.is_full():
            raise FixedStack.Full # raise문을 통한 예외 처리
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        return self.str[self.ptr - 1]

    def clear(self) -> None:
        self.ptr = 0 # 스택에서 푸시나 팝 등 모든 작업은 스택 포인터를 바탕으로 이루어진다. 따라서 스택의 배열 원솟값을 변경할 필요 없이 ptr의 값을 0으로 변경하면 스택의 모든 데이터를 삭제할 수 있다.

    def find(self, value: Any) -> Any:
        for i in range(self.ptr - 1, -1, -1): # top에서부터 선형 검색
            if self.stk[i] == value:
                return i
        return -1

    def count(self, value: Any) -> int:
        c = 0
        for i in range(self.ptr - 1, -1, -1): # top에서부터 선형 검색
            if self.stk[i] == value:
                c += 1
        return c

    def __contains__(self, value: Any) -> bool:
        return self.count(value) > 0

    def dump(self) -> None:
        if self.is_empty():
            print("스택이 비어 있습니다.")
        else:
            print(self.stk[:self.ptr])
