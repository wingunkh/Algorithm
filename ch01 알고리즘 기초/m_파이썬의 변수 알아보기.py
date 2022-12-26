# 파이썬에서는 데이터, 함수, 클래스, 모듈, 패키지 등을 모두 객체로 취급합니다.
# 이러한 특징 때문에 "파이썬의 변수는 값을 갖지 않는다"는 특징이 있습니다.

n = 1 # 전역 변수
# 파이썬의 대입식은 값 자체가 아니라 참조하는 객체의 식별 번호를 대입합니다.

def put_id():
    x = 1 # 지역 변수
    print(f"id(x) = {id(x)}") # id() 함수는 객체의 식별 번호를 반환해 줍니다.

print(f"id(1) = {id(1)}")
print(f"id(n) = {id(n)}")
put_id()
# 3개의 출력문의 결과가 모두 동일하며 이에 따라 n과 x는 모두 int 형 객체 1을 참조하는 이름에 불과하다는 것을 알 수 있습니다.
