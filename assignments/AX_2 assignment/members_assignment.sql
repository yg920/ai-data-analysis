CREATE SCHEMA practice; 


SELECT schema_name 
FROM information_schema.schemata 
WHERE schema_name = 'practice'; 


CREATE TABLE practice.members ( 
    member_id SERIAL PRIMARY KEY, 
    name VARCHAR(50) NOT NULL, 
    email VARCHAR(100) UNIQUE NOT NULL, 
    age INTEGER, 
    joined_at DATE 
); 

SELECT table_schema, table_name 
FROM information_schema.tables 
WHERE table_schema = 'practice' 
  AND table_name = 'members'; 

SELECT 
    column_name, 
    data_type, 
    character_maximum_length 
FROM information_schema.columns 
WHERE table_schema = 'practice' 
  AND table_name = 'members' 
ORDER BY ordinal_position; 


INSERT INTO practice.members 
(name, email, age, joined_at) 
VALUES 
('김민수', 'minsu@example.com', 25, '2026-08-01'), 
('이서연', 'seoyeon@example.com', 29, '2026-08-05'), 
('박준호', 'junho@example.com', 22, '2026-08-10'), 
('최유진', 'yujin@example.com', 31, '2026-08-15'), 
('정하늘', 'haneul@example.com', 27, '2026-08-20'); 


SELECT * 
FROM practice.members; 



SELECT name, email 
FROM practice.members; 



SELECT name, email, age 
FROM practice.members; 


SELECT * 
FROM practice.members 
WHERE age >= 25; 


SELECT * 
FROM practice.members 
WHERE name = '김민수'; 


SELECT * 
FROM practice.members 
ORDER BY age DESC; 


SELECT * 
FROM practice.members 
ORDER BY joined_at ASC; 


UPDATE practice.members 
SET age = 30 
WHERE member_id = 1; 

SELECT * 
FROM practice.members 
WHERE member_id = 1; 


SELECT * 
FROM practice.members 
WHERE member_id = 5; 


DELETE FROM practice.members 
WHERE member_id = 5; 


SELECT * 
FROM practice.members; 



SELECT COUNT(*) AS total_members 
FROM practice.members; 


SELECT AVG(age) AS average_age 
FROM practice.members; 


SELECT MAX(age) AS max_age 
FROM practice.members; 


SELECT MIN(age) AS min_age 
FROM practice.members; 


SELECT COUNT(*) AS age_25_or_more 
FROM practice.members 
WHERE age >= 25; 


SELECT * 
FROM practice.members 
ORDER BY joined_at DESC 
LIMIT 1; 


-- 1. PRIMARY KEY는 왜 필요한가요? 
-- PRIMARY KEY는 각각의 데이터를 구분하는 고유한 키값 
-- 예를 들어 이름이 같은 회원이 여러 명 있어도 member_id가 다르면 다른 회원으로 구분할 수 있다 

-- 2. WHERE 없이 UPDATE 또는 DELETE를 실행하면 어떤 문제가 발생할 수 있나요? 
-- WHERE 조건이 없으면 특정 데이터만 수정하거나 삭제하는 것이 아니라 
-- 테이블의 모든 데이터가 수정되거나 삭제될 수 있다 

-- 3. SELECT *와 필요한 컬럼만 선택하는 SQL의 차이는 무엇인가요? 
-- SELECT *는 테이블의 모든 컬럼을 조회 
-- SELECT name, email처럼 작성하면 필요한 컬럼만 조회할 수 있다 
-- 필요한 데이터만 조회하면 결과를 확인하기 쉽고 불필요한 데이터를 가져오지 않아도 된다 

-- 4. COUNT()와 AVG()는 각각 어떤 값을 계산하나요? 
-- COUNT()는 데이터의 개수를 계산 
-- AVG()는 숫자로 저장된 데이터의 평균값을 계산 

-- 5. Python에서 데이터를 처리하는 것과 DB에서 SQL로 데이터를 조회하는 것의 차이를 어떻게 이해했나요? 
-- Python에서는 데이터를 불러온 뒤 여러 조건문으로 데이터 호출이 가능함 
-- SQL에서는 데이터베이스에 저장된 데이터 중 필요한 데이터를 SELECT, WHERE, ORDER BY 등을 이용해 
-- 바로 조회하거나 정리할 수 있다 
-- 필요한 데이터를 SQL로 먼저 조회하고 Python에서 추가로도 조회가 가능함 
