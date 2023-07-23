# for 반복문
## for a in [1, 2, 3, 4] :
##      print(a)

lolChampions = ["리신", "마오카이", "헤카림", "아무무"]

for jungleChapion in lolChampions :
    print(jungleChapion)


    if jungleChapion == '마오카이' :
        print(jungleChapion + " 정글은 6렙이후 궁극기를 통한 갱킹이 좋습니다.")
    
    elif jungleChapion > '리신' :
        print(jungleChapion + "은 무난한 난이도의 챔피언입니다")

    elif jungleChapion == '리신' :
        print(jungleChapion + "은 초반 갱킹 싸움에서 좋은 성능을 보여줍니다.")
    

# range() 함수


## ex) range(5) => 0부터 4까지 순서열을 반환

for i in range(10):
    print (i, "분") # 숫자와 함께 사용하기 위해서는 ',' 쉼표표시 사용


## ex2) range(2,8) => 2부터 7까지의 숫자가 나옴.

for i in range(3, 11):
    print ("카운트 :", i) # 숫자와 함께 사용하기 위해서는 ',' 쉼표표시 사용


## ex3) range(1, 10, 2) => 1, 3, 5, 7, 9 와 같이 '2'씩 증가함.
for i in range(1, 14, 2):
    print ("2씩카운트 :", i)
