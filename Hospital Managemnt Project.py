from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector



class Hospital:
    def __init__(self,root):
            self.root=root
            self.root.title("Hospital Management System")
            self.root.geometry("1540x800+0+0")

            self.nameoftablets=StringVar()
            self.ref=StringVar()
            self.dose=StringVar()
            self.nooftablets=StringVar()
            self.lot=StringVar()
            self.issuedate=StringVar()
            self.expdate=StringVar()
            self.dailydose=StringVar()
            self.sideeffect=StringVar()
            self.furtherinformation = StringVar()
            self.storage = StringVar()
            self.drivingusingmachine = StringVar()
            self.howtousemedication = StringVar()
            self.patientid = StringVar()
            self.nhsnumber = StringVar()
            self.pname = StringVar()
            self.dob = StringVar()
            self.address = StringVar()

            lbltitle = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="gold", bg="black",font=("times new roman",50,"bold"))
            lbltitle.pack(side=TOP, fill=X)

            # ====================dataframe==========================

            DataFrame=Frame(self.root, bd=20, relief=RIDGE,bg="gray")
            DataFrame.place(x=0, y=130, width=1530, height=400)

            DataFrameLeft=LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=10, font=("times new roman", 12, "bold"),text="patient Information")
            DataFrameLeft.place(x=0, y=5, width=980, height=350)

            DataFrameRight = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=10, font=("times new roman", 12, "bold"),text="Prescription")
            DataFrameRight.place(x=990, y=5, width=460, height=350)

            # =======================button frame======================

            Buttonframe=Frame(self.root, bd=20, relief=RIDGE,bg="gray")
            Buttonframe.place(x=0, y=500, width=1530, height=70)

            # ===============Details frame==============================

            Detailsframe=Frame(self.root, bd=20, relief=RIDGE,bg="gray")
            Detailsframe.place(x=0, y=560, width=1380, height=150)

            # ==============DataframeLeft====================

            lblNameTablet=Label(DataFrameLeft,text="Names OF Tablet",font=("times new roman", 12,"bold"),padx=2, pady=6)
            lblNameTablet.grid(row=0, column=0)

            comNametablet = ttk.Combobox(DataFrameLeft,textvariable=self.nameoftablets, font=("times new roman", 12, "bold"),width=33)
            comNametablet["values"] = ("Nice", "Corona vaccine", "Acetaminophen", "Adderall", "Amlodipine", "Ativan")
            comNametablet.current(0)
            comNametablet.grid(row=0, column=1)

            lblref=Label(DataFrameLeft,font=("arial", 12, "bold"),text="Reference No:", padx=2)
            lblref.grid(row=1, column=0, sticky=W)
            txtref=Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.ref, width=35)
            txtref.grid(row=1, column=1)

            lblDose=Label(DataFrameLeft,font=("arial", 12, "bold"),text="Dose:", padx=2, pady=4)
            lblDose.grid(row=2, column=0, sticky=W)
            txtDose = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.dose,width=35)
            txtDose.grid(row=2, column=1)

            lblNoOftablets=Label(DataFrameLeft, font=("arial", 12, "bold"), text="No Of Tablets:", padx=2, pady=6)
            lblNoOftablets.grid(row=3, column=0, sticky=W)
            txtNoOftablets = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.nooftablets,width=35)
            txtNoOftablets.grid(row=3, column=1)

            lblLot=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Lot:", padx=2, pady=6)
            lblLot.grid(row=4, column=0, sticky=W)
            txtLot=Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.lot,width=35)
            txtLot.grid(row=4, column=1)

            lblissueDate = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Issue Date:", padx=2, pady=6)
            lblissueDate.grid(row=5, column=0, sticky=W)
            txtissueDate = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.issuedate,width = 35)
            txtissueDate.grid(row=5, column=1)

            lblExpDate = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Exp Date:", padx=2, pady=6)
            lblExpDate.grid(row=6, column=0, sticky=W)
            txtExpDate=Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.expdate,width=35)
            txtExpDate.grid(row=6, column=1)

            lblDailyDose = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Daily Dose:", padx=2, pady=4)
            lblDailyDose.grid(row=7, column=0, sticky=W)
            txtDailyDose=Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.dailydose, width=35)
            txtDailyDose.grid(row=7, column=1)

            lblSideEffect = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Side effect:", padx=2, pady=6)
            lblSideEffect.grid(row=8, column=0, sticky=W)
            txtSideEffect = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.sideeffect,width=35)
            txtSideEffect.grid(row=8, column=1)

            lblFurtherinfo = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Further Information", padx=2)
            lblFurtherinfo.grid(row=0, column=2, sticky=W)
            txtFurtherinfo = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.furtherinformation,width=35)
            txtFurtherinfo.grid(row=0, column=3)


            lblDrivingMachine = Label(DataFrameLeft, font=("arial", 12, "bold"), text="BloodPresure", padx=2, pady=6)
            lblDrivingMachine.grid(row=1, column=2, sticky=W)
            txtDrivingMachine=Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.drivingusingmachine,width=35)
            txtDrivingMachine.grid(row=1, column=3)

            lblStorage = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Storage Advice", padx=2, pady=6)
            lblStorage.grid(row=2, column=2, sticky=W)
            txtStorage = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.storage,width=35)
            txtStorage.grid(row=2, column=3)

            lblMedicine = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Medication", padx=2, pady=6)
            lblMedicine.grid(row=3, column=2, sticky=W)
            txtMedicine = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.howtousemedication,width=35)
            txtMedicine.grid(row=3, column=3, sticky=W)

            lblPatientId = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient Id", padx=2, pady=6)
            lblPatientId.grid(row=4, column=2, sticky=W)
            txtPatientId = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.patientid,width=35)
            txtPatientId.grid(row=4, column=3)

            lblNhsNumber = Label(DataFrameLeft, font=("arial", 12, "bold"), text="NHS Number", padx=2, pady=6)
            lblNhsNumber.grid(row=5, column=2, sticky=W)
            txtNhsNumber = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.nhsnumber,width=35)
            txtNhsNumber.grid(row=5, column=3)

            lblPatientname = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient Name", padx=2, pady=6)
            lblPatientname.grid(row=6, column=2, sticky=W)
            txtPatientname = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.pname,width=35)
            txtPatientname.grid(row=6, column=3)

            lblDateOfBirth = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date Of Birth", padx=2, pady=6)
            lblDateOfBirth.grid(row=7, column=2, sticky=W)
            txtDateOfBirth = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.dob,width = 35)
            txtDateOfBirth.grid(row=7, column=3)

            lblPatientAddress = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient Address", padx=2, pady=6)
            lblPatientAddress.grid(row=8, column=2, sticky=W)
            txtPatientAddress = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.address,width=35)
            txtPatientAddress.grid(row=8, column=3)

            # ===================DataFrameRight======================

            self.txtPrescription = Text(DataFrameRight, font=("arial", 12, "bold"),bg="gray", width=45, height=16, padx=2, pady=6)
            self.txtPrescription.grid(row=0, column=0)

            # =========================Button=======================

            btnPre=Button(Buttonframe,command=self.iPrescription,text="Prescription",bg="black",fg="gold",font=("arial",12,"bold"),width=23,height=1,padx=2,pady=2)
            btnPre.place(x=5,y=2)

            btnPrescriptionData=Button(Buttonframe,text="Prescription Data",command=self.iPrescriptionData,bg="black",fg="gold",font=("arial", 12, "bold"),width=20,height=1,padx=2,pady=2)
            btnPrescriptionData.place(x=246,y=2)

            btnUpdate=Button(Buttonframe,text="Update",command=self.update_data, bg="black", fg="gold",font=("arial", 12, "bold"), width=23, height=1, padx=2, pady=2)
            btnUpdate.place(x=458,y=2)

            btnDelete=Button(Buttonframe,command=self.idelete,text="Delete", bg="black", fg="gold", font=("arial", 12, "bold"), width=23,height=1, padx=2, pady=2)
            btnDelete.place(x=680,y=2)

            btnClear=Button(Buttonframe,command=self.clear, text="Clear", bg="black", fg="gold", font=("arial", 12, "bold"), width=23,height=1, padx=2, pady=2)
            btnClear.place(x=900,y=2)

            btnExit=Button(Buttonframe,command=self.iExit, text="Exit", bg="black", fg="gold", font=("arial", 12, "bold"), width=23, height=1,padx=2, pady=2)
            btnExit.place(x=1100,y=2)

    # # ========================Table==========================================

    # # ========================Scrollbar===================================
            scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
            scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
            self.hospital_table=ttk.Treeview(Detailsframe,column=("nameoftable","ref","dose","nooftablets","lot","issuedate","expdate",
                                   "dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)

            scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
            scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

            self.hospital_table.heading("nameoftable", text="Name Of Table")
            self.hospital_table.heading("ref", text="Reference No.")
            self.hospital_table.heading("dose", text="Dose")
            self.hospital_table.heading("nooftablets", text="No Of Tablets")
            self.hospital_table.heading("lot", text="Lot")
            self.hospital_table.heading("issuedate", text="Issuedate")
            self.hospital_table.heading("expdate", text="Exp Date")
            self.hospital_table.heading("dailydose", text="Daily Dose")
            self.hospital_table.heading("storage", text="storage")
            self.hospital_table.heading("nhsnumber", text="NHS Number")
            self.hospital_table.heading("pname", text="Patient Name")
            self.hospital_table.heading("dob", text="DOB")
            self.hospital_table.heading("address", text="Address")

            self.hospital_table["show"]="headings"

          

            self.hospital_table.column("nameoftable", width=100)
            self.hospital_table.column("ref", width=100)
            self.hospital_table.column("dose", width=100)
            self.hospital_table.column("nooftablets", width=100)
            self.hospital_table.column("lot", width=100)
            self.hospital_table.column("issuedate", width=100)
            self.hospital_table.column("expdate", width=100)
            self.hospital_table.column("dailydose", width=100)
            self.hospital_table.column("storage", width=100)
            self.hospital_table.column("nhsnumber", width=100)
            self.hospital_table.column("pname", width=100)
            self.hospital_table.column("dob", width=100)
            self.hospital_table.column("address", width=100)

            self.hospital_table.pack(fill=BOTH, expand=1)
            self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)
            self.fetch_data()

            


    # # ====================FunctinalityDeclartion==========================

    def iPrescriptionData(self):
        if self.nameoftablets.get()=="" or self.ref.get()=="":
               messagebox.showerror("Error","All fields are required")
        else:
              conn=mysql.connector.connect(host="localhost",username="root",password="root",database="pythongui")
              my_cursor=conn.cursor()
              my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",

                          (self.nameoftablets.get(),
                           self.ref.get(),
                           self.dose.get(),
                           self.nooftablets.get(),
                           self.lot.get(),
                           self.issuedate.get(),
                           self.expdate.get(),
                           self.dailydose.get(),
                           self.storage.get(),
                           self.nhsnumber.get(),
                           self.pname.get(),
                           self.dob.get(),
                           self.address.get()))
              conn.commit()
              self.fetch_data()
              conn.close()
              messagebox.showinfo("Success", "Record has been inserted")

    def update_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database="pythongui")
        my_cursor=conn.cursor()
        my_cursor.execute("update hospital set nameoftablets=%s,dose=%s,nooftablets=%s,lot=%s,issuedate=%s,expdate=%s,dailydose=%s,storage =%s,nhsnumber=%s,pname=%s,dob=%s,address=%s where ref=%s",
                               (
                             self.nameoftablets.get(),
                             self.dose.get(),
                             self.nooftablets.get(),
                             self.lot.get(),
                             self.issuedate.get(),
                             self.expdate.get(),
                             self.dailydose.get(),
                             self.storage.get(),
                             self.nhsnumber.get(),
                             self.pname.get(),
                             self.dob.get(),
                             self.address.get(),
                             self.ref.get()))

        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Update","Your details has been updated successfully")                    

    def fetch_data(self):
          conn=mysql.connector.connect(host="localhost",username="root",password="root",database="pythongui")
          my_cursor=conn.cursor()
          my_cursor.execute("select * from hospital")
          rows=my_cursor.fetchall()
          if len(rows)!=0:
             self.hospital_table.delete(*self.hospital_table.get_children())
             for i in rows:
                self.hospital_table.insert("", END, values=i)
             conn.commit()
          conn.close()

    def get_cursor(self, event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.dose.set(row[2])
        self.nooftablets.set(row[3])
        self.lot.set(row[4])
        self.issuedate.set(row[5])
        self.expdate.set(row[6])
        self.dailydose.set(row[7])
        self.storage.set(row[8])
        self.nhsnumber.set(row[9])
        self.pname.set(row[10])
        self.dob.set(row[11])
        self.address.set(row[12])

    def iPrescription(self):

        self.txtPrescription.insert(END, "Name of Tablets:\t\t\t" + self.nameoftablets.get() + "\n")
        self.txtPrescription.insert(END, "Reference No:\t\t\t" + self.ref.get() + "\n")
        self.txtPrescription.insert(END, "Dose:\t\t\t" + self.dose.get() + "\n")
        self.txtPrescription.insert(END, "Number of Tablets:\t\t\t" + self.nooftablets.get() + "\n")
        self.txtPrescription.insert(END, "Lot:\t\t\t" + self.lot.get() + "\n")
        self.txtPrescription.insert(END, "Issue Date:\t\t\t" + self.issuedate.get() + "\n")
        self.txtPrescription.insert(END, "Exp Date:\t\t\t" + self.expdate.get() + "\n")
        self.txtPrescription.insert(END, "daily Dose:\t\t\t" + self.dailydose.get() + "\n")
        self.txtPrescription.insert(END, "Side Effect:\t\t\t" + self.sideeffect.get() + "\n")
        self.txtPrescription.insert(END, "Further Information:\t\t\t" + self.furtherinformation.get() + "\n")
        self.txtPrescription.insert(END, "StorageAdvice:\t\t\t" + self.storage.get() + "\n")
        self.txtPrescription.insert(END, "Driving Using Machine:\t\t\t" + self.drivingusingmachine.get() + "\n")
        self.txtPrescription.insert(END, "Patient Id:\t\t\t" + self.patientid.get() + "\n")
        self.txtPrescription.insert(END, "NHSNumber:\t\t\t" + self.nhsnumber.get() + "\n")
        self.txtPrescription.insert(END, "PatientName:\t\t\t" + self.pname.get() + "\n")
        self.txtPrescription.insert(END, "Date Of Birth:\t\t\t" + self.dob.get() + "\n")
        self.txtPrescription.insert(END, "PatientAddress:\t\t\t" + self.address.get() + "\n")

    def idelete(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="root", database="pythongui")
        my_cursor=conn.cursor()
        query="delete from hospital where ref=%s"
        value=(self.ref.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete","Patient has been deleted successfully")

    def clear(self):
        self.nameoftablets.set("")
        self.ref.set("")
        self.dose.set("")
        self.nooftablets.set("")
        self.lot.set("")
        self.issuedate.set("")
        self.expdate.set("")
        self.dailydose.set("")
        self.sideeffect.set("")
        self.furtherinformation.set("")
        self.storage.set("")
        self.drivingusingmachine.set("")
        self.howtousemedication.set("")
        self.patientid.set("")
        self.nhsnumber.set("")
        self.pname.set("")
        self.dob.set("")
        self.address.set("")
        self.txtPrescription.delete("1.0",END)

    def iExit(self):
        iExit=messagebox.askyesno("Hospital management system","Confirm you want to exit")
        if iExit>0:
            root.destroy()
            return



root=Tk()
ob = Hospital(root)
root.mainloop()



