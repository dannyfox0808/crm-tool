from tkinter import *
from tkinter import ttk
import tkinter as tk
import mysql.connector
from tkinter import messagebox as mb
import csv
import sqlite3


'''
import subprocess
proc = subprocess.check_output("ipconfig" ).decode('utf-8')
print (proc)'''

#============================================================================ START TEMPLATE ======================================================================

root =tk.Tk()
root.title("iStoreX")
root.geometry("1000x600")
root.config(bg="black")


# Logo
logo = Label(root, text="iStoreX", font=("Halvetica", 24, 'bold'), fg="white", bg="black")
logo.place(x=25, y=15)

# Title
title = Label(root, text="Welcome To iStoreX!", font=("Halvetica", 16, 'bold'), bg="black", fg="white")
title.pack(pady=25)



# Version
#title = Label(root, text="Version 1.0.0", font=("Halvetica", 10, 'bold'), bg="black", fg="white")
#title.place(x=30, y=575)

global color
global canvas
# Color border
color = Frame(root, width=800, height=500, bg="blue")
canvas = Canvas(color, bg="blue")
color.pack()



# Tabs #

global my_notebook
my_notebook = ttk.Notebook(color)
my_notebook.pack(pady=5,padx=10)


# TAB 1 #

container0 = Frame(my_notebook)
container0.pack(fill=BOTH, expand=True)
my_notebook.add(container0, text='Welcome')


canvas0 = Canvas(container0, width=985, height=485)
scroll = Scrollbar(container0, command=canvas0.yview)
canvas0.config(yscrollcommand=scroll.set, scrollregion=(0,0,100,500), bg="gray22")
canvas0.config(bg="gray22")
canvas0.pack(side=LEFT, fill=BOTH, expand=True)
scroll.pack(side=RIGHT, fill=Y)

frame0 = Frame(canvas0, width=1450, height=1000, bg="gray22")
canvas0.create_window(625, 400, window=frame0)


frame_p = Frame(frame0, width=1500, height=800, bg="gray22")
frame_p.pack(pady=20)


# Title
title2 = Label(frame_p, text="Welcome To The iStoreX Database", font=("Halvetica", 18, 'bold'), bg="gray22", fg="white")
title2.place(x=425,y=25)

# WELCOME TEXT

texts = str("The full documentation on how to use iStoreX, as well as some of \n our other databases, is all on our website! Please read the full manual \n before using the database for any major projects.")

l = Label(frame_p, text = texts, font=("Halvetica", 14, 'bold'), bg="gray22", fg="white")
l.place(x=300,y=125)

# TAB 2 #

container1 = Frame(my_notebook)
container1.pack(fill=BOTH, expand=True)
my_notebook.add(container1, text='Database')

canvas1 = Canvas(container1)
scroll = Scrollbar(container1, command=canvas1.yview)

canvas1.config(yscrollcommand=scroll.set, scrollregion=(0,0,100,725), bg="gray22")
canvas1.config(bg="gray22")
canvas1.pack(side=LEFT, fill=BOTH, expand=True)
scroll.pack(side=RIGHT, fill=Y)

frame1 = Frame(canvas1, bg="gray22")
canvas1.create_window(475, 350, window=frame1)


frame_p1 = Frame(frame1,bg="gray22", height=250, width=1500)
frame_p1.pack(pady=20)

# Title
title = Label(frame_p1, text="Welcome To The Database", font=("Halvetica", 16, 'bold'), bg="gray22", fg="white")
title.pack(pady=25)

#============================================================================ END OF START TEMPLATE ======================================================================


# Database application #======================================================================================================================================

