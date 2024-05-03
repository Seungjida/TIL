-- 1. tracks 테이블의 모든 데이터 조회
SELECT
  *
FROM
  tracks;

-- 2. 특정 열의 모든 데이터 조회
SELECT
  Name, Milliseconds, UnitPrice
FROM
  tracks;

-- 3. Genreld 행의 값이 1인 모든 데이터 조회
SELECT
  *
FROM
  tracks
WHERE
  GenreId = 1;

-- 4. 모든 데이터를 name을 기준으로 오름차순 정렬하여 조회
SELECT
  *
FROM
  tracks
ORDER BY
  Name;

-- 5. tracks 테이블의 모든 데이터를 조회하되, 10개만 출력
SELECT
  *
FROM
  tracks
LIMIT
  10;