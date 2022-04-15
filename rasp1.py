import telebot
from telebot import types
import PIL.Image
import PIL.ImageStat
import PIL.ImageDraw
import face_recognition as fr
import matplotlib.pyplot as plt
import string
from PIL import ImageFilter


bot = telebot.TeleBot('5321967311:AAE3k2eaCvp7feGTSJPGcyDBlYARFrDGGWw')
words = ['мгу', 'вшэ']
x = False
src_f = ''
src1 = ''
yn = 0
yy = 0
h = 0
userid = ''
nn = False


@bot.message_handler(commands=["start"])
def start(m):
    global user
    global nn
    global yy
    global src_f
    yy = 0
    src_f = ''
    user_s = m.from_user.first_name
    user_n = m.from_user.last_name
    userid = m.from_user.id
    user = m.from_user.username
    if user is None:
        user = 'id_unknown'
    print(f'{user_n}_{user_s}___@{user}___id{userid}')
    with open("blocked.txt", 'r') as filexx:
        if str(userid) in filexx.read():
            nn = True
    if not nn:
        gg = False
        user_n = m.from_user.first_name
        user_s = m.from_user.last_name
        with open("users.txt", 'r', encoding='utf-8') as filex:
            if user not in filex.read():
                gg = True
        with open("users.txt", 'a', encoding='utf-8') as filex:
            if gg:
                filex.write(f'\n{user_n} {user_s} - @{user} - id{userid}')
        bot.send_message(
            m.chat.id, text='''Я на связи.🤖 Чтобы ознакомиться с моим \
            функционалом используй команду /help''')
    else:
        bot.send_message(m.chat.id, '🚫Доступ к ресурсу ограничен.')


@bot.message_handler(commands=["a1"])
def a1(m):
    global nn
    userid = m.from_user.id
    sf = []
    if userid == 2113073703:
        with open("blocked.txt", 'r') as fl:
            for l in fl.readlines():
                if f'-{2113073703}-' not in l:
                    sf.append(l)
        if len(sf) != 0:
            del sf[-1]
            with open("blocked.txt", 'w') as fy:
                for i in range(len(sf)):
                    fy.write(f'{sf[i]}')
                sf = []
            bot.send_message(m.chat.id, 'Вы успешно удалены из черного списка')
            nn = False
        else:
            bot.send_message(m.chat.id, 'Черный список пуст')


@bot.message_handler(commands=["a2"])
def a2(m):
    global nn
    userid = m.from_user.id
    if userid == 2113073703:
        with open("blocked.txt", 'w') as fy:
            fy.write('')
        bot.send_message(m.chat.id, 'Все пользователи успешно разблокированы.')
        nn = False


@bot.message_handler(commands=["a1"])
def a1(m):
    global nn
    userid = m.from_user.id
    sf = []
    if userid == 2113073703:
        with open("blocked.txt", 'r') as fl:
            for l in fl.readlines():
                if f'-{2113073703}-' not in l:
                    sf.append(l)
        if len(sf) != 0:
            with open("blocked.txt", 'w') as fy:
                for i in range(len(sf)):
                    fy.write(f'{sf[i]}')
                sf = []
            bot.send_message(m.chat.id, 'Вы успешно удалены из черного списка')
            nn = False
        else:
            bot.send_message(m.chat.id, 'Черный список пуст')


@bot.message_handler(commands=["a2"])
def a2(m):
    global nn
    userid = m.from_user.id
    if userid == 2113073703:
        with open("blocked.txt", 'w') as fy:
            fy.write('')
        bot.send_message(m.chat.id, 'Все пользователи успешно разблокированы.')
        nn = False


