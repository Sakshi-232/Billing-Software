from tkinter import *
from tkinter import font
from tkinter.font import BOLD
import random,math
from tkinter import messagebox
import os


class bill_app():
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x900+0+0")
        self.root.title("BILLING SOFTWARE")
        title=Label(self.root,text="BILLING SOFTWARE", font=("times new roman", 30, "bold"),bd=12,bg="steelblue",fg="white",relief=GROOVE)
        title.pack(pady=5,fill=BOTH)

        #---creating variables---#

        self.bath_soap = IntVar()
        self.body_lotion = IntVar()
        self.hair_gel = IntVar()
        self.face_gel = IntVar()
        self.face_wash = IntVar()
        self.face_cream = IntVar()

        self.rice = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.daal = IntVar()
        self.food_oil = IntVar()
        self.tea = IntVar()

        self.frooti = IntVar()
        self.thumbs_up = IntVar()
        self.cock = IntVar()
        self.maaza = IntVar()
        self.limca = IntVar()
        self.sprite = IntVar()

        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.drink_price = StringVar()
        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.drink_tax = StringVar()


        self.customer_name = StringVar()
        self.phone_no = StringVar()

        #--to generate raandom bill number
        self.bill_no = StringVar()
        x = random.randint(1000,9999)
        self.bill_no.set(str(x))

        self.search_bill = StringVar()

        #---Customer Details Frame---#

        f1 = LabelFrame(self.root,text="Customer Details", font="lucida 15 bold",bg="steelblue",fg="gold",bd=10,relief=GROOVE)
        f1.place(x=0,y=80,relwidth=1)

        customer_label = Label(f1,text="Customer Name", font="lucida 15 bold",bg="steelblue",fg="white")
        customer_label.grid(row=0,column=0,padx=20,pady=10)

        phone_label = Label(f1,text="Phone Number", font="lucida 15 bold",bg="steelblue",fg="white")
        phone_label.grid(row=0,column=3,padx=20,pady=10)

        bill_label = Label(f1,text="Bill Number", font="lucida 15 bold",bg="steelblue",fg="white")
        bill_label.grid(row=0,column=5,padx=20,pady=10)

        #--creating entry field for customer name---#

        customer_value_entry = Entry(f1,textvariable=self.customer_name,width=20,font="arial",bd=6,relief=SUNKEN)
        customer_value_entry.grid(row=0,column=1,pady=10)

        #--creating entry field for phone number---#

        phone_value_entry = Entry(f1,textvariable=self.phone_no,width=20,font="arial",bd=6,relief=SUNKEN)
        phone_value_entry.grid(row=0,column=4,pady=10)

        #--creating entry field for bill number---#
        #,textvariable=self.bill_no
        bill_value_entry = Entry(f1,bd=6,width=20,font="arial",relief=SUNKEN,textvariable=self.search_bill)
        bill_value_entry.grid(row=0,column=6,pady=10)

        #---creating a button to search---#

        bill_button = Button(f1,text="Search",width=12,bg="white",fg="black",relief=GROOVE,bd=7,font="arial 15 bold",command=self.find_bill)
        bill_button.grid(row=0,column=7,pady=10,padx=15)

        #---Creating a cosmetic frame---#

        f2 = LabelFrame(self.root,text="Cosmetics",font="lucida 15 bold",bg="steelblue",fg="gold",bd=10,relief=GROOVE)
        f2.place(x=5,y=190,width=300,height=370)

        bath_soap = Label(f2,text="Bath Soap",font="lucida 15 bold",bg="steelblue",fg="white")
        bath_soap.grid(row=0,column=0,padx=3,pady=11)

        body_lotion = Label(f2,text="Body Lotion",font="lucida 15 bold",bg="steelblue",fg="white")
        body_lotion.grid(row=1,column=0,padx=3,pady=11)

        hair_gel = Label(f2,text="Hair Gel",font="lucida 15 bold",bg="steelblue",fg="white")
        hair_gel.grid(row=2,column=0,padx=3,pady=11)

        face_wash = Label(f2,text="Face wash",font="lucida 15 bold",bg="steelblue",fg="white")
        face_wash.grid(row=3,column=0,padx=3,pady=11)

        face_cream = Label(f2,text="Face Cream",font="lucida 15 bold",bg="steelblue",fg="white")
        face_cream.grid(row=4,column=0,padx=3,pady=11)

        hair_spray = Label(f2,text="Hair Spray",font="lucida 15 bold",bg="steelblue",fg="white")
        hair_spray.grid(row=5,column=0,padx=3,pady=11)

        #---creating entry field for all labels in f2--#

        bath_soap_entry = Entry(f2,textvariable=self.bath_soap,width=8,bd=5,relief=SUNKEN,font="ariel ")
        bath_soap_entry.grid(row=0,column=1,padx=3,pady=7)

        body_lotion_entry = Entry(f2,textvariable=self.body_lotion,width=8,bd=5,relief=SUNKEN,font="ariel ")
        body_lotion_entry.grid(row=1,column=1,padx=3,pady=7)

        hair_gel_entry = Entry(f2,textvariable=self.hair_gel,width=8,bd=5,relief=SUNKEN,font="ariel ")
        hair_gel_entry.grid(row=2,column=1,padx=3,pady=7)

        face_gel_entry = Entry(f2,textvariable=self.face_gel,width=8,bd=5,relief=SUNKEN,font="ariel ")
        face_gel_entry.grid(row=3,column=1,padx=3,pady=7)

        face_wash_entry = Entry(f2,textvariable=self.face_wash,width=8,bd=5,relief=SUNKEN,font="ariel ")
        face_wash_entry.grid(row=4,column=1,padx=3,pady=7)

        face_cream_entry = Entry(f2,textvariable=self.face_cream,width=8,bd=5,relief=SUNKEN,font="ariel ")
        face_cream_entry.grid(row=5,column=1,padx=3,pady=7)


        #---creating grocery frame---#


        f3 = LabelFrame(self.root,text="Grocery",font="lucida 15 bold",bg="steelblue",fg="gold",bd=10,relief=GROOVE)
        f3.place(x=305,y=190,width=280,height=370)

        rice = Label(f3,text="Rice",font="lucida 15 bold",bg="steelblue",fg="white")
        rice.grid(row=0,column=3,padx=3,pady=11)

        Wheat = Label(f3,text="Wheat",font="lucida 15 bold",bg="steelblue",fg="white")
        Wheat.grid(row=1,column=3,padx=3,pady=11)

        Sugar = Label(f3,text="Sugar",font="lucida 15 bold",bg="steelblue",fg="white")
        Sugar.grid(row=2,column=3,padx=3,pady=11)

        daal = Label(f3,text="Daal",font="lucida 15 bold",bg="steelblue",fg="white")
        daal.grid(row=3,column=3,padx=3,pady=11)

        food_oil = Label(f3,text="Food Oil",font="lucida 15 bold",bg="steelblue",fg="white")
        food_oil.grid(row=4,column=3,padx=3,pady=11)

        tea = Label(f3,text="Tea",font="lucida 15 bold",bg="steelblue",fg="white")
        tea.grid(row=5,column=3,padx=3,pady=11)

        #---creating entry field for all labels in f3--#

        rice_entry = Entry(f3,textvariable=self.rice,width=8,bd=5,relief=SUNKEN,font="ariel ")
        rice_entry.grid(row=0,column=4,padx=5,pady=7)

        wheat_entry = Entry(f3,textvariable=self.wheat,width=8,bd=5,relief=SUNKEN,font="ariel ")
        wheat_entry.grid(row=1,column=4,padx=3,pady=7)

        sugar_entry = Entry(f3,textvariable=self.sugar,width=8,bd=5,relief=SUNKEN,font="ariel ")
        sugar_entry.grid(row=2,column=4,padx=3,pady=7)

        daal_entry = Entry(f3,textvariable=self.daal,width=8,bd=5,relief=SUNKEN,font="ariel ")
        daal_entry.grid(row=3,column=4,padx=3,pady=7)

        food_oil_entry = Entry(f3,textvariable=self.food_oil,width=8,bd=5,relief=SUNKEN,font="ariel ")
        food_oil_entry.grid(row=4,column=4,padx=3,pady=7)

        tea_entry = Entry(f3,textvariable=self.tea,width=8,bd=5,relief=SUNKEN,font="ariel ")
        tea_entry.grid(row=5,column=4,padx=3,pady=7)



        #---Creating a cold drink frame---#

        f4 = LabelFrame(self.root,text="Cold Drinks",font="lucida 15 bold",bg="steelblue",fg="gold",bd=10,relief=GROOVE)
        f4.place(x=585,y=190,width=300,height=370)

        frooti = Label(f4,text="Frooti",font="lucida 15 bold",bg="steelblue",fg="white")
        frooti.grid(row=0,column=5,padx=3,pady=11)

        thumbs_up = Label(f4,text="Thumbs Up",font="lucida 15 bold",bg="steelblue",fg="white")
        thumbs_up.grid(row=1,column=5,padx=3,pady=11)

        cock = Label(f4,text="Cock",font="lucida 15 bold",bg="steelblue",fg="white")
        cock.grid(row=2,column=5,padx=3,pady=11)

        maaza = Label(f4,text="Maaza",font="lucida 15 bold",bg="steelblue",fg="white")
        maaza.grid(row=3,column=5,padx=3,pady=11)

        limca = Label(f4,text="Limca",font="lucida 15 bold",bg="steelblue",fg="white")
        limca.grid(row=4,column=5,padx=3,pady=11)

        sprite = Label(f4,text="Sprite",font="lucida 15 bold",bg="steelblue",fg="white")
        sprite.grid(row=5,column=5,padx=3,pady=11)

        #---creating entry field for all labels in f4--#

        frooti_entry = Entry(f4,textvariable=self.frooti,width=8,bd=5,relief=SUNKEN,font="ariel ")
        frooti_entry.grid(row=0,column=6,padx=3,pady=7)

        thumbs_up_entry = Entry(f4,textvariable=self.thumbs_up,width=8,bd=5,relief=SUNKEN,font="ariel ")
        thumbs_up_entry.grid(row=1,column=6,padx=3,pady=7)

        cock_entry = Entry(f4,textvariable=self.cock,width=8,bd=5,relief=SUNKEN,font="ariel ")
        cock_entry.grid(row=2,column=6,padx=3,pady=7)

        maaza_entry = Entry(f4,textvariable=self.maaza,width=8,bd=5,relief=SUNKEN,font="ariel ")
        maaza_entry.grid(row=3,column=6,padx=3,pady=7)

        limca_entry = Entry(f4,textvariable=self.limca,width=8,bd=5,relief=SUNKEN,font="ariel ")
        limca_entry.grid(row=4,column=6,padx=3,pady=7)

        sprite_entry = Entry(f4,textvariable=self.sprite,width=8,bd=5,relief=SUNKEN,font="ariel ")
        sprite_entry.grid(row=5,column=6,padx=3,pady=7)  


        #---creating bill area---#


        f5 = LabelFrame(self.root,bd=10,relief=GROOVE)
        f5.place(x=910,y=190,width=600,height=370)

        bill_title= Label(f5,text="Bill Area", font="lucida 15 bold",bd=7,relief=GROOVE)  
        bill_title.pack(fill="x")    

        #--scroll bar in bill area--#

        scrol_y = Scrollbar(f5,orient=VERTICAL)
        self.textarea = Text(f5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #--Button Frame--#

        f6 = LabelFrame(self.root,text="Bill Menu",font="lucida 15 bold",bg="steelblue",fg="gold",bd=10,relief=GROOVE)
        f6.place(x=0,y=565,relwidth=1,height=230)

        
        cosmetic_price = Label(f6,text="Total Cosmetic Price",font="lucida 15 bold",bg="steelblue",fg="white")
        cosmetic_price.grid(row=0,column=0,padx=3,pady=15)

        grocery_price = Label(f6,text="Total Grocery Price",font="lucida 15 bold",bg="steelblue",fg="white")
        grocery_price.grid(row=1,column=0,padx=3,pady=15)

        drink_price = Label(f6,text="Total Cold Drink Price",font="lucida 15 bold",bg="steelblue",fg="white")
        drink_price.grid(row=2,column=0,padx=3,pady=15)

        cosmetic_price_entry = Entry(f6,textvariable=self.cosmetic_price,width=10,bd=5,relief=SUNKEN,font="ariel ")
        cosmetic_price_entry.grid(row=0,column=2,padx=3,pady=7)

        grocery_price_entry = Entry(f6,textvariable=self.grocery_price,width=10,bd=5,relief=SUNKEN,font="ariel ")
        grocery_price_entry.grid(row=1,column=2,padx=3,pady=7)

        drink_price_entry = Entry(f6,textvariable=self.drink_price,width=10,bd=5,relief=SUNKEN,font="ariel ")
        drink_price_entry.grid(row=2,column=2,padx=3,pady=7)


        cosmetic_tax = Label(f6,text="Cosmetic Tax",font="lucida 15 bold",bg="steelblue",fg="white")
        cosmetic_tax.grid(row=0,column=3,padx=3,pady=15)

        grocery_tax = Label(f6,text="Grocery Tax",font="lucida 15 bold",bg="steelblue",fg="white")
        grocery_tax.grid(row=1,column=3,padx=5,pady=15)

        drink_price_tax = Label(f6,text="Cold Drink Tax",font="lucida 15 bold",bg="steelblue",fg="white")
        drink_price_tax.grid(row=2,column=3,padx=5,pady=15)

        cosmetic_tax_entry = Entry(f6,textvariable=self.cosmetic_tax,width=10,bd=5,relief=SUNKEN,font="ariel ")
        cosmetic_tax_entry.grid(row=0,column=4,padx=5,pady=7)

        grocery_tax_entry = Entry(f6,textvariable=self.grocery_tax,width=10,bd=5,relief=SUNKEN,font="ariel ")
        grocery_tax_entry.grid(row=1,column=4,padx=5,pady=7)

        drink_tax_entry = Entry(f6,textvariable=self.drink_tax,width=10,bd=5,relief=SUNKEN,font="ariel ")
        drink_tax_entry.grid(row=2,column=4,padx=3,pady=7)

        bottom_button_frame = Frame(f6,bd=7,relief=GROOVE)
        bottom_button_frame.place(x=800,width=700,height=180)

        total_button = Button(bottom_button_frame,text="Total",font=("times new roman",18,"bold"),bg="steelblue",fg="white",padx=10,pady=13,width=8,bd=5,command=self.total)
        total_button.grid(row=0,column=0,pady=28,padx=13)

        generate_bill_button = Button(bottom_button_frame,text="Generate Bill",font=("times new roman",18,"bold"),bg="steelblue",fg="white",padx=10,pady=13,width=9,bd=5,command=self.bill_area)
        generate_bill_button.grid(row=0,column=1,pady=28,padx=13)

        clear_button = Button(bottom_button_frame,text="Clear",font=("times new roman",18,"bold"),bg="steelblue",fg="white",padx=10,pady=13,width=8,bd=5,command=self.clear_data)
        clear_button.grid(row=0,column=2,pady=28,padx=13)

        exit_button = Button(bottom_button_frame,text="Exit",font=("times new roman",18,"bold"),bg="steelblue",fg="white",padx=10,pady=13,width=7,bd=5,command=self.exit_app)
        exit_button.grid(row=0,column=3,pady=28,padx=13)
        self.welcome_bill()


    def total(self):
        self.price_bath_soap = (self.bath_soap.get()*36)
        self.price_body_lotion=(self.body_lotion.get()*70)
        self.price_hair_gel=(self.hair_gel.get()*55)
        self.price_face_gel=(self.face_gel.get()*30)
        self.price_face_wash=(self.face_wash.get()*40)
        self.price_face_cream=(self.face_cream.get()*120)


        self.price_rice=(self.rice.get()*70)
        self.price_wheat=(self.wheat.get()*50)
        self.price_sugar=(self.sugar.get()*85)
        self.price_daal=(self.daal.get()*73)
        self.price_food_oil=(self.food_oil.get()*112)
        self.price_tea=(self.tea.get()*50)

        self.price_frooti=(self.frooti.get()*20)
        self.price_thumbs_up=(self.thumbs_up.get()*70)
        self.price_cock=(self.cock.get()*200)
        self.price_maaza=(self.maaza.get()*130)
        self.price_limca=(self.limca.get()*75)
        self.price_sprite=(self.sprite.get()*120)


        self.total_cosmetic_price = float(self.price_bath_soap+
            self.price_body_lotion+
            self.price_hair_gel+
            self.price_face_gel+
            self.price_face_wash+
            self.price_face_cream
        )

        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax = round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))   
 

        self.total_grocery_price = float(
            self.price_rice+
            self.price_wheat+
            self.price_sugar+
            self.price_daal+
            self.price_food_oil+
            self.price_tea
        )

        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price*0.07),2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))  #--7% tax on grocery products

        self.total_drink_price = float(self.price_frooti+
            self.price_thumbs_up+
            self.price_cock+
            self.price_maaza+
            self.price_limca+
            self.price_sprite
        )

        self.drink_price.set("Rs. "+str(self.total_drink_price))
        self.d_tax = round((self.total_drink_price*0.1),2)
        self.drink_tax.set("Rs. "+str(self.d_tax))   #--10% tax on cosmetic products

        self.total_bill = float(self.total_cosmetic_price + 
                        self.total_grocery_price + 
                        self.total_drink_price +
                        self.c_tax +
                        self.g_tax +
                        self.d_tax
            )

        

    #--Welcome text in bill area

    def welcome_bill(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t\tWELCOME TO LADUU SHOPPING MART")
        self.textarea.insert(END,f"\n\n BILL NUMBER : {self.bill_no.get()}")
        self.textarea.insert(END,f"\n CUSTOMER NAME : {self.customer_name.get()}")
        self.textarea.insert(END,f"\n PHONE NUMBER : {self.phone_no.get()}")
        self.textarea.insert(END,"\n---------------------------------------------------------------------")
        self.textarea.insert(END,"\n PRODUCTS\t\t\t\t\tQTY\t\tPRICE")
        self.textarea.insert(END,"\n---------------------------------------------------------------------")
       

    def bill_area(self):
        if self.customer_name.get() =="" or self.phone_no.get()  =="":
                messagebox.showerror("Error!","Please Fill Customer Details")
        elif self.cosmetic_price.get() == "Rs. 0.0" and self.grocery_price.get() == "Rs. 0.0" and self.drink_price.get() == "Rs. 0.0":
                messagebox.showerror("Error!","Select Atleast One Product")
        else:
            self.welcome_bill()
            #---cosmetics--#
            if self.bath_soap.get() !=0 :
                self.textarea.insert(END,f"\n Bath Soap\t\t\t\t\t {self.bath_soap.get()}\t\t {self.price_bath_soap}")
            if self.body_lotion.get() !=0 :
                self.textarea.insert(END,f"\n Body Lotion\t\t\t\t\t {self.body_lotion.get()}\t\t {self.price_body_lotion}")
            if self.hair_gel.get() !=0 :
                self.textarea.insert(END,f"\n Hair Gel\t\t\t\t\t {self.hair_gel.get()}\t\t {self.price_hair_gel}")
            if self.face_gel.get() !=0 :
                self.textarea.insert(END,f"\n Face Gel\t\t\t\t\t {self.face_gel.get()}\t\t {self.price_face_gel}")
            if self.face_wash.get() !=0 :
                self.textarea.insert(END,f"\n Face Wash\t\t\t\t\t {self.face_wash.get()}\t\t {self.price_face_wash}")
            if self.face_cream.get() !=0 :
                self.textarea.insert(END,f"\n Face Cream\t\t\t\t\t {self.face_cream.get()}\t\t {self.price_face_cream}")

            #--grocery--#
            if self.rice.get() !=0 :
                self.textarea.insert(END,f"\n Rice\t\t\t\t\t {self.rice.get()}\t\t {self.price_rice}")
            if self.wheat.get() !=0 :
                self.textarea.insert(END,f"\n Wheat\t\t\t\t\t {self.wheat.get()}\t\t {self.price_wheat}")
            if self.sugar.get() !=0 :
                self.textarea.insert(END,f"\n Sugar\t\t\t\t\t {self.sugar.get()}\t\t {self.price_sugar}")
            if self.daal.get() !=0 :
                self.textarea.insert(END,f"\n Daal\t\t\t\t\t {self.daal.get()}\t\t {self.price_daal}")
            if self.food_oil.get() !=0 :
                self.textarea.insert(END,f"\n Food Oil\t\t\t\t\t {self.food_oil.get()}\t\t {self.price_food_oil}")
            if self.tea.get() !=0 :
                self.textarea.insert(END,f"\n Tea\t\t\t\t\t {self.tea.get()}\t\t {self.price_tea}")

            #--cold drink--#
            if self.frooti.get() !=0 :
                self.textarea.insert(END,f"\n Frooti\t\t\t\t\t {self.frooti.get()}\t\t {self.price_frooti}")
            if self.thumbs_up.get() !=0 :
                self.textarea.insert(END,f"\n Thumbs Up\t\t\t\t\t {self.thumbs_up.get()}\t\t {self.price_thumbs_up}")
            if self.cock.get() !=0 :
                self.textarea.insert(END,f"\n Cock\t\t\t\t\t {self.cock.get()}\t\t {self.price_cock}")
            if self.maaza.get() !=0 :
                self.textarea.insert(END,f"\n Maaza\t\t\t\t\t {self.maaza.get()}\t\t {self.price_maaza}")
            if self.limca.get() !=0 :
                self.textarea.insert(END,f"\n Limca\t\t\t\t\t {self.limca.get()}\t\t {self.price_limca}")
            if self.sprite.get() !=0 :
                self.textarea.insert(END,f"\n Sprite\t\t\t\t\t {self.sprite.get()}\t\t {self.price_sprite}")

            
            self.textarea.insert(END,"\n---------------------------------------------------------------------")
            if self.cosmetic_tax.get() != "Rs. 0.0":
                self.textarea.insert(END,f"\n Cosmetic Tax\t\t\t\t\t\t\t {self.c_tax}")
            if self.grocery_tax.get() != "Rs. 0.0":
                self.textarea.insert(END,f"\n Grocery Tax\t\t\t\t\t\t\t {self.g_tax}")
            if self.drink_tax.get() != "Rs. 0.0":
                self.textarea.insert(END,f"\n Cold Drink Tax\t\t\t\t\t\t\t {self.d_tax}")
            self.textarea.insert(END,"\n---------------------------------------------------------------------")
            self.textarea.insert(END,f"\n Total\t\t\t\t\t\t\tRs. {self.total_bill}")
            self.save_bill()


    def save_bill(self):
        generate = messagebox.askyesno("Save Bill","Do You Want To Save The Bill")
        if generate>0:      
            self.bill_data = self.textarea.get('1.0',END)
            f1 = open("generate_bill/"+ str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved","Bill Saved Succesfully")
        else:
            return

    def find_bill(self):
        present=1
        for i in os.listdir("generate_bill/"):        
            if i.split(".")[0] == self.search_bill.get():
                f1= open(f"generate_bill/{i}","r")
                self.textarea.delete('1.0',END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                present=0
        if present==1:
            messagebox.showerror("Error","Invalid Bill Number")

    def clear_data(self):
        cut = messagebox.askyesno("Clear","Are you Sure You Want Clear The Data")
        if cut>0:
            self.bath_soap.set(0)
            self.body_lotion.set(0)
            self.hair_gel.set(0)
            self.face_gel.set(0)
            self.face_wash.set(0)
            self.face_cream.set(0)

            self.rice.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.daal.set(0)
            self.food_oil.set(0)
            self.tea.set(0)

            self.frooti.set(0)
            self.thumbs_up.set(0)
            self.cock.set(0)
            self.maaza.set(0)
            self.limca.set(0)
            self.sprite.set(0)

            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.drink_price.set("")
            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.drink_tax.set("")


            self.customer_name.set("")
            self.phone_no.set("")

            #--to generate raandom bill number
            self.bill_no.set("")
            x = random.randint(1000,9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()

    def exit_app(self):
        erase= messagebox.askyesno("Exit","Are You Sure You Want To Exit")
        if erase > 0:
            self.root.destroy()
 





    



if __name__ == '__main__':
    root = Tk()
    obj = bill_app(root)                         #creating an object of bill app

    root.mainloop()