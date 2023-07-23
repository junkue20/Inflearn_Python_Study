# 게임 프로그래밍 예제

while True :
    print("[메뉴를 입력하세요.]")
    remote = int(input("1. 게임시작  2. 랭킹보기  3. 게임종료"+"\n"))

    if remote == 1 :
        print("-> 게임을 시작합니다! <-")
    elif remote == 2 :
        print("-> 랭킹보기 <-")
    elif remote == 3 :
        print("-> 게임을 종료합니다. <-")
        break
    else :
        print("-> 다시 입력해 주세요 <-")
    