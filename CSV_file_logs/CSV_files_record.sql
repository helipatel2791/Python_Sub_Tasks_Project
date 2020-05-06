create database filesrecord;
use filesrecord;
create table files(file_id int auto_increment,
                   file_name varchar(100),
                   process_status varchar(20),
                   num_rows int,
                   constraint files_pk primary key (file_id));
                   
select * from files;
truncate files;
select * from files_data;
truncate files_data;

create table files_data(file_name_id int,
                        id int,
                        age int, 
                        sex varchar(10), 
                        country varchar(7), 
                        date_confirmation date, 
                        recovered varchar(5));
                        