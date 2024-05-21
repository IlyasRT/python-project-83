CREATE TABLE urls (
  id bigint PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  created_at DATE NOT NULL
);


insert into "urls" ("id", "name", "created_at") values ('1', 'hexlet.io', '2024-05-13');