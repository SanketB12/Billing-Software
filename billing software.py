from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk 
import random,os
from tkinter import messagebox
import tempfile
from time import strftime

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Mobile Billing Software")

        # Variables

        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000, 9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.tax=IntVar()
        self.disc=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()
        self.grand_total=StringVar()

        #PRODUCT Category list
        self.Category=["Select Option","Mobiles"]
        self.Subcatmobile=["Oppo","Vivo","Samsung","Redmi","Iphone"]

        self.oppo=["Reno7 Pro","F21 Pro","A74 5G","A31","Find X3 Pro"]
        self.price_reno7_pro=39999
        self.price_F21_Pro=22999
        self.price_A74_5G=15490
        self.price_A31=12690
        self.price_X3_Pro=99990

        self.Vivo=["V20","Y31","X60 Pro","Y20I","V17 PRO"]
        self.price_V20=9990
        self.price_Y31=7999
        self.price_X60_pro=49990
        self.price_Y20I=13990
        self.price_V17_pro=19999

        self.Samsung=["Galaxy S20","Galaxy M33","Galaxy F23","Galaxy M53","Galaxy S22 Ultra"]
        self.price_S20=34820
        self.price_M33=16920
        self.price_F23=15999
        self.price_M53=26499
        self.price_S22=99999

        self.Redmi=["Note 11 Pro","Note 11S","Note 11T","Note 9i Sport","Note 10 Pro Max"]
        self.price_11_pro=15999
        self.price_11S=17499
        self.price_11T=16999
        self.price_9i=8999
        self.price_10_pro=19999
        
        self.Iphone=["iphone 11","iphone 12","iphone 13","iphone 13 Pro M","iphone 10"]
        self.price_11=42900
        self.price_12=58990
        self.price_13=72990
        self.price_13_pro=173990
        self.price_10=29990

 

        #image1
        img=Image.open("store1.jpg")
        img=img.resize((390,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=0,y=2,width=390,height=130)
        
        #image2
        img_1=Image.open("store2.jpg")
        img_1=img_1.resize((390,130),Image.Resampling.LANCZOS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)
        
        lbl_img_1=Label(self.root,image=self.photoimg_1)
        lbl_img_1.place(x=390,y=0)
        
        #image3
        img_2=Image.open("store3.jpg")
        img_2=img_2.resize((390,130),Image.Resampling.LANCZOS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)
        
        lbl_img_2=Label(self.root,image=self.photoimg_2)
        lbl_img_2.place(x=780,y=0)
       
        #image4
        img_3=Image.open("store4.jpg")
        img_3=img_3.resize((390,130),Image.Resampling.LANCZOS)
        self.photoimg_3=ImageTk.PhotoImage(img_3)
        
        lbl_img_3=Label(self.root,image=self.photoimg_3)
        lbl_img_3.place(x=1170,y=0)

        #Title
        lbl_title=Label(self.root,text="MOBILE  BILLING  SOFTWARE",font=("times new roman",35,"bold"),bg="black",fg="white")
        lbl_title.place(x=0,y=130,width=1540,height=45)

        def time():
            string = strftime('%I:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(lbl_title,font=('times new roman',16,'bold'),background= 'black',foreground='yellow')
        lbl.place(x=0,y=0,width=120,height=45)
        time()

        # def date():   
        #     string = strftime('%d/%m/%Y')
        #     lbl.config(text=string)
        #     lbl.after(1000, date)

        # lbl = Label(lbl_title,font=('times new roman',16,'bold'),background= 'black',foreground='yellow')
        # lbl.place(x=1412,y=0,width=120,height=45)
        # date()

         
        #Frame
        Main_Frame=Frame(self.root,bd=20,relief=GROOVE,bg="black")
        Main_Frame.place(x=0,y=175,width=1538,height=664)
        
        #Customer
        Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",20,"bold"),bd=5,bg="black",fg="yellow")
        Cust_Frame.place(x=20,y=12,width=355,height=160)
        
        #Mobile
        self.lbl_mob=Label(Cust_Frame,text=" Mobile No :",font=("times new roman",15,"bold"),bg="black",fg="white")
        self.lbl_mob.grid(row=0,column=0,stick=W,padx=5,pady=5)
        self.entry_mob=ttk.Entry(Cust_Frame,textvariable= self.c_phon,font=("times new roman",10,"bold"),width=30)
        self.entry_mob.grid(row=0,column=1)
        
        #Name
        self.lbl_name=Label(Cust_Frame,text=" Name        :",font=("times new roman",15,"bold"),bg="black",fg="white")
        self.lbl_name.grid(row=1,column=0,stick=W,padx=5,pady=2)
        self.entry_name=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=("times new roman",10,"bold"),width=30)
        self.entry_name.grid(row=1,column=1)
        
        #Email
        self.lbl_mail=Label(Cust_Frame,text=" Email        :",font=("times new roman",15,"bold"),bg="black",fg="white")
        self.lbl_mail.grid(row=2,column=0,stick=W,padx=5,pady=5)
        self.entry_mail=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=("times new roman",10,"bold"),width=30)
        self.entry_mail.grid(row=2,column=1)
       
        #Product
        Product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",20,"bold"),bd=5,bg="black",fg="Yellow")
        Product_Frame.place(x=20,y=180,width=355,height=315)
        
        #Category
        self.lbl_cat=Label(Product_Frame,text=" Select Category :",font=("times new roman",15,"bold"),bg="black",fg="white")
        self.lbl_cat.grid(row=0,column=0,stick=W,padx=5,pady=5)
        self.Combo_cat=ttk.Combobox(Product_Frame,value=self.Category,font=("times new roman",10,"bold"),width=20,state="readonly")
        self.Combo_cat.current(0)
        self.Combo_cat.grid(row=0,column=1,stick=W,padx=5,pady=5)
        self.Combo_cat.bind("<<ComboboxSelected>>",self.cats)
        
        #SubCategory
        self.lbl_sub=Label(Product_Frame,text=" Sub - Category   :",font=("times new roman",15,"bold"),bg="black",fg="white")
        self.lbl_sub.grid(row=1,column=0,stick=W,padx=5,pady=5)
        self.Combo_sub=ttk.Combobox(Product_Frame,value=[""],font=("times new roman",10,"bold"),width=20,state="readonly")
        self.Combo_sub.grid(row=1,column=1,stick=W,padx=5,pady=5)
        self.Combo_sub.bind("<<ComboboxSelected>>",self.Product_add)
        
        #Product Name
        self.lbl_pn=Label(Product_Frame,text=" Product Name    :",font=("times new roman",15,"bold"),bg="black",fg="white")
        self.lbl_pn.grid(row=2,column=0,stick=W,padx=5,pady=5)
        self.Combo_pn=ttk.Combobox(Product_Frame,textvariable=self.product,font=("times new roman",10,"bold"),width=20,state="readonly")
        self.Combo_pn.grid(row=2,column=1,stick=W,padx=5,pady=5) 
        self.Combo_pn.bind("<<ComboboxSelected>>",self.price)
        
        #Price
        self.lbl_price=Label(Product_Frame,text=" Price                   :",font=("times new roman",15,"bold"),bg="black",fg="white")
        self.lbl_price.grid(row=3,column=0,stick=W,padx=5,pady=5)
        self.Combo_price=ttk.Combobox(Product_Frame,textvariable=self.prices,font=("times new roman",10,"bold"),width=20,state="readonly")
        self.Combo_price.grid(row=3,column=1,stick=W,padx=5,pady=5)
        

        #Quantity
        self.lbl_qua=Label(Product_Frame,text=" Quantity             :",font=("times new roman",15,"bold"),bg="black",fg="white")
        self.lbl_qua.grid(row=4,column=0,stick=W,padx=5,pady=5)
        self.entry_qua=ttk.Entry(Product_Frame,textvariable=self.qty,font=("times new roman",10,"bold"),width=22)
        self.entry_qua.grid(row=4,column=1)
        
        # Discount
        self.lbl_disc=Label(Product_Frame,text=" Discount             :",font=("times new roman",15,"bold"),bg="black",fg="white")
        self.lbl_disc.grid(row=5,column=0,stick=W,padx=5,pady=5)
        self.entry_disc=ttk.Entry(Product_Frame,textvariable=self.disc,font=("times new roman",10,"bold"),width=22)
        self.entry_disc.grid(row=5,column=1)

        # Tax
        self.lbl_tax=Label(Product_Frame,text=" Tax  %                :",font=("times new roman",15,"bold"),bg="black",fg="white")
        self.lbl_tax.grid(row=6,column=0,stick=W,padx=5,pady=5)

        self.entry_tax=ttk.Entry(Product_Frame,textvariable=self.tax,font=("times new roman",10,"bold"),width=22)
        self.entry_tax.grid(row=6,column=1,sticky=W,padx=5,pady=5)

        # Bill Frame
        billframe = LabelFrame(Main_Frame,text="Bill",font=("times new roman",20,"bold"),bd=5,bg="black",fg="yellow")
        billframe.place(x=990,y=40,width=490,height=435)
        
        scroll_y=Scrollbar(billframe,orient=VERTICAL)
        self.textarea=Text(billframe,yscrollcommand=scroll_y.set,font=("times new roman",15,"bold"),bg="black",fg="white")
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

         #Bill Counter
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",20,"bold"),bd=5,bg="black",fg="yellow")
        Bottom_Frame.place(x=990,y=480,width=490,height=135)

         
        # self.lblSubTotal=Label(Bottom_Frame,text="Sub Total :",font=("times new roman",15,"bold"),bg="black",fg="white")
        # self.lblSubTotal.grid(row=0,column=0,stick=W,padx=5,pady=5)

        # self.entry_qua=ttk.Entry(Bottom_Frame,font=("times new roman",10,"bold"),width=22)
        # self.entry_qua.grid(row=0,column=1,sticky=W,padx=5,pady=5)

        # self.lbl_tax=Label(Bottom_Frame,text="Tax % :",font=("times new roman",15,"bold"),bg="black",fg="white")
        # self.lbl_tax.grid(row=1,column=0,stick=W,padx=5,pady=5)

        # self.txt_tax=ttk.Entry(Bottom_Frame,textvariable=self.tax,font=("times new roman",10,"bold"),width=22)
        # self.txt_tax.grid(row=1,column=1,sticky=W,padx=5,pady=5)

        # self.lblamount=Label(Bottom_Frame,text="Total        :",font=("times new roman",15,"bold"),bg="black",fg="white")
        # self.lblamount.grid(row=2,column=0,sticky=W,padx=5,pady=5)

        # self.txtamount=ttk.Entry(Bottom_Frame,font=("times new roman",10,"bold"),width=22)
        # self.txtamount.grid(row=2,column=1,sticky=W,padx=5,pady=5)

        #Button frame
        Btn_frame=Frame(Bottom_Frame, bd=2,bg="white")
        Btn_frame.place(x=7,y=0)

        self.BtnAddToCart=Button(Btn_frame,command=self.AddItem,text="Add To Cart", font=("times new roman",16,"bold"),bg="Blue", fg="White", width=12)
        self.BtnAddToCart.grid(row=0, column=0)

        self.BtnGenerateBill=Button(Btn_frame,command=self.gen_bill,text="Generate Bill", font=("times new roman",16,"bold"),bg="Blue", fg="White", width=12)
        self.BtnGenerateBill.grid(row=1, column=0)

        self.BtnSave=Button(Btn_frame,command=self.save_bill,text="Save", font=("times new roman",16,"bold"),bg="Blue", fg="White", width=12)
        self.BtnSave.grid(row=0, column=2)

        self.BtnPrint=Button(Btn_frame,command=self.iprint,text="Print", font=("times new roman",16,"bold"),bg="Blue", fg="White", width=12)
        self.BtnPrint.grid(row=1, column=2)

        self.BtnClear=Button(Btn_frame,command=self.Clear,text="Clear", font=("times new roman",16,"bold"),bg="Blue", fg="White", width=12)
        self.BtnClear.grid(row=0, column=3)

        self.BtnExit=Button(Btn_frame,command=self.root.destroy,text="Exit", font=("times new roman",16,"bold"),bg="Blue", fg="White", width=12)
        self.BtnExit.grid(row=1, column=3)
        self.welcome()

        

        # Search
        Search_Frame=Frame(Main_Frame, bd=2,bg="black")
        Search_Frame.place(x=998,y=5,width=490,height=35)

        self.lblBill=Label(Search_Frame,text="Bill No",font=("times new roman",16,"bold"),bg="Red", fg="White", width=13)
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1)

        #Entry
        self.txt_Entry=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=("times new roman",16,"bold"),width=15)
        self.txt_Entry.grid(row=0,column=1,sticky=W,padx=2)
        
        # Search Button
        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search", font=("times new roman",12,"bold"),bg="Green", fg="White", width=13)
        self.BtnSearch.grid(row=0, column=2)

        #Middle frame
        middle_frame=Frame(self.root,bd=5,bg="Black")
        middle_frame.place(x=401,y=215,width=610,height=450)
        
        #image5
        img5=Image.open("store5.jpg")
        img5=img5.resize((450,210),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        lbl_img5=Label(middle_frame,image=self.photoimg5,bd=5,bg="Black")
        lbl_img5.place(x=70,y=225)

         #image6
        img6=Image.open("store6.jpg")
        img6=img6.resize((450,210),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        lbl_img6=Label(middle_frame,image=self.photoimg6,bd=5,bg="Black")
        lbl_img6.place(x=70,y=-8)

        self.l=[]
    
    # ===========================================Function Declaration============================================

    def AddItem(self):
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n 
        self.o=self.disc.get()
        self.q=self.tax.get()
        self.l.append(self.m)
        
        if self.product.get()=="":
            messagebox.showerror("Error","Please Select the Product Name")
        else:
            self.textarea.insert(END, f"\n {self.product.get()}\t\t      {self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%(((((sum(self.l)))*self.q)/100))))
            self.total.set(str('Rs.%.2f'%(((sum(self.l))) + (sum(self.l)*self.q/100))))
            self.grand_total.set(str('Rs.%.2f'%(((sum(self.l))) + (sum(self.l)*self.q/100) - (self.o))))

    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please Add To Cart Product")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END, text )
            self.textarea.insert(END,"\n =========================================")
            self.textarea.insert(END, f"\n Sub Amount   :\t{self.sub_total.get()}")
            self.textarea.insert(END, f"\n Tax Amount   :\t{self.tax_input.get()}")
            self.textarea.insert(END, f"\n Total Amount :\t{self.total.get()}")
            self.textarea.insert(END, f"\n Discount     :\tRs.{self.o}")
            self.textarea.insert(END, f"\n Grand Total  :\t{self.grand_total.get()}")
            self.textarea.insert(END,"\n =========================================")

    def save_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","No Data Found To Save !!")
        else:
            op=messagebox.askyesno("Save Bill" , "Do you want to save the Bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('bills/'+str(self.bill_no.get())+".txt",'w')
            f1.write(self.bill_data)
            op=messagebox.showinfo("Saved" , f"Bill No:{self.bill_no.get()} Saved Successfully")
            f1.close()

    def iprint(self):
        if self.product.get()=="":
            messagebox.showerror("Error","No Data Found To Print !!")
        else:
            q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")

    def find_bill(self):
        found="No"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f'bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="Yes"
        if found=='No':
            messagebox.showerror("Error","Invalid Bill No")

    def Clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phon.set("")
        self.c_email.set("")
        z=random.randint(1000, 9999)
        self.bill_no.set(str(z))
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.tax.set(0)
        self.disc.set(0)
        self.l=[0]
        self.sub_total.set("")
        self.tax_input.set("")
        self.total.set("")
        self.welcome()

        
    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END, "\t                   WELCOME")
        self.textarea.insert(END, f"\n Bill Number : {self.bill_no.get()}")
        self.textarea.insert(END, f"\n Customer Name : {self.c_name.get()}")
        self.textarea.insert(END, f"\n Phone Number : {self.c_phon.get()}")
        self.textarea.insert(END, f"\n Customer Email : {self.c_email.get()}")

        self.textarea.insert(END, f"\n =========================================")
        self.textarea.insert(END, f"\n Products\t\t     QTY\t\tPrice")
        self.textarea.insert(END, f"\n =========================================\n")

        

    def cats(self,event=" "):
        if self.Combo_cat.get()=="Mobiles":
            self.Combo_sub.config(value=self.Subcatmobile)
            self.Combo_sub.current(0)

    def Product_add(self,event=" "):
        if self.Combo_sub.get()=="Oppo":
            self.Combo_pn.config(value=self.oppo)
            self.Combo_pn.current(0)

        if self.Combo_sub.get()=="Vivo":
            self.Combo_pn.config(value=self.Vivo)
            self.Combo_pn.current(0)

        if self.Combo_sub.get()=="Samsung":
            self.Combo_pn.config(value=self.Samsung)
            self.Combo_pn.current(0)

        if self.Combo_sub.get()=="Redmi":
            self.Combo_pn.config(value=self.Redmi)
            self.Combo_pn.current(0)

        if self.Combo_sub.get()=="Iphone":
            self.Combo_pn.config(value=self.Iphone)
            self.Combo_pn.current(0)

    def price(self,event=""):
        # Oppo
        if self.Combo_pn.get()=="Reno7 Pro":
            self.Combo_price.config(value=self.price_reno7_pro)
            self.Combo_price.current(0)
            self.qty.set(1)
            self.disc.set(0)
            self.tax.set(0)

        if self.Combo_pn.get()=="F21 Pro":
            self.Combo_price.config(value=self.price_F21_Pro)
            self.Combo_price.current(0)
            self.qty.set(1)
            self.disc.set(0)
            self.tax.set(0)



        if self.Combo_pn.get()=="A74 5G":
            self.Combo_price.config(value=self.price_A74_5G)
            self.Combo_price.current(0)
            self.qty.set(1)
            self.disc.set(0)
            self.tax.set(0)



        if self.Combo_pn.get()=="A31":
            self.Combo_price.config(value=self.price_A31)
            self.Combo_price.current(0)
            self.qty.set(1)
            self.disc.set(0)
            self.tax.set(0)



        if self.Combo_pn.get()=="Find X3 Pro":
            self.Combo_price.config(value=self.price_X3_Pro)
            self.Combo_price.current(0)
            self.qty.set(1)
            self.disc.set(0)
            self.tax.set(0)



        # Vivo
        if self.Combo_pn.get()=="V20":
            self.Combo_price.config(value=self.price_V20)
            self.Combo_price.current(0)
            self.qty.set(1)
            self.disc.set(0)
            self.tax.set(0)



        if self.Combo_pn.get()=="Y31":
            self.Combo_price.config(value=self.price_Y31)
            self.Combo_price.current(0)
            self.qty.set(1)
            self.disc.set(0)
            self.tax.set(0)

            

        if self.Combo_pn.get()=="X60 Pro":
            self.Combo_price.config(value=self.price_X60_pro)
            self.Combo_price.current(0)
            self.qty.set(1)
            self.disc.set(0)
            self.tax.set(0)



        if self.Combo_pn.get()=="Y20I":
            self.Combo_price.config(value=self.price_Y20I)
            self.Combo_price.current(0)
            self.qty.set(1)
            self.disc.set(0)
            self.tax.set(0)

            

        if self.Combo_pn.get()=="V17 PRO":
            self.Combo_price.config(value=self.price_V17_pro)
            self.Combo_price.current(0)
            self.qty.set(1)
            self.disc.set(0)
            self.tax.set(0)



        # Samsung
        if self.Combo_pn.get()=="Galaxy S20":
            self.Combo_price.config(value=self.price_S20)
            self.Combo_price.current(0)
            self.qty.set(1)
            self.disc.set(0)
            self.tax.set(0)



        if self.Combo_pn.get()=="Galaxy M33":
            self.Combo_price.config(value=self.price_M33)
            self.Combo_price.current(0)
            self.qty.set(1)
            self.disc.set(0)
            self.tax.set(0)



        if self.Combo_pn.get()=="Galaxy F23":
            self.Combo_price.config(value=self.price_F23)
            self.Combo_price.current(0)
            self.qty.set(1)
            self.tax.set(0)
            self.disc.set(0)


        if self.Combo_pn.get()=="Galaxy M53":
            self.Combo_price.config(value=self.price_M53)
            self.Combo_price.current(0)
            self.qty.set(1)
            self.tax.set(0)
            self.disc.set(0)


        if self.Combo_pn.get()=="Galaxy S22 Ultra":
            self.Combo_price.config(value=self.price_S22)
            self.Combo_price.current(0)
            self.qty.set(1)
            self.tax.set(0)
            self.disc.set(0)


        # Redmi
        if self.Combo_pn.get()=="Note 11 Pro":
            self.Combo_price.config(value=self.price_11_pro)
            self.Combo_price.current(0)
            self.qty.set(1)
            self.tax.set(0)
            self.disc.set(0)
            

        if self.Combo_pn.get()=="Note 11S":
            self.Combo_price.config(value=self.price_11S)
            self.Combo_price.current(0)
            self.qty.set(1)
            self.tax.set(0)
            self.disc.set(0)


        if self.Combo_pn.get()=="Note 11T":
            self.Combo_price.config(value=self.price_11T)
            self.Combo_price.current(0)
            self.tax.set(0)
            self.qty.set(1)
            self.disc.set(0)


        if self.Combo_pn.get()=="Note 9i Sport":
            self.Combo_price.config(value=self.price_9i)
            self.Combo_price.current(0)
            self.qty.set(1)
            self.tax.set(0)
            self.disc.set(0)
            

        if self.Combo_pn.get()=="Note 10 Pro Max":
            self.Combo_price.config(value=self.price_10_pro)
            self.Combo_price.current(0)
            self.qty.set(1)
            self.tax.set(0)
            self.disc.set(0)


        # Iphone
        if self.Combo_pn.get()=="iphone 11":
            self.Combo_price.config(value=self.price_11)
            self.Combo_price.current(0)
            self.qty.set(1)
            self.tax.set(0)
            self.disc.set(0)


        if self.Combo_pn.get()=="iphone 12":
            self.Combo_price.config(value=self.price_12)
            self.Combo_price.current(0)
            self.qty.set(1)
            self.tax.set(0)
            self.disc.set(0)
            

        if self.Combo_pn.get()=="iphone 13":
            self.Combo_price.config(value=self.price_13)
            self.Combo_price.current(0)
            self.qty.set(1)
            self.tax.set(0)
            self.disc.set(0)


        if self.Combo_pn.get()=="iphone 13 Pro M":
            self.Combo_price.config(value=self.price_13_pro)
            self.Combo_price.current(0)
            self.qty.set(1)
            self.tax.set(0)
            self.disc.set(0)


        if self.Combo_pn.get()=="iphone 10":
            self.Combo_price.config(value=self.price_10)
            self.Combo_price.current(0)
            self.qty.set(1)
            self.tax.set(0)
            self.disc.set(0)

if __name__=='__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()