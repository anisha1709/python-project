from idlelib.searchengine import get_line_col
from tkinter import *
from tkinter import messagebox
import random, os,tempfile

"""name=StringVar()
Phone_no=IntVar()
Bill_no=IntVar()
Cosmetic_price=IntVar()
Grocery_price=IntVar
Cold_drinks_price=IntVar()
Total=IntVar()
Bath_Soap=IntVar()
Face_Cream=IntVar()
Face_Wash=IntVar()
Hair_Spray=IntVar()
Hair_Gel=IntVar()
Body_Lotion=IntVar()
Rice=IntVar()
Oil=IntVar()
Daal=IntVar()
Wheat=IntVar()
Sugar=IntVar()
Tea=IntVar()
Maaza=IntVar()
Pepsi=IntVar()
Sprite=IntVar()
Dew=IntVar()
Frooti=IntVar()
Coco_Cola=IntVar()"""



def print_buttun():
    if textaria.get(1.0,END)=="\n":
        messagebox.showerror("Error","Bill iis empty")
    else:
        file=tempfile.mktemp(".txt")
        open(file,"w").write(textaria.get(1.0,END))
        os.startfile(file,"print")


def search_bill():
    for i in os.listdir("bills/"):
        if i.split(".")[0]==billEntry.get():
            f=open(f"bills/{i}","r")
            textaria.delete(1.0,END)
            for data in f:
                textaria.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror("Error","Invalid Bill Number")


if not os.path.exists("bills"):
    os.mkdir("bills")

def save_bill():
    global billnumber
    result=messagebox.askyesno("Confirm","Do you want to save the bill?")
    if result:
        bill_content=textaria.get(1.0,END)
        file= open(f"bills/{billnumber}.txt","w")
        file.write(bill_content)
        file.close()
        messagebox.showinfo("Success",f"{billnumber} is saved successfully")
        billnumber = random.randint(500, 1000)

billnumber=random.randint(500,1000)

def bill_aria():
    if nameEntry.get()=="" or phoneEntry.get()=="":
        messagebox.showerror("Error","Customer details are Required")
    elif cosmeticpriceEntry.get()=="" and grocerypriceEntry.get()=="" and colddrinkpriceEntry.get()=="":
        messagebox.showerror("Error","No Products are selected ")
    else:
        textaria.delete(1.0,END) #repet repet genreted bill is deleted

        textaria.insert(END,"\t\t*** Welcome Customer***\n")
        textaria.insert(END,f"\n Bill Number      : {billnumber}")# randam vallu formet
        textaria.insert(END, f"\n Customer Name    : {nameEntry.get()}")
        textaria.insert(END, f"\n Customer Phon No : {phoneEntry.get()}")
        textaria.insert(END,"\n===========================================================")
        textaria.insert(END, f"\n Product\t\t\tQuantity\t\t\tPrice")
        textaria.insert(END, "\n===========================================================")


def open_tree1():
    win = Toplevel(root)
    win.title("🧾 Main Billing Report")
    win.geometry("800x400")

    frame = Frame(win)
    frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

    scroll_y = Scrollbar(frame, orient=VERTICAL)
    scroll_x = Scrollbar(frame, orient=HORIZONTAL)

    tree = Tk.Treeview(frame,
        columns=("NAME", "PHONE NO.", "BILL NO", "COSMETIC PRICE", "GROCERY PRICE", "COLD DRINK PRICE", "TOTAL"),
        show="headings",
        yscrollcommand=scroll_y.set,
        xscrollcommand=scroll_x.set
    )

    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.config(command=tree.yview)
    scroll_x.config(command=tree.xview)

    for col in ("NAME", "PHONE NO.", "BILL NO", "COSMETIC PRICE", "GROCERY PRICE", "COLD DRINK PRICE", "TOTAL"):
        tree.heading(col, text=col)
        tree.column(col, width=120)
    tree.pack(fill=BOTH, expand=True)

    # Fetch data
    conn = get_line_col()
    cur = conn.cursor()
    cur.execute("SELECT * FROM billing system 1")
    rows = cur.fetchall()
    for r in rows:
        tree.insert("", END, values=r)
    conn.close()

def cosmetic_price():
    new=Tk()
    new.title("Cosmetic price total")
    new.geometry("500x500")
    new['bg']="white"
    Tk.resizable(False,False)



def grocery_price():
    new1=Tk()
    new1.title("Grocery price total")
    new1.geometry("500x500")
    new1['bg']="white"
    Tk.resizable(False,False)

