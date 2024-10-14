grant all privileges on *.* to 'skn06-1st-7team'@'localhost';
show databases;
use the_number_of_registered_vehicle;

ALTER USER 'skn06-1st-7team'@'localhost' IDENTIFIED BY '1234';
CREATE USER 'skn06-1st-7team'@'localhost' IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES ON the_number_of_registered_vehicle.* TO 'skn06-1st-7team'@'localhost';
use the_number_of_registered_vehicle;
select * from gu;
select * from MY;
select * from type;
select * from PC;
select * from number;

