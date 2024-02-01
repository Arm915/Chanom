from tkinter import *
import tkinter as tk
import mysql.connector
import webbrowser

po=Tk()
po.title("ชานมไช่มุก")

#ตัวแปร
c01=StringVar()
cc1=StringVar()
c02=StringVar()
cc2=StringVar()
c03=StringVar()
cc3=StringVar()
c04=StringVar()
cc4=StringVar()
c05=StringVar()
cc5=StringVar()
c06=StringVar()
cc6=StringVar()
c07=StringVar()
cc7=StringVar()
c08=StringVar()
cc8=StringVar()
c09=StringVar()
cc9=StringVar()
top01=StringVar()
top11=StringVar()
top02=StringVar()
top12=StringVar()
top03=StringVar()
top13=StringVar()
Price=StringVar()
Cash=StringVar()
Cange=StringVar()
Cange1=StringVar()
Cange4=StringVar()
Cange5=StringVar()
Total=StringVar()
Total2=StringVar()
Total11=StringVar()
num=StringVar()
Product = []
Number_Product = []
topping= []
arm = []
total1 = []
total2 = []
total3= []
Cash1 = []

#บันทึกข้อมูล
def databest(a,b,c,e):
    con = mysql.connector.connect(user='root', password='', host='127.0.0.1',
                                      database='db_testt')
    cursor = con.cursor()
    sql = """INSERT INTO kaimook(number,produc,number_Product,total,chan)
    VALUE(NULL,%s,%s,%s,%s) """
    cursor.execute(sql,(a,b,c,e))
    con.commit()
    con.close()

#เรียกดูข้อมูล
def datashow():
    con = mysql.connector.connect(user='root', password='', host='127.0.0.1',
                                  database='db_test')
    cursor = con.cursor()
    sql = "SELECT number,produc,number_Product,total,chan FROM kaimook"
    cursor.execute(sql)
    m=int(num.get())
    data=cursor.fetchall()
    r=(data[m-1])
    cursor.close()
    con.close()
    s = "=======================================================\n" \
        "\t\t\tรายการเก่า\n=======================================================\n""" +str(r)+ "\n"
    txtBill1.insert(END, (s))
    num.set(m)

#ใบเสร็จ
def Data():
    slip = "\t\t\tรายการที่สั่ง\n=======================================================\n"
    for i in range(len(Product)):
        slip += "" + str(i+1) + "." + str(Product[i]) + "x" + str(Number_Product[i]) + " ราคา " + str(arm[i]) + " บาท\n"
    slip += "\nสั่งทั้งหมด " + str(total3[0]) + " แก้ว\n" "ใส่ท๊อปปิ๊ง " + str(topping[0]) + " แก้ว\n""\nรวมราคา " \
            + str(total1[0]) + " บาท\n" "รับเงินมา " + str(Cash1[0]) + " บาท\n" "เงินทอน " + str(total2[0]) + " บาท\n"
    txtBill.insert(END, (slip))
    databest(str(Product),str(Number_Product),str(total1),str(total2))

#รายการชา
def chataiwan1():
    c1 = int(c01.get())
    totol = 20 * c1
    cc1.set(totol)
    Product.append("ชานมไต้หวัน")
    Number_Product.append(c1)
    arm.append(totol)
def chathai2():
    c2 =int(c02.get())
    totol = 20 * c2
    cc2.set(totol)
    Product.append("ชาไทย")
    Number_Product.append(c2)
    arm.append(totol)
def chanomchocho3():
    c3 = int (c03.get())
    totol = 25 * c3
    cc3.set(totol)
    Product.append("ชานมโกโก้")
    Number_Product.append(c3)
    arm.append(totol)
def chakownom4():
    c4 = int(c04.get())
    totol = 25 * c4
    cc4.set(totol)
    Product.append("ชาเขียวนม")
    Number_Product.append(c4)
    arm.append(totol)
def chanomjen5():
    c5 = int(c05.get())
    totol = 20 * c5
    cc5.set(totol)
    Product.append("ชานมเย็น")
    Number_Product.append(c5)
    arm.append(totol)
def chanompark6():
    c6 = int(c06.get())
    totol = 20 * c6
    cc6.set(totol)
    Product.append("ชานมชมพู")
    Number_Product.append(c6)
    arm.append(totol)
def chakowsatoberre7():
    c7 = int(c07.get())
    totol = 25 * c7
    cc7.set(totol)
    Product.append("ชาเขียวสตอเบอรี่")
    Number_Product.append(c7)
    arm.append(totol)
