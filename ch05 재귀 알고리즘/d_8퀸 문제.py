# 8퀸 문제 알고리즘 구현하기

pos = [0] * 8 # 배열 pos는 퀸의 위치를 나타낸다.
flag_a = [False] * 8 # 각 행에 퀸을 배치했는지 체크
flag_b = [False] * 15 # 대각선 방향(↙↗)으로 퀸을 배치했는지 체크
flag_c = [False] * 15 # 대각선 방향(↘↖)으로 퀸을 배치했는지 체크

def put() -> None: # 각 열에 배치한 퀸의 위치를 출력하는 함수
    for j in range(8):
        for i in range(8):
            print('■' if pos[i] == j else '□', end='')
        print()
    print()

def set(i: int) -> None: # i열의 알맞은 위치에 퀸을 배치하는 함수
    for j in range(8):
        if not(flag_a[j] or flag_b[i+j] or flag_c[i-j+7]): # 드모르간의 법칙 적용
            pos[i] = j # 퀸을 i열의 j행에 배치
            if i == 7:
                put()
            else:
                flag_a[j] = flag_b[i+j] = flag_c[i-j+7] = True
                set(i+1)
                flag_a[j] = flag_b[i+j] = flag_c[i-j+7] = False

set(0)
