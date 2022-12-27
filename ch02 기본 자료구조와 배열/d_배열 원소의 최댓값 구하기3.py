# 각 배열 원소의 최댓값을 구해서 출력하기(튜플, 문자열, 문자열 리스트)

from a_max import max_of

t = (4,7,5.6,2,3.14,1) # 튜플
s = "string" # 문자열
a = ["KIM","HYUN","GEUN"] # 문자열 리스트

print(f"{t}의 최댓값은 {max_of(t)}입니다.")
print(f"{s}의 최댓값은 {max_of(s)}입니다.")
print(f"{a}의 최댓값은 {max_of(a)}입니다.")