def chakowapple8():
    c8 = int(c08.get())
    totol = 25 * c8
    cc8.set(totol)
    Product.append("ชาเขียวแอพเปิ่ล")
    Number_Product.append(c8)
    arm.append(totol)
def chakowkewe9():
    c9 = int(c09.get())
    totol =int(25 * c9)
    cc9.set(totol)
    Product.append("ชาเขียวกีวี้")
    Number_Product.append(c9)
    arm.append(totol)

#ท็อปปิ๊ง
def kaimook():
    top1 = int(top01.get())
    totol =int(10 * top1)
    top11.set(totol)
    Product.append("ไข่มุก")
    Number_Product.append(top1)
    arm.append(totol)
def browsugar():
    top2 = int(top02.get())
    totol =int(20 * top2)
    top12.set(totol)
    Product.append("บราวชูก้า")
    Number_Product.append(top2)
    arm.append(totol)
def frotsarat():
    top3 = int(top03.get())
    totol =int(10 * top3)
    top13.set(totol)
    Product.append("ฟลุตสลัด")
    Number_Product.append(top3)
    arm.append(totol)

#คิดตังค่าชา
def change1(): #ราคาชา
    ccc1 = cc1.get()
    ccc2 = cc2.get()
    ccc3 = cc3.get()
    ccc4 = cc4.get()
    ccc5 = cc5.get()
    ccc6 = cc6.get()
    ccc7 = cc7.get()
    ccc8 = cc8.get()
    ccc9 = cc9.get()
    if ccc1 == '':
        ccc1 = 0
    if ccc2 == '':
        ccc2 = 0
    if ccc3 == '':
        ccc3 = 0
    if ccc4 == '':
        ccc4 = 0
    if ccc5 == '':
        ccc5 = 0
    if ccc6 == '':
        ccc6 = 0
    if ccc7 == '':
        ccc7 = 0
    if ccc8 == '':
        ccc8 = 0
    if ccc9 == '':
        ccc9 = 0
    total = int(ccc1)+int(ccc2)+int(ccc3)+int(ccc4)+int(ccc5)+int(ccc6)+int(ccc7)+int(ccc8)+int(ccc9)
    Cange.set(total)

def change3(): #นับจำนวนแก้ว
    c21 = c01.get()
    c22 = c02.get()
    c23 = c03.get()
    c24 = c04.get()
    c25 = c05.get()
    c26 = c06.get()
    c27 = c07.get()
    c28 = c08.get()
    c29 = c09.get()
    if c21 == '':
        c21 = 0
    if c22 == '':
        c22 = 0
    if c23 == '':
        c23 = 0
    if c24 == '':
        c24 = 0
    if c25 == '':
        c25 = 0
    if c26 == '':
        c26 = 0
    if c27 == '':
        c27 = 0
    if c28 == '':
        c28 = 0
    if c29 == '':
        c29 = 0
    Total2 = int(c21) + int(c22) + int(c23) + int(c24) + int(c25) + int(c26) + int(c27) + int(c28) + int(c29)
    Cange1.set(Total2)
    total3.append(Total2)


#คิดตังท๊อปป๊ัง
def change4(): # รวมแก้วท๊อปปิ้ง
    top21 = top01.get()
    top22 = top02.get()
    top23 = top03.get()
    if top21 == '':
        top21 = 0
    if top22 == '':
        top22 = 0
    if top23 == '':
        top23 = 0
    total =int(top21)+int(top22)+int(top23)
    Cange4.set(total)
    topping.append(total)
def change5(): #รวมราคาท๊อปปิ้ง
    top31 = top11.get()
    top32 = top12.get()
    top33 = top13.get()
    if top31 == '':
        top31 = 0
    if top32 == '':
        top32 = 0
    if top33 == '':
        top33 = 0
    total =int(top31)+int(top32)+int(top33)
    Cange5.set(total)

#ราคารวม
def change6(): #คิดตังทชา+ท๊อปปิ้ง
    cash=int(Cange.get())
    cash1=int(Cange5.get())
    total=cash1+cash
    Total11.set(total)
    total1.append(total)
def change2(): #คิดตังทั้งหมด
    cash=int(Total11.get())
    cash1=int(Cash.get())
    total=cash1-cash
    Total.set(total)
    total2.append(total)
    Cash1.append(cash1)

#ใบเสร็จออนไลน์
def printter(name_product, number_product):
    webbrowser.open('https://www.oralanddental.com/computer_science/app/approve/report/slip.php?name_product='
                    + str(name_product) + '&number_product=' + str(number_product))

