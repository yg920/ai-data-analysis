colums = []
with open("csv_example.txt", "r", encoding="utf-8") as file:
    for line in file:
        # print(line.strip())
        line2 = line.strip()
        columns = line2.split(',')
print(colums)
# csv.example.txt 가 여러 줄 이라면?????        