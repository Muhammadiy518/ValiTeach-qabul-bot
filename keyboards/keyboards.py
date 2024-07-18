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
            KeyboardButton(text="Dasturlash"),
            KeyboardButton(text="Kompyuter savodxonligi")
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


