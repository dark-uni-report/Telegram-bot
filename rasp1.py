import PIL.Image
import PIL.ImageDraw
import face_recognition as fr
import matplotlib.pyplot as plt
import telebot


image = fr.load_image_file("kem1.jpg")
face_loc = fr.face_locations(image)
if len(face_loc) == 0:
    print('Нет лиц на фотографии.')
pil_image = PIL.Image.fromarray(image)
for face_location in face_loc:
    top, right, bottom, left = face_location
    draw_shape = PIL.ImageDraw.Draw(pil_image)
    draw_shape.rectangle([left, top, right, bottom], fill=(0, 0, 0), outline="white")
pil_image.save("output3.jpg")


#bot=telebot.TeleBot('5209828662:AAHHCrzz8DSSYV1rrahW2i5-L56HhtIz3qU')


#@bot.message_handler(commands=["start"])
#def start(m, res=False):
    #bot.send_message(m.chat.id, 'Я на связи. Чтобы ознакомиться с моим функционалом \
#используй команду /help')


#@bot.message_handler(commands=["help"])
#def help(m, res=False):
    #bot.send_message(m.chat.id, 'Отправь фотографию с людьми \
#и я скрою их лица')


#@bot.message_handler(content_types=["photo"])
#def send_help_text(message):
    #bot.send_message(message.chat.id, 'Хорошо, мы обработаем фотографию и я обязательно отвечу!')
    ##bot.forward_message(config, message.chat.id, message.message_id)
    #photo_id = message.photo[-1].file_id
    ## Достаём картинку
    #photo_file = bot.get_file(photo_id)    
    
    
    
    #image = face_recognition.load_image_file(photo_file)
    #face_loc = fr.face_locations()
    #if len(face_loc) == 0:
        #print('Нет лиц на фотографии.')
    #pil_image = PIL.Image.fromarray(image)
    #for face_location in face_loc:
        #top, right, bottom, left = face_location
        #draw_shape = PIL.ImageDraw.Draw(pil_image)
        #draw_shape.rectangle([left, top, right, bottom], fill=(0, 0, 0), outline="white")
    #pil_image.save("output2.jpg")    
    
    
    ##photo = open('output2.jpg', 'rb')
    ##bot.send_photo(chat_id, photo)
    #bot.send_photo(message.chat.id, open('output2.jpg', 'rb'))    
    ##bot.send_photo(message.chat.id, message.photo)



#bot.infinity_polling()
