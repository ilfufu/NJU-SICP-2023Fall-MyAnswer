.read hw10_data.sql

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name,size FROM dogs,sizes WHERE height<=max AND height>min;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT d1.name FROM dogs AS d1,parents,dogs AS d2
  WHERE d1.name=child AND d2.name=parent
  ORDER BY d2.height DESC;

CREATE TABLE siblings AS
  SELECT s1.name AS name1,s2.name AS name2,s1.size AS size1
   FROM size_of_dogs AS s1, size_of_dogs AS s2, dogs AS d1, parents AS p1, dogs AS d2,
   parents AS p2
   WHERE s1.name<s2.name AND s1.size=s2.size AND s1.name=d1.name AND d1.name=p1.child
   AND s2.name=d2.name AND d2.name=p2.child AND p1.parent=p2.parent;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT "The two siblings, "||name1||" plus "||name2||" have the same size: "||size1
  FROM siblings;
