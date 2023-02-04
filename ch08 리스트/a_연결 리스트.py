# 포인터로 연결 리스트 구현하기

from typing import Any, Type

class Node:
    def __init__(self, data: Any = None, next: Node = None):
        self.data = data # 데이터
        self.next = next # 뒤쪽 포인터

class LinkedList:
    def __init__(self) -> None:
        self.no = 0 # 노드의 개수
        self.head = None # 머리 노드
        self.current = None # 주목 노드

    def __len__(self) -> int:
        return self.no

    def search(self, data: Any) -> int:
        cnt = 0
        ptr = self.head

        while ptr is not None:
            if ptr.data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1

    def __contains__(self, data: Any) -> bool:
        return self.search(data) >= 0
