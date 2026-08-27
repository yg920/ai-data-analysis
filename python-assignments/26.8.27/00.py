with open("python-assignments/26.8.27/memo.txt", "a", encoding="utf-8") as file:
    for num in range(1,11):
            if num < 10:
                file.write(f"새로운 내용을 추가합니다. {num}번째 \n")
            else:
                file.write(f"새로운 내용을 추가합니다. {num}번째")
print("파일 쓰기 완료")