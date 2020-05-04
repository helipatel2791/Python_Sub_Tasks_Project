create database usa_cars;
use usa_cars;

create table car(ID int,
                 Price int,
                 Brand varchar(20),
                 Model varchar(20),
                 Year int,
                 Title_Status varchar(20),
                 Mileage int,
                 Color varchar(20),
                 State varchar(20),
                 Country varchar(50),
                 current_condition varchar(30),
				constraint car_pk primary key (ID));
                
select * from car;