# Add fake data
'''
data = [


	["Danny", "Fox", 1,  "Dannyfox080808@outlook.com", "London Road", "Waterlooville", "Portsmouth", "West sussex", "PO77SH"],
	["Tim", "Smith", 2, "TimSmith@outlook.com", "Clevelend Estate", "Hamphop", "Acklon", "East sussex", "PO73YE"],
	["Mike", "James", 3, "MikeJames@outlook.com", "Oakfield Avenue", "Childam", "Frickshire", "Ohio", "PO2ED"],
	["Clair", "Helm", 4, "ClairHelm@outlook.com", "Oving Road", "Strachire", "Pastvile", "Canada", "44F24F"],
	["Ray", "Jeff", 5, "RayJeff@outlook.com", "Ports Drive", "Wayfield", "Ockland", "London", "PO9BEB"],
	["Asmir", "Afir", 6, "AsmirAfir@outlook.com", "Sling Creascent", "Strickham", "Frion", "Essex", "12ESS2"],
	["Jeff", "Ling", 7, "JeffLing@outlook.com", "Easter Cottage", "Florceiser", "Streych", "Petersburg", "12EED3"],
	["Sam", "Treah", 8, "SamTreah@outlook.com", "Lavant Road", "Millview", "Newtown", "California", "4432FE"],
	["Mary", "May", 9,"MaryMay@outlook.com", "Pilow Gardens", "Staffrom", "Playbuck", "New York", "G55G55"],
	["Peter", "Day", 10,"PeterDay@outlook.com", "11 Lock Road", "Aspin", "Axeion", "Virginia", "6YG4GT"]

]

'''

# Database

# Create a database or connect to one that exists

conn = sqlite3.connect('tree_crm.db')

# Create a cursor instance

c = conn.cursor()

# Create a table

c.execute(""" CREATE TABLE if not exists customers (

	first_name text,
	last_name text,
	id integer,
	email text,
	address_1 text,
	address_2 text,
	city text,
	state text,
	zipcode text)
	""")

# Add dummy data 
'''
for record in data:
	c.execute("INSERT INTO customers VALUES (:first_name, :last_name,:id,:email,:address_1,:address_2,:city,:state,:zipcode)",
		{
		'first_name' : record[0],
		'last_name' : record[1],
		'id' : record[2],
		'email' : record[3],
		'address_1' : record[4],
		'address_2' : record[5],
		'city' : record[6],
		'state' : record[7],
		'zipcode' : record[8]
		}
		)

'''


# Commit the changes

conn.commit()

# Close the connection

conn.close()

def query_database():


	# Create a database or connect to one that exists

	conn = sqlite3.connect('tree_crm.db')

	# Create a cursor instance

	c = conn.cursor()


	c.execute("SELECT rowid,  * FROM customers")

	records = c.fetchall()

	
	# Add our data to the screen
	global count
	count = 0

	#for record in records:

	for record in records:
		if count % 2 == 0:
			my_tree.insert(parent='', index='end', iid=count, text='', values=(record[1], record[2], record[0], record[4], record[5], record[6], record[7], record[8], record[9]), tags=('evenrow',))
		else:
			my_tree.insert(parent='', index='end', iid=count, text='', values=(record[1], record[2], record[0], record[4], record[5], record[6], record[7], record[8], record[9]), tags=('oddrow', ))

		count += 1

	# Commit the changes

	conn.commit()

	# Close the connection

	conn.close()





# Add Some Style
style = ttk.Style()

# Pick A Theme
style.theme_use('default')

# Configure the Treeview Colors
style.configure("Treeview",
	background="gray22",
	foreground="black",
	rowheight=25,
	fieldbackground="#D3D3D3")

# Change Selected Color
style.map('Treeview',
	background=[('selected', "#347083")])

# Create a Treeview Frame
tree_frame = Frame(frame_p1)
tree_frame.pack(pady=10)

# Create a Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

horizontal_tree_scroll = Scrollbar(tree_frame, orient = HORIZONTAL)
horizontal_tree_scroll.pack(side=BOTTOM, fill=X)

# Create The Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set ,selectmode="extended")
my_tree.pack()

