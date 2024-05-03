-- 공통
SELECT * FROM articles;
SELECT * FROM users;
DROP TABLE articles;
DROP TABLE users;
PRAGMA table_info('articles');


-- 실습용 데이터
CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(50) NOT NULL
);

CREATE TABLE articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(50) NOT NULL,
  content VARCHAR(100) NOT NULL,
  userId INTEGER NOT NULL,
  FOREIGN KEY (userId) 
    REFERENCES users(id)
);

INSERT INTO 
  users (name)
VALUES 
  ('하석주'),
  ('송윤미'),
  ('유하선');

INSERT INTO
  articles (title, content, userId)
VALUES 
  ('제목1', '내용1', 1),
  ('제목2', '내용2', 2),
  ('제목3', '내용3', 1),
  ('제목4', '내용4', 4),
  ('제목5', '내용5', 1);


-- INNER JOIN : 두 테이블에서 값이 일치하는 레코드에 대해서만 결과를 반환

SELECT
  *
FROM
-- 메인 테이블 지정, 내용을 가지고 있는 articles 하면 되겠지
  articles

-- 메인 테이블과 조인할 테이블을 지정
INNER JOIN users
-- 조인 조건으로 두 테이블간의 레코드를 일치시키는 규칙을 지정
  ON users.id = articles.userId;

SELECT articles.title, users.name
FROM articles
INNER JOIN users
  ON users.id = articles.userId
WHERE
  users.id = 1;

-- LEFT JOIN : 오른쪽 테이블에 일치하는 레코드와 함께 왼쪽 테이블의 모든 레코드 반환
SELECT
  *
FROM
-- 왼쪽 테이블 지정
  articles
-- 오른쪽 테이블 지정
LEFT JOIN users
-- 조인 조건을 작성
  ON users.id = articles.userId;

SELECT
  *
FROM
  users
LEFT JOIN articles
-- 이후에 오는 lr는 오른쪽 테이블 기준으로 해야하나봄?
  ON articles.userId = users.id
WHERE
  articles.userId IS NULL;

-- 왼쪽 테이블의 모든 레코드를 표기,,
-- 오른쪽 테이블과 매칭되는 레코드가 없으면 NULL 표시


