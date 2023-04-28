DROP TABLE IF EXISTS PUBLISHER;
CREATE TABLE PUBLISHER (
	Publisher_Name varchar(30) not null,
	Phone char(12) not null,
	Address varchar(65) not null
);

DROP TABLE IF EXISTS LIBRARY_BRANCH;
CREATE TABLE LIBRARY_BRANCH (
	Branch_Id INTEGER not null unique,
	Branch_Name varchar (15) not null,
	Branch_Address varchar(65) not null,
	CONSTRAINT branch_primary_key PRIMARY KEY(Branch_Id)
);

DROP TABLE IF EXISTS BORROWER;
CREATE TABLE BORROWER (
	Card_No INTEGER not null unique,
	Name varchar(15) not null,
	Address varchar(65),
	Phone char(12),
	CONSTRAINT borrower_primary_key PRIMARY KEY(Card_No)
);

DROP TABLE IF EXISTS BOOK;
CREATE TABLE BOOK (
	Book_Id INTEGER not null unique,
	Title varchar(40) not null,
	Publisher_Name varchar(30) not null,
	CONSTRAINT book_primary_key PRIMARY KEY(Book_Id),
	CONSTRAINT book_foreign_key FOREIGN KEY(Publisher_Name) REFERENCES PUBLISHER(Publisher_Name)
);

DROP TABLE IF EXISTS BOOK_LOANS;
CREATE TABLE BOOK_LOANS (
	Book_Id int not null,
	Branch_Id int not null,
	Card_No int not null,
	Date_Out date not null,
	Due_Date date not null,
	Returned_date date,
	CONSTRAINT loans_foreign_key1 FOREIGN KEY(Book_Id) REFERENCES BOOK(Book_Id),
	CONSTRAINT loans_foreign_key2 FOREIGN KEY(Branch_Id) REFERENCES LIBRARY_BRANCH(Branch_Id),
	CONSTRAINT loans_foreign_key3 FOREIGN KEY(Card_No) REFERENCES BORROWER(Card_No)
);

DROP TABLE IF EXISTS BOOK_COPIES;
CREATE TABLE BOOK_COPIES (
	Book_Id int not null,
	Branch_Id int not null,
	No_Of_Copies int not null,
	CONSTRAINT copies_foreign_key1 FOREIGN KEY(Book_Id) REFERENCES BOOK(Book_Id),
	CONSTRAINT copies_foreign_key2 FOREIGN KEY(Branch_Id) REFERENCES LIBRARY_BRANCH(Branch_Id)
);

DROP TABLE IF EXISTS BOOK_AUTHORS;
CREATE TABLE BOOK_AUTHORS (
	Book_Id int not null unique,
	Author_Name varchar(25) not null,
	CONSTRAINT authors_foreign_key FOREIGN KEY(Book_Id) REFERENCES BOOK(Book_Id)
);

.import --csv --skip 1 Publisher.csv PUBLISHER
.import --csv --skip 1 Library_Branch.csv LIBRARY_BRANCH
.import --csv --skip 1 Borrower.csv BORROWER
.import --csv --skip 1 Book.csv BOOK
.import --csv --skip 1 Book_Loans.csv BOOK_LOANS
.import --csv --skip 1 Book_Copies.csv BOOK_COPIES
.import --csv --skip 1 Book_Authors.csv BOOK_AUTHORS