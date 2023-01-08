# 고정 길이 스택 클래스(Fixed Stack)를 사용하기

from enum import Enum
from a_스택 import FixedStack

Menu = Enum("Menu", ["푸시", "팝", "피크", "검색", "덤프", "종료"])

def select_menu() -> Menu:
    s = [f"({m.value}){m.name}" for m in Menu]
    while True:
        print(*s, sep='  ', end='')
        n = int(input(": "))
        if 1 <= n <= len(Menu): # __len__() 함수를 정의하였기 때문에 len(obj) 작성 가능
            return Menu(n)

s = FixedStack(64)

while True:
    print(f"현재 데이터 개수: {len(s)} / {s.capacity}")
    menu = select_menu()

    if menu == Menu.푸시:
        x = int(input("데이터를 입력하세요.: "))
        try:
            s.push(x)
        except FixedStack.Full:
            print("스택이 가득 차 있습니다.")

    elif menu == Menu.팝:
        try:
            x = s.pop()
            print(f"팝한 데이터는 {x}입니다.")
        except FixedStack.Empty:
            print("스택이 비어 있습니다.")

    elif menu == Menu.피크:
        try:
            x = s.peek()
            print(f"피크한 데이터는 {x}입니다.")
        except FixedStack.Empty:
            print("스택이 비어 있습니다.")

    elif menu == Menu.검색:
        x = int(input("검색할 데이터를 입력하세요.: "))
        if x in s: # __contains__() 함수를 정의하였기 때문에 x in obj 작성 가능 (in은 멤버십 판단 연산자)
            print(f"{s.count(x)}개 포함되고, 맨 앞의 위치는 {s.find(x)}입니다.")
        else:
            print("검색값을 찾을 수 없습니다.")

    elif menu == Menu.덤프:
        s.dump()

    else:
        break
            
