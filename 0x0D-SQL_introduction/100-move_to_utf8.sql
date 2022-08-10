-- Script that converts hbtn_0c_0 database to utf8
ALTER DATABASE hbtn_0c_0 CHARECTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARECTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
