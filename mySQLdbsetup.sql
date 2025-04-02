-- Create database
CREATE DATABASE IF NOT EXISTS JF_todolist_app;

-- Use the created database
USE JF_todolist_app;

-- Create tbl_user table
CREATE TABLE IF NOT EXISTS tbl_user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Create stored procedure to insert a new user
DELIMITER //

CREATE PROCEDURE sp_createUser (
    IN p_username VARCHAR(255),
    IN p_password VARCHAR(255)
)
BEGIN
    DECLARE user_exists INT;

    -- Check if username already exists
    SELECT COUNT(*) INTO user_exists
    FROM tbl_user
    WHERE username = p_username;

    IF user_exists = 0 THEN
        -- Insert new user if username does not exist
        INSERT INTO tbl_user (username, password)
        VALUES (p_username, p_password);
    ELSE
        -- Signal an error if username already exists
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Username already exists';
    END IF;
END //

DELIMITER ;