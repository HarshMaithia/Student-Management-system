from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System.")
        self.root.geometry("2000x920+0+0")
        self.root.minsize(2000,920)
        title = Label(self.root,text=" Student Management System .",font=("times new roman",40,"bold"),bg="#222831",fg="#eeeeee",relief=GROOVE,borderwidth=10)
        title.pack(side=TOP,fill=X)

        def userText(event):
            txt_dob.delete(0,END) 
            txt_dob.configure(fg="black")

        self.roll_no_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()

        self.search_by_var = StringVar()
        self.search_txt_var = StringVar()    

        # MANAGE FRAME CODE ===============
        Manage_Frame = Frame(self.root, borderwidth=4,relief=RIDGE,bg="#00adb5")
        Manage_Frame.place(x=15,y=100,width=450,height=800)

        label_1 = Label(Manage_Frame,text="Mange Students",font=("times new roman",30,"bold"),bg="#00adb5",fg="white")
        label_1.grid(row=0,columnspan=2,pady=20)
        # =========Roll Number Field ====
        lbl_roll = Label(Manage_Frame,text="Roll No.",font=("times new roman",20,"bold"),bg="#00adb5",fg="white")
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_roll = Entry(Manage_Frame,textvariable=self.roll_no_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        #========= Name Field ======
        lbl_name = Label(Manage_Frame,text="Student Name",font=("times new roman",20,"bold"),bg="#00adb5",fg="white")
        lbl_name.grid(row=2,column=0,pady=10,padx=15,sticky="w")

        txt_name = Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        #=========== E-mail Field =====
        lbl_mail = Label(Manage_Frame,text="Email ID",font=("times new roman",20,"bold"),bg="#00adb5",fg="white")
        lbl_mail.grid(row=3,column=0,pady=10,padx=15,sticky="w")

        txt_mail = Entry(Manage_Frame,textvariable=self.email_var,font=("times new roman",15),bd=5,relief=GROOVE)
        txt_mail.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        #========= Gender Field =====
        lbl_gender = Label(Manage_Frame,text="Gender",font=("times new roman",20,"bold"),bg="#00adb5",fg="white")
        lbl_gender.grid(row=4,column=0,pady=10,padx=15,sticky="w")

        combo_gender = ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",15,"bold"),state="readonly")
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        #=== Contact ======
        lbl_contact = Label(Manage_Frame,text="Contact ",font=("times new roman",20),bg="#00adb5",fg="white")
        lbl_contact.grid(row=5,column=0,pady=10,padx=15,sticky="w")

        txt_contact = Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman",15),bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        #=== D O B =======
        lbl_dob = Label(Manage_Frame,text="D O B",font=("times new roman",20,"bold"),bg="#00adb5",fg="white")
        lbl_dob.grid(row=6,column=0,pady=10,padx=15,sticky="w")

        txt_dob = Entry(Manage_Frame,textvariable=self.dob_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE,fg="grey")
        txt_dob.insert(0,"(dd/mm/yyyy)")
        txt_dob.bind("<Button>",userText)
        txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky="w")


        #=== Address =====
        lbl_addr = Label(Manage_Frame,text="Address ",font=("times new roman",20,"bold"),bg="#00adb5",fg="white")
        lbl_addr.grid(row=7,column=0,pady=10,padx=15,sticky="w")

        self.txt_addr = Text(Manage_Frame,font=("times new roman",11),width=26,height=5)
        self.txt_addr.grid(row=7,column=1,pady=10,padx=20,sticky="w")


        # ====== BUTTON FRAME =====================================

        btn_frame = Frame(Manage_Frame, borderwidth=4,relief=RIDGE,bg="#00adb5")
        btn_frame.place(x=15,y=700,width=420)

        #== Buttons
        add_btn = Button(btn_frame,text="ADD",width=7,bg="#393e46",fg="white",command=self.add_student).grid(row=0,column=0,padx=10,pady=10)
        update_btn = Button(btn_frame,text="UPDATE",width=7,bg="#393e46",fg="white",command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        delete_btn = Button(btn_frame,text="DELETE",width=7,bg="#393e46",fg="white",command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        clear_btn = Button(btn_frame,text="CLEAR",width=7,bg="#393e46",fg="white",command=self.clear).grid(row=0,column=3,padx=10,pady=10)

        # DETAIL FRAME =======================
        Detail_Frame = Frame(self.root, borderwidth=4,relief=RIDGE,bg="#00adb5")
        Detail_Frame.place(x=490,y=100,width=1400,height=800)

        # Search Bar =========
        lbl_search = Label(Detail_Frame,text="Search By ",font=("times new roman",20,"bold"),bg="#00adb5",fg="white")
        lbl_search.grid(row=0,column=0,pady=10,padx=15,sticky="w")

        combo_search = ttk.Combobox(Detail_Frame,textvariable=self.search_by_var,font=("times new roman",15,"bold"),state="readonly",width=10)
        combo_search['values']=("roll_no","name","contact")
        combo_search.grid(row=0,column=1,pady=10,padx=15,sticky="w")

        txt_search = Entry(Detail_Frame,textvariable=self.search_txt_var,font=("times new roman",15,"bold"),bd=2,width=20)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        search_btn = Button(Detail_Frame,text="Search",width=10,bg="#393e46",fg="white",font="bold",command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showAll_btn = Button(Detail_Frame,text="Show All",width=10,bg="#393e46",fg="white",font="bold",command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

        # TABLE FRAME ========================
        table_frame = Frame(Detail_Frame, borderwidth=4,relief=RIDGE,bg="#00adb5")
        table_frame.place(x=10,y=70,width=1350,height=720)  

        scroll_x = Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame,orient=VERTICAL)
        self.Student_table = ttk.Treeview(table_frame,columns=("RollNO.","Name","email","Gender","Contact","DOB","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)  
        self.Student_table.heading("RollNO.",text="Roll No.")
        self.Student_table.heading("Name",text="Name")
        self.Student_table.heading("email",text="Email ID")
        self.Student_table.heading("Gender",text="Gender")
        self.Student_table.heading("Contact",text="Contact")
        self.Student_table.heading("DOB",text="D.O.B")
        self.Student_table.heading("Address",text="Address")
        self.Student_table['show']='headings'
        self.Student_table.column("RollNO.",width=100)
        self.Student_table.column("Name",width=200)
        self.Student_table.column("email",width=200)
        self.Student_table.column("Gender",width=100)
        self.Student_table.column("Contact",width=100)
        self.Student_table.column("DOB",width=100)
        self.Student_table.column("Address",width=300)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_table_data)

        self.fetch_data()

    def add_student(self):
        if self.roll_no_var.get()=="" or self.name_var.get()=="" or self.email_var.get()=="" or self.contact_var.get()=="" or self.dob_var.get()=="":
            messagebox.showerror("Error","All Fields are Required.")
        elif self.gender_var.get()=="":
            messagebox.showerror("Error","Select Gender")

        else:    
            con=pymysql.connect(host="localhost",user="root",password="Maithia@99",database="stm")
            cur=con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.roll_no_var.get(),self.name_var.get(),self.email_var.get(),self.gender_var.get(),self.contact_var.get(),self.dob_var.get(),self.txt_addr.get('1.0',END)))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record Added Successfully.")

    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="Maithia@99",database="stm")
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def clear(self):
        self.roll_no_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_addr.delete('1.0',END)

    def get_table_data(self,event):
        table_row=self.Student_table.focus()
        contents=self.Student_table.item(table_row)
        row=contents['values']
        self.roll_no_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_addr.delete('1.0',END)
        self.txt_addr.insert(END,row[6])

    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="Maithia@99",database="stm")
        cur=con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(self.name_var.get(),self.email_var.get(),self.gender_var.get(),self.contact_var.get(),self.dob_var.get(),self.txt_addr.get('1.0',END),self.roll_no_var.get()))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="Maithia@99",database="stm")
        cur=con.cursor()
        cur.execute("delete from students where roll_no=%s",self.roll_no_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="Maithia@99",database="stm")
        cur=con.cursor()
        
        cur.execute("select * from students where "+str(self.search_by_var.get())+" Like '%"+str(self.search_txt_var.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()    




root=Tk()
ob=Student(root)
root.mainloop()
