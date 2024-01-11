from telethon import TelegramClient,events,sync
import tkinter as tk
#hàm lấy code từ số điện thoại
def getCode(phoneNumber,client : TelegramClient):
    client.send_code_request(phone=phoneNumber)
#Hàm đăng nhập
def signIn(phoneNumber,code,client : TelegramClient):
    client.sign_in(phoneNumber,code)
#hàm đăng xuất
def logOut(client : TelegramClient):
    client.log_out()