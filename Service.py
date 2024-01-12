from telethon import TelegramClient,events,sync

#Vòng lặp chính
def start(client : TelegramClient,chat):

    def main():
        client.start()
        
        @client.on(events.NewMessage(chats=chat))
        async def handler(event):
            messages = await client.get_messages(chat)
            print(messages[0].text)
            
        client.run_until_disconnected()



    client.loop.run_until_complete(main())
