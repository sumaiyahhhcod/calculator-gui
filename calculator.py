from tkinter import *
# def login():
root=Tk()
root.title('facebook log in')
root.geometry('1000x600')
frame1=Frame(root,width=400,height=350,border=1,bg='white',relief='flat')
frame1.place(x=750,y=150)
uname_t=Text(frame1,width=52,height=2,relief='flat',bg='gray90',font=('helvetica',10,'normal'))
uname_t.place(x=12,y=30)
username=Label(frame1,text='username',fg="gray40",bg='white')
username.place(x=12,y=7)
pword_t=Text(frame1,width=52,height=2,relief='flat',bg='gray90',font=('helvetica',10,'normal'))
pword_t.place(x=12,y=99)
password=Label(frame1,text='password',bg='white',fg='gray40')
password.place(x=12,y=75)
log_btn=Button(frame1,text='login',bg='royalblue',fg='white',font=('helvetica',13,'normal'))
log_btn.place(x=13,y=155)
fg_btn=Label(frame1,text='forgot password',bg='white',fg='royal blue',font=('couriernew',15,'normal'))
fg_btn.place(x=140,y=250)
frame2=Frame(root,width=400,height=100,bg='white',relief='flat')
frame2.place(x=750,y=505)
creat_btn=Button(frame2,width=20,height=2,text='create new account',font=('helvetica',15,'normal'))
creat_btn.place(x=100,y=25)
fb=Label(root,text='facebook',font=('arial',50,'bold'),fg='royalblue')
fb.place(x=150,y=200)
stnt=Label(root,text='connect with friends and the world \naround you on facebook') 
stnt.place(x=150,y=270) 
root.mainloop()               