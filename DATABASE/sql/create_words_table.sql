CREATE TABLE Words (
  ObjectPath VARCHAR(255),
  Date DATETIME DEFAULT CURRENT_TIMESTAMP,
  AmountOfWords INT,
  PRIMARY KEY (ObjectPath, Date)
);