def cold_drinks_price():
    new2=Tk()
    new2.title("Cold drinks total")
    new2.geometry("500x500")
    new2['bg']="white"
    Tk.resizable(False,False)

    #cosmatic show bill entry exp = name,qnt, rate

    if bathshopEntry.get()!="0": #repit not printing method
        textaria.insert(END,f"\t\nBath Soap\t\t\t{bathshopEntry.get()}\t\t\t{sopvalue} Rs")
    if facecreamEntry.get() != "0":  # repit not printing method
        textaria.insert(END, f"\t\nFace Cream\t\t\t{facecreamEntry.get()}\t\t\t{facecreamvalu} Rs")
    if facewashEntry.get() != "0":  # repit not printing method
        textaria.insert(END, f"\t\nFace Wash\t\t\t{facewashEntry.get()}\t\t\t{facewashvalu} Rs")
    if hairspryEntry.get() != "0":  # repit not printing method
        textaria.insert(END, f"\t\nHairsprye\t\t\t{hairspryEntry.get()}\t\t\t{hairspryvalu} Rs")
    if hairgelEntry.get() != "0":  # repit not printing method 0 valu in all columns
        textaria.insert(END, f"\t\nHairgel\t\t\t{hairgelEntry.get()}\t\t\t{hairgelvalu} Rs")
    if bodylotionEntry.get() != "0":  # repit not printing method
        textaria.insert(END, f"\t\nBody Lotion\t\t\t{bodylotionEntry.get()}\t\t\t{bodylotionvalu} Rs")

    #grocery price

        if riceEntry.get()!="0": #repit not printing method
            textaria.insert(END,f"\t\nRice\t\t\t{riceEntry.get()}\t\t\t{ricvalu} Rs")
        if oilEntry.get() != "0":  # repit not printing method
            textaria.insert(END, f"\t\nOile\t\t\t{oilEntry.get()}\t\t\t{oilvalu} Rs")
        if daalEntry.get() != "0":  # repit not printing method
            textaria.insert(END, f"\t\nDaal\t\t\t{daalEntry.get()}\t\t\t{daalvalu} Rs")
        if wheatEntry.get() != "0":  # repit not printing method
            textaria.insert(END, f"\t\nWhetvalu\t\t\t{wheatEntry.get()}\t\t\t{whetvalu} Rs")
        if sugarEntry.get() != "0":  # repit not printing method 0 valu in all columns
            textaria.insert(END, f"\t\nSugar\t\t\t{sugarEntry.get()}\t\t\t{sugarvalu} Rs")
        if teaEntry.get() != "0":  # repit not printing method
            textaria.insert(END, f"\t\n Teat\t\t{teaEntry.get()}\t\t\t{teavalu} Rs")

            #drink
        if maazaEntry.get() != "0":  # repit not printing method
            textaria.insert(END, f"\t\nMaaza\t\t\t{maazaEntry.get()}\t\t\t{maazavallu} Rs")
        if pepsiEntry.get() != "0":  # repit not printing method
            textaria.insert(END, f"\t\nPepsi\t\t\t{pepsiEntry.get()}\t\t\t{pepsivallu} Rs")
        if spriteEntry.get() != "0":  # repit not printing method
            textaria.insert(END, f"\t\nSprite\t\t\t{spriteEntry.get()}\t\t\t{spritelvallu} Rs")
        if dewEntry.get() != "0":  # repit not printing method
            textaria.insert(END, f"\t\nDew\t\t\t{dewEntry.get()}\t\t\t{dewvallu} Rs")
        if frootiEntry.get() != "0":  # repit not printing method 0 valu in all columns
            textaria.insert(END, f"\t\nFrooti\t\t\t{frootiEntry.get()}\t\t\t{frootivallu} Rs")
        if cocacolaEntry.get() != "0":  # repit not printing method
            textaria.insert(END, f"\t\n Cocacola\t\t\t{teaEntry.get()}\t\t\t{cocacolavalu}Rs")
        textaria.insert(END, "\n===========================================================")

        if cosmetictaxEntry.get()!="0.0":
            textaria.insert(END,f"\n Cosmetic Tax\t\t\t\t\t\t{cosmetictaxEntry.get()}")

        if grocerytaxEntry.get()!="0.0":
            textaria.insert(END,f"\n Grocery Tax\t\t\t\t\t\t{grocerytaxEntry.get()}")

        if colddrinktaxEntry.get()!="0.0":
            textaria.insert(END,f"\n Cold drink Tax\t\t\t\t\t\t{colddrinktaxEntry.get()}")

        if totalbillEntry.get()!="0.0":
            textaria.insert(END,f"\n \n Total Bill \t\t\t\t\t\t{totalbillEntry.get()}")
        textaria.insert(END, "\n\n\t\t******  Thank You For Visit  ******")

        save_bill()