@bot.message_handler(commands=["help"])
def help(m, res=False):
    global yy
    global nn
    markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
    userid = m.from_user.id
    with open("blocked.txt", 'r') as filex:
        if str(userid) in filex.read():
            nn = True
    yy = 0
    if not nn:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("/1")
        btn2 = types.KeyboardButton("/2")
        btn3 = types.KeyboardButton("/3")
        btn4 = types.KeyboardButton("/4")
        btn5 = types.KeyboardButton("/clear")
        markup.add(btn1, btn2, btn3, btn4, btn5)
        if src_f == '':
            bot.send_message(
                m.chat.id, f'''Отправь фотографию с людьми *в формате файла* \
                и я:\n''', reply_markup=markup)
            bot.send_message(m.chat.id, 'скрою лицо - /1\n')
            bot.send_message(m.chat.id, 'выделю черты лица - /2\n')
            bot.send_message(m.chat.id, 'распозаю лицо - /3\n')
            bot.send_message(m.chat.id, 'заблюрю лицо - /4\n')
            bot.send_message(m.chat.id, 'удалю наши сообщения - /clear\n')
        else:
            bot.send_message(m.chat.id, 'скрыть лицо - /1\n')
            bot.send_message(m.chat.id, 'выделить черты лица - /2\n')
            bot.send_message(m.chat.id, 'распозать лицо - /3\n')
            bot.send_message(m.chat.id, 'заблюрить лицо - /4\n')
    else:
        bot.send_message(m.chat.id, '🚫Доступ к ресурcу ограничен.')


@bot.message_handler(commands=["1"])
def one(m, res=False):
    global nn
    global src_f
    global src1
    global yy
    yy = 0
    global color
    userid = m.from_user.id
    with open("blocked.txt", 'r') as filex:
        if str(userid) in filex.read():
            nn = True
    if not nn:
        if src_f != '':
            bot.send_message(m.chat.id, 'Пару секунд...\n')
            try:
                filen = src_f
                image = fr.load_image_file(filen)
                face_landmarks_list = fr.face_landmarks(image)
                face_loc = fr.face_locations(image)
                if len(face_loc) == 0:
                    bot.send_message(
                        m.chat.id, '''Лицо частично скрыто, что затрудняет \
                        мою работу😣''')
                    bot.send_message(
                        m.chat.id, 'Используй другое изображение.')
                else:
                    pil_image = PIL.Image.fromarray(image)
                    im = pil_image.convert('L')
                    stat = PIL.ImageStat.Stat(im)
                    br = stat.mean
                    if br[0] >= 80:
                        color = (255, 255, 255)
                        outline = 'black'
                    elif br[0] < 80:
                        color = (0, 0, 0)
                        outline = 'white'
                    for face_location in face_loc:
                        top, right, bottom, left = face_location
                        draw_shape = PIL.ImageDraw.Draw(pil_image)
                        draw_shape.rectangle(
                            [left, 0.94 * top, right, bottom], fill=color,
                            outline=outline)
                        pil_image.save(f'dd{src_f}')
                    photo = open(src1, 'rb')
                    bot.send_photo(m.chat.id, photo)
            except:
                bot.send_message(
                    m.chat.id, '''Скорость интернета не позволяет обработать \
                    это фото''')
                bot.send_message(m.chat.id, 'Используй другое изображение.\n')
                src_f = ''
                src1 = ''
        else:
            bot.send_message(
                m.chat.id, '️⚠️Сначала необхожимо загрузить фото!')
    else:
        bot.send_message(m.chat.id, '🚫Доступ к ресурсу ограничен.')