# Configure the Scrollbar
tree_scroll.config(command=my_tree.yview)
horizontal_tree_scroll.config(command=my_tree.xview)


# Define columns

my_tree['columns'] = ("First Name"), str("Last Name"), "ID", str("Email"), str("Address 1"), str("Address 2"), str("City"), str("State"), str("Zipcode")

# Format columns

my_tree.column("#0", width=0, stretch = NO)
my_tree.column("First Name", anchor = W, minwidth=0, width=86, stretch=NO)
my_tree.column("Last Name", anchor = W, minwidth=0, width=86, stretch=NO)
my_tree.column("ID", anchor = CENTER, minwidth=0, width=50, stretch=NO)
my_tree.column("Email", anchor = CENTER, minwidth=0, width=125, stretch=NO)
my_tree.column("Address 1", anchor = CENTER, minwidth=0, width=125, stretch=NO)
my_tree.column("Address 2", anchor = CENTER, minwidth=0, width=125, stretch=NO)
my_tree.column("City", anchor = CENTER, minwidth=0, width=86, stretch=NO)
my_tree.column("State", anchor = CENTER, minwidth=0, width=86, stretch=NO)
my_tree.column("Zipcode", anchor = CENTER, minwidth=0, width=50, stretch=NO)

# Create headings

my_tree.heading("#0", text = "", anchor = W)
my_tree.heading("First Name", text = "First Name", anchor = W)
my_tree.heading("Last Name", text = "Last Name", anchor = W)
my_tree.heading("ID", text = "ID", anchor = CENTER)
my_tree.heading("Email", text = "Email", anchor = CENTER)
my_tree.heading("Address 1", text = "Address 1", anchor = CENTER)
my_tree.heading("Address 2", text = "Address 2", anchor = CENTER)
my_tree.heading("City", text = "City", anchor = CENTER)
my_tree.heading("State", text = "State", anchor = CENTER)
my_tree.heading("Zipcode", text = "Zipcode", anchor = CENTER)


# Create Striped Row Tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")



# Add Record Entry Boxes
data_frame = LabelFrame(frame_p1, text="Record", bg="gray22", fg="white")
data_frame.pack(padx=10, pady=25)

fn_label = Label(data_frame, text="First Name", font=("Halvetica", 14), bg="gray22", fg="white")
fn_label.grid(row=0, column=0, padx=10, pady=10)
fn_entry = Entry(data_frame)
fn_entry.grid(row=0, column=1, padx=10, pady=10)

ln_label = Label(data_frame, text="Last Name", font=("Halvetica", 14), bg="gray22", fg="white")
ln_label.grid(row=1, column=0, padx=10, pady=10)
ln_entry = Entry(data_frame)
ln_entry.grid(row=1, column=1, padx=10, pady=10)

id_label = Label(data_frame, text="ID", font=("Halvetica", 14), bg="gray22", fg="white")
id_label.grid(row=0, column=2, padx=10, pady=10)
id_entry = Entry(data_frame)
id_entry.grid(row=0, column=3, padx=10, pady=10) #

email_label = Label(data_frame, text="Email", font=("Halvetica", 14), bg="gray22", fg="white")
email_label.grid(row=1, column=2, padx=10, pady=10)
email_entry = Entry(data_frame)
email_entry.grid(row=1, column=3, padx=10, pady=10)

address1_label = Label(data_frame, text="Address 1", font=("Halvetica", 14), bg="gray22", fg="white")
address1_label.grid(row=2, column=0, padx=10, pady=10)
address_entry = Entry(data_frame)
address_entry.grid(row=2, column=1, padx=10, pady=10)

address2_label = Label(data_frame, text="Address 2", font=("Halvetica", 14) , bg="gray22", fg="white")
address2_label.grid(row=2, column=2, padx=10, pady=10)
address2_entry = Entry(data_frame)
address2_entry.grid(row=2, column=3, padx=10, pady=10)