#ส่วนหลัก
char=LabelFrame(po,font = "Verdana 14 underline",text="สินค้าที่มี",labelanchor='n',bg = '#CFECBC',fg ='#0022FF')
char.grid(column=0,row=0,padx=5,pady=5)
toppingg=LabelFrame(po,font = "Verdana 14 underline",text="ท๊อปปิ้ง",labelanchor='n',bg = '#CFECBC',fg ='#0022FF')
toppingg.grid(column=0,row=1,padx=5,pady=5)
price=LabelFrame(po,font = "Verdana 14 underline",text="คำนวณค่าใช้จ่าย",labelanchor='n',bg = '#CFECBC',fg ='#0022FF')
price.grid(column=1,row=0,padx=5,pady=5)
TxT1=LabelFrame(po,font = "Verdana 14 underline",text="ใบเสร็จ",labelanchor='n')
TxT1.grid(column=3,row=0,padx=5,pady=5)
Data1=LabelFrame(po,font = "Verdana 14 underline",text="ระบบData",labelanchor='n',bg = '#CFECBC',fg ='#0022FF')
Data1.grid(column=1,row=1,padx=5,pady=5)
TxT2=LabelFrame(po,font = "Verdana 14 underline",text="แสดงData",labelanchor='n')
TxT2.grid(column=3,row=1,padx=5,pady=5)

#ส่วนสินค้า
chataiwan=Label(char,text="ชานมไต้หวัน 20฿",fg ='#0022FF', font = "Verdana 12 underline",bg = '#AAB5FF',padx = 20,
               pady = 5 ).grid(column=2,row=1 ,pady = 3 )
chataiwan=Label(char,text='จำนวน:',font=("TH Salabun New",'12')).grid(column=3,row=1,pady=0,padx=0,)
chataiwan=tk.Entry(char,width=10,textvariable=c01,bg='#FDF5E6').grid(column=4,row=1,pady=0,padx=0,)
chataiwan=Label(char,text='แก้ว',font=("TH Salabun New",'12')).grid(column=5,row=1,pady=0,padx=0,)
chataiwan=Button(char,text="ราคา",comman=chataiwan1).grid(column=6,row=1,padx=0,pady=0)
chataiwan=Entry(char,width=10,textvariable=cc1,bg='#FDF5E6').grid(column=7,row=1,pady=0,padx=5,)

chathai=Label(char,text="ชาไทย 20฿",fg = '#0022FF', font = "Verdana 12 underline",bg = '#AAB5FF',padx = 38,
               pady = 5 ).grid(column=2,row=2, pady = 3 )
chathai=Label(char,text='จำนวน:',font=("TH Salabun New",'12')).grid(column=3,row=2,pady=0,padx=0,)
chathai=tk.Entry(char,width=10,textvariable=c02,bg='#FDF5E6').grid(column=4,row=2,pady=0,padx=0,)
chathai=Label(char,text='แก้ว',font=("TH Salabun New",'12')).grid(column=5,row=2,pady=0,padx=0,)
chathai=Button(char,text="ราคา",comman=chathai2).grid(column=6,row=2,padx=0,pady=0)
chathai=Entry(char,width=10,textvariable=cc2,bg='#FDF5E6').grid(column=7,row=2,pady=0,padx=5,)

chanomchocho=Label(char,text="ชานมโกโก้ 25฿",fg ='#0022FF', font = "Verdana 12 underline",bg = '#AAB5FF',padx = 26,
               pady = 5 ).grid(column=2,row=3, pady = 3 )
chanomchocho=Label(char,text='จำนวน:',font=("TH Salabun New",'12')).grid(column=3,row=3,pady=0,padx=0,)
chanomchocho=Entry(char,width=10,textvariable=c03,bg='#FDF5E6').grid(column=4,row=3,pady=0,padx=0,)
chanomchocho=Label(char,text='แก้ว',font=("TH Salabun New",'12')).grid(column=5,row=3,pady=0,padx=0,)
chanomchocho=Button(char,text="ราคา",comman=chanomchocho3).grid(column=6,row=3,padx=0,pady=0)
chanomchocho=Entry(char,width=10,textvariable=cc3,bg='#FDF5E6').grid(column=7,row=3,pady=0,padx=5,)

chakownom=Label(char,text="ชาเขียวนม 25฿",fg = '#0022FF', font = "Verdana 12 underline",bg = '#AAB5FF',padx = 26,
               pady = 5 ).grid(column=2,row=4, pady = 3 )
