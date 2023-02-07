# 포인터를 이용한 연결 리스트 클래스 LinkedList 사용하기

from enum import Enum
from a_연결리스트 import LinkedList

Menu = Enum("Menu", ["머리에노드삽입", "꼬리에노드삽입", "머리노드삭제",
                     "꼬리노드삭제", "주목노드출력", "주목노드이동",
                     "주목노드삭제", "모든노드삭제", "검색", "멤버십판단",
                     "모든노드출력", "스캔", "종료",])

def select_Menu() -> Menu:
    s = [f"({m.value}){m.name}" for m in Menu]
    while True:
        print(*s, sep='  ', end='')
        n = int(input(": "))
        if 1 <= n <= len(Menu):
            return Menu(n)

lst = LinkedList()  # 연결 리스트를 생성

while True:
    menu = select_Menu()  # 메뉴 선택

    if menu == Menu.머리에노드삽입:
        lst.add_first(int(input('머리에 넣을 값을 입력하세요.: ')))

    elif menu == Menu.꼬리에노드삽입:
        lst.add_last(int(input('꼬리에 넣을 값을 입력하세요.: ')))

    elif menu == Menu.머리노드삭제:
        lst.remove_first()

    elif menu == Menu.꼬리노드삭제:
        lst.remove_last()

    elif menu == Menu.주목노드출력:
        lst.print_current_node()

    elif menu == Menu.주목노드이동:
        lst.next()

    elif menu == Menu.주목노드삭제:
        lst.remove_current_node()

    elif menu == Menu.모든노드삭제:
        lst.clear()

    elif menu == Menu.검색:
        pos = lst.search(int(input('검색할 값을 입력하세요.: ')))
        if pos >= 0:
            print(f'그 값의 데이터는 {pos + 1}번째에 있습니다.')
        else:
            print('해당 데이터가 없습니다.')

    elif menu == Menu.멤버십판단:
        print('그 값의 데이터는 포함되어' + (' 있습니다.' if int(input('멤버십 판단할 값을 입력하세요.: ')) in lst else ' 있지 않습니다.'))

    elif menu == Menu.모든노드출력:
        lst.print()

    elif menu == Menu.스캔:
        for e in lst:
            print(e)

    else: 
        break
