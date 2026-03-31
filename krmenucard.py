from tkinter import *
window = Tk()
# specify it's size
window.title("KR RESTAURANT MENU CARD")
window.geometry("1350x750+0+0")
window.resizable(0, 0)

#bg = PhotoImage(file="C:\Heena\kr.png")

#label=Label(window, image=bg)
#label.place(x=0, y=0)

menu=Menu(window)
window.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label='Home',menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open')
filemenu.add_separator()
filemenu.add_command(label='Exit',command=window.quit)
editmenu=Menu(menu)
menu.add_cascade(label='Edit',menu=(editmenu))
editmenu.add_command(label='Edit')
helpmenu=Menu(menu)
menu.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About')

def calculate(): 

    dic = {'aloo_partha': [e1, 30], 

           'samosa': [e2, 15], 

           'pizza': [e3, 150], 

           'chilli_potato': [e4, 50], 

           'chowmein': [e5, 70], 

           'gulab_jamun': [e6, 35],

           'Burger': [e7, 35],
           
           'Fries': [e8, 300],
           
           'Sandwich': [e9, 50],

           'Coffee': [e10, 200],

           'Tea': [e11, 20],

           'Stawberry Shake': [e12, 100],

           'Vanilla Shake': [e13,100],

           'Lassi': [e14, 80],

           'Water Bottal': [e15, 30],

           'Naan': [e16, 50]}
    total = 0

    for key, val in dic.items(): 

        if val[0].get() != "": 

            total += int(val[0].get())*val[1] 

  

    label16 = Label(window, 

                    text="Your Total Bill is - "+str(total), 

                    font="times 18") 

   

    label16.place(x=370, y=490) 

    label16.after(1000, label16.destroy) 

    window.after(1000, calculate) 

  

  

label8 = Label(window, 

               text=" KR'S RESTAURANT  ", 

               font="times 28 bold") 

label8.place(x=600, y=20, anchor="center") 

  

  

label1 = Label(window, 

               text="Menu", 

               font="times 28 bold",) 

  

label1.place(x=1100, y=0)


labe33 = Label(window, 

               text="Food Menu", 

               font="times 18 bold",) 

  

labe33.place(x=1090, y=40) 


  

label2 = Label(window, text="Aloo Paratha  \
       Rs 30", font=" times 18") 
 
label2.place(x=1010, y=70) 

  

label3 = Label(window, text="Samosa         \
         Rs 15", font="times 18") 
 
label3.place(x=1010, y=100) 

  

label4 = Label(window, text="Pizza       \
               Rs 150", font="times 18") 

label4.place(x=1010, y=130) 

  

label5 = Label(window, text="Chilli Potato  \
         Rs 50", font="times 18") 

label5.place(x=1010, y=160) 

  

label6 = Label(window, text="Chowmein    \
          Rs 70", font="times 18") 

label6.place(x=1010, y=190) 

  

label7 = Label(window, text="Gulab Jamun   \
       Rs 35", font="times 18") 

label7.place(x=1010, y=220) 


label19 = Label(window, text="Burger   \
                 Rs 25", font="times 18") 

label19.place(x=1010, y=250)



label19 = Label(window, text="Fries   \
                    Rs 300", font="times 18") 

label19.place(x=1010, y=280)


label19 = Label(window, text="Sandwich   \
            Rs 50", font="times 18") 

label19.place(x=1010, y=310)



label19 = Label(window, text="Naan   \
                   Rs 50", font="times 18") 

label19.place(x=1010, y=340)





labe23 = Label(window, 

               text="Drink Menu", 

               font="times 18 bold",)
  

labe23.place(x=1090, y=390)



label24 = Label(window, text="Water Bottal   \
         Rs 30", font="times 18") 

label24.place(x=1010, y=430)



label24 = Label(window, text="Vanilla Shake   \
       Rs 100", font="times 18") 

label24.place(x=1010, y=460)



label24 = Label(window, text="Coffee      \
               Rs 200", font="times 18") 

label24.place(x=1010, y=490)



label24 = Label(window, text="Tea     \
                     Rs 20", font="times 18") 

label24.place(x=1010, y=520)



label24 = Label(window, text="Stawberry Shake    \
 Rs 100", font="times 18") 

label24.place(x=1010, y=550)



label24 = Label(window, text="Lassi      \
                  Rs 80", font="times 18") 

label24.place(x=1010, y=580)






  
# billing section 

label9 = Label(window, text=" SELECT THE ITEMS ", 

               font="times 18  bold") 

label9.place(x=400, y=70) 

  

label10 = Label(window, 

                text="Aloo Paratha", 

                font="times 18") 

label10.place(x=20, y=120) 

  

e1 = Entry(window) 

e1.place(x=20, y=150) 

  

label11 = Label(window, text="Samosa", 

                font="times 18") 

label11.place(x=20, y=200) 

  

e2 = Entry(window) 

e2.place(x=20, y=230) 

  

label12 = Label(window, text="Pizza", 

                font="times 18") 

label12.place(x=20, y=280) 

  

e3 = Entry(window) 

e3.place(x=20, y=310) 

  

label13 = Label(window, 

                text="Chilli Potato", 

                font="times 18") 

label13.place(x=20, y=360) 

  

e4 = Entry(window) 

e4.place(x=20, y=390) 

  

label14 = Label(window, 

                text="Chowmein", 

                font="times 18") 

label14.place(x=250, y=120) 

  

e5 = Entry(window) 

e5.place(x=250, y=150) 

  

label15 = Label(window, 

                text="Gulab Jamun", 

                font="times 18") 

  

label15.place(x=250, y=200)


e6 = Entry(window) 

e6.place(x=250, y=230) 



label20 = Label(window, 

                text="Burger", 

                font="times 18") 

  

label20.place(x=250, y=270) 


e7 = Entry(window) 

e7.place(x=250, y=300)


label21 = Label(window, 

                text="Fries", 

                font="times 18") 

  

label21.place(x=250, y=360) 


e8 = Entry(window) 

e8.place(x=250, y=390) 


label21 = Label(window, 

                text="Sandwich ", 

                font="times 18") 

  

label21.place(x=480, y=120) 


e9 = Entry(window) 

e9.place(x=480, y=150)



label21 = Label(window, 

                text="Coffee", 

                font="times 18") 

  

label21.place(x=480, y=200) 


e10 = Entry(window) 

e10.place(x=480, y=230) 




label21 = Label(window, 

                text="Tea", 

                font="times 18") 

  

label21.place(x=480, y=280) 


e11= Entry(window) 

e11.place(x=480, y=310) 




label21 = Label(window, 

                text="Stawberry Shake ", 

                font="times 18") 

  

label21.place(x=480, y=360) 


e12 = Entry(window) 

e12.place(x=480, y=390) 



label21 = Label(window, 

                text="Vanilla Shake ", 

                font="times 18") 

  

label21.place(x=710, y=120) 


e13 = Entry(window) 

e13.place(x=710, y=150) 



label21 = Label(window, 

                text="Lassi ", 

                font="times 18") 

  

label21.place(x=710, y=200) 


e14 = Entry(window) 

e14.place(x=710, y=230)



label21 = Label(window, 

                text="Water Bottal ", 

                font="times 18") 

  

label21.place(x=710, y=270) 


e15 = Entry(window) 

e15.place(x=710, y=300)



label21 = Label(window, 

                text="Naan", 

                font="times 18") 

  

label21.place(x=710, y=360) 


e16 = Entry(window) 

e16.place(x=710, y=390) 


  
# execute calculate function after 1 second 

window.after(1000, calculate) 
                    
 
window.mainloop()