city_label = Label(data_frame, text="City", font=("Halvetica", 14), bg="gray22", fg="white")
city_label.grid(row=1, column=4, padx=10, pady=10)
city_entry = Entry(data_frame)
city_entry.grid(row=0, column=5, padx=10, pady=10)


state_label = Label(data_frame, text="State", font=("Halvetica", 14), bg="gray22", fg="white")
state_label.grid(row=0, column=4, padx=10, pady=10)
state_entry = Entry(data_frame)
state_entry.grid(row=1, column=5, padx=10, pady=10)

zipcode_label = Label(data_frame, text="Zipcode", font=("Halvetica", 14), bg="gray22", fg="white")
zipcode_label.grid(row=2, column=4, padx=10, pady=10)
zipcode_entry = Entry(data_frame)
zipcode_entry.grid(row=2, column=5, padx=10, pady=10)

def up():
	rows = my_tree.selection()
	for row in rows:
		my_tree.move(row, my_tree.parent(row), my_tree.index(row) - 1)

def down():
	rows = my_tree.selection()
	for row in reversed(rows):
		my_tree.move(row, my_tree.parent(row), my_tree.index(row) + 1)

def clear_record():

	fn_entry.delete(0, END)
	ln_entry.delete(0, END)
	id_entry.delete(0, END)
	email_entry.delete(0, END)
	address_entry.delete(0, END)
	address2_entry.delete(0, END)
	city_entry.delete(0, END)
	state_entry.delete(0, END)
	zipcode_entry.delete(0, END)

# Select record

def select_record(e):
	fn_entry.delete(0, END)
	ln_entry.delete(0, END)
	id_entry.delete(0, END)
	email_entry.delete(0, END)
	address_entry.delete(0, END)
	address2_entry.delete(0, END)
	city_entry.delete(0, END)
	state_entry.delete(0, END)
	zipcode_entry.delete(0, END)

	# get record number

	selected = my_tree.focus()

	# get record values

	values = my_tree.item(selected, 'values')

	# Output to entry boxes

	fn_entry.insert(0, values[0])
	ln_entry.insert(0, values[1])
	id_entry.insert(0, values[2])
	email_entry.insert(0, values[3])
	address_entry.insert(0, values[4])
	address2_entry.insert(0, values[5])
	city_entry.insert(0, values[6])
	state_entry.insert(0, values[7])
	zipcode_entry.insert(0, values[8])

# Remove one record
def remove_one():
	x = my_tree.selection()[0]
	my_tree.delete(x)

	# Update the database
	# Create a database or connect to one that exists
	conn = sqlite3.connect('tree_crm.db')

	# Create a cursor instance
	c = conn.cursor()
	# Delete a record
	c.execute("DELETE from customers WHERE oid=" + id_entry.get())

	# Commit changes
	conn.commit()

	# Close our connection
	conn.close()


	clear_record()

	mb.showinfo("Deleted!", "Your record was successfully deleted!")

# Remove Many record
def remove_many():
	x = my_tree.selection()
	for record in x:
		my_tree.delete(record)


# Remove all records
def remove_all():
	response = mb.askyesno("Are You Sure?", "This will delete everything from the table. This can not be undone.")

	if response == 1:
		for record in my_tree.get_children():
			my_tree.delete(record)

		# Create a database or connect to one that exists
		conn = sqlite3.connect('tree_crm.db')

		# Create a cursor instance
		c = conn.cursor()

		# Delete everything fromd database

		c.execute("DROP TABLE customers")

		# Commit changes
		conn.commit()

		# Close our connection
		conn.close()

		clear_record()

		create_table()

