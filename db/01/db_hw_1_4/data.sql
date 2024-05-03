-- 1. name의 값에 love 글자를 포함한 데이터를 조회하시오
SELECT
  *
FROM
  tracks
WHERE
  -- 대소문자 구분 안 하고 %에 뭐 안 와도 되구나
  name LIKE '%love%';

-- 2. GenreId의 값이 1이고, Milliseconds의 값이 300000 이상인 데이터를 모두 조회하여, UnitPrice 기준으로 내림차순 정렬하여 조회

SELECT
  *
FROM
  tracks
WHERE
  GenreId = 1
  AND Milliseconds >= 300000
ORDER BY
  UnitPrice DESC;

-- 3. GenreId별로 그룹화 하여, GenreId와 각 그룹별 데이터의 수를 조회하시오. 단 그룹별 데이터의 수는 TotalTracks 필드로 표기하여 나타내시오

SELECT
  GenreId, COUNT(*) AS TotalTracks
FROM
  tracks
GROUP BY
  GenreId;

-- 4. GenreId별로 그룹화 하여, GenreId와 각 그룹별 UnitPrice의 총합을 계산하여 조회. 단 UnitPrice의 총합은 TotalPrice 필드로 표기하며, 그 중 TotalPrice의 값이 100이상인 데이터만 조회

SELECT
  GenreId, SUM(UnitPrice) AS TotalPrice
FROM
  tracks
GROUP BY
  GenreId
HAVING
  TotalPrice >= 100;