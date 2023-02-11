# 이진 검색 트리 구현하기

from __future__ import Annotations
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
            self.root = None(key, value, None, None)
            return True
        else:
            return add_node(self.root, key, value)