# Update record
def update_record():
	# Grab the record number
	selected = my_tree.focus()
	# Update record
	my_tree.item(selected, text="", values=(fn_entry.get(), ln_entry.get(), id_entry.get(), email_entry.get(), address_entry.get(),address2_entry.get(), city_entry.get(), state_entry.get(), zipcode_entry.get(),))

	# Update the database
	# Create a database or connect to one that exists
	conn = sqlite3.connect('tree_crm.db')

	# Create a cursor instance
	c = conn.cursor()

	c.execute("""UPDATE customers SET
		first_name = :first,
		last_name = :last,
		email = :email,
		address_1 = :address_1,
		address_2 = :address_2,
		city = :city,
		state = :state,
		zipcode = :zipcode

		WHERE oid = :oid""",
		{
			'first': fn_entry.get(),
			'last': ln_entry.get(),
			'email': email_entry.get(),
			'address_1': address_entry.get(),
			'address_2': address2_entry.get(),
			'city': city_entry.get(),
			'state': state_entry.get(),
			'zipcode': zipcode_entry.get(),
			'oid': id_entry.get(),
		})
	


	# Commit changes
	conn.commit()

	# Close our connection
	conn.close()


	clear_record()


# add new record
def add_record():
 	# Update the database

	# Create a database or connect to one that exists
	conn = sqlite3.connect('tree_crm.db')

	# Create a cursor instance
	c = conn.cursor()


	# Add new record
	c.execute("INSERT INTO customers VALUES(:first,:last,:id,:email,:address_1,:address_2,:city,:state,:zipcode)",
		{


			'first': fn_entry.get(),
			'last': ln_entry.get(),
			'id' :id_entry.get(),
			'email': email_entry.get(),
			'address_1': address_entry.get(),
			'address_2': address2_entry.get(),
			'city': city_entry.get(),
			'state': state_entry.get(),
			'zipcode': zipcode_entry.get(),

		})






	# Commit changes
	conn.commit()

	# Close our connection
	conn.close()
		


	fn_entry.delete(0, END)
	ln_entry.delete(0, END)
	id_entry.delete(0, END)
	email_entry.delete(0, END)
	address_entry.delete(0, END)
	address2_entry.delete(0, END)
	city_entry.delete(0, END)
	state_entry.delete(0, END)
	zipcode_entry.delete(0, END)

	my_tree.delete(*my_tree.get_children())

	query_database()

def create_table():

	conn = sqlite3.connect('tree_crm.db')

	# Create a cursor instance

	c = conn.cursor()

	# Create a table

	c.execute(""" CREATE TABLE if not exists customers (

		first_name text,
		last_name text,
		id integer,
		email text,
		address_1 text,
		address_2 text,
		city text,
		state text,
		zipcode text)
		""")
	conn.commit()

	conn.close()





# Add Buttons
button_frame = LabelFrame(frame_p1, text="Commands", bg="gray22", fg="white")
button_frame.pack(padx=20, pady=25)

update_button = Button(button_frame, text="Update Record", command = update_record)
update_button.grid(row=0, column=0, padx=10, pady=10)

add_button = Button(button_frame, text="Add Record", command = add_record)
add_button.grid(row=0, column=1, padx=10, pady=10)

remove_all_button = Button(button_frame, text="Remove All Records", command = remove_all)
remove_all_button.grid(row=0, column=2, padx=10, pady=10)

remove_one_button = Button(button_frame, text="Remove One Selected", command = remove_one)
remove_one_button.grid(row=0, column=3, padx=10, pady=10)

remove_many_button = Button(button_frame, text="Remove Many Selected",command = remove_many)
remove_many_button.grid(row=0, column=4, padx=10, pady=10)

move_up_button = Button(button_frame, text="Move Up", command = up)
move_up_button.grid(row=0, column=5, padx=10, pady=10)

move_down_button = Button(button_frame, text="Move Down", command = down)
move_down_button.grid(row=0, column=6, padx=10, pady=10)

clear_record_button = Button(button_frame, text="Clear Fields", command = clear_record)
clear_record_button.grid(row=0, column=7, padx=10, pady=10)

# Bind the treeview
my_tree.bind("<ButtonRelease-1>", select_record)

# Run to pull data from database on start
query_database()


root.mainloop()