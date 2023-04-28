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

ALTER TABLE BOOK_LOANS ADD COLUMN Late int;
UPDATE BOOK_LOANS SET Late = 0 WHERE Returned_date <= Due_date;
UPDATE BOOK_LOANS SET Late = 1 WHERE Returned_date > Due_date;

CREATE TRIGGER late_loan_insert
AFTER INSERT ON BOOK_LOANS
FOR EACH ROW
BEGIN
	UPDATE BOOK_LOANS SET Late = 0 WHERE Returned_date <= Due_date;
	UPDATE BOOK_LOANS SET Late = 1 WHERE Returned_date > Due_date;
END;

CREATE TRIGGER late_loan_update
AFTER UPDATE ON BOOK_LOANS
FOR EACH ROW
BEGIN
	UPDATE BOOK_LOANS SET Late = 0 WHERE Returned_date <= Due_date;
	UPDATE BOOK_LOANS SET Late = 1 WHERE Returned_date > Due_date;
END;

ALTER TABLE LIBRARY_BRANCH ADD COLUMN LateFee Real;
UPDATE LIBRARY_BRANCH SET LateFee = 1.00 WHERE Branch_Id = 1;
UPDATE LIBRARY_BRANCH SET LateFee = 1.50 WHERE Branch_Id = 2;
UPDATE LIBRARY_BRANCH SET LateFee = 0.75 WHERE Branch_Id = 3;

DROP VIEW IF EXISTS vBookLoanInfo;
CREATE VIEW vBookLoanInfo ('Card_No', 'Borrower Name', Date_Out, Due_Date, Returned_date, TotalDays, 'Book Title', 'Number of days later return', Branch_Id, LateFeeBalance)
AS SELECT BL.Card_No, Name, Date_Out, Due_Date, Returned_date, julianday(Returned_date) - julianday(Date_Out), Title, 
	 CASE WHEN (julianday(BL.Returned_date) - julianday(BL.Due_Date)) < 0
	 THEN 0
	 ELSE julianday(Returned_date) - julianday(Due_Date)
	 END,
Bl.Branch_Id, LateFee * (SELECT CASE 
						 WHEN (julianday(BL.Returned_date) - julianday(BL.Due_Date)) < 0 THEN 0
						 WHEN (BL.Returned_date IS NULL) THEN 0 
						 ELSE julianday(Returned_date) - julianday(Due_Date)
						 END)
FROM BOOK_LOANS BL, BORROWER B, BOOK BK, LIBRARY_BRANCH LB
WHERE BL.Card_No = B.Card_No AND BL.Branch_Id = LB.Branch_Id AND BK.Book_Id = BL.Book_Id;

select * from vBookLoanInfo;