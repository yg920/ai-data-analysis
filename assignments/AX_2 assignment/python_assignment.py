# AX 2회차 Ch 1 Python 기초 과제
# 리스트, 반복문, 딕셔너리, 함수, 예외처리를 직접 사용해보는 과제


# Part 1. 리스트와 반복문

scores = [78, 45, 92, 60, 55, 88, 30]

# 60점 이상인 점수 개수를 저장
pass_count = 0

print("=== Part 1 ===")

# 리스트에서 점수를 하나씩 꺼내 확인
for score in scores:
    if score >= 60:
        print(f"{score}점 : 통과")
        pass_count += 1

print(f"60점 이상인 점수 개수: {pass_count}개")


# Part 2. 딕셔너리로 단어 빈도 세기

sentence = """
파이썬 공부는 재미있다
파이썬 공부는 어렵지만 재미있다
데이터 분석에도 파이썬을 사용한다
파이썬 공부를 계속하면 실력이 늘어난다
"""

# split()으로 문장을 단어 단위로 나누기
words = sentence.split()

# 단어와 등장 횟수를 저장할 딕셔너리
word_count = {}

for word in words:
    # 이미 나온 단어면 1 증가
    if word in word_count:
        word_count[word] += 1
    else:
        # 처음 나온 단어면 1로 저장
        word_count[word] = 1

print("\n=== Part 2 ===")

# 단어와 등장 횟수 전체 출력
for word, count in word_count.items():
    print(f"{word} : {count}회")

print("\n2회 이상 등장한 단어")

for word, count in word_count.items():
    if count >= 2:
        print(f"{word} : {count}회")


# Part 3. 함수로 정리하기

def count_words(text):
    # 문자열을 단어로 나눈 뒤 빈도를 계산하는 함수
    words = text.split()
    result = {}

    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

    # 계산한 결과를 함수 밖으로 전달
    return result


def print_words_over_count(word_dict, minimum):
    # 기준 횟수 이상 나온 단어만 출력
    for word, count in word_dict.items():
        if count >= minimum:
            print(f"{word} : {count}회")


print("\n=== Part 3 ===")

result = count_words(sentence)
print_words_over_count(result, 2)


# Part 4. 오류 처리
# input()은 문자열로 들어오기 때문에 int()로 바꿔야 함
# 숫자가 아닌 값을 입력하면 ValueError가 발생할 수 있음

print("\n=== Part 4 ===")

try:
    minimum = int(input("몇 회 이상 등장한 단어를 찾을까요? : "))
    print_words_over_count(result, minimum)

except ValueError:
    print("숫자만 입력해주세요.")


# 도전 문제. 특정 단어 검색하기

search_word = input("\n검색할 단어를 입력하세요: ").strip()

if search_word in result:
    print(f"{search_word} : {result[search_word]}회 등장")
else:
    print(f"{search_word}는 등장하지 않았습니다.")


# 과제를 하면서 정리한 내용
# - for문은 여러 데이터를 하나씩(반복) 확인할 때 사용
# - 딕셔너리는 단어와 등장 횟수처럼 서로 관련된 값을 저장할 때 편리함
# - 함수로 만들면 같은 코드를 다시 사용할 수 있음
# - try-except를 사용하면 잘못된 입력 때문에 프로그램이 바로 종료되는 것을 막을 수 있음
#
# AI는 코드 오류 확인과 개념 설명에 참고했고,
# 직접 실행하면서 결과가 맞는지 확인함