-- Creates the database hbtn_0d_2 and the user user_0d_2
CREATE Database IF NOT EXISTS hbtn_0d_02;
CREATE user IF NOT EXISTS 'user_0d_2' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON Database TO 'user_0d_2@localhost';