def total():#total button funtion
    global sopvalue #printng rate in sopvalu nad creat a global valu
    global facecreamvalu
    global hairspryvalu
    global facewashvalu
    global hairgelvalu
    global bodylotionvalu
#grocery riport
    global ricvalu
    global oilvalu
    global daalvalu
    global whetvalu
    global sugarvalu
    global teavalu

    global maazavallu
    global pepsivallu

    global spritelvallu
    global dewvallu
    global frootivallu
    global cocacolavalu









    sopvalue=int(bathshopEntry.get())*20  #creating veriable and set multification vallu and set rate
    facecreamvalu=int(facecreamEntry.get())*100
    hairspryvalu = int(hairspryEntry.get()) *120
    facewashvalu = int(facewashEntry.get()) * 80
    hairgelvalu = int(hairgelEntry.get()) * 50
    bodylotionvalu = int(bodylotionEntry.get()) * 50

    totalcosmeticprice=sopvalue+facecreamvalu+hairspryvalu+facewashvalu+hairgelvalu+bodylotionvalu
    cosmeticpriceEntry.delete(0, END)
    cosmeticpriceEntry.insert(0,str(totalcosmeticprice)+"  Rs") # Rs comment is string and totalcosmetics price is inte


    cosmetictax=totalcosmeticprice * 0.12
    cosmetictaxEntry.delete(0,END)
    cosmetictaxEntry.insert(0,str(cosmetictax)+" Rs")


    #grocery product
    ricvalu = int(riceEntry.get()) * 20  # creating veriable and set multification vallu and set rate
    oilvalu = int(oilEntry.get()) * 100
    daalvalu = int(daalEntry.get()) * 120
    whetvalu = int(wheatEntry.get()) * 80
    sugarvalu = int(sugarEntry.get()) * 50
    teavalu = int(teaEntry.get()) * 50

    totalgroceryprice=ricvalu+oilvalu+daalvalu+whetvalu+sugarvalu+teavalu
    grocerypriceEntry.delete(0,END)
    grocerypriceEntry.insert(0,str(totalgroceryprice)+"  Rs")
    grocerytax=totalgroceryprice * 0.10
    grocerytaxEntry.delete(0, END)
    grocerytaxEntry.insert(0, str(grocerytax) + " Rs")

    #cold drinks
    maazavallu = int(maazaEntry.get()) * 20  # creating veriable and set multification vallu and set rate
    pepsivallu = int(pepsiEntry.get()) * 100
    spritelvallu = int(spriteEntry.get()) * 120
    dewvallu = int(dewEntry.get()) * 80
    frootivallu= int(frootiEntry.get()) * 50
    cocacolavalu = int(cocacolaEntry.get()) * 50

    totalcolddrinkprice=maazavallu+pepsivallu+spritelvallu+dewvallu+frootivallu+cocacolavalu
    colddrinkpriceEntry.delete(0,END)
    colddrinkpriceEntry.insert(0,str(totalcolddrinkprice)+" Rs")
    colddrinktax = totalcolddrinkprice * 0.15
    colddrinktaxEntry.delete(0, END)
    colddrinktaxEntry.insert(0, str(colddrinktax) + " Rs")

    total_bill=totalcosmeticprice+cosmetictax+totalgroceryprice+grocerytax+totalcolddrinkprice+colddrinktax
    totalbillEntry.insert(0,total_bill)



root=Tk()

root.title("Hotel Manegemant System")
root.geometry("1366x768")
headingLabel=(Label(root,text="Retail Billing System",font="arial 15 bold",bg="black",fg="yellow",relief=GROOVE))
headingLabel.pack(fill=X,pady=10,padx=10)

customer_details_frame=(LabelFrame(root,text="Customer Details",font="arial 13 bold"))
customer_details_frame.pack(fill=X)

nameLabel=Label(customer_details_frame,text="Name",font="arial 10 bold")
nameLabel.grid(row=0,column=0 ,padx=30)

nameEntry=Entry(customer_details_frame,font="arial 10 bold",bd=5,width=27)
nameEntry.grid(row=0,column=1,padx=30)

