from tkinter import *

import sqlite3
import random


# create tkinter window 

root = Tk()

root.title('Library Database Management System')

root.geometry("400x400")


LMS_connect = sqlite3.connect('library/LMS.db')

LMS_cur = LMS_connect.cursor()


def accPublisher(pub_name, pub_phone, pub_addr):
	accPub_conn = sqlite3.connect('library/LMS.db')

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
	accBor_conn = sqlite3.connect('library/LMS.db')

	accBor_curr = accBor_conn.cursor()
	cardNo = random.randint(100000, 999999)

	accBor_curr.execute("INSERT INTO BORROWER VALUES (NULL, :bor_name, :bor_phone, :bor_addr) ",
		{
			'NULL': cardNo,
			'bor_name': bor_name.get(),
			'bor_phone': bor_phone.get(),
			'bor_addr': bor_addr.get()
		})

	print("Your card number:", cardNo)
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


f_name_label = Label(root, text = 'Publisher')
f_name_label.grid(row =0, column = 0)
b1_label = Label(root, text = 'Borrower')
b1_label.grid(row =1, column = 0)

new_Publisher_btn = Button(root, text ='Add Publisher ', command = newPublisher)
new_Publisher_btn.grid(row = 0, column =1, columnspan = 2, pady = 10, padx = 10, ipadx = 140)

new_Borrower_btn = Button(root, text ='Add Borrower ', command = newBorrower)
new_Borrower_btn.grid(row = 1, column =1, columnspan = 2, pady = 10, padx = 10, ipadx = 140)
#update_Publisher_btn = Button(root, text ='Update Publisher ', command = submit)
#update_Publisher_btn.grid(row = 0, column =1, columnspan = 2, pady = 10, padx = 10, ipadx = 140)

#executes tinker components
root.mainloop()