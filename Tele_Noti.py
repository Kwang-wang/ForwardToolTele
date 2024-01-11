from typing import Final
from telethon import TelegramClient,events,sync
import telethon
import tkinter as tk
import LogginFunction as logginFunction
import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type
#Global variable
API_ID : Final = '23925763'
API_HASH : Final = 'fb99e16048c00204847949bb7af987a9'
global isAuthorized
isAuthorized :bool
client = TelegramClient('GetNoTi',API_ID,API_HASH)
global sdt
#Connect Tele api
client.connect()
#register GUI
root = tk.Tk()
root.title('BloodMoon_forwardBot_1.0.0')
root.geometry("900x600")
#TextBox
Noti = tk.Text(root,height=1,width=900)
Noti.configure(font=200)
Noti.pack(padx=10,pady=0,anchor='e')
#Label
PhoneNumberLabel = tk.Label(root,text='Phone Number :',font=('Arial',10))
#entry--------------------------------------------------------------
#EntryPhoneNumber
EntryPhoneNumber = tk.Entry(root)
#EntryCodeNumber
EntryCodeNumber = tk.Entry(root)
#btn----------------------------------------------------------------
#GetcodeBTN
GetCodeBtn = tk.Button(text='GetCode',font=('Arial',10),command=lambda: getCode())
#sign in btn
SigninBtn = tk.Button(text='Sign in',font=('Arial',10),command=lambda:signIn())
#LoggoutBtn
LoggoutBtn = tk.Button(text='Logout',font=('Arial',10),command=lambda:logOut())


isAuthorized = client.is_user_authorized()
#hàm hiển thị UI đăng nhập
def turnOnLoginUi():
    PhoneNumberLabel.pack(padx=10,pady=0,anchor='w')
    EntryPhoneNumber.pack(padx=10,pady=0,anchor='w')
    GetCodeBtn.pack(padx=10,pady=0,anchor='w')
#hàm ẩn UI đăng nhập
def turnOffLoginUi():
    PhoneNumberLabel.pack_forget()
    EntryPhoneNumber.pack_forget()
    GetCodeBtn.pack_forget()
    EntryCodeNumber.pack_forget()
    SigninBtn.pack_forget()
    
#Hàm hiển thị UI bot
def turnOnBotUi():
    LoggoutBtn.pack(padx=10,pady=0,anchor='w')
    
#Hàm tắt UI bot
def turnOffBotUi():
    LoggoutBtn.pack_forget()
#Hàm thông báo
def Notification(text:str):
    Noti.delete("1.0",tk.END)
    Noti.insert(tk.END,text)
#check xem có đang đăng nhập không
if isAuthorized == False:
    Notification('You are not logged in')
    turnOnLoginUi()
else:
    Notification('Logged in')
    turnOnBotUi()











#addtionalfunction
#Hàm lấy code sau khi nhập số điện thoại
def getCode():
    global sdt
    sdt = EntryPhoneNumber.get()
    try:
        carrier._is_mobile(number_type(phonenumbers.parse(sdt)))
    except phonenumbers.phonenumberutil.NumberParseException as b:
        Notification("Your entered phonenumber did not seem to be a phone number")
        return
    else:
        try:
            logginFunction.getCode(sdt,client=client)
        except (telethon.errors.rpcerrorlist.SendCodeUnavailableError
                ,telethon.errors.rpcerrorlist.PhoneNumberInvalidError
                ,TypeError) as e:
            if isinstance(e,telethon.errors.rpcerrorlist.SendCodeUnavailableError):
                Notification('You failed to log in too many times, please try again later')
            if isinstance(e,telethon.errors.rpcerrorlist.PhoneNumberInvalidError):
                Notification('The phone number is invalid')
            if isinstance(e,TypeError):
                Notification('Please enter the correct phone number')
        else:
            EntryCodeNumber.pack(padx=10,pady=0,anchor='w')
            SigninBtn.pack(padx=10,pady=0,anchor='w')
    
#Hàm đăng nhập
def signIn():
    entryCode = EntryCodeNumber.get()
    if(entryCode == ''):
        Notification('Please enter the sent code')
        return
    if(len(entryCode) != 5):
        Notification('The code is incorrect, the code includes 6 numbers')
        return
    if not entryCode.isdigit():
        Notification('The code is incorrect, the code includes 6 numbers')
        return 
    try:
        logginFunction.signIn(sdt,EntryCodeNumber.get(),client=client)
    except telethon.errors.rpcerrorlist.PhoneCodeInvalidError as e:
        Notification('Code không khả dụng')
    else:
        Notification('Logged in successfully')
        turnOnBotUi()
        turnOffLoginUi()
#hàm đăng xuất
def logOut():
    try:
        logginFunction.logOut(client)
    except:
        Notification('There are some errorr occurr')
    else:
        turnOnLoginUi()
        turnOffBotUi()
        Notification('Logged out successfully')
        


#run
root.mainloop()



