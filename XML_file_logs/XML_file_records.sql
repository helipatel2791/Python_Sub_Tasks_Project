create database employee_data;
use employee_data;

create table employee(file_id int,
                      employee_id int,
                      name varchar(15),
                        age int, 
                        sex varchar(10), 
                        country varchar(20), 
                        date_joined date, 
                        points float4);
                        
                        
create table files(file_id int auto_increment,
                   file_name varchar(100),
                   process_status varchar(20),
                   num_rows int,
                   constraint files_pk primary key (file_id));