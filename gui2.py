from tkinter import *

import sqlite3
import random


# create tkinter window 

root = Tk()

root.title('Library Database Management System')

root.geometry("400x400")


LMS_connect = sqlite3.connect('LMS.db')

LMS_cur = LMS_connect.cursor()


def accPublisher(pub_name, pub_phone, pub_addr):
	accPub_conn = sqlite3.connect('LMS.db')

	accPub_curr = accPub_conn.cursor()

	accPub_curr.execute("INSERT INTO PUBLISHER VALUES (:pub_name, :pub_phone, :pub_addr) ",
		{
			'pub_name': pub_name.get(),
			'pub_phone': pub_phone.get(),
			'pub_addr': pub_addr.get()
		})

	#commit changes
	accPub_conn.commit()
	#close the DB connection
	accPub_conn.close()

def newPublisher():
	sub = Tk()
	
	sub.title("Update Publisher")
	sub.geometry("400x400")

	pub_name = Entry(sub, width = 30)
	pub_name.grid(row = 0, column = 1, padx = 20)

	pub_phone = Entry(sub, width = 30)
	pub_phone.grid(row = 1, column = 1)

	pub_addr = Entry(sub, width = 30)
	pub_addr.grid(row = 2, column = 1)

	Pub_name_label = Label(sub, text = 'Publisher Name: ')
	Pub_name_label.grid(row = 0, column = 0)

	Pub_phone_label = Label(sub, text = 'Publisher Phone: ')
	Pub_phone_label.grid(row = 1, column = 0)

	Pub_addr_label = Label(sub, text = 'Publisher Addr: ')
	Pub_addr_label.grid(row = 2, column = 0)

	submit_btn = Button(sub, text =' Add Publisher', command = lambda: accPublisher(pub_name,pub_phone,pub_addr))
	submit_btn.grid(row = 3, column = 1, columnspan = 1, pady = 10, padx = 10, ipadx = 140)
	acc_Publisher_btn = Button(sub, text ='Cancel      ', command = sub.destroy)
	acc_Publisher_btn.grid(row = 4, column = 1, columnspan = 1, pady = 10, padx = 10, ipadx = 140)

	sub.mainloop()

def newBook():
	sub = Tk()
	
	sub.title("New Book")
	sub.geometry("400x400")

	book_auth = Entry(sub, width = 30)
	book_auth.grid(row = 0, column = 1)

	book_title = Entry(sub, width = 30)
	book_title.grid(row = 1, column = 1)

	book_publisher = Entry(sub, width = 30)
	book_publisher.grid(row = 2, column = 1)

	book_id = Entry(sub, width = 30)
	book_id.grid(row = 3, column = 1)

	book_auth_label = Label(sub, text = 'Book Author: ')
	book_auth_label.grid(row = 0, column = 0)

	book_title_label = Label(sub, text = 'Book Title: ')
	book_title_label.grid(row = 1, column = 0)

	book_publisher_label = Label(sub, text = 'Book Publisher: ')
	book_publisher_label.grid(row = 2, column = 0)

	book_id_label = Label(sub, text = 'Book ID: ')
	book_id_label.grid(row = 3, column = 0)

	def accBook(book_auth,book_title,book_publisher,book_id):
		accBook_conn = sqlite3.connect('LMS.db')
		accBook_curr = accBook_conn.cursor()

		accBook_curr.execute("INSERT INTO BOOK VALUES (:book_id, :book_title, :book_publisher) ",
			{	
				'book_id': book_id.get(),
				'book_title': book_title.get(),
				'book_publisher': book_publisher.get()
			})
		
		accBook_curr.execute("INSERT INTO BOOK_AUTHORS VALUES (:book_id, :book_auth) ",
			{	
				'book_id': book_id.get(),
				'book_auth': book_auth.get()
			})
		
		branches = accBook_curr.execute("SELECT Branch_Id FROM LIBRARY_BRANCH").fetchall()

		for branch in branches:
			branch_id = branch[0]
			accBook_curr.execute("INSERT INTO BOOK_COPIES VALUES (:book_id, :branch_id, :no_of_copies) ",
					{
						'book_id': book_id.get(),
						'branch_id': branch_id,
						'no_of_copies': 5
					})
		book_copies = accBook_curr.execute("SELECT * FROM BOOK_COPIES").fetchall()
		updated_copies = "Book_Id | Branch_Id | No_Of_Copies\n"
		for copy in book_copies:
			updated_copies += str(str(copy[0]) + " | " + str(copy[1]) + " | " + str(copy[2]) + "\n")
		print(updated_copies)
		result_label.config(text = updated_copies)
		root.update_idletasks()
		
		#commit changes
		accBook_conn.commit()
		#close the DB connection
		accBook_conn.close()
		cancelBook()

	def listBooks(book_title):
		accBook_conn = sqlite3.connect('LMS.db')
		accBook_curr = accBook_conn.cursor()

		# Given a book title list the number of copies loaned out per branch.
		accBook_curr.execute(" SELECT Branch_Name, COUNT(*) FROM BOOK_LOANS NATURAL JOIN LIBRARY_BRANCH NATURAL JOIN BOOK NATURAL JOIN BOOK COPIES WHERE Title =:book_title GROUP BY Branch_Name",
			{
				'book_title': book_title.get(),
			})
		
		results = accBook_curr.fetchall()

		print_result = 'Branch | Num Copies\n'

		for result in results:
			print_result += str(result[0] + ": " + str(result[1]) + "\n")
		print(print_result)
		result_label.config(text = print_result)
		root.update_idletasks()
		cancelBook()

		#commit changes
		accBook_conn.commit()
		#close the DB connection
		accBook_conn.close()
	def cancelBook():
		sub.destroy()
		

	submit_btn3 = Button(sub, text =' Add New Book', command = lambda: accBook(book_auth,book_title,book_publisher,book_id))
	submit_btn3.grid(row = 4, column = 1, columnspan = 1, pady = 10, padx = 10, ipadx = 140)

	submit_btn4 = Button(sub, text =' List Copies', command = lambda: listBooks(book_title))
	submit_btn4.grid(row = 5, column = 1, columnspan = 1, pady = 10, padx = 10, ipadx = 140)

	acc_Book_btn = Button(sub, text ='Cancel      ', command = sub.destroy)
	acc_Book_btn.grid(row = 6, column = 1, columnspan = 1, pady = 10, padx = 10, ipadx = 140)

	sub.mainloop()

