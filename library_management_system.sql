create database library_management_system;
use library_management_system;

create table books(
book_id int auto_increment primary key,
title varchar(255) not null,
author varchar(255) not null,
publisher varchar(255),
published_year int,
isbn varchar(13),
copies_available int not null,
total_copies int not null);

create table members(
member_id int auto_increment primary key,
name varchar(255) not null,
email varchar(255) not null,
phone varchar(15),
join_date date not null,
membership_type varchar(50));

create table loans(
loan_id int auto_increment primary key,
book_id int,
member_id int,
loan_date date not null,
due_date date not null,
return_date date,
foreign key (book_id) references books(book_id),
foreign key (member_id) references members(member_id));

/*
Relationships
Books table and member table have many-to-many relationship through Loans table
Books table can optionally have many-to-many relationship  with categories through book categories table
*/

show tables;




INSERT INTO books (title, author, publisher, published_year, isbn, total_copies, copies_available) VALUES
('To Kill a Mockingbird', 'Harper Lee', 'J.B. Lippincott & Co.', 1960, '9780060935467', 5, 5),
('1984', 'George Orwell', 'Secker & Warburg', 1949, '9780451524935', 3, 3),
('The Great Gatsby', 'F. Scott Fitzgerald', 'Charles Scribner\'s Sons', 1925, '9780743273565', 4, 4),
('Moby Dick', 'Herman Melville', 'Harper & Brothers', 1851, '9781503280786', 2, 2),
('Pride and Prejudice', 'Jane Austen', 'T. Egerton', 1813, '9781503290563', 6, 6);


INSERT INTO members (name, email, phone, join_date, membership_type) VALUES
('Alice Smith', 'alice@example.com', '1234567890', '2023-01-15', 'Regular'),
('Bob Johnson', 'bob@example.com', '0987654321', '2023-02-20', 'Premium'),
('Charlie Brown', 'charlie@example.com', '5555555555', '2023-03-10', 'Regular'),
('Diana Prince', 'diana@example.com', '1112223333', '2023-04-05', 'Premium');



INSERT INTO loans (book_id, member_id, loan_date, due_date) VALUES
(1, 1, '2023-09-01', '2023-09-15'),
(2, 2, '2023-09-10', '2023-09-24'),
(3, 3, '2023-09-15', '2023-09-29');

select * from books;
select * from members;
select * from loans;