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
            ptr.next = ptr.current = Node(data, None)
            self.no += 1

    def remove_first(self) -> None:
        if self.head is not None:
            self.head = self.current = self.head.next
        self -= no

    def remove_last(self) -> None:
        if self.head is not None:
            if self.next is None:
                self.remove_first()
            else:
                ptr = self.head # 스캔 중인 노드
                pre = self.head # 스캔 중인 노드의 앞쪽 노드

                while ptr.next is not None:
                    pre = ptr
                    ptr = ptr.next
                pre.next = None
                self.current = pre
                self.no -= 1

    def remove(self, p: Node) -> None:
        if self.head is not None:
            if p is self.head:
                remove_first()
            else:
                ptr = self.head
                
                while ptr.next is not p:
                    ptr = ptr.next
                    if ptr is None:
                        return
                ptr.next = p.next
                self.current = ptr
                self.no -= 1

    def remove_current_node(self) -> None:
        self.remove(self.current)

    def clear(self) -> None:
        while self.head is not None:
            self.remove_first()
        self.current = None
        self.no = 0

    def next(self) -> bool:
        if self.current is None or self.current.next is None:
            return False
        self.current = self.current.next
        return True

    def print_current_node(self) -> None:
        if self.current is None:
            print("주목 노드가 존재하지 않습니다.")
        else:
            print(self.current.data)

    def print(self) -> None:
        ptr = self.head

        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next

    # 클래스 LinkedList가 이터러블하도록 iter() 함수와 next() 함수를 구현한다.
    def __iter__(self): # __next__() 함수를 갖는 이터레이터(반복자)를 반환하는 __iter()__ 함수 구현
        self.current = self.head
        return self

    def __next__(self): # 다음 원소를 꺼내 반환하며 반환하는 원소가 없으면 StopIteration 예외처리를 내보내는 __next()__ 함수 구현
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data