chakownom=Label(char,text='จำนวน:',font=("TH Salabun New",'12')).grid(column=3,row=4,pady=0,padx=0,)
chakownom=Entry(char,width=10,textvariable=c04,bg='#FDF5E6').grid(column=4,row=4,pady=0,padx=0,)
chakownom=Label(char,text='แก้ว',font=("TH Salabun New",'12')).grid(column=5,row=4,pady=0,padx=0,)
chakownom=Button(char,text="ราคา",comman=chakownom4).grid(column=6,row=4,padx=0,pady=0)
chakownom=Entry(char,width=10,textvariable=cc4,bg='#FDF5E6').grid(column=7,row=4,pady=0,padx=5,)

chanomjen=Label(char,text="ชานมเย็น 20฿",fg = '#0022FF', font = "Verdana 12 underline",bg = '#AAB5FF',padx = 29,
               pady = 5 ).grid(column=2,row=5, pady = 3 )
chanomjen=Label(char,text='จำนวน:',font=("TH Salabun New",'12')).grid(column=3,row=5,pady=0,padx=0,)
chanomjen=Entry(char,width=10,textvariable=c05,bg='#FDF5E6').grid(column=4,row=5,pady=0,padx=0,)
chanomjen=Label(char,text='แก้ว',font=("TH Salabun New",'12')).grid(column=5,row=5,pady=0,padx=0,)
chanomjen=Button(char,text="ราคา",comman=chanomjen5).grid(column=6,row=5,padx=0,pady=0)
chanomjen=Entry(char,width=10,textvariable=cc5,bg='#FDF5E6').grid(column=7,row=5,pady=0,padx=5,)

chanompark=Label(char,text="ชานมเผิอก 20฿",fg = '#0022FF', font = "Verdana 12 underline",bg = '#AAB5FF',padx = 24,
               pady = 5 ).grid(column=2,row=6,pady = 3 )
chanompark=Label(char,text='จำนวน:',font=("TH Salabun New",'12')).grid(column=3,row=6,pady=0,padx=0,)
chanompark=Entry(char,width=10,textvariable=c06,bg='#FDF5E6').grid(column=4,row=6,pady=0,padx=0,)
chanompark=Label(char,text='แก้ว',font=("TH Salabun New",'12')).grid(column=5,row=6,pady=0,padx=0,)
chanompark=Button(char,text="ราคา",comman=chanompark6).grid(column=6,row=6,padx=0,pady=0)
chanompark=Entry(char,width=10,textvariable=cc6,bg='#FDF5E6').grid(column=7,row=6,pady=0,padx=5,)

chakowsatoberre=Label(char,text="ชาเขียวสตอเบอรี่ 25฿",fg = '#0022FF', font = "Verdana 12 underline",bg = '#AAB5FF',padx = 6,
               pady = 5 ).grid(column=2,row=7,pady = 3 )
chakowsatoberre=Label(char,text='จำนวน:',font=("TH Salabun New",'12')).grid(column=3,row=7,pady=0,padx=0,)
chakowsatoberre=Entry(char,width=10,textvariable=c07,bg='#FDF5E6').grid(column=4,row=7,pady=0,padx=0,)
chakowsatoberre=Label(char,text='แก้ว',font=("TH Salabun New",'12')).grid(column=5,row=7,pady=0,padx=0,)
chakowsatoberre=Button(char,text="ราคา",comman=chakowsatoberre7).grid(column=6,row=7,padx=0,pady=0)
chakowsatoberre=Entry(char,width=10,textvariable=cc7,bg='#FDF5E6').grid(column=7,row=7,pady=0,padx=5,)

chakowapple=Label(char,text="ชาเขียวแอปเปิ่ล 25฿",fg = '#0022FF', font = "Verdana 12 underline",bg = '#AAB5FF',padx = 10,
               pady = 5 ).grid(column=2,row=8,pady = 3 )
chakowapple=Label(char,text='จำนวน:',font=("TH Salabun New",'12')).grid(column=3,row=8,pady=0,padx=0,)
chakowapple=Entry(char,width=10,textvariable=c08,bg='#FDF5E6').grid(column=4,row=8,pady=0,padx=0,)
chakowapple=Label(char,text='แก้ว',font=("TH Salabun New",'12')).grid(column=5,row=8,pady=0,padx=0,)
chakowapple=Button(char,text="ราคา",comman=chakowapple8).grid(column=6,row=8,padx=0,pady=0)
chakowapple=Entry(char,width=10,textvariable=cc8,bg='#FDF5E6').grid(column=7,row=8,pady=0,padx=5,)

