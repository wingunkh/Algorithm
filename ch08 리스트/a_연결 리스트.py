# 포인터로 연결 리스트 구현하기

from __future__ import annotations
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

    def add_first(self, data: Any) -> None:
        ptr = self.head # 삽입 전 머리 노드
        self.head = self.current = Node(data, ptr)
        self.no += 1

    def add_last(self, data: Any) -> None:
        if self.head is None:
            self.add_first(data)
        else:
            ptr = self.head
            while ptr is not None:
                ptr = ptr.next
            ptr.next = ptr.current = None(data, None)
            self.no += 1