@bot.message_handler(commands=["4"])
def one(m, res=False):
    global nn
    global src_f
    global src1
    global yy
    yy = 0
    userid = m.from_user.id
    with open("blocked.txt", 'r') as filex:
        if str(userid) in filex.read():
            nn = True
    if not nn:
        if src_f != '':
            bot.send_message(m.chat.id, 'Пару секунд...\n')
            filen = src_f
            img = PIL.Image.open(filen)
            image = fr.load_image_file(filen)
            face_landmarks_list = fr.face_landmarks(image)
            face_loc = fr.face_locations(image)
            if len(face_loc) == 0:
                bot.send_message(
                    m.chat.id, '''Лицо частично скрыто, что затрудняет \
                    мою работу😣''')
                bot.send_message(m.chat.id, 'Используй другое изображение.')
            else:
                try:
                    solid_fill = (0, 0, 0, 255)

                    def create_rounded_rectangle_mask(rectangle, radius):
                        i = PIL.Image.new("RGBA", rectangle.size, (0, 0, 0, 0))
                        corner = PIL.Image.new(
                            'RGBA', (radius, radius), (0, 0, 0, 0))
                        draw = PIL.ImageDraw.Draw(corner)
                        draw.pieslice((0, 0, radius * 2, radius * 2),
                                      180, 270, fill=solid_fill)
                        mx, my = rectangle.size

                        i.paste(corner, (0, 0), corner)
                        i.paste(corner.rotate(90),
                                (0, my - radius), corner.rotate(90))
                        i.paste(corner.rotate(180), (mx - radius,
                                my - radius), corner.rotate(180))
                        i.paste(corner.rotate(270),
                                (mx - radius, 0), corner.rotate(270))

                        draw = PIL.ImageDraw.Draw(i)
                        draw.rectangle(
                            [(radius, 0), (mx - radius, my)], fill=solid_fill)
                        draw.rectangle(
                            [(0, radius), (mx, my - radius)], fill=solid_fill)

                        return i
                    for face_location in face_loc:
                        x2, x3, x4, x1 = face_location
                        dx = x3 - x1
                        radius = int(round(dx * 0.28, 0))
                        blur = int(round(dx * 0.09, 0))
                        cropped_img = img.crop(
                            (x1, int(round(0.9 * x2, 0)), x3, x4))
                        blurred_img = cropped_img.filter(
                            ImageFilter.GaussianBlur(blur),).convert("RGBA")
                        img.paste(blurred_img, (x1, int(round(0.9 * x2, 0))),
                                  create_rounded_rectangle_mask(cropped_img,
                                  radius))
                    img.save(f'dd{src_f}')
                    photo = open(src1, 'rb')
                    bot.send_photo(m.chat.id, photo)
                except:
                    bot.send_message(
                        m.chat.id, '''Скорость интернета не позволяет \
                        обработать это фото''')
                    bot.send_message(
                        m.chat.id, 'Используй другое изображение.\n')
                    src_f = ''
                    src1 = ''
        else:
            bot.send_message(
                m.chat.id, '️⚠️Сначала необхожимо загрузить фото!')
    else:
        bot.send_message(m.chat.id, '🚫Доступ к ресурсу ограничен.')


@bot.message_handler(commands=["2"])
def two(m, res=False):
    global nn
    global src_f
    global src1
    global yy
    yy = 0
    userid = m.from_user.id
    ch = 1
    with open("blocked.txt", 'r') as filex:
        if str(userid) in filex.read():
            nn = True
    if not nn:
        if src_f != '':
            try:
                bot.send_message(m.chat.id, 'Пару секунд...\n')
                filen = src_f
                image = fr.load_image_file(filen)
                face_landmarks_list = fr.face_landmarks(image)
                pil_image = PIL.Image.fromarray(image)
                if len(face_landmarks_list) == 0:
                    bot.send_message(
                        m.chat.id, '''Лицо частично скрыто, что затрудняет \
                        мою работу😣''')
                    bot.send_message(
                        m.chat.id, 'Используй другое изображение.')
                else:
                    n = 0
                    for face_landmarks in face_landmarks_list:
                        face_loc = fr.face_locations(image)
                        x2, x3, x4, x1 = face_loc[n]
                        dx = x3 - x1
                        d = PIL.ImageDraw.Draw(pil_image, 'RGBA')

                        d.polygon(
                            face_landmarks['left_eyebrow'], fill=(0, 0, 0, 0))
                        d.polygon(
                            face_landmarks['right_eyebrow'], fill=(0, 0, 0, 0))
                        d.line(face_landmarks['left_eyebrow'], fill=(
                            0, 0, 0, 150), width=int(round(dx * 0.0377, 0)))
                        d.line(face_landmarks['right_eyebrow'], fill=(
                            0, 0, 0, 150), width=int(round(dx * 0.0377, 0)))

                        d.polygon(
                            face_landmarks['top_lip'], fill=(0, 0, 0, 110))
                        d.polygon(
                            face_landmarks['bottom_lip'], fill=(0, 0, 0, 110))
                        d.line(face_landmarks['top_lip'], fill=(
                            0, 0, 0, 64), width=int(round(dx * 0.043, 0)))
                        d.line(face_landmarks['bottom_lip'], fill=(
                            0, 0, 0, 64), width=int(round(dx * 0.043, 0)))

                        d.polygon(face_landmarks['left_eye'], fill=(
                            255, 255, 255, 0))
                        d.polygon(face_landmarks['right_eye'], fill=(
                            255, 255, 255, 0))
                        d.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]], fill=(
                            0, 0, 0, 110), width=int(round(dx * 0.0323, 0)))
                        d.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]], fill=(
                            0, 0, 0, 110), width=int(round(dx * 0.0323, 0)))
                        n += 1
                    pil_image.save(f'dd{src_f}')
                    photo = open(src1, 'rb')
                    bot.send_photo(m.chat.id, photo)
            except:
                bot.send_message(
                    m.chat.id, '''Скорость интернета не позволяет обработать \
                    это фото''')
                bot.send_message(m.chat.id, 'Используй другое изображение.\n')
                src_f = ''
                src1 = ''
        else:
            bot.send_message(
                m.chat.id, '️⚠️Сначала необхожимо загрузить фото!')
    else:
        bot.send_message(m.chat.id, '🚫Доступ к ресурсу ограничен.')


