sentense = "파이썬 어렵다 파이썬 복잡하다 파이썬 즐겁다 파이썬 짱이다"
words = sentense.split()
dic = {}


# sentense에서 3회 이상 등장하는 단어는 무었일까요? 각 단어와 빈도수를 출력하시오
# 단 오늘 배운 딕셔너리를 활용해 주시오. 
# 지금까지 배우지 않은 기능은 사용하지 말것

for word in words:
    if word not in dic:
        dic[word] = 1
    else:
        dic[word] +=1
print(dic)

for word, count in dic.items():
    if count >= 3:
        print(f" 3번이상 사용된 단어는{word}이고, 반복된 횟수는 {count}번 입니다.")