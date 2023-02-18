-- Creates the database hbtn_0d_2 and the user user_0d_2
-- The user should have SELECT privilege
CREATE Database IF NOT EXISTS hbtn_0d_02;
CREATE user IF NOT EXISTS 'user_0d_2@localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2@localhost';