@bot.message_handler(commands=["3"])
def one(m, res=False):
    global nn
    global src_f
    global src1
    global yy
    userid = m.from_user.id
    with open("blocked.txt", 'r') as filex:
        if str(userid) in filex.read():
            nn = True
    if not nn:
        if src_f != '':
            filen = src_f
            sp = {}
            abc = 'абвгдеёжзийклмнопрстуюхцчшщъыьэюя12344567890'
            with open("sp.txt", "r", encoding='utf-8') as f:
                for line in f:
                    key, *value = line.split('&&&')
                    sp[key] = value
            v = 0
            try:
                image = fr.load_image_file(filen)
                face_landmarks_list = fr.face_landmarks(image)
                pil_image = PIL.Image.fromarray(image)
                if len(face_landmarks_list) == 0:
                    bot.send_message(
                        m.chat.id, '''Лицо частично скрыто, что затрудняет \
                        мою работу😣''')
                    bot.send_message(
                        m.chat.id, 'Используй другое изображение.')
                    src_f = ''
                    src1 = ''
                else:
                    time = int(round((len(sp) * 5), 0))
                    face_loc = fr.face_locations(image)
                    if len(face_loc) != 1:
                        bot.send_message(
                            m.chat.id, '''Обращаю Ваше внимание, что будет \
                            проверен только один человек с фотографии.''')
                    x1 = ['1']
                    x2 = ['2', '3', '4']
                    x3 = ['0', '5', '6', '7', '8', '9']
                    if str(time)[-1] in x1:
                        o = 'у'
                    elif str(time)[-1] in x1:
                        o = 'ы'
                    else:
                        o = ''
                    if time < 60:
                        bot.send_message(
                            m.chat.id, f"""🔍Проверяю лицо по базе, это займет \
                            примерно {time} секунд{o}...""")
                    else:
                        bot.send_message(
                            m.chat.id, f"""🔍Проверяю лицо по базе, это займет \
                            чуть больше минуты...""")
                    for k in sp.keys():
                        known_image = fr.load_image_file(str(k))
                        unknown_image = fr.load_image_file(filen)
                        biden_encoding = fr.face_encodings(known_image)[0]
                        unknown_encoding = fr.face_encodings(unknown_image)[0]
                        results = fr.compare_faces(
                            [biden_encoding], unknown_encoding)
                        n1 = sp.get(k)
                        n2 = n1[0]
                        if results == [True]:
                            bot.send_message(
                                m.chat.id, f'На фотографии {n2}\n')
                            v = 1
                            break
                    if v == 0:
                        bot.send_message(
                            m.chat.id, f"Лицо на фотографии неопознано.\n")
                        bot.send_message(
                            m.chat.id, f"""️Если хочешь добавить человека с
                            фотографии в базу нажми /yes\n""")
                        yy = 1
            except:
                bot.send_message(
                    m.chat.id, '''Скорость интернета не позволяет обработать \
                    это фото''')
                bot.send_message(m.chat.id, 'Используй другое изображение.\n')
                src_f = ''
                src1 = ''
        else:
            bot.send_message(m.chat.id, '⚠️Сначала необхожимо загрузить фото!')
    else:
        bot.send_message(m.chat.id, '🚫Доступ к ресурсу ограничен.')


@bot.message_handler(content_types=['photo'])
def ph(m):
    global yy
    global nn
    userid = m.from_user.id
    yy = 0
    with open("blocked.txt", 'r') as filex:
        if str(userid) in filex.read():
            nn = True
    if not nn:
        bot.send_message(
            m.chat.id, 'Я не умею работать с таким такими фотографиями :(\n')
        bot.send_message(m.chat.id, '📄Отправь фото в формате файла\n')
    else:
        bot.send_message(m.chat.id, '🚫Доступ к ресурсу ограничен.')


