# x = input("첫번째 숫자를 입력 : ")
# y = input("두번째 숫자를 입력 : ")

# print("두 수의 곱은 ...")
# print(x * y)


# 위와 같이 연산을 진행할경우 오류가 발생!
# - 입력받은 수가 str 판정이기 때문. -
# 형변환을 위해서는 `int(변수)`, `str(변수)` 와 같이 자료형 뒤에 소괄호!

# x = int(input("첫번째 숫자를 입력 : "))
# y = int(input("두번째 숫자를 입력 : "))

# print("두 수의 곱은 ...")
# print(int(x) * int(y))




# 실습!

# 사용자로부터 배어난 년도를 입력받으면 현재 나이를 계산하여 출력할 것.

# 비교할 현재년도 정보
todayYear = 2023

# 입력받을 수
userBirth = int(input("출생년도를 입력해주세요! : "))

# 나이 출력
print("만 " + todayYear -  userBirth + "세 이시네요!")


# 파이썬은 Java에서와 달리 `숫자 + 문자`로 출력하면 오류가 발생한다.
# 이를 해결하기 위하여 숫자값 앞에 str()을 붙이거나, 숫자로 된 문자값 앞에 int()를 붙여주어야 한다.
#

# 비교할 현재년도 정보
todayYear = 2023

# 입력받을 수
userBirth = int(input("출생년도를 입력해주세요! : "))

# 나이 출력
print("만 " + str(todayYear -  userBirth) + "세 이시네요!")