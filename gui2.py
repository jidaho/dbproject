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

def accBorrower(bor_name,bor_phone,bor_addr):
	accBor_conn = sqlite3.connect('LMS.db')

	accBor_curr = accBor_conn.cursor()

	accBor_curr.execute("INSERT INTO BORROWER VALUES (NULL, :bor_name, :bor_phone, :bor_addr) ",
		{
			'bor_name': bor_name.get(),
			'bor_phone': bor_phone.get(),
			'bor_addr': bor_addr.get()
		})
	query = "SELECT Card_No FROM BORROWER WHERE Name = 'William Chen'"
	
	print("Your card number:", accBor_curr.execute("SELECT Card_No FROM BORROWER WHERE Name = :bor_name AND Address = :bor_addr AND Phone = :bor_phone",
		{
			'bor_name': bor_name.get(),
			'bor_addr': bor_addr.get(),
			'bor_phone': bor_phone.get()
		}).fetchone())

	#commit changes
	accBor_conn.commit()
	#close the DB connection
	accBor_conn.close()

def newBorrower():
	sub = Tk()
	
	sub.title("New Borrower")
	sub.geometry("400x400")

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

	submit_btn2 = Button(sub, text =' Add Borrower', command = lambda: accBorrower(bor_name,bor_phone,bor_addr))
	submit_btn2.grid(row = 3, column = 1, columnspan = 1, pady = 10, padx = 10, ipadx = 140)

	acc_Borrower_btn = Button(sub, text ='Cancel      ', command = sub.destroy)
	acc_Borrower_btn.grid(row = 4, column = 1, columnspan = 1, pady = 10, padx = 10, ipadx = 140)

	sub.mainloop()

def accLoan(loan_bkID, loan_bchID, loan_cardNo, loan_date_ot, loan_date_du, loan_date_rtn):
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

	#commit changes
	accLN_conn.commit()
	#close the DB connection
	accLN_conn.close()

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

	submit_btn = Button(sub, text =' Add Loan', command = lambda: accLoan(loan_bkID, loan_bchID, loan_cardNo, 
																			   loan_date_ot, loan_date_du, loan_date_rtn))
	submit_btn.grid(row = 6, column = 1, columnspan = 1, pady = 10, padx = 10, ipadx = 140)

	acc_Borrower_btn = Button(sub, text ='Cancel ', command = sub.destroy)
	acc_Borrower_btn.grid(row = 7, column = 1, columnspan = 1, pady = 10, padx = 10, ipadx = 140)

	sub.mainloop()


def newAuthor():
	sub = Tk()
	
	sub.title("New Author")
	sub.geometry("400x400")

	bk_ID = Entry(sub, width = 30)
	bk_ID.grid(row = 0, column = 1)

	auth_name = Entry(sub, width = 30)
	auth_name.grid(row = 1, column = 1)

	bk_ID_label = Label(sub, text = 'Book ID: ')
	bk_ID_label.grid(row = 0, column = 0)

	auth_name_label = Label(sub, text = 'Author Name: ')
	auth_name_label.grid(row = 1, column = 0)

	submit_btn2 = Button(sub, text =' Add Author', command = lambda: accBorrower(bor_name,bor_phone,bor_addr))
	submit_btn2.grid(row = 3, column = 1, columnspan = 1, pady = 10, padx = 10, ipadx = 140)

	acc_Borrower_btn = Button(sub, text ='Cancel      ', command = sub.destroy)
	acc_Borrower_btn.grid(row = 4, column = 1, columnspan = 1, pady = 10, padx = 10, ipadx = 140)

	sub.mainloop()


f_name_label = Label(root, text = 'Publisher')
f_name_label.grid(row =0, column = 0)
b1_label = Label(root, text = 'Borrower')
b1_label.grid(row =1, column = 0)
loan_label = Label(root, text = 'Loan')
loan_label.grid(row = 4, column =0)
author_label = Label(root, text = 'Author')
author_label.grid(row = 5, column = 0)

new_Publisher_btn = Button(root, text ='Add Publisher ', command = newPublisher)
new_Publisher_btn.grid(row = 0, column =1, columnspan = 2, pady = 10, padx = 10, ipadx = 140)

new_Borrower_btn = Button(root, text ='Add Borrower ', command = newBorrower)
new_Borrower_btn.grid(row = 1, column =1, columnspan = 2, pady = 10, padx = 10, ipadx = 140)

new_Loan_btn = Button(root, text ='Add Loan ', command = newLoan)
new_Loan_btn.grid(row = 4, column = 1, columnspan = 2, pady = 10, padx = 10, ipadx = 140)

new_Author_btn = Button(root, text = 'Add Author ', command = newAuthor)
new_Author_btn.grid(row = 5, column = 1, columnspan = 2, pady = 10, padx = 10, ipadx = 140)

#update_Publisher_btn = Button(root, text ='Update Publisher ', command = submit)
#update_Publisher_btn.grid(row = 0, column =1, columnspan = 2, pady = 10, padx = 10, ipadx = 140)

#executes tinker components
root.mainloop()