@bot.message_handler(content_types=["sticker"])
def text(message):
    global yy
    global nn
    userid = message.from_user.id
    with open("blocked.txt", 'r') as filex:
        if str(userid) in filex.read():
            nn = True
    if not nn:
        yy = 0
        bot.send_message(message.chat.id, 'Я не помимаю😕')
        bot.send_sticker(
            message.chat.id, '''CAACAgIAAxkBAAEEV2hiRvLHnJUHJUioXGozd87OVZ4dVA\
            ACQgADUomRI4PIVGMzu-RZIwQ''')
    else:
        bot.send_message(message.chat.id, '🚫Доступ к ресурсу ограничен.')


@bot.message_handler(content_types=["audio"])
def audio(m):
    global yy
    yy = 0
    bot.send_message(
        m.chat.id, '''Аудио это конечно хорошо, но я работаю только с \
        фотографиями.''')


@bot.message_handler(commands=["clear"])
def yes(m, res=False):
    global src_f, src1
    global yy
    yy = 0
    src_f = ''
    src1 = ''
    try:
        for i in range(300):
            bot.delete_message(m.chat.id, m.message_id - i)
        bot.send_message(m.chat.id, 'Сообщения успешно удалены🗑')
    except:
        bot.send_message(m.chat.id, 'Сообщения успешно удалены🗑')


@bot.message_handler(commands=["yes"])
def yes(m, res=False):
    global yn, yy, nn
    userid = m.from_user.id
    with open("blocked.txt", 'r') as filex:
        if str(userid) in filex.read():
            nn = True
    if not nn:
        if yy == 0:
            bot.send_message(m.chat.id, '⚠️Эта кнопка пока недоступна')
        else:
            yn = 1
            bot.send_message(m.chat.id, 'Ок, теперь отправь мне имя')
    else:
        bot.send_message(m.chat.id, '🚫Доступ к ресурсу ограничен.')


@bot.message_handler(content_types=["text"])
def text(message):
    global x
    global yy
    global yn
    global nn
    userid = message.from_user.id
    with open("blocked.txt", 'r') as filex:
        if str(userid) in filex.read():
            nn = True
    if not nn:
        if message.text == 'Я не умею отвечать на такие сообщения.':
            bot.delete_message(message.chat.id, message.message_id - 1)
        if yn == 1 and yy == 1:
            text = message.text
            with open('sp.txt', 'r', encoding='utf-8') as ff:
                if text in ff.read():
                    bot.send_message(
                        message.chat.id, '''Такой человек уже есть в базе. \
                        Нужно использовать другое имя.''')
                else:
                    with open('sp.txt', 'a', encoding='utf-8') as fff:
                        fff.write(f"\n{src_f}&&&{text}")
                        bot.send_message(
                            message.chat.id, '✅Человек успешно добавен в базу')
                        yn = 0
                        yy = 0
        else:
            user = message.from_user.username
            userid = message.from_user.id

            # phrase = message.text.lower().replace(" ", "")
            # def distance(a, b):
            # n, m = len(a), len(b)
            # if n > m:
            # a, b = b, a
            # n, m = m, n
            # current_row = range(n + 1)
            # for i in range(1, m + 1):
            # previous_row, current_row = current_row, [i] + [0] * n
            # for j in range(1, n + 1):
            # add, delete, change = (previous_row[j] + 1,
            #                       current_row[j - 1] + 1,
            #                       previous_row[j - 1])
            # if a[j - 1] != b[i - 1]:
            # change += 1
            # current_row[j] = min(add, delete, change)
            # return current_row[n]
            # d = {'а' : ['а', 'a', '@'],
            # 'б' : ['б', '6', 'b'],
            # 'в' : ['в', 'b', 'v'],
            # 'г' : ['г', 'r', 'g'],
            # 'д' : ['д', 'd', 'g'],
            # 'е' : ['е', 'e'],
            # 'ё' : ['ё', 'e'],
            # 'ж' : ['ж', 'zh', '*'],
            # 'з' : ['з', '3', 'z'],
            # 'и' : ['и', 'u', 'i'],
            # 'й' : ['й', 'u', 'i'],
            # 'к' : ['к', 'k', 'i{', '|{'],
            # 'л' : ['л', 'l', 'ji'],
            # 'м' : ['м', 'm'],
            # 'н' : ['н', 'h', 'n'],
            # 'о' : ['о', 'o', '0'],
            # 'п' : ['п', 'n', 'p'],
            #  'р' : ['р', 'r', 'p'],
            # 'с' : ['с', 'c', 's'],
            # 'т' : ['т', 'm', 't'],
            # 'у' : ['у', 'y', 'u'],
            # 'ф' : ['ф', 'f'],
            # 'х' : ['х', 'x', 'h' , '}{'],
            # 'ц' : ['ц', 'c', 'u,'],
            # 'ч' : ['ч', 'ch'],
            # 'ш' : ['ш', 'sh'],
            # 'щ' : ['щ', 'sch'],
            # 'ь' : ['ь', 'b'],
            # 'ы' : ['ы', 'bi'],
            # 'ъ' : ['ъ'],
            # 'э' : ['э', 'e'],
            # 'ю' : ['ю', 'io'],
            # 'я' : ['я', 'ya']}
            # for key, value in d.items():
            # for letter in value:
            # for phr in phrase:
            # if letter == phr:
            # phrase = phrase.replace(phr, key)
            # for word in words:
            # for part in range(len(phrase)):
            # fragment = phrase[part: part+len(word)]
            # if distance(fragment, word) <= len(word)*0.25:
            # x = True

            phrase = message.text.lower()
            if phrase in words:
                x = True
            if x:
                bot.delete_message(message.chat.id, message.message_id)
                with open("blocked.txt", 'a') as filex:
                    filex.write(f'\n-{userid}-')
                bot.send_message(
                    message.chat.id, '''Вы нарушили правила использывания \
                    нашего бота.''')
                bot.send_message(
                    message.chat.id, '🚫Доступ к ресурсу ограничен.')
            else:
                bot.send_message(
                    message.chat.id, 'Я не умею отвечать на такие сообщения.')
                bot.send_message(
                    message.chat.id, '''Использую команду /help для \
                    ознакомления с функционалом.''')
            x = False
    else:
        bot.send_message(message.chat.id, '🚫Доступ к ресурсу ограничен.')


