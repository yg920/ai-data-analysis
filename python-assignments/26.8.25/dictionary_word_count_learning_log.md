# Python 딕셔너리 단어 빈도수 과제 — AI와 단계별 문제 해결 기록

> 목표: 완성 코드를 바로 받지 않고, 지금까지 배운 `split()`, 딕셔너리, `for`, `if`, `else`, `in`, `items()`, f-string만 활용해 문제를 단계별로 해결한다.

## 과제

```python
sentense = "나는 대한민국 서울 수로에서 파이썬 공부를 하고 있습니다" # 단어가 100개 이상
words = sentense.split()

print(type(words))
print(words)

# sentense에서 3회 이상 등장하는 단어는 무었일까요? 각 단어와 빈도수를 출력하시오
# 단 오늘 배운 딕셔너리를 활용해 주시오.
# 지금까지 배우지 않은 기능은 사용하지 말것
```

---

## 문제 해결 과정

### 1단계 — 빈 딕셔너리 만들기

**AI:** 단어별 등장 횟수를 저장할 빈 딕셔너리가 필요하다. 변수 이름을 정해서 만들어보자.

**나:**

```python
sentense = "나는 대한민국 서울 수로에서 파이썬 공부를 하고 있습니다"
words = sentense.split()
dic = {}
```

**배운 점:** `{}`는 빈 딕셔너리다.

---

### 2단계 — words에서 단어 하나씩 꺼내기

**AI:** `words`에 들어 있는 단어를 처음부터 하나씩 꺼내려면 `for`문을 어떻게 작성할까?

**나의 첫 시도:**

```python
for dic in words:
```

**AI 피드백:** `dic`은 이미 딕셔너리 변수 이름으로 사용하고 있으므로, 단어 하나를 의미하는 변수 이름을 사용하는 것이 좋다.

**나의 수정:**

```python
for word in words:
```

**배운 점:** `words`에서 단어를 하나씩 꺼내 `word`에 넣는다.

---

### 3단계 — 단어가 딕셔너리에 존재하는지 확인하기

**AI:** 현재 `word`라는 키가 `dic` 안에 있는지 먼저 확인하려면 `[]`, `get()`, `in` 중 무엇을 사용해야 할까?

**나:** `get()`

**AI:** `get()`은 없는 키를 안전하게 조회할 때 사용한다. 존재 여부를 먼저 확인할 때는 다른 방법이 있다.

**나:** `[]`

**AI:** `[]`는 반드시 존재해야 하는 키의 값을 조회할 때 사용한다. 존재 여부 판단은 `in`이다.

**나:** `in`

**배운 점:**

```text
반드시 필요한 키       → []
없을 수도 있는 키      → get()
키 존재 여부 먼저 확인 → in
```

---

### 4단계 — 아직 등장하지 않은 단어 확인하기

**AI:** 현재 `word`가 `dic` 안에 **없는지** 확인해보자.

**나의 첫 시도:**

```python
for word in words:
    if word in not wors
```

이후 수정 시도:

```python
for word in words:
    if word in not words
```

다시 수정 시도:

```python
for word in words:
    if word in not dic
```

**AI 피드백:** `not`과 `in`의 순서는 `not in`이다. 또한 확인 대상은 전체 단어 리스트 `words`가 아니라 빈도수를 저장할 `dic`이다.

**수정된 조건:**

```python
for word in words:
    if word not in dic:
```

**배운 점:**

```python
word not in dic
```

은 `word`라는 **키가 dic에 없는가?**라는 뜻이다.

---

### 5단계 — 처음 등장한 단어를 1로 저장하기

**AI:** 처음 등장한 단어라면 딕셔너리를 `{"파이썬": 1}` 같은 형태로 만들어야 한다.

**나의 첫 시도:**

```python
for word in words:
    if word not in dic{word, 1}
```

**AI 피드백:** 딕셔너리에 값을 저장하는 기본 형태는 다음과 같다.

```python
딕셔너리[키] = 값
```

**나의 다음 시도:**

```python
for word in words:
    if word not in dic[word] = 1
```

**AI 피드백:** 조건과 조건이 참일 때 실행할 명령은 서로 다른 줄에 작성한다.

**나의 수정:**

```python
for word in words:
    if word not in dic:
        dic[word] = 1
```

**배운 점:**

```python
dic[word] = 1
```

에서 `word`는 **키**, `1`은 **값**이다.

---

### 6단계 — 이미 등장한 단어 처리하기

**AI:** 같은 단어가 다시 등장하면 `if word not in dic:` 조건은 거짓이 된다. `if` 조건이 거짓일 때 사용하는 키워드는?

**나:**

