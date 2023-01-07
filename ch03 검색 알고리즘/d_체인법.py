# 체인법으로 해시 함수 구현하기

from __future__ import annotations
from typing import Any, Type
import hashlib

class Node: # 개별 버킷을 나타내는 Node 클래스
    def __init__(self, key: Any, value: Any, next: Node) -> Node:
        self.key = key # 키
        self.value = value # 값
        self.next = next # 뒤쪽 노드를 참조

class ChainedHash: # 체인법으로 해시 클래스 구현
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity # 해시 테이블의 크기를 지정
        self.table = [None] * self.capacity  # 해시 테이블(리스트)을 선언

    def hash_value(self, key: Any) -> int: # 해시 함수
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)

    def search(self, key: Any) -> Any:
        hash = self.hash_value(key) # 검색하는 키의 해시값
        p = self.table[hash] # 노드를 주목

        while p is not None:
            if p.key == key:
                return p.value # 검색 성공
            p = p.next # 뒤쪽 노드를 주목

        return None # 검색 실패

    def add(self, key: Any, value: Any) -> bool:
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return False
            p = p.next

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
        return True

    def remove(self, key: Any) -> bool:
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None # 바로 앞의 노드를 주목

        while p is not None:
            if p.key == key:
                if pp is None: # 연결 리스트의 첫번째 노드일 때
                    self.table[hash] = p.next
                else: # 연결 리스트의 첫번째 노드가 아닐 때
                    pp.next = p.next
                return True
            pp = p
            p = p.next

        return False

    def dump(self) -> None:
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f"  →{p.key} ({p.value})", end='')
                p = p.next
            print()
