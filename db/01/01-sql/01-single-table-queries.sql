-- Data Query Language : 데이터 검색

-- 01. Querying data
-- 조회 ~~!
-- SELECT 필드명 FROM 테이블명;

SELECT 
  LastName
FROM 
  employees;

SELECT 
  LastName, FirstName
FROM 
  employees;

SELECT 
  *
FROM 
  employees;

SELECT 
  FirstName AS '이름'
FROM 
  employees;

SELECT 
  Name,
  Milliseconds / 60000 AS '재생 시간(분)'
FROM 
  tracks;

-- 02. Sorting data

SELECT 
  FirstName
FROM 
  employees
ORDER BY
  FirstName DESC;

SELECT 
  Country, City
FROM 
  customers
ORDER BY
  Country DESC,
  City;

SELECT 
  Name,
  Milliseconds / 60000 AS '재생 시간(분)'
FROM 
  tracks
ORDER BY
  Milliseconds DESC;

-- NULL 정렬 예시
-- NULL 값이 존재할 경우 오름차순에서 제일 먼저 나옴

SELECT 
  ReportsTo
FROM 
  employees
ORDER BY
  ReportsTo;

-- 03. Filtering data
-- 절

-- 'DISTINCT': 중복제거, SELECT 뒤에 붙임
SELECT DISTINCT
  Country
FROM
  customers
ORDER BY
  Country;

-- 'WHERE' : 특정 조건, FROM 절 뒤에 위치, 연산자 사용 가능
SELECT
  LastName, FirstName, City
FROM
  customers
WHERE
  City = 'Prague';

SELECT
  LastName, FirstName, City
FROM
  customers
WHERE
  City != 'Prague';

SELECT
  LastName, FirstName, Company, Country
FROM
  customers
WHERE
  Company IS NULL
  AND Country = 'USA';

SELECT
  LastName, FirstName, Company, Country
FROM
  customers
WHERE
  Company IS NULL
  OR Country = 'USA';

SELECT
  Name, Bytes
FROM
  tracks
WHERE
  -- Bytes >= 100000
  -- AND Bytes <= 500000;
  Bytes BETWEEN 100000 AND 500000
ORDER BY
  Bytes;

SELECT
  LastName, FirstName, Country
FROM
  customers
WHERE
  -- Country = 'Canada'
  -- OR Country = 'Germany'
  -- OR Country = 'France';
  Country NOT IN ('Canada', 'Germany', 'France');
  
SELECT
  LastName, FirstName
FROM 
  customers
WHERE
  -- LIKE는 패턴이 일치하는지 봄
  -- %는 0개 이상의 문자열과 일치하는지 확인, _는 단일문자와 일치하는지 확인
  LastName LIKE '%son';

SELECT
  LastName, FirstName
FROM 
  customers
WHERE
  FirstName LIKE '___a';

-- 'OFFSET' & 'LIMIT' : 조회 개수 제한
SELECT
  TrackId, Name, Bytes
FROM
  tracks
ORDER BY
  Bytes DESC
LIMIT
  7;

SELECT
  TrackId, Name, Bytes
FROM
  tracks
ORDER BY
  Bytes DESC
-- LIMIT 3, 4;
LIMIT 4 OFFSET 3;

-- 04. Grouping data : 묶어서 뭔가 한다.. 평균값, 최대, 최소 ...
-- 'GROUP BY' : 레코드를 그룹화하여 요약본 생성, 집계 함수와 함께 사용(중복제거 알아서), FROM/WHERE 뒤에 위치

-- 보여줄 필드
SELECT
  Country, COUNT(*)
FROM
  customers
-- country들을 보면서 겹치는 거는 한 그룹으로 묶고 나머지 데이터들을 그들을 기준으로 정리할 거임
-- 여기서는 count(*)니까 다 더한 거를 한 그룹별로 나타내주면 됨(그룹을 구성한 하나하나의 개수도 더해야하니까.. count를 모든 걸 다해야함)
GROUP BY
  Country;

SELECT
  Composer, AVG(Bytes) AS avgOFBytes
FROM
  tracks
GROUP BY
  Composer
ORDER BY 
  avgOFBytes DESC;

SELECT
  Composer, AVG(Milliseconds / 60000) AS avgOFMinuite
FROM
  tracks
GROUP BY
  Composer
-- 집계 항목에 대한 조건은 WHERE절이 아님
HAVING
  avgOFMinuite < 10;