def newBorrower():
	sub = Tk()
	
	sub.title("New Borrower")
	sub.geometry("400x400")

	accBor_conn = sqlite3.connect('LMS.db')

	accBor_curr = accBor_conn.cursor()

	bor_name = Entry(sub, width = 30)
	bor_name.grid(row = 0, column = 1)

	bor_addr = Entry(sub, width = 30)
	bor_addr.grid(row = 1, column = 1)

	bor_phone = Entry(sub, width = 30)
	bor_phone.grid(row = 2, column = 1)

	bor_name_label = Label(sub, text = 'Borrower Name: ')
	bor_name_label.grid(row = 0, column = 0)

	bor_phone_label = Label(sub, text = 'Borrower Phone: ')
	bor_phone_label.grid(row = 1, column = 0)

	bor_addr_label = Label(sub, text = 'Borrower Addr: ')
	bor_addr_label.grid(row = 2, column = 0)

	def accBorrower():
		print("accBorrower called")
		print(bor_name.get())
		print(bor_phone.get())
		print(bor_addr.get())
		accBor_curr.execute("INSERT INTO BORROWER VALUES (NULL, :bor_name, :bor_addr, :bor_phone ) ",
			{
				'bor_name': bor_name.get(),
				'bor_phone': bor_phone.get(),
				'bor_addr': bor_addr.get()
			})
		printBorrower()
	
	def printBorrower():
		print("printBorrower called")
		print(bor_name.get())
		print(bor_phone.get())
		print(bor_addr.get())
		text1 = "Your Card number: "
		text1 += str(accBor_curr.execute("SELECT Card_No FROM BORROWER WHERE Name = :bor_name AND Address = :bor_addr AND Phone = :bor_phone",
			{
				'bor_name': bor_name.get(),
				'bor_addr': bor_addr.get(),
				'bor_phone': bor_phone.get()
			}).fetchone()[0])
		print(text1)
		result_label.config(text = text1)
		cancelBorrower()
	def cancelBorrower():
		accBor_conn.commit()
		accBor_conn.close()
		sub.destroy()

	submit_btn2 = Button(sub, text =' Add Borrower', command = lambda: [accBorrower()])
	submit_btn2.grid(row = 3, column = 1, columnspan = 1, pady = 10, padx = 10, ipadx = 140)

	acc_Borrower_btn = Button(sub, text ='Cancel      ', command = lambda: cancelBorrower())
	acc_Borrower_btn.grid(row = 4, column = 1, columnspan = 1, pady = 10, padx = 10, ipadx = 140)

	sub.mainloop()