```text
else
```

**구조:**

```python
for word in words:
    if word not in dic:
        dic[word] = 1
    else:
        ???
```

---

### 7~8단계 — 기존 등장 횟수에 1 더하기

**나의 첫 시도:**

```python
for word in words:
    if word not in dic:
        dic[word] = 1
    else:
        dic[word] =+1
```

**AI 피드백:** `=+ 1`이 아니라 기존 값에 1을 더하려면 `+= 1`을 사용한다.

**나의 수정:**

```python
for word in words:
    if word not in dic:
        dic[word] = 1
    else:
        dic[word] += 1
```

**배운 점:**

```python
dic[word] += 1
```

은 `dic[word]`의 현재 값에 1을 더해서 다시 저장한다는 뜻이다.

---

### 9단계 — 빈도수 딕셔너리 확인하기

**AI:** 지금까지 만든 딕셔너리가 제대로 만들어졌는지 전체를 출력해서 확인해보자.

**나:**

```python
for word in words:
    if word not in dic:
        dic[word] = 1
    else:
        dic[word] +=1

print(dic)
```

**배운 점:** 중간 결과를 출력해보면 코드가 예상대로 동작하는지 검증할 수 있다.

---

### 10단계 — 키와 값을 동시에 가져오는 방법

**AI:** 과제는 모든 단어가 아니라 3회 이상 등장한 단어와 빈도수를 출력해야 한다. 딕셔너리에서 키와 값을 동시에 가져오려면 `keys()`, `values()`, `items()` 중 무엇을 사용할까?

**나:**

```text
items()
```

**배운 점:**

```text
keys()   → 키
values() → 값
items()  → 키와 값
```

---

### 11~12단계 — items()를 for문에서 사용하기

**AI:** `dic.items()`에서 단어와 횟수를 동시에 꺼내보자.

**나의 첫 시도:**

```python
for word, words in dic.items()
```

**AI 피드백:** 두 번째 변수에는 여러 단어가 아니라 해당 단어의 **횟수**가 들어가므로 `count`라는 이름이 이해하기 쉽다. 끝에는 `:`도 필요하다.

**나의 수정:**

```python
for word, count in dic.items():
```

**배운 점:**

```text
word  → 키(단어)
count → 값(등장 횟수)
```

---

### 13단계 — 3회 이상인지 조건 확인하기

**AI:** `count`가 3보다 크거나 같은지 `if`문으로 표현해보자.

**나:**

```python
if count >= 3:
```

---

### 14~15단계 — 단어와 횟수 출력하기

**나의 첫 시도:**

```python
print(f" 3번이상 사용된 단어는{dic}이고, 반복된 횟수는 {count}번 입니다.")
```

**AI 피드백:** `dic`은 딕셔너리 전체이고, 현재 확인 중인 단어 하나는 `word`에 들어 있다.

**나의 수정:**

```python
print(f" 3번이상 사용된 단어는{word}이고, 반복된 횟수는 {count}번 입니다.")
```

**배운 점:**

```text
dic   → 전체 딕셔너리
word  → 현재 단어 하나
count → 현재 단어의 등장 횟수
```

---

### 16단계 — 조건 안에 출력문 넣기

**나:**

```python
for word, count in dic.items():
    if count >= 3:
        print(f" 3번이상 사용된 단어는{word}이고, 반복된 횟수는 {count}번 입니다.")
```

3회 이상이라는 조건을 만족한 단어만 출력하도록 완성했다.

---

### 17단계 — 전체 코드 직접 조립하기

AI가 완성 코드를 보여주지 않은 상태에서 처음부터 끝까지 직접 작성했다.

```python
sentense = "나는 대한민국 서울 수로에서 파이썬 공부를 하고 있습니다" # 단어가 100개 이상
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
```

**AI 확인:** 과제의 핵심 로직은 맞았다.

---

### 18~20단계 — 테스트 문장 만들기

기존 예제 문장에는 같은 단어가 3회 이상 등장하지 않기 때문에, 코드를 검증하기 위한 테스트 문장을 직접 만들었다.

**나의 첫 테스트 문장:**

```text
파이썬에 파이썬에의한 파이썬을 위한 정의
```

**AI 질문:** `split()`은 띄어쓰기를 기준으로 나누기 때문에 다음 문자열들을 같은 단어로 볼까?

```text
파이썬에
파이썬에의한
파이썬을
```

**나:** 다르다.

**배운 점:** 문자열은 정확히 같아야 딕셔너리에서 같은 키로 처리된다.

---

### 21~24단계 — 실제 빈도수와 출력 결과 예측하기

**나의 다음 테스트 문장:**

