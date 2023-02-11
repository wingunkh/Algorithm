# 이진 검색 트리 구현하기

from __future__ import annotations
from typing import Any, Type

class Node:
    def __init__(self, key: Any, value: Any, left: Node = None, right: Node = None):
        self.key = key # 키
        self.value = value # 값
        self.left = left # 왼쪽 포인터
        self.right = right # 오른쪽 포인터

class BinarySearchTree:
    def __init__(self):
        self.root = None # 루트

    def search(self, key: Any) -> Any:
        p = self.root
        while True:
            if p is None:
                return None
            if key == p.key:
                return p.value
            elif key < p.key:
                p = p.left
            else:
                p = p.right

    def add(self, key: Any, value: Any) -> bool:
        def add_node(node: Node, key: Any, value: Any) -> None:
            if key == node.key:
                return False
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)
            return True

        if self.root is None:
            self.root = Node(key, value, None, None)
            return True
        else:
            return add_node(self.root, key, value)

    def remove(self, key: Any) -> bool:
        p = self.root # 스캔 중인 노드
        parent = None # 스캔 중인 노드의 부모 노드
        is_left_child = True # p는 parent의 왼쪽 자식 노드인지 확인

        while True: # 삭제할 키를 검색
            if p is None:
                return False

            if key == p.key:
                break
            else:
                parent = p
                if key < p.key:
                    is_left_child = True
                    p = p.left
                else:
                    is_left_child = False
                    p = p.right

        if p.left is None: # p에 왼쪽 자식이 없을 때
            if p is self.root:
                self.root = p.right
            elif is_left_child:
                parent.left = p.right
            else:
                parent.right = p.right
        elif p.right is None: # p에 오른쪽 자식이 없을 때
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left
            else:
                parent.right = p.left
                
        else: # p에 양쪽 자식이 모두 있을 때
            parent = p
            big = p.left
            is_left_child = True
            while big.right is not None: # p의 왼쪽 서브트리에서 가장 큰 노드 big을 검색
                parent = big
                big = big.right
                is_left_child = False

            p.key = big.key
            p.value = big.value
            # 서브트리에서 가장 큰 노드 big을 p의 위치로 복사
            if is_left_child: # big이 왼쪽 자식일 때
                parent.left = big.left
            else:
                parent.right = big.left
            return True

    def dump(self) -> None: # DFS 중 중위 순회 방식으로 스캔 후 출력(오름차순)
        def print_subtree(node: Node):
            if node is not None:
                print_subtree(node.left)
                print(f"{node.key}  {node.value}")
                print_subtree(node.right)

        print_subtree(self.root)

    def min_key(self) -> Any:
        if self.root is None:
            return None
        p = self.root
        while p.left is not None:
            p = p.left
        return p.key
    
    def max_key(self) -> Any:
        if self.root is None:
            return None
        p = self.root
        while p.right is not None:
            p = p.right
        return p.key