phoneLabel=Label(customer_details_frame,text="Phone Number",font="arial 10 bold")
phoneLabel.grid(row=0,column=2,pady=10)
phoneEntry=Entry(customer_details_frame,font="arial 10 bold",bd=5,width=27)
phoneEntry.grid(row=0,column=3,padx=30)

billLabel=Label(customer_details_frame,text="Billl Number",font="arial 10 bold")
billLabel.grid(row=0,column=4,pady=10)
billEntry=Entry(customer_details_frame,font="arial 10 bold",bd=5,width=27)
billEntry.grid(row=0,column=5,padx=30)



searchButton=Button(customer_details_frame,text="SEARCH",font="arial 10 bold",bd=4,width="10",command=search_bill)
searchButton.grid(row=0,column=6,padx=30,pady=10)

productFrame=Frame(root)
productFrame.pack()

cosmetic_details_frame=LabelFrame(productFrame,text="Cosmetics",font="arial 13 bold")
cosmetic_details_frame.grid(row=0,column=0)

bathshopLabel=Label(cosmetic_details_frame,text="Bath Soap",font="arial 10 bold")
bathshopLabel.grid(row=0,column=0 ,padx=20)
bathshopEntry=Entry(cosmetic_details_frame,font="arial 10 bold",bd=5,width=10,)
bathshopEntry.grid(row=0,column=1,padx=10,pady=10)
bathshopEntry.insert(0,0) #multifacation  vallu is start to 0

facecreamLabel=Label(cosmetic_details_frame,text="Face Cream",font="arial 10 bold")
facecreamLabel.grid(row=1,column=0 ,padx=20)
facecreamEntry=Entry(cosmetic_details_frame,font="arial 10 bold",bd=5,width=10)
facecreamEntry.grid(row=1,column=1,padx=10,pady=10)
facecreamEntry.insert(0,0)

facewashLabel=Label(cosmetic_details_frame,text="Face Wash",font="arial 10 bold")
facewashLabel.grid(row=2,column=0 ,padx=20)
facewashEntry=Entry(cosmetic_details_frame,font="arial 10 bold",bd=5,width=10)
facewashEntry.grid(row=2,column=1,padx=10,pady=10)
facewashEntry.insert(0,0)

hairspryLabel=Label(cosmetic_details_frame,text="Hair Spray",font="arial 10 bold")
hairspryLabel.grid(row=3,column=0 ,padx=20)
hairspryEntry=Entry(cosmetic_details_frame,font="arial 10 bold",bd=5,width=10)
hairspryEntry.grid(row=3,column=1,padx=10,pady=10)
hairspryEntry.insert(0,0)

hairgelLabel=Label(cosmetic_details_frame,text="Hair Gel",font="arial 10 bold")
hairgelLabel.grid(row=4,column=0 ,padx=20)
hairgelEntry=Entry(cosmetic_details_frame,font="arial 10 bold",bd=5,width=10)
hairgelEntry.grid(row=4,column=1,padx=10,pady=10)
hairgelEntry.insert(0,0)

bodylotionLabel=Label(cosmetic_details_frame,text="Body Lotion",font="arial 10 bold")
bodylotionLabel.grid(row=5,column=0 ,padx=20)
bodylotionEntry=Entry(cosmetic_details_frame,font="arial 10 bold",bd=5,width=10)
bodylotionEntry.grid(row=5,column=1,padx=10,pady=10)
bodylotionEntry.insert(0,0)



grocerydetails_frame=LabelFrame(productFrame,text="Grocery",font="arial 13 bold")
grocerydetails_frame.grid(row=0,column=2,padx=10)

riceLabel=Label(grocerydetails_frame,text="Rice",font="arial 10 bold")
riceLabel.grid(row=0,column=0 ,padx=20,pady=10)
riceEntry=Entry(grocerydetails_frame,font="arial 10 bold",bd=5,width=10)
riceEntry.grid(row=0,column=1,padx=10,pady=10)
riceEntry.insert(0,0)

oilLabel=Label(grocerydetails_frame,text="Oil",font="arial 10 bold")
oilLabel.grid(row=1,column=0 ,padx=20,pady=10)
oilEntry=Entry(grocerydetails_frame,font="arial 10 bold",bd=5,width=10)
oilEntry.grid(row=1,column=1,padx=10,pady=10)
oilEntry.insert(0,0)