```text
파이썬 어렵다 파이썬 힘들다 파이썬 즐겁다 파이썬 그렇다
```

**AI:** `파이썬`은 몇 번 등장하는가?

**나:** 4

따라서 딕셔너리에는 다음과 같이 저장될 수 있다.

```python
'파이썬': 4
```

조건:

```python
count >= 3
```

실제 값을 넣으면:

```python
4 >= 3
```

**나:** `True`

따라서 예상 출력은:

```text
3번 이상 사용된 단어는 파이썬이고, 반복된 횟수는 4번입니다.
```

직접 실행하기 전에 결과를 예상하면서 로직을 검증했다.

---

### 25~30단계 — 코드를 한국어로 설명하기

**AI:** 다음 코드를 코드 용어 없이 설명해보자.

```python
for word in words:
    if word not in dic:
        dic[word] = 1
    else:
        dic[word] += 1
```

**나의 첫 설명:**

> word에 words를 넣어서 하나씩 확인한다.  
> 만약 word에 dic안에 있는 값이 없다면  
> dic 안에 word 는 1이다.  
> 만약 그렇지 않다면  
> dic에 word count를 하나씩 추가한다.

**AI 피드백:** 전체 흐름은 맞지만 딕셔너리의 **키와 값**이 섞여 있다.

예시:

```python
dic = {
    "파이썬": 4,
    "AI": 2
}
```

**나의 구분:**

```text
키 : 파이썬
값 : 4
키 : AI
값 : 2
```

이후 다시 설명하면서 다음을 확인했다.

```python
if word not in dic:
```

은 `word`가 `dic`의 **키에 없는지** 확인한다.

```python
dic[word] = 1
```

에서는 `word`가 **키**, `1`이 **값**이다.

```python
dic[word] += 1
```

에서는 이미 존재하는 `word` 키의 **값에 1을 더한다.**

최종적으로 코드의 의미를 다음처럼 정리했다.

> `words`에서 단어를 하나씩 꺼내 `word`에 넣는다.  
> `word`가 `dic`의 키에 없다면 `word`를 새로운 키로 저장하고 값을 1로 만든다.  
> 이미 `word`가 `dic`의 키에 있다면 그 키의 값에 1을 더한다.

---

## 최종 코드

```python
sentense = "파이썬 어렵다 파이썬 힘들다 파이썬 즐겁다 파이썬 그렇다"
words = sentense.split()
dic = {}

for word in words:
    if word not in dic:
        dic[word] = 1
    else:
        dic[word] += 1

print(dic)

for word, count in dic.items():
    if count >= 3:
        print(f"3번 이상 사용된 단어는 {word}이고, 반복된 횟수는 {count}번입니다.")
```

## 이번 문제에서 직접 익힌 핵심

- `{}`로 빈 딕셔너리를 만든다.
- `for word in words:`로 리스트에서 단어를 하나씩 꺼낸다.
- `word not in dic`으로 단어가 딕셔너리의 키에 없는지 확인한다.
- `dic[word] = 1`에서 `word`는 키이고 `1`은 값이다.
- 이미 존재하는 단어는 `dic[word] += 1`로 빈도수를 증가시킨다.
- `items()`를 사용하면 딕셔너리의 키와 값을 함께 꺼낼 수 있다.
- `count >= 3`으로 3회 이상 등장했는지 판단할 수 있다.
- `dic`은 전체 딕셔너리, `word`는 현재 단어, `count`는 현재 단어의 빈도수다.
- `=+ 1`과 `+= 1`은 다르다.
- `word in not dic`이 아니라 `word not in dic`이라고 작성한다.
- `split()`은 현재 코드에서 띄어쓰기를 기준으로 문자열을 나누므로 `파이썬`, `파이썬을`, `파이썬에`는 서로 다른 문자열이다.
- 코드를 실행하기 전에 테스트 데이터와 예상 결과를 직접 생각해보면 오류를 찾는 데 도움이 된다.

## 문제 해결 방식에서 배운 점

이번 과제에서는 AI에게 완성 코드를 바로 요청하지 않았다.

```text
문제 확인
↓
한 단계의 힌트 받기
↓
직접 작성
↓
실수 확인
↓
힌트를 조금 더 받기
↓
직접 수정
↓
테스트 데이터 만들기
↓
결과 예상
↓
코드를 한국어로 설명
```

처음에는 하나의 큰 문제처럼 보였지만, 문제를 작은 단계로 나누자 지금까지 배운 문법만으로도 직접 해결할 수 있었다.

> **오늘의 핵심: 정답을 외우는 것보다, 문제를 작은 단계로 나누어 스스로 정답에 도달하는 과정을 연습한다.**
