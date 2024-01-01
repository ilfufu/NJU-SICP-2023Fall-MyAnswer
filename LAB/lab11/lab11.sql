.read lab11_data.sql


CREATE TABLE bluedog AS
  SELECT color,pet FROM students WHERE color="blue" AND pet="dog";

CREATE TABLE bluedog_songs AS
  SELECT color,pet,song FROM students WHERE color="blue" AND pet="dog";


CREATE TABLE smallest_int_having AS
  SELECT time,smallest FROM students GROUP BY smallest HAVING count(*)=1;


CREATE TABLE matchmaker AS
  SELECT a.pet,a.song,a.color,b.color 
   FROM students AS a,students AS b
    WHERE a.time<b.time AND a.pet=b.pet AND a.song=b.song;


CREATE TABLE sevens AS
  SELECT stu.seven FROM students AS stu,numbers AS num
    WHERE stu.time=num.time AND stu.number=7 AND num."7"="True"
  ;


CREATE TABLE avg_difference AS
  SELECT ROUND(AVG(ABS(number-smallest))) FROM students;

