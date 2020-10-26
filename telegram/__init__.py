from telegram import notifly

token = '1347043184:AAGmj_-VlRsIyQGSTTTcSFMhBJh3-aPQkto'
bot=notifly.BotHandler(token)
text = input("Enter text message : ")
print(bot.send_message(text,True))

opt_image = input("Do you want to send image ?")

if(opt_image=='y' or opt_image=='Y'):
    img_path = input("Enter full image path : ")
    bot.send_image(img_path)

opt_doc = input("Do you want to send a document ?")

if(opt_doc=='y' or opt_doc=='Y'):
    doc_path = input("Enter full document path : ")
    bot.send_document(doc_path)