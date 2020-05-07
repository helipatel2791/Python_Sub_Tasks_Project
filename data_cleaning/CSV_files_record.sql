create database filesrecord;
use filesrecord;

select * from files;
create table files_data(
                        id int,
                        age int, 
                        sex varchar(10), 
                        country varchar(7), 
                        date_confirmation date, 
                        recovered varchar(5));
                        