daalLabel=Label(grocerydetails_frame,text="daal",font="arial 10 bold")
daalLabel.grid(row=2,column=0 ,padx=20,pady=10)
daalEntry=Entry(grocerydetails_frame,font="arial 10 bold",bd=5,width=10)
daalEntry.grid(row=2,column=1,padx=10,pady=10)
daalEntry.insert(0,0)

wheatLabel=Label(grocerydetails_frame,text="Wheat",font="arial 10 bold")
wheatLabel.grid(row=3,column=0 ,padx=20,pady=10)
wheatEntry=Entry(grocerydetails_frame,font="arial 10 bold",bd=5,width=10)
wheatEntry.grid(row=3,column=1,padx=10,pady=10)
wheatEntry.insert(0,0)

sugarLabel=Label(grocerydetails_frame,text="Sugar",font="arial 10 bold")
sugarLabel.grid(row=4,column=0 ,padx=20,pady=10)
sugarEntry=Entry(grocerydetails_frame,font="arial 10 bold",bd=5,width=10)
sugarEntry.grid(row=4,column=1,padx=10,pady=10)
sugarEntry.insert(0,0)

teaLabel=Label(grocerydetails_frame,text="Tea",font="arial 10 bold")
teaLabel.grid(row=5,column=0 ,padx=20,pady=10)
teaEntry=Entry(grocerydetails_frame,font="arial 10 bold",bd=5,width=10)
teaEntry.grid(row=5,column=1,padx=10,pady=10)
teaEntry.insert(0,0)



colddrinkdetails_frame=LabelFrame(productFrame,text="Cold Drinks",font="arial 13 bold")
colddrinkdetails_frame.grid(row=0,column=3,padx=10)

maazaLabel=Label(colddrinkdetails_frame,text="Maaza",font="arial 10 bold")
maazaLabel.grid(row=0,column=0 ,padx=20,pady=10)
maazaEntry=Entry(colddrinkdetails_frame,font="arial 10 bold",bd=5,width=10)
maazaEntry.grid(row=0,column=1,padx=10,pady=10)
maazaEntry.insert(0,0)

pepsiLabel=Label(colddrinkdetails_frame,text="Pepsi",font="arial 10 bold")
pepsiLabel.grid(row=1,column=0 ,padx=20,pady=10)
pepsiEntry=Entry(colddrinkdetails_frame,font="arial 10 bold",bd=5,width=10)
pepsiEntry.grid(row=1,column=1,padx=10,pady=10)
pepsiEntry.insert(0,0)


spriteLabel=Label(colddrinkdetails_frame,text="Sprite",font="arial 10 bold")
spriteLabel.grid(row=2,column=0 ,padx=20,pady=10)
spriteEntry=Entry(colddrinkdetails_frame,font="arial 10 bold",bd=5,width=10)
spriteEntry.grid(row=2,column=1,padx=10,pady=10)
spriteEntry.insert(0,0)


dewLabel=Label(colddrinkdetails_frame,text="Dew",font="arial 10 bold")
dewLabel.grid(row=3,column=0 ,padx=20,pady=10)
dewEntry=Entry(colddrinkdetails_frame,font="arial 10 bold",bd=5,width=10)
dewEntry.grid(row=3,column=1,padx=10,pady=10)
dewEntry.insert(0,0)


frootiLabel=Label(colddrinkdetails_frame,text="Frooti",font="arial 10 bold")
frootiLabel.grid(row=4,column=0 ,padx=20,pady=10)
frootiEntry=Entry(colddrinkdetails_frame,font="arial 10 bold",bd=5,width=10)
frootiEntry.grid(row=4,column=1,padx=10,pady=10)
frootiEntry.insert(0,0)



cocacolaLabel=Label(colddrinkdetails_frame,text="Coca Cola",font="arial 10 bold")
cocacolaLabel.grid(row=5,column=0 ,padx=20,pady=10)
cocacolaEntry=Entry(colddrinkdetails_frame,font="arial 10 bold",bd=5,width=10)
cocacolaEntry.grid(row=5,column=1,padx=10,pady=10)
cocacolaEntry.insert(0,0)

billframe=Frame(productFrame,bd=5,relief=GROOVE)
billframe.grid(row=0,column=4 ,pady=4)

billariaLabel=Label(billframe,text="Bill Aria",font="arial 13 bold",bd="4",relief=GROOVE)
billariaLabel.pack(fill=X)



scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)

textaria=Text(billframe,height=14,width=60,bd=5 ,relief=GROOVE,font="arial 12 bold",yscrollcommand=scrollbar.set)
scrollbar.config(command=textaria.yview)
textaria.pack()