@bot.message_handler(content_types=['document'])
def save_text(message):
    global src_f
    global src1
    global user
    global nn
    global yy
    yy = 0
    ss = ['jpg', 'png', 'heic', 'jpeg']
    user = message.from_user.username
    userid = message.from_user.id
    with open("blocked.txt", 'r') as filex:
        if str(userid) in filex.read():
            nn = True
    if nn is False:
        try:
            chat_id = message.chat.id
            file_info = bot.get_file(message.document.file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            src1 = 'dd' + message.document.file_name
            src_f = message.document.file_name
            filen = 'dd' + src_f
            # print(src_f)
            a1, a2 = src_f.split('.')
            if a2.lower() in ss:
                with open(src_f, 'wb') as new__file:
                    new__file.write(downloaded_file)
                with open(filen, 'wb') as new_file:
                    new_file.write(downloaded_file)
                image = fr.load_image_file(filen)
                face_landmarks_list = fr.face_landmarks(image)
                face_loc = fr.face_locations(image)
                try:
                    if len(face_loc) == 0:
                        bot.send_message(
                            message.chat.id, '''Я не вижу лиц на фото :( \
                            Возможно, они частично скрыты.''')
                        bot.send_message(
                            message.chat.id, 'Используй другое изображение.')
                        src_f = ''
                        src1 = ''
                    else:
                        bot.reply_to(message, "Фото успешно получено.")
                        bot.send_message(
                            message.chat.id, '''Выбери, что нужно сделать с \
                            фотографией. (/help)\n''')
                except:
                    bot.send_message(
                        message.chat.id, '''Скорость интернета не позволяет \
                        обработать это фото''')
                    bot.send_message(
                        message.chat.id, 'Используй другое изображение.\n')
            else:
                bot.reply_to(message, "Хм, это не фотография.")
                src_f = ''
                src1 = ''
        except:
            bot.send_message(message.chat.id, 'Я не могу найти здесь людей.\n')
            bot.send_message(
                message.chat.id, 'Используй другое изображение.\n')
            src_f = ''
            src1 = ''
    else:
        bot.send_message(
            message.chat.id, '''🚫Вы попали в черный список нашего бота. \
            Доступ к ресурсу ограничен.\n''')
        bot.send_message(
            message.chat.id, 'Связаться с администрацией: @vse_na_vseros\n')
        src_f = ''
        src1 = ''


bot.infinity_polling()
