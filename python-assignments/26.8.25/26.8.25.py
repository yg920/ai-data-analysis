# sentense에서 3회 이상 등장하는 단어는 무었일까요? 각 단어와 빈도수를 출력하시오
# 단 오늘 배운 딕셔너리를 활용해 주시오. 
# 지금까지 배우지 않은 기능은 사용하지 말것


sentense = "파이썬 어렵다 파이썬 힘들다 파이썬 즐겁다 파이썬 그렇다"

words = sentense.split()
dic = {}

for word in words:
    if word not in dic:
        dic[word] = 1
    else:
        dic[word] += 1

for word, count in dic.items():
    if count >= 3:
        print(f"3번 이상 사용된 단어는 {word}이고, 반복된 횟수는 {count}번입니다.")