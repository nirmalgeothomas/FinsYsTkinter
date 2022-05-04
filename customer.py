
from tkinter import *
import tkinter.font as font
from  tkinter import ttk
import tkinter as tk

import mysql.connector
from tkinter import messagebox



def fun():#db connection
    global mydb,mycursor
    mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='finsys_tkinter'
        )
    mycursor = mydb.cursor()

def add_customer():
    from addcustomer_form import CheckVar2,CheckVar1
    import addcustomer_form
    


#edir customer 
def edit_customer():
    #update data
    def change_data():
        fun()
        global etitle,efirst_name,elast_name,ecompany,elocation,egst,egstin,epan_no,eemail,ewebsite,emobile,estreet,ecity,estate,epin,ecountry,eshipstreet,eshipcity,eshipstate,eshippin,eshipcountry
        
        etitle=e_title.get()
        efirst_name=e_first_name.get()
        elast_name=e_last_name.get()
        ecompany=e_company.get()
        elocation=e_location.get()
        egst=e_gst.get()
        egstin=e_gstin.get()
        epan_no=e_pan_no.get()
        eemail=e_email.get()
        ewebsite=e_website.get()
        emobile=e_mobile.get()
        estreet=e_street.get()
        ecity=e_city.get()
        estate=e_state.get()
        epin=e_pin.get()
        ecountry=e_country.get()
        eshipstreet=e_shipstreet.get()
        eshipcity=e_shipcity.get()
        eshipstate=e_shipstate.get()
        eshippin=e_shippin.get()
    
        eshipcountry=e_shipcountry.get()
        mycursor.execute("UPDATE customer SET title =%s, firstname =%s, lastname =%s, company =%s, location =%s, gsttype =%s, gstin =%s, panno =%s, email =%s, website =%s,mobile =%s, street =%s,city =%s, state =%s, pincode =%s, country=%s, shipstreet =%s, shipcity =%s, shipstate =%s, shippincode =%s, shipcountry =%s where customerid=%s"
            ,(etitle, efirst_name, elast_name, ecompany,elocation, egst, egstin, epan_no, eemail, ewebsite, emobile, estreet, ecity, estate, epin, ecountry, eshipstreet,eshipcity, eshipstate, eshippin, eshipcountry,s[0]))
        mydb.commit()
        messagebox.showinfo('successfully Updated')
        mydb.close()


    # selected_item = custom_data.selection()[0]
    global fname
    focus_data = custom_data.focus()
    values=custom_data.item(focus_data,'values')
    fname=[values[0]]
    mycursor.execute("SELECT * FROM customer WHERE firstname=%s",(fname))
    s=mycursor.fetchone()
    editcustomer_form = tk.Tk()
    editcustomer_form.title("finsYs")
    editcustomer_form.geometry("2000x2000")
    editcustomer_form['bg']='#2f516a'
    wrappen=ttk.LabelFrame(editcustomer_form)
    mycanvas=Canvas(wrappen)
    mycanvas.pack(side=LEFT,fill="both",expand="yes")
    yscrollbar=ttk.Scrollbar(wrappen,orient='vertical',command=mycanvas.yview)
    yscrollbar.pack(side=RIGHT,fill='y')

    mycanvas.configure(yscrollcommand=yscrollbar.set)
    mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))

    full_frame=Frame(mycanvas,width=2000,height=2000,bg='#2f516a')
    mycanvas.create_window((0,0),window=full_frame,anchor="nw")


    heading_frame=Frame(mycanvas)
    mycanvas.create_window((150,40),window=heading_frame,anchor="nw")
    addcustomer_heading= tk.Label(heading_frame, text="EDIT CUSTOMER",fg='#fff',bg='#243e55',height=2,bd=5,relief="groove",font=('Times', 25),width=93)
    addcustomer_heading.pack()


    form_frame=Frame(mycanvas,width=1600,height=1000,bg='#243e55')
    mycanvas.create_window((150,150),window=form_frame,anchor="nw")
    form_lable=tk.Label(form_frame,bg='#243e55',width=100)
    form_lable.place(x=0,y=0)
    form_heading=tk.Label(form_lable, text="Customer Information",fg='#fff',bg='#243e55',height=2,bd=1,relief="groove",font=('Times', 20),width=125)
    form_heading.pack(fill=X)


    global e_title,e_first_name,e_last_name,e_company,e_location,e_gst,e_gstin,e_pan_no,e_email,e_website,e_mobile,e_street,e_city,e_state,e_pin,e_country,e_shipstreet,e_shipcity,e_shipstate,e_shippin,e_shipcountry
    e_title=StringVar(form_frame)
    e_first_name=StringVar(form_frame)
    e_last_name=StringVar(form_frame)
    e_company=StringVar(form_frame)
    e_location=StringVar(form_frame)
    e_gst=StringVar(form_frame)
    e_gstin=StringVar(form_frame)
    e_pan_no=StringVar(form_frame)
    e_email=StringVar(form_frame)
    e_website=StringVar(form_frame)
    e_mobile=StringVar(form_frame)
    e_street=StringVar(form_frame)
    e_city=StringVar(form_frame)
    e_state=StringVar(form_frame)
    e_pin=StringVar(form_frame)
    e_country=StringVar(form_frame)
    e_shipstreet=StringVar(form_frame)
    e_shipcity=StringVar(form_frame)
    e_shipstate=StringVar(form_frame)
    e_shippin=StringVar(form_frame)
    e_shipcountry=StringVar(form_frame)






    title_lab=tk.Label(form_frame,text="Title",bg='#243e55',fg='#fff')
    drop2=ttk.Combobox(form_frame,textvariable = e_title)

    drop2['values']=("Mr","Mrs","Miss","Ms")

    title_lab.place(x=10,y=100,height=15,width=100)
    drop2.place(x=30,y=130,height=40,width=450)
    wrappen.pack(fill='both',expand='yes',)


    fname=Label(form_frame,text="First Name",bg='#243e55',fg='#fff')
    fname.place(x=530,y=100,)
    fname_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff',textvariable = e_first_name)
    fname_input.place(x=530,y=130,height=40)


    lname=Label(form_frame,text="Last Name",bg='#243e55',fg='#fff')
    lname.place(x=1060,y=100,)
    lname_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff',textvariable = e_last_name)
    lname_input.place(x=1060,y=130,height=40)

    company_lab=Label(form_frame,text="Company",bg='#243e55',fg='#fff')
    company_lab.place(x=30,y=200,)
    company_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff',textvariable = e_company)
    company_input.place(x=30,y=230,height=40)

    location_lab=Label(form_frame,text="Location",bg='#243e55',fg='#fff')
    location_lab.place(x=530,y=200,)
    location_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff',textvariable = e_location)
    location_input.place(x=530,y=230,height=40)

    GST_lab=tk.Label(form_frame,text="GST Type",bg='#243e55',fg='#fff')
    GST_drop=ttk.Combobox(form_frame,textvariable = e_gst)
    GST_drop['values']=("Consumer","GST Registered-Regular","GST unregistered","GST Registered-Composition","Overseas", "Deemed exports - EOU's STP's EHTP's")
    GST_lab.place(x=20,y=300,height=15,width=100)
    GST_drop.place(x=30,y=330,height=40,width=450)

    gstin_lab=Label(form_frame,text="GSTIN",bg='#243e55',fg='#fff')
    gstin_lab.place(x=530,y=300,)
    gstin_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff',textvariable = e_gstin)
    gstin_input.place(x=530,y=330,height=40)

    pan_no_lab=Label(form_frame,text="PAN NO",bg='#243e55',fg='#fff')
    pan_no_lab.place(x=1060,y=300,)
    pan_no_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff',textvariable = e_pan_no)
    pan_no_input.place(x=1060,y=330,height=40)

    email_lab=Label(form_frame,text="Email",bg='#243e55',fg='#fff')
    email_lab.place(x=30,y=400,)
    email_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff',textvariable = e_email)
    email_input.place(x=30,y=430,height=40)

    web_lab=Label(form_frame,text="Website",bg='#243e55',fg='#fff')
    web_lab.place(x=530,y=400,)
    web_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff',textvariable = e_website)
    web_input.place(x=530,y=430,height=40)


    mobile_lab=Label(form_frame,text="Mobile",bg='#243e55',fg='#fff')
    mobile_lab.place(x=1060,y=400,)
    mobile_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff',textvariable = e_mobile)
    mobile_input.place(x=1060,y=430,height=40)

    #Billing session
    sub_headingfont=font.Font(family='Times New Roman', size=18,)
    form2_frame=Frame(mycanvas,width=1600,height=650,bg='#243e55',bd=1,relief="groove")
    mycanvas.create_window((150,650),window=form2_frame,anchor="nw")

    bill_heading=tk.Label(form2_frame, text="Billing Address",fg='#fff',bg='#243e55',height=2,font=sub_headingfont,width=15)
    bill_heading.place(x=30,y=10,)

    street_lab=Label(form2_frame,text="Street",bg='#243e55',fg='#fff')
    street_lab.place(x=30,y=100,)
    street_input=Entry(form2_frame,width=85,bg='#2f516a',fg='#fff',textvariable = e_street)
    street_input.place(x=30,y=130,height=80)


    city_lab=Label(form2_frame,text="City",bg='#243e55',fg='#fff')
    city_lab.place(x=30,y=250,)
    city_input=Entry(form2_frame,width=40,bg='#2f516a',fg='#fff',textvariable = e_city)
    city_input.place(x=30,y=280,height=40)


    state_lab=tk.Label(form2_frame,text="State",bg='#243e55',fg='#fff')
    state_lab.place(x=370,y=250,)
    state_drop=ttk.Combobox(form2_frame,textvariable = e_state)
    state_drop['values']=("" ,"Andaman and Nicobar Islads","Andhra Predhesh","Arunachal Predesh","Assam","Bihar","Chandigarh","Chhattisgarh","Dadra and Nagar Haveli","Damn anad Diu","Delhi","Goa","Gujarat","Haryana","Himachal Predesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Ladakh","Lakshadweep","Madhya Predesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Predesh","Uttarakhand","West Bengal","Other Territory")
    state_drop.place(x=370,y=280,height=40,width=330)

    pin_lab=Label(form2_frame,text="Pin code",bg='#243e55',fg='#fff')
    pin_lab.place(x=30,y=350,)
    pin_input=Entry(form2_frame,width=40,bg='#2f516a',fg='#fff',textvariable = e_pin)
    pin_input.place(x=30,y=380,height=40)

    country_lab=Label(form2_frame,text="Country",bg='#243e55',fg='#fff')
    country_lab.place(x=370,y=350,)
    country_input=Entry(form2_frame,width=40,bg='#2f516a',fg='#fff',textvariable = e_country)
    country_input.place(x=370,y=380,height=40)



    #Shipping Address 

    shipping_heading=tk.Label(form2_frame, text="Shipping Address",fg='#fff',bg='#243e55',height=2,font=sub_headingfont,width=15)
    shipping_heading.place(x=850,y=10,)



    street_lab=Label(form2_frame,text="Street",bg='#243e55',fg='#fff')
    street_lab.place(x=850,y=100,)
    street_input=Entry(form2_frame,width=85,bg='#2f516a',fg='#fff',textvariable = e_shipstreet)
    street_input.place(x=850,y=130,height=80)


    city_lab=Label(form2_frame,text="City",bg='#243e55',fg='#fff')
    city_lab.place(x=850,y=250,)
    city_input=Entry(form2_frame,width=40,bg='#2f516a',fg='#fff',textvariable = e_shipcity)
    city_input.place(x=850,y=280,height=40)


    state_lab=tk.Label(form2_frame,text="State",bg='#243e55',fg='#fff')
    state_lab.place(x=1200,y=250,)
    state_drop=ttk.Combobox(form2_frame,textvariable = e_shipstate)
    state_drop['values']=("" ,"Andaman and Nicobar Islads","Andhra Predhesh","Arunachal Predesh","Assam","Bihar","Chandigarh","Chhattisgarh","Dadra and Nagar Haveli","Damn anad Diu","Delhi","Goa","Gujarat","Haryana","Himachal Predesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Ladakh","Lakshadweep","Madhya Predesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Predesh","Uttarakhand","West Bengal","Other Territory")
    state_drop.place(x=1200,y=280,height=40,width=330)

    pin_lab=Label(form2_frame,text="Pin code",bg='#243e55',fg='#fff')
    pin_lab.place(x=850,y=350,)
    pin_input=Entry(form2_frame,width=40,bg='#2f516a',fg='#fff',textvariable = e_shippin)
    pin_input.place(x=850,y=380,height=40)

    country_lab=Label(form2_frame,text="Country",bg='#243e55',fg='#fff')
    country_lab.place(x=1200,y=350,)
    country_input=Entry(form2_frame,width=40,bg='#2f516a',fg='#fff',textvariable = e_country)
    country_input.place(x=1200,y=380,height=40)

    submit_button=Button(form2_frame,text="Submit Form",background="#2f516a", foreground="white",width=40,height=2,command=change_data)

    submit_button.place(x=600,y=500)