Bill_menu_frame=LabelFrame(root,text="Bill Record",font="arial 13 bold",bd=6)
Bill_menu_frame.pack(pady=10)

cosmeticprice=Label(Bill_menu_frame,text="cosmetic price",font="arial 10 bold")
cosmeticprice.grid(row=0,column=0 ,padx=10,sticky="w")
cosmeticpriceEntry=Entry(Bill_menu_frame,font="arial 10 bold",bd=6,width=17)
cosmeticpriceEntry.grid(row=0,column=1,padx=10,pady=5)

groceryprice=Label(Bill_menu_frame,text="Grocery Price",font="arial 10 bold")
groceryprice.grid(row=1,column=0 ,padx=10,sticky="w")
grocerypriceEntry=Entry(Bill_menu_frame,font="arial 10 bold",bd=6,width=17)
grocerypriceEntry.grid(row=1,column=1,padx=10,pady=5)

colddrinkprice=Label(Bill_menu_frame,text="Cold Drik price",font="arial 10 bold")
colddrinkprice.grid(row=2,column=0 ,padx=10,sticky="w")
colddrinkpriceEntry=Entry(Bill_menu_frame,font="arial 10 bold",bd=6,width=17)
colddrinkpriceEntry.grid(row=2,column=1,padx=10,pady=5)

cosmetictax=Label(Bill_menu_frame,text="cosmetic Tax",font="arial 10 bold")
cosmetictax.grid(row=0,column=2 ,padx=10,sticky="w")
cosmetictaxEntry=Entry(Bill_menu_frame,font="arial 10 bold",bd=6,width=17)
cosmetictaxEntry.grid(row=0,column=3,padx=10,pady=5)

grocerytax=Label(Bill_menu_frame,text="Grocery Tax",font="arial 10 bold")
grocerytax.grid(row=1,column=2 ,padx=10,sticky="w")
grocerytaxEntry=Entry(Bill_menu_frame,font="arial 10 bold",bd=6,width=17)
grocerytaxEntry.grid(row=1,column=3,padx=10,pady=5)

colddrinktax=Label(Bill_menu_frame,text="Cold Drik Tax",font="arial 10 bold")
colddrinktax.grid(row=2,column=2 ,padx=10,sticky="w")
colddrinktaxEntry=Entry(Bill_menu_frame,font="arial 10 bold",bd=6,width=17)
colddrinktaxEntry.grid(row=2,column=3,padx=10,)

totalbill=Label(Bill_menu_frame,text="Total Bill",font="arial 15 bold")
totalbill.grid(row=0,column=4 ,padx=10,sticky="w")
totalbillEntry=Entry(Bill_menu_frame,font="arial 15 bold",bd=6, width=15)
totalbillEntry.grid(row=1,column=4,padx=10,)


buttonFrame=Frame(Bill_menu_frame,bd=5,relief=GROOVE)
buttonFrame.grid(row=0,column=5,rowspan=4,padx=25)

totalButton=Button(buttonFrame,text="Total",font="arial 15 bold",bd=5,width=8,command=total)
totalButton.grid(row=0,column=0,padx=5,pady=30)

bill_Button=Button(buttonFrame,text="Bill",font="arial 15 bold",bd=4,width=8,command=bill_aria)
bill_Button.grid(row=0,column=1,padx=5,pady=4)

emailButton=Button(buttonFrame,text="Email",font="arial 15 bold",bd=4,width=8)
emailButton.grid(row=0,column=2,padx=5,pady=4)

printButton=Button(buttonFrame,text="Print",font="arial 15 bold",bd=4,width=8,command=print_buttun)
printButton.grid(row=0,column=3,padx=5,pady=4)

printButton=Button(root,text="Cosmetic Total",font="arial 12 bold",bg="Orchid",fg="black",bd=4,width=15,command=cosmetic_price)
printButton.place(x=70,y=630)

printButton=Button(root,text="Grocery Total",font="arial 12 bold",bg="PeachPuff",fg="black",bd=4,width=15,command=grocery_price)
printButton.place(x=310,y=630)

printButton=Button(root,text="Cold drinks Total",font="arial 12 bold",bg="sky blue",fg="black",bd=4,width=15,command=cold_drinks_price)
printButton.place(x=540,y=630)

printButton=Button(root,text="All Total",font="arial 12 bold",bg="yellow",fg="black",bd=4,width=15,command=open_tree1)
printButton.place(x=740,y=630)

root.mainloop()