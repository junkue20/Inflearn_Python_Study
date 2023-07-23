# 파이썬 조건문 종류
# if else elif

# distance = int(input("현재 거리를 입력하시오(미터단위) : "))

# if distance >= 300 :
#     print("300m 이상입니다.")
# elif distance >= 200:
#     print("200m 이상입니다.")
# elif distance >= 100:
#     print("100m 이상입니다.")
# else :
#     print("100m 이하입니다.")



# ----------------------------------------------------------

# # 생일 알리미를 만들어 보도록 하자.
# month = int(input("태어난 달 입력 : "))
# day = int(input("태어난 일 입력 : "))

# if month > 7 or day > 23 :
#     print("생일이 지났습니다.")
# elif month == 7 and day == 23:
#     print("오늘 생일이시군요!")
# else :
#     print("생일이 지나지 않았습니다.")


# ----------------------------------------------------------

# + 만 나이 계산기를 만들어 보자.
year = int(input("태어난 년도 입력 : "))
month = int(input("태어난 달 입력 : "))
day = int(input("태어난 일 입력 : "))

yourAge = 2023 - year

if month < 7 or day < 23 :
    print("당신은 현재 만 " + str(yourAge) + "살 입니다.")
elif month == 7 and day == 23:
    print("생일 축하합니다! 1997" + "당신은 오늘부로 만 " + str(yourAge) + "살 입니다!")
else :
    print("당신은 현재 만" + str(yourAge - 1) + "살 입니다.")