# newLoan
def newLoan():
	sub = Tk()

	sub.title("New Book Loan")
	sub.geometry("400x400")

	loan_bkID = Entry(sub, width = 30)
	loan_bkID.grid(row = 0, column = 1)

	loan_bchID = Entry(sub, width = 30)
	loan_bchID.grid(row = 1, column = 1)

	loan_cardNo = Entry(sub, width = 30)
	loan_cardNo.grid(row = 2, column = 1)

	loan_date_ot = Entry(sub, width = 30)
	loan_date_ot.grid(row = 3, column = 1)

	loan_date_du = Entry(sub, width = 30)
	loan_date_du.grid(row = 4, column = 1)

	loan_date_rtn = Entry(sub, width = 30)
	loan_date_rtn.grid(row = 5, column = 1)

	loan_bkID_label = Label(sub,text = 'Book ID: ')
	loan_bkID_label.grid(row = 0, column = 0)

	loan_bchID_label = Label(sub, text = 'Library Branch ID: ')
	loan_bchID_label.grid(row = 1, column = 0)

	loan_cardNo_label = Label(sub, text = 'Borrower Card No: ')
	loan_cardNo_label.grid(row = 2, column = 0)

	loan_date_ot_label = Label(sub, text = 'Date Out: ')
	loan_date_ot_label.grid(row = 3, column = 0)

	loan_date_du_label = Label(sub, text = 'Date Due: ')
	loan_date_du_label.grid(row = 4, column = 0)

	loan_date_rtn_label = Label(sub, text = 'Date Returned: ')
	loan_date_rtn_label.grid(row = 5, column = 0)

	submit_btn = Button(sub, text =' Add Loan', command = lambda: accLoan())
	submit_btn.grid(row = 6, column = 1, columnspan = 1, pady = 10, padx = 10, ipadx = 140)

	acc_Borrower_btn = Button(sub, text ='Cancel ', command = sub.destroy)
	acc_Borrower_btn.grid(row = 7, column = 1, columnspan = 1, pady = 10, padx = 10, ipadx = 140)

	
	def accLoan():
		accLN_conn = sqlite3.connect('LMS.db')

		accLN_curr = accLN_conn.cursor()

		accLN_curr.execute("INSERT INTO BOOK_LOANS VALUES (:loan_bkID, :loan_bchID, :loan_cardNo, :loan_date_ot, :loan_date_du, :loan_date_rtn, NULL) ",
			{
				'loan_bkID': loan_bkID.get(),
				'loan_bchID': loan_bchID.get(),
				'loan_cardNo': loan_cardNo.get(),
				'loan_date_ot': loan_date_ot.get(),
				'loan_date_du': loan_date_du.get(),
				'loan_date_rtn': loan_date_rtn.get()
			})

		accLN_curr.execute("UPDATE BOOK_COPIES SET No_Of_Copies = No_Of_Copies - 1 WHERE Book_Id = :loan_bkID AND Branch_Id = :bchID",
			{
				'loan_bkID': loan_bkID.get(),
				'bchID': loan_bchID.get()

			})
		updated = accLN_curr.execute("SELECT * FROM BOOK_COPIES").fetchall()

		updated_copies = "Book_Id | Branch_Id | No_Of_Copies\n"
		for copy in updated:
			updated_copies += str(str(copy[0]) + " | " + str(copy[1]) + " | " + str(copy[2]) + "\n")
		print(updated_copies)
		result_label.config(text = updated_copies)
		root.update_idletasks()

		#commit changes
		accLN_conn.commit()
		#close the DB connection
		accLN_conn.close()
		sub.destroy()

	sub.mainloop()

def newAuthor():
	sub = Tk()
	
	sub.title("New Author")
	sub.geometry("400x400")

	accLN_conn = sqlite3.connect('LMS.db')
	accLN_curr = accLN_conn.cursor()


	bk_ID = Entry(sub, width = 30)
	bk_ID.grid(row = 0, column = 1)

	auth_name = Entry(sub, width = 30)
	auth_name.grid(row = 1, column = 1)

	bk_ID_label = Label(sub, text = 'Book ID: ')
	bk_ID_label.grid(row = 0, column = 0)

	auth_name_label = Label(sub, text = 'Author Name: ')
	auth_name_label.grid(row = 1, column = 0)

	submit_btn2 = Button(sub, text =' Add Author', command = lambda: accAuthor())
	submit_btn2.grid(row = 3, column = 1, columnspan = 1, pady = 10, padx = 10, ipadx = 140)

	acc_Borrower_btn = Button(sub, text ='Cancel      ', command = lambda: cancelAuthor())
	acc_Borrower_btn.grid(row = 4, column = 1, columnspan = 1, pady = 10, padx = 10, ipadx = 140)

	sub.mainloop()

	def accAuthor():
		accLN_curr.execute("INSERT INTO BOOK_AUTHORS VALUES (:bk_ID, :auth_name )",
			{
				'bk_ID': bk_ID.get(),
				'auth_name': auth_name.get(),
			})
		cancelAuthor()
	def cancelAuthor():
		accLN_conn.commit()
		accLN_conn.close()
		sub.destroy()

