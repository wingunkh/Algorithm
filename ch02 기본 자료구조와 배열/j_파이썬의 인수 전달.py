# 파이썬에서는 "값에 의한 호출"과 "참조에 의한 호출"의 중간적인 방식으로 "객체 참조에 의한 전달"이라는 용어를 사용한다.
# 함수에 인수를 전달할 때 참조가 전달되지만, 인수가 가리키는 객체의 뮤터블리티(mutability)에 따라 동작이 달라진다.

def sum(n):
    s = 0
    while n > 0:
        s += n
        n -= 1
    return s

x = int(input("x의 값을 입력하세요.: "))
print(f"1부터 {x}까지 정수의 합은 {sum(x)}입니다.")

# 함수에서 매개변수의 값을 변경할 시 인수가 이뮤터블인 경우 실제 인수에는 영향을 주지 않는다.

def change(lst, idx, val):
    lst[idx] = val

x = [1,2,3,4,5]
print("x = ", x)

index = int(input("업데이트할 인덱스를 선택하세요.: "))
value = int(input("새로운 값을 입력하세요.: "))

change(x, index, value)
print(f"x = {x}")

# 함수에서 매개변수의 값을 변경할 시 인수가 뮤터블인 경우 실제 인수의 값이 변경된다.
