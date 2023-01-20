-- Create table to store Books games. 

CREATE TABLE Books (
  title varchar(255) NOT NULL, 
  author varchar(255) NOT NULL,
  isbn varchar(12),
  genre varchar(255) NOT NULL,
  my_rating float NOT NULL,
  average_rating float NOT NULL,
  date_start datetime NOT NULL,
  date_end datetime,

  PRIMARY KEY (title, author, date_start)
);