def viewLoanBWR():
	sub = Tk()
	sub.title("List Borrowed Books")
	sub.geometry("400x400")

	LoanBWR_conn = sqlite3.connect('LMS.db')

	LoanBWR_curr = LoanBWR_conn.cursor()

	bwer_ID = Entry(sub, width = 30)
	bwer_ID.grid(row = 0, column = 1)

	bwer_name = Entry(sub, width = 30)
	bwer_name.grid(row = 1, column = 1)

	bwer_ID_label = Label(sub, text = 'Borrower ID:')
	bwer_ID_label.grid(row = 0, column = 0)

	bwer_name_label = Label(sub, text = 'Borrower Name:')
	bwer_name_label.grid(row = 1, column = 0)

	def viewLoans():
		nones = 0
		conditions = ' '
		print(bwer_ID.get())
		print(bwer_name.get())
		if len(bwer_ID.get()) == 0:
			nones += 1
		else:
			conditions += str("Card_No = " + bwer_ID.get())

		if len(bwer_name.get()) == 0:
			nones += 1
		else:
			if nones == 0:
				conditions += " AND "
			conditions += str("[Borrower Name] LIKE '%" + bwer_name.get() + "%'")

		if nones < 2:
			conditions = "WHERE" + conditions
		elif nones == 2:
			conditions = "Order By LateFeeBalance DESC"
		conditions = "Select Card_No, [Borrower Name], LateFeeBalance from vBookLoanInfo " + conditions
		print(conditions)
		LoanBWR_curr.execute(conditions)
		results = LoanBWR_curr.fetchall()
		printLoans(results)
	def printLoans(results):
		record = "Card_No | Borrower Name | LateFeeBalance\n"
		for result in results:
			record += str(str(result[0]).ljust(10) + " | " + str(result[1]).ljust(15) + " | " + str("$%.2f" % float(result[2])) + "\n")
		result_label.config(text = record)
		root.update_idletasks()
		cancel()
	def cancel():
		LoanBWR_conn.commit()
		LoanBWR_conn.close()
		sub.destroy()

	submit_btn = Button(sub, text = 'List Loans', command = lambda: viewLoans())
	submit_btn.grid(row = 2, column = 1, columnspan = 1, pady = 10, padx = 10, ipadx = 140)

	cancel_btn = Button(sub, text = 'Cancel', command = lambda: cancel())
	cancel_btn.grid(row = 3, column = 1, columnspan = 1, pady = 10, padx = 10, ipadx = 140)

f_name_label = Label(root, text = 'Publisher')
f_name_label.grid(row =0, column = 0)
b1_label = Label(root, text = 'Borrower')
b1_label.grid(row =1, column = 0)
loan_label = Label(root, text = 'Loan')
loan_label.grid(row = 4, column =0)
author_label = Label(root, text = 'Author')
author_label.grid(row = 5, column = 0)
book_label = Label(root, text = 'Books')
book_label.grid(row = 6, column = 0)

new_Publisher_btn = Button(root, text ='Add Publisher ', command = newPublisher)
new_Publisher_btn.grid(row = 0, column =1, columnspan = 2, pady = 10, padx = 10, ipadx = 140)

new_Borrower_btn = Button(root, text ='Add Borrower ', command = newBorrower)
new_Borrower_btn.grid(row = 1, column =1, columnspan = 2, pady = 10, padx = 10, ipadx = 140)

new_Loan_btn = Button(root, text ='Add Loan ', command = newLoan)
new_Loan_btn.grid(row = 4, column = 1, columnspan = 2, pady = 10, padx = 10, ipadx = 140)

view_Loan_bwr_btn = Button(root, text = 'View By Borrower', command = viewLoanBWR)
view_Loan_bwr_btn.grid(row = 4, column = 2, columnspan = 1, pady = 10, padx = 10, ipadx = 150);

view_Loan_bk_btn = Button(root, text = 'View by Book', command = viewLoanBK)
view_Loan_bk_btn.grid(row = 4, column = 3, columnspan = 1, pady = 10, padx = 10, ipadx = 150);

new_Author_btn = Button(root, text = 'Add Author ', command = newAuthor)
new_Author_btn.grid(row = 5, column = 1, columnspan = 2, pady = 10, padx = 10, ipadx = 140)

new_Book_btn = Button(root, text ='Add Book ', command = newBook)
new_Book_btn.grid(row = 6, column =2, columnspan = 2, pady = 10, padx = 10, ipadx = 140)

result_label = Label(root, text = '')
result_label.grid(row = 20, column = 0)

#update_Publisher_btn = Button(root, text ='Update Publisher ', command = submit)
#update_Publisher_btn.grid(row = 0, column =1, columnspan = 2, pady = 10, padx = 10, ipadx = 140)

#executes tinker components
root.mainloop()