chakowkewe=Label(char,text="ชาเขียวกีวี้ 25฿",fg = '#0022FF', font = "Verdana 12 underline",bg = '#AAB5FF',padx = 26,
               pady = 5 ).grid(column=2,row=9,pady = 3 )
chakowkewe=Label(char,text='จำนวน:',font=("TH Salabun New",'12')).grid(column=3,row=9,pady=0,padx=0,)
chakowkewe=Entry(char,width=10,textvariable=c09,bg='#FDF5E6').grid(column=4,row=9,pady=0,padx=0,)
chakowkewe=Label(char,text='แก้ว',font=("TH Salabun New",'12')).grid(column=5,row=9,pady=0,padx=0,)
chakowkewe=Button(char,text="ราคา",comman=chakowkewe9).grid(column=6,row=9,padx=0,pady=0)
chakowkewe=Entry(char,width=10,textvariable=cc9,bg='#FDF5E6').grid(column=7,row=9,pady=0,padx=5,)
ch1=Button(char,text="รวมราคา",comman=change1).grid(column=6,row=10,padx=7,pady=7)
ch1=Entry(char,width=10,textvariable=Cange1,bg='#FDF5E6').grid(column=4,row=10,pady=0,padx=0,)
ch1=Label(char,text='แก้ว',font=("TH Salabun New",'12')).grid(column=5,row=10,pady=0,padx=0,)
ch2=Button(char,text="รวมจำนวนแก้ว",comman=change3).grid(column=3,row=10,padx=7,pady=7)
ch2=Entry(char,width=10,textvariable=Cange,bg='#FDF5E6').grid(column=7,row=10,pady=0,padx=0,)

#ส่วนท๊อปปิ้ง
kaimook1=Label(toppingg,text="ไข่มุก 10฿",fg = '#0022FF', font = "Verdana 12 underline",bg = '#AAB5FF',padx = 31,
               pady = 5 ).grid(column=2,row=1 ,pady = 3 )
kaimook1=Label(toppingg,text='จำนวน:',font=("TH Salabun New",'12')).grid(column=3,row=1,pady=0,padx=0,)
kaimook1=tk.Entry(toppingg,width=10,textvariable=top01,bg='#FDF5E6').grid(column=4,row=1,pady=0,padx=0,)
kaimook1=Label(toppingg,text='แก้ว',font=("TH Salabun New",'12')).grid(column=5,row=1,pady=0,padx=0,)
kaimook1=Button(toppingg,text="ราคา",comman=kaimook).grid(column=6,row=1,padx=0,pady=0)
kaimook1=Entry(toppingg,width=10,textvariable=top11,bg='#FDF5E6').grid(column=7,row=1,pady=0,padx=5,)

browsugar1=Label(toppingg,text="บราวชูก้า 20฿",fg = '#0022FF', font = "Verdana 12 underline",bg = '#AAB5FF',padx = 20,
               pady = 5 ).grid(column=2,row=2 ,pady = 3 )
browsugar1=Label(toppingg,text='จำนวน:',font=("TH Salabun New",'12')).grid(column=3,row=2,pady=0,padx=0,)
browsugar1=tk.Entry(toppingg,width=10,textvariable=top02,bg='#FDF5E6').grid(column=4,row=2,pady=0,padx=0,)
browsugar1=Label(toppingg,text='แก้ว',font=("TH Salabun New",'12')).grid(column=5,row=2,pady=0,padx=0,)
browsugar1=Button(toppingg,text="ราคา",comman=browsugar).grid(column=6,row=2,padx=0,pady=0)
browsugar1=Entry(toppingg,width=10,textvariable=top12,bg='#FDF5E6').grid(column=7,row=2,pady=0,padx=5,)

frotsarat1=Label(toppingg,text="ฟุตสลัด 10฿",fg = '#0022FF', font = "Verdana 12 underline",bg = '#AAB5FF',padx = 20,
               pady = 5 ).grid(column=2,row=3 ,pady = 3 )
