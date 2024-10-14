create database the_number_of_registered_vehicle;
SHOW GRANTS FOR 'skn06-1st-7team'@'localhost';
GRANT ALL PRIVILEGES ON car_accident.* TO 'skn06-1st-7team'@'localhost';
FLUSH PRIVILEGES;
use car_accident;
select * from gu;
select * from my;
select * from number;