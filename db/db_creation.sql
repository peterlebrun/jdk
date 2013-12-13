-- Some notes on sqlite
-- It always likes a ';' at the end of the statement, even simple one-liners
-- (i.e. "SELECT * FROM jdk_entries;" always needs a trailing semi-colon)
-- .tables to show all tables
-- .exit to exit
-- to run a file of sql commands on a db:
-- -- sqlite3 db_filename < sql_filename
-- -- i.e. sqlite3 jdk_entries.db < sql_creation.sql
-- to create a blank db:
-- -- touch filename
-- -- i.e. touch jdk_entries.db
-- to get current time in local timezone
-- DATETIME(CURRENT_TIMESTAMP, 'localtime')
-- no native support for date/time columns
-- need to store date/time as int or text
-- storing as int = unix seconds since 12/1/1970 (or something to that effect)
-- Best bet - use native functions to work with date/times

DROP TABLE IF EXISTS jdk_entries;

CREATE TABLE IF NOT EXISTS jdk_entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT
  , title CHAR(200)
  , body TEXT
  , date_created INTEGER NOT NULL -- Store unix timestamp
  , date_last_modified INTEGER NOT NULL -- Store unix timestamp
);

-- insert test data to work with
INSERT INTO jdk_entries (title, body, date_created, date_last_modified)
  VALUES ('Test Title 0', 'Test body 0', DATETIME(CURRENT_TIMESTAMP, 'localtime'), DATETIME(CURRENT_TIMESTAMP, 'localtime'));
INSERT INTO jdk_entries (title, body, date_created, date_last_modified)
  VALUES ('Test Title 1', 'Test body 1', DATETIME(CURRENT_TIMESTAMP, 'localtime'), DATETIME(CURRENT_TIMESTAMP, 'localtime'));
INSERT INTO jdk_entries (title, body, date_created, date_last_modified)
  VALUES ('Test Title 2', 'Test body 2', DATETIME(CURRENT_TIMESTAMP, 'localtime'), DATETIME(CURRENT_TIMESTAMP, 'localtime'));
INSERT INTO jdk_entries (title, body, date_created, date_last_modified)
  VALUES ('Test Title 3', 'Test body 3', DATETIME(CURRENT_TIMESTAMP, 'localtime'), DATETIME(CURRENT_TIMESTAMP, 'localtime'));
INSERT INTO jdk_entries (title, body, date_created, date_last_modified)
  VALUES ('Test Title 4', 'Test body 4', DATETIME(CURRENT_TIMESTAMP, 'localtime'), DATETIME(CURRENT_TIMESTAMP, 'localtime'));
INSERT INTO jdk_entries (title, body, date_created, date_last_modified)
  VALUES ('Test Title 5', 'Test body 5', DATETIME(CURRENT_TIMESTAMP, 'localtime'), DATETIME(CURRENT_TIMESTAMP, 'localtime'));
INSERT INTO jdk_entries (title, body, date_created, date_last_modified)
  VALUES ('Test Title 6', 'Test body 6', DATETIME(CURRENT_TIMESTAMP, 'localtime'), DATETIME(CURRENT_TIMESTAMP, 'localtime'));
INSERT INTO jdk_entries (title, body, date_created, date_last_modified)
  VALUES ('Test Title 7', 'Test body 7', DATETIME(CURRENT_TIMESTAMP, 'localtime'), DATETIME(CURRENT_TIMESTAMP, 'localtime'));
INSERT INTO jdk_entries (title, body, date_created, date_last_modified)
  VALUES ('Test Title 8', 'Test body 8', DATETIME(CURRENT_TIMESTAMP, 'localtime'), DATETIME(CURRENT_TIMESTAMP, 'localtime'));
INSERT INTO jdk_entries (title, body, date_created, date_last_modified)
  VALUES ('Test Title 9', 'Test body 9', DATETIME(CURRENT_TIMESTAMP, 'localtime'), DATETIME(CURRENT_TIMESTAMP, 'localtime'));