frotsarat1=Label(toppingg,text='จำนวน:',font=("TH Salabun New",'12')).grid(column=3,row=3,pady=0,padx=0,)
frotsarat1=tk.Entry(toppingg,width=10,textvariable=top03,bg='#FDF5E6').grid(column=4,row=3,pady=0,padx=0,)
frotsarat1=Label(toppingg,text='แก้ว',font=("TH Salabun New",'12')).grid(column=5,row=3,pady=0,padx=0,)
frotsarat1=Button(toppingg,text="ราคา",comman=frotsarat).grid(column=6,row=3,padx=0,pady=0)
frotsarat1=Entry(toppingg,width=10,textvariable=top13,bg='#FDF5E6').grid(column=7,row=3,pady=0,padx=5,)
ch3=Button(toppingg,text="รวมแก้ว",comman=change4).grid(column=3,row=4,padx=7,pady=7)
ch3=Entry(toppingg,width=10,textvariable=Cange4,bg='#FDF5E6').grid(column=4,row=4,pady=0,padx=0,)
ch3=Label(toppingg,text='แก้ว',font=("TH Salabun New",'12')).grid(column=5,row=4,pady=0,padx=0,)
ch4=Button(toppingg,text="รวมท๊อปปิ้ง",comman=change5).grid(column=6,row=4,padx=7,pady=7)
ch4=Entry(toppingg,width=10,textvariable=Cange5,bg='#FDF5E6').grid(column=7,row=4,pady=0,padx=0,)

#คิดราคา
Price11=Label(price,text='ค่าชานม :',font=("TH Salabun New",'16'))
Price11.grid(column=0,row=0,pady=5,padx=5,sticky='E')
Price11=Label(price,text='บาท',font=("TH Salabun New",'16'))
Price11.grid(column=2,row=0,pady=5,padx=5,sticky='E')
Price11=Label(price,text='ค่าท๊อปปิ้ง :',font=("TH Salabun New",'16'))
Price11.grid(column=0,row=1,pady=5,padx=5,sticky='E')
Price11=Label(price,text='บาท',font=("TH Salabun New",'16'))
Price11.grid(column=2,row=1,pady=5,padx=5,sticky='E')
Price11=Label(price,text='รวมราคา :',font=("TH Salabun New",'16'))
Price11.grid(column=0,row=3,pady=5,padx=5,sticky='E')
Price11=Label(price,text='บาท',font=("TH Salabun New",'16'))
Price11.grid(column=2,row=3,pady=5,padx=5,sticky='E')
Price11=Label(price,text='รับเงินมา :',font=("TH Salabun New",'16'))
Price11.grid(column=0,row=4,pady=5,padx=5,sticky='E')
Price11=Label(price,text='บาท',font=("TH Salabun New",'16'))
Price11.grid(column=2,row=4,pady=5,padx=5,sticky='E')
Price11=Label(price,text='เงินทอน :',font=("TH Salabun New",'16'))
Price11.grid(column=0,row=5,pady=5,padx=5,sticky='E')
Price11=Label(price,text='บาท',font=("TH Salabun New",'16'))
Price11.grid(column=2,row=5,pady=5,padx=5,sticky='E')
Price11=Entry(price,bg='#FDF5E6',textvariable=Cange).grid(column=1,row=0)
Price11=Entry(price,bg='#FDF5E6',textvariable=Cange5).grid(column=1,row=1)
Price11=Entry(price,bg='#FDF5E6',textvariable=Total11).grid(column=1,row=3)
Price11=Entry(price,textvariable=Cash,bg='#FDF5E6').grid(column=1,row=4)
Price11=Entry(price,textvariable=Total,bg='#FDF5E6').grid(column=1,row=5)
Price11=Button(price,text="คำนวณ",font=("TH Salabun New",'12'),comman=change6).grid(column=1,row=2,padx=7,pady=7)
Price11=Button(price,text="คำนวณ",font=("TH Salabun New",'12'),comman=change2).grid(column=1,row=7,padx=7,pady=7)

#TxT
txtBill=Text(TxT1,height=25, width=55)
txtBill.pack(side=TOP, fill=X)
txtBill1=Text(TxT2,height=10, width=55)
txtBill1.pack(side=TOP, fill=X)

#เรียกดูข้อมูล
Price11=Label(Data1,text='ป้อนเลข :',font=("TH Salabun New",'16'))
Price11.grid(column=0,row=0,pady=5,padx=5,sticky='E')
Price11=Entry(Data1,textvariable=num,bg='#FDF5E6').grid(column=1,row=0)
Save = Button(Data1, text="แสดงออเด้อเก่า",font=("TH Salabun New",'12'), command=datashow).grid(column=0, row=1)
Save = Button(price, text="ปริ้นใบเสร็จ",font=("TH Salabun New",'12'), command=Data).grid(column=1, row=8)

po.mainloop()