#Delete constomer
def delete_customer():
    focus_data = custom_data.focus()
    values=custom_data.item(focus_data,'values')
    fname=[values[0]]
    mycursor.execute("DELETE FROM customer WHERE firstname=%s",(fname))
    mydb.commit()
    messagebox.showinfo('successfully Delated')
    print('sucessfully deleted')
    custom_data.delete(focus_data)


#customer home

customer =tk.Tk()
fun()
customer.title('fynsYs')
customer.geometry("2000x2000")
customer['bg']='#2f516a'
headingfont=font.Font(family='Helvitica', size=25,)
inv_heading= Label(customer, text="CUSTOMERS",bd=10,relief="groove",font=headingfont,bg='#243e55', fg='#fff',height=2,pady=2)
inv_heading.pack(fill=X)

content_label=Label(customer,relief="groove",bg='#243e55', fg='#fff',width=500,height=30)

add_customer=Button(content_label,text="Add Customer",background='#243e55', foreground="white",command=add_customer)
add_customer.place(x=1450,y=100)

style = ttk.Style()
style.theme_use('classic')

global custom_data
custom_data = ttk.Treeview(content_label)


custom_data['columns']= ('customer', 'gst_type','gstin','panno','email','mobile')
custom_data.column("#0", width=0,  stretch=NO)
custom_data.column("customer",anchor=CENTER )
custom_data.column("gst_type",anchor=CENTER, )
custom_data.column("gstin",anchor=CENTER,)
custom_data.column("panno",anchor=CENTER,)
custom_data.column("email",anchor=CENTER,)
custom_data.column("mobile",anchor=CENTER)

custom_data.heading("#0",text="",anchor=CENTER)
custom_data.heading("customer",text="CUSTOME",anchor=CENTER)
custom_data.heading("gst_type",text="GST TYPE",anchor=CENTER)
custom_data.heading("gstin",text="GSTIN",anchor=CENTER)
custom_data.heading("panno",text="PAN NO",anchor=CENTER)
custom_data.heading("email",text="EMAIL ID",anchor=CENTER)
custom_data.heading("mobile",text="MOBILE NO",anchor=CENTER)

custom_data.place(x=280,y=200)

sql='SELECT firstname,gsttype,gstin,panno,email,mobile from customer'
mycursor.execute(sql)
customer_data=mycursor.fetchall()
total=mycursor.rowcount


for data in customer_data: 
    custom_data.insert("", 'end',values=data)


content_label.place(x=0,y=150)

edit=Button(content_label,text="Edit",background='#243e55', foreground="white",command=edit_customer)
edit.place(x=850,y=450)

delete=Button(content_label,text="Delete",background='#243e55', foreground="white",command=delete_customer)

delete.place(x=950,y=450)

customer.mainloop()
