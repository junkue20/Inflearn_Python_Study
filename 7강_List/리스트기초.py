# -str형 리스트 만들기
# 리스트명 = [데이터, 데이터, 데이터...]

lolChampions = ["일라오이", "사미라", "롤로노아 김동현", "니코"]
print(lolChampions)


# -데이터 접근하기

oneChamp = lolChampions[2]
print(oneChamp)


# -데이터 추가하기

lolChampions.append("이즈리얼")
print(lolChampions)


# -데이터 삭제하기

# del lolChampions[1]
# print(lolChampions)  # '사미라'가 삭제됨!


# -리스트 슬라이싱 (데이터를 가져옴)

print(lolChampions[1:4])


# -리스트 길이

print(len(lolChampions))

## 리스트 정렬 (오름차순)
lolChampions.sort()
print(lolChampions)

## 역순도 가능!
lolChampions.sort(reverse=True)
print(lolChampions)
