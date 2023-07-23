# 프로그램 사용자로부터 자연수를 입력받아 0부터 자연수까지의 합계를 구할 것.

# print("아무 자연수나 입력해주세요!")
# inputNum = int(input("0부터 입력된 자연수까지 더한 값을 출력합니다. : "))

# count = 1
# totalSum1 = 0
# totalSum2 = 0

# ## while 사용
# while count <= inputNum :
#     totalSum1 += count
#     count += 1
# print("0부터" + str(inputNum)+"까지의 총 합은 " + str(totalSum1))

# ## for 사용
# for i in range(inputNum + 1) :
#     totalSum2 += i
# print("0부터" + str(inputNum) + "까지의 총 합은 " + str(totalSum2))


#------------------------------------------------------------------------

# 프로그램 사용자로부터 -1을 입력받으면 종료되는 프로그램을 작성할 것.

# code = 0
# while code != -1 :
#     print("현재 프로그램 상태 : on")
#     code = int(input("종료하려면 -1을 입력해주세요. : "))
# print("프로그램 종료")

while True:
    print("현재 프로그램 상태 : on")
    code = int(input("종료하려면 -1을 입력해주세요. : "))
    if code == -1 :
        print("프로그램 종료")
        break