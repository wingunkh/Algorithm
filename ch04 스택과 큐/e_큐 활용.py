# 고정 길이 큐 클래스를 사용하기

from enum import Enum
from d_큐 import FixedQueue

Menu = Enum("Menu", ["인큐", "디큐", "피크", "검색", "덤프", "종료"])

def select_menu() -> Menu:
    s = [f"({m.value}){m.name}" for m in Menu]
    while True:
        print(*s, sep='  ', end='')
        n = int(input(": "))
        if 1 <= n <= len(Menu): # __len__() 함수를 정의하였기 때문에 len(obj) 작성 가능
            return Menu(n)

q = FixedQueue(64)

while True:
    print(f"현재 데이터 개수: {len(q)} / {q.capacity}")
    menu = select_menu()

    if menu == Menu.인큐:
        x = int(input("데이터를 입력하세요.: "))
        try:
            q.enque(x)
        except FixedQueue.Full:
            print("큐가 가득 차 있습니다.")

    elif menu == Menu.디큐:
        try:
            x = q.deque()
            print(f"디큐한 데이터는 {x}입니다.")
        except FixedQueue.Empty:
            print("큐가 비어 있습니다.")

    elif menu == Menu.피크:
        try:
            x = q.peek()
            print(f"피크한 데이터는 {x}입니다.")
        except FixedQueue.Empty:
            print("큐가 비어 있습니다.")

    elif menu == Menu.검색:
        x = int(input("검색할 데이터를 입력하세요.: "))
        if x in q: # __contains__() 함수를 정의하였기 때문에 x in obj 작성 가능 (in은 멤버십 판단 연산자)
            print(f"{q.count(x)}개 포함되고, 맨 앞의 위치는 {q.find(x)}입니다.")
        else:
            print("검색값을 찾을 수 없습니다.")

    elif menu == Menu.덤프:
        q.dump()

    else:
        break
