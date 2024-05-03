-- Data Manipulation Language : 데이터 조작

-- 공통
SELECT * FROM articles;
DROP TABLE articles;
PRAGMA table_info('articles');

-- 실습 테이블 생성
CREATE TABLE articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(100) NOT NULL,
  content VARCHAR(200) NOT NULL,
  createdAt DATE NOT NULL
);

-- 1. Insert data into table
INSERT INTO
  articles (title, content, createdAt)
VALUES
  ('title1', 'content1', '1900-01-01'),
  ('title2', 'content2', '1800-01-01'),
  ('title3', 'content3', '1700-01-01'),
  ('title4', 'content4', DATE());

-- 2. Update data in table
UPDATE 
  articles
SET
  title = 'update Title'
-- WHERE절 작성 안 하면 모든 레코드 수정
WHERE
  id = 1;

UPDATE 
  articles
SET
  title = 'update Title',
  content = 'update Content'
-- WHERE절 작성 안 하면 모든 레코드 수정
WHERE
  id = 2;

-- 3. Delete data from table
DELETE FROM
  articles
WHERE
  id = 1;

DELETE FROM
  articles
WHERE id IN (
  SELECT
    id
  FROM
    articles
  ORDER BY
    createdAt
  LIMIT
    2
);