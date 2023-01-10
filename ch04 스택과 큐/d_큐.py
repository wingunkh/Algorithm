# 고정 길이 큐 클래스 FixedQueue 구현하기

from typing import Any

class FixedQueue:
    class Empty(Exception):
        pass
    
    class Full(Exception):
        pass

    def __init__(self, capacity: int) -> None:
        self.no = 0 # 현재 데이터 개수
        self.front = 0 # front는 맨 앞 원소의 인덱스
        self.rear = 0 # rear는 맨 끝 원소 바로 뒤의 인덱스(다음 인큐되는 데이터가 저장되는 위치)
        self.capacity = capacity # 큐의 크기
        self.que = [None] * capacity # 큐의 본체

    def __len__(self) -> int:
        return self.no

    def is_empty(self) -> bool:
        return self.no <= 0

    def is_full(self) -> bool:
        return self.no >= self.capacity

    def enque(self, x: Any) -> None:
        if self.is_full():
            raise FixedQueue.Full
        self.que[self.rear] = x
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0

    def deque(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty
        x = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x

    def peek(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty
        return self.que[self.front]

    def find(self, value: Any) -> Any:
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                return idx
        return -1

    def count(self, value: Any) -> Any:
        c = 0
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                c += 1
        return c

    def __contains__(self, value: Any) -> bool:
        return self.count(value)

    def clear(self) -> None:
        self.no = self.front = self.rear = 0
        # 큐에서 인큐나 디큐 등 모든 작업은 no, front, rear를 바탕으로 이루어진다.
        # 따라서 큐의 배열 원솟값을 변경할 필요 없이 이들의 값을 0으로 변경하면 큐의 모든 데이터를 삭제할 수 있다.

    def dump(self) -> None:
        if self.is_empty():
            print("큐가 비었습니다.")
        else:
            for i in range(self.no):
                print(self.que[(i + self.front) % self.capacity], end=' ')
            print()
