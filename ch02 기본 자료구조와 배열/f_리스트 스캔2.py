# 리스트의 모든 원소를 enumerate() 함수로 스캔하기

x = ["John", "George", "Paul", "Ringo"]

for i, name in enumerate(x): # enumerate() 함수는 인덱스와 원소를 짝지어 튜플로 꺼내는 내장 함수이다.
    print(f"x[{i}] = {name}")
print()

for i, name in enumerate(x,1): # 이 때 1부터 카운트한다.
    print(f"{i}번째 = {name}")

    
