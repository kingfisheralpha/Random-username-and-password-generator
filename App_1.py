from tkinter import *
import os
import random




win_1=Tk()
#default_font = tkFont.nametofont("TkDefaultFont")
#default_font.config(size=9)
var=IntVar()
t_p=StringVar(win_1)
t_u=StringVar(win_1)

path_=os.getcwd()+'\\'

class window_1:
    def __init__(self,master):
        
        def RNG(x,y):
            _=random.randint(x,y)
            return _

        def RNG_list(z):
            _=random.choice(z)
            return _

        def uppercase(_):
            _=_[0].upper()+_[1:]
            return _


        def RNG_password():
            
            with open(path_+'keys.txt') as f:
                keys=f.read().splitlines()
            password=''
            for i in range(var.get()):
                password+=(keys[RNG(0,len(keys)-1)])
                
            e2.delete(0,END)
            e2.insert(0,password)
            return(password)

        
        def RNG_username():
            #first_name=''
            #last_name=''
            
            
            with open(path_+'first_names.txt') as f:
                first_names=f.read().splitlines()
            first_name=RNG_list(first_names)
            middle_name=RNG_list(first_names)
            #first_name=uppercase(first_name)
            
            with open(path_+'last_names.txt') as f:
                last_names=f.read().splitlines()
            last_name=RNG_list(last_names)
            #last_name=uppercase(last_name)

                
            
            if RNG(0,1)==1:
                first_name=uppercase(first_name)
                last_name=uppercase(last_name)
                middle_name=uppercase(middle_name)

            if RNG(0,1)==1:
                username=first_name+middle_name+last_name
            else:
                username=first_name+last_name

            
            #username=first_name+middle_name+last_name

            for i in range(RNG(2,4)):
                username+=str(RNG(0,9))

            e1.delete(0,END)
            e1.insert(0,username)
            RNG_password()
            return(username)


        



        

        frame1=Frame(master)
        frame1.grid(row=0,column=0)

        label1=Label(frame1,text='Username:')
        label1.grid(row=0,column=0,sticky=W)

        label2=Label(frame1,text='Password:')
        label2.grid(row=1,column=0,sticky=W)

        e1=Entry(frame1,textvariable=t_u,width=38)
        e1.grid(row=0,column=1)

        e2=Entry(frame1,textvariable=t_p,width=38)
        e2.grid(row=1,column=1)
        RNG_password()

        button1=Button(frame1,height=2,width=8,text='Generate\n username',command=RNG_username)
        button1.grid(row=2,column=0)

        button2=Button(frame1,height=2,width=8,text='Generate\n password', command=RNG_password)
        button2.grid(row=3,column=0)

        label3=Label(frame1,text='Use the slider below to pick \nthe length of a password:')
        label3.grid(column=1,row=2,sticky=W)

        slider=Scale(frame1, from_=8,to=32,orient=HORIZONTAL,variable=var)
        slider.grid(row=3, column=1,sticky=W)

        RNG_username()

        #button3=Button(frame1,text='Save',width=8)
        #button3.grid(column=0,row=4)


_=window_1(win_1)


win_1.mainloop()

