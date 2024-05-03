-- Data Definition Language : 데이터의 기본 구조 및 형식 변경

-- Table 구조 확인
PRAGMA table_info('examples');

-- 1. Create a table
CREATE TABLE examples (
  -- col이름, 데이터타입, 제약조건, 레코드의 값이 중복되지 않고 1씩 자동 증가하는 필드 속성
  ExamId INTEGER PRIMARY KEY AUTOINCREMENT,
  LastName VARCHAR(50) NOT NULL,
  FirstName VARCHAR(50) NOT NULL
);

-- 2. Modifying table fields
-- ALTER TABLE statement : 테이블 및 필드 조작

-- 2.1 ADD COLUMN : 필드 추가(1개씩만)
ALTER TABLE
  examples
ADD COLUMN
  Country VARCHAR(50) NOT NULL DEFAULT 'default value';

ALTER TABLE
  examples
ADD COLUMN
  Address VARCHAR(50) NOT NULL DEFAULT 'default value';

-- sqlite는 단일 문을 사용하여 한번에 여러 열을 추가하는 것을 지원하지 않음

-- 2.2 RENAME COLUMN : 필드 이름 변경
ALTER TABLE
  examples
RENAME COLUMN
  Address TO PostCode;

-- 2.3 RENAME TO : 테이블 이름 변경
ALTER TABLE
  examples
RENAME TO
  new_examples;

-- 3. Delete a table
-- DROP TABLE 테이블 삭제
DROP TABLE new_examples;


-- sqlite는 컬럼 수정 불가
-- 대신 테이블의 이름을 바꾸고, 새 테이블을 만들고 데이터를 새 테이블에 복사하는 방식을 사용
