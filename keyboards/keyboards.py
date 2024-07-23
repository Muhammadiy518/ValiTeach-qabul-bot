from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


boshmenyu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kursga ro'yxatdan o'tish"),
            KeyboardButton(text="Kurslar haqida ma'lumot olish"),
         
        ],
        [
            KeyboardButton(text="Biz haqimizda ma'lumot olish"),
            KeyboardButton(text="Demo darslari")
        ]

    ],
    resize_keyboard=True
)



Kurslar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kompyuter savodxonligi"),
            KeyboardButton(text="Dasturlash")
        ],
        [
            KeyboardButton(text="Grafik dizayn")
        ],
        [

            KeyboardButton(text="🔙 Orqaga")
        ]
    ],
    resize_keyboard=True
)




Kurslar2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="D.Ch.j "),
            KeyboardButton(text="S.P.Sh ")
        ]
    ],
    resize_keyboard=True
)



Kurslar3 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Abetdan oldingi darslar"),
            KeyboardButton(text="Abetdan keyingi darslar"),
        ],
    ],
    resize_keyboard=True
)


