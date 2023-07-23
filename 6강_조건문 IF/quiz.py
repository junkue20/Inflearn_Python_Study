# 1. 주식 거래 프로그램 작성

# print("환영합니다, 주식 거래 시스템입니다.")

# price = int(input("삼성전자의 현재 가격 (만원): "))

# # 현재가격 9만원 이상 시 "매도합니다" 출력 
# if price >= 9 :
#     print("매도합니다")
# # 현재가격 9만원 이하, 8만원 이상 시 "대기중입니다" 출력 
# elif price >= 8  :
#     print("대기중입니다.")
# # 현재가격 8만원 이하 시 "매수합니다" 출력 
# else :
#     print("매수합니다.")


# -------------------------------------------------------

# 2. 할인률 계산 프로그램
bag = int(input("가방의 현재 가격 : "))
watch = int(input("시계의 현재 가격 : "))

sumPrice = bag + watch


print("총 금액 : " + str(sumPrice) + "원")

if sumPrice >= 100000 : 
    totalPrice = (sumPrice) - int((sumPrice) * 0.3)
elif sumPrice >= 50000 :
    totalPrice = (sumPrice) - int((sumPrice) * 0.2)
else :
    totalPrice = (sumPrice) - int((sumPrice) * 0.1)

    print("할인 적용된 금액 : " + str(totalPrice) + "원")