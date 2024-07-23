from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import html
from keyboards.keyboards import boshmenyu, Kurslar
from states.state import BoshmenuKeyboardStates, Register
from aiogram.fsm.context import FSMContext
from loader import bot
from keyboards.keyboards import Kurslar2 , Kurslar3

router: Router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        f"Assalomu aleykum, {html.bold(message.from_user.full_name)}! Vali teach qabul botiga Xush kelibsiz!",
        reply_markup=boshmenyu
    )

@router.message(F.text.contains("Biz haqimizda ma'lumot olish"))
async def biz_haqimizda_handler(message: Message , state : FSMContext):
    await state.set_state()
    await message.answer("ValiTeach qabul boti orqali siz masofaviy tarzda ro'yxatdan o'tishingiz mumkin. ValiTeach o'quv markazi Batafsil shu yerdan topishingiz mumkin➡️: t.me/Vali_Teach_Kokand")

@router.message(F.text.contains("Demo darslari"))
async def demo_handler(message: Message):
    await message.answer("Assalomu aleykum! Demo darslari bu video darslar va mana shu link orqali➡️ https://t.me/ValiTeachDars_bot siz hohlagan kursni video darsini ko'rishingiz mumkin e'tiboringiz uchun rahmat hurmatli mijoz")

@router.message(F.text.contains("Dasturlash") , BoshmenuKeyboardStates.information)
async def dasturlash_handler(message: Message):
    await message.answer("Dasturlash — kompyuterlar va boshqa mikroprotsessorli elektron mashinalar uchun dasturlar tuzish, sinash va oʻzgartirish jarayonidan iborat. Odatda dasturlash yuqori saviyali dasturlash tillari (PHP, Java, C++, Python) vositasida amalga oshiriladi. Bu dasturlash tillarining semantikasi odam tiliga yaqinligi tufayli dastur tuzish jarayoni ancha oson kechadi.")


@router.message(F.text.contains("🔙 Orqaga"))
async def orqaga_handler(message: Message):
    await message.answer("🔙 Orqaga qaytildi", reply_markup=boshmenyu)

@router.message(F.text.contains("Kurslar haqida ma'lumot olish"))
async def kurslar_handler(message: Message, state: FSMContext):
    await state.set_state(BoshmenuKeyboardStates.information)
    await message.answer("Kurslar haqidagi ma'lumotlar", reply_markup=Kurslar)

@router.message(F.text.contains("Kursga ro'yxatdan o'tish"))
async def kursga_royxatdan_otish_handler(message: Message, state: FSMContext):
    await state.set_state(BoshmenuKeyboardStates.register)
    await message.answer("Kursni tanlang", reply_markup=Kurslar) 

@router.message(F.text == "Kompyuter savodxonligi" , BoshmenuKeyboardStates.information) 
async def kompyuter_savodxonligi_handler(message: Message):
        await message.answer("Kompyuter savodxonligi — kompyuter tizimlaridan samarali foydalanish, turli dasturlar va internet xizmatlaridan foydalanishni o'rgatadi. Kurslarimiz sizga kompyuter savodxonligini oshirishda yordam beradi.")

@router.message(F.text == " Dasturlash" , BoshmenuKeyboardStates.information)
async def dasturlash_handler(message: Message):
        await message.answer("Dasturlash kursimiz sizga PHP, Java, C++, Python kabi dasturlash tillarida chuqur bilim beradi.")

@router.message(F.text == "Grafik dizayn" , BoshmenuKeyboardStates.information)
async def grafik_dizayn_handler(message: Message):
        await message.answer("Grafik dizayn — vizual san'at va dizayn elementlarini o'z ichiga olgan kurs bo'lib, sizga logotip, plakativ va boshqa grafik materiallarni yaratishni o'rgatadi.")







malumotlari = []
@router.message(F.text == "Kompyuter savodxonligi" , BoshmenuKeyboardStates.register)
async def Kompyuter1_handler(message : Message , state : FSMContext):
     await state.set_state(Register.full_name)
     malumotlari.append("Kompyuter savodxonligi")
     await message.answer("Ro'yxatdan o'tishlik uchun Ism va Familyangizni kiriting")


@router.message(Register.full_name)
async def Fyull_name1_handler(message : Message , state : FSMContext):
     await state.set_state(Register.age)
     malumotlari.append(message.text)
     print(malumotlari)
     await message.answer("Yoshingizni kiriting")
     


@router.message(Register.age)
async def are1_handler(message : Message , state : FSMContext):
     await state.set_state(Register.phone_number)
     malumotlari.append(message.text)
     print(malumotlari)
     await message.answer("Telefon raqamingizni kiriting")




@router.message(Register.phone_number)
async def phon_number1_handler(message : Message , state : FSMContext):
     await state.set_state(Register.phone_number2)
     malumotlari.append(message.text)
     print(malumotlari)
     await message.answer("Qo'shimcha telefon raqam kiriting (agar yo'q bo'lsa \"yo'q\" deb yozib qoldiring)")



@router.message(Register.phone_number2)
async def phne_number21_handler(message : Message , state : FSMContext):
     await state.set_state(Register.week)
     malumotlari.append(message.text)
     print(malumotlari)
     await message.answer("Siz uchun maqul bo'lgan hafta kunini kiriting" , reply_markup=Kurslar2)     


@router.message(Register.week)
async def eek1_handler(message : Message , state : FSMContext):
     await state.set_state(Register.time)
     malumotlari.append(message.text)
     print(malumotlari)
     await message.answer("Siz uchun qaysi vaqt qulayroq ?" , reply_markup=Kurslar3)


@router.message(Register.time)
async def tim_handler(message : Message , state : FSMContext):
     await state.clear()
     await bot.send_message(6929399603 , f"<b>Kurs</b>:{malumotlari[0]}\n<b>F.I.SH</b>:{malumotlari[1]}\n<b>Yosh</b>:{malumotlari[2]}\n<b>Telefon raqam</b>:{malumotlari[3]}\n<b>Qo'shimcha telefon raqam</b>:{malumotlari[4]}\n<b>Borayotgan hafta kuni</b>:{malumotlari[5]}\n<b>Vaqti</b>:{message.text}")
     await message.answer("Ma'lumotlaringiz qabul qilindi.Tez orada siz bilan bog'lanamiz hurmatli mijoz" , reply_markup=boshmenyu)
     malumotlari.clear()
    







@router.message(F.text == "Dasturlash" , BoshmenuKeyboardStates.register)
async def Dasturlash2_handler(message : Message , state : FSMContext):
     await state.set_state(Register.full_name)
     malumotlari.append("Dasturlash")
     await message.answer("Ro'yxatdan o'tishlik uchun Ism va Familyangizni kiriting")


@router.message(Register.full_name)
async def ull_name2_handler(message : Message , state : FSMContext):
     await state.set_state(Register.age)
     malumotlari.append(message.text)
     print(malumotlari)
     await message.answer("Yoshingizni kiriting")
     


@router.message(Register.age)
async def ag2_handler(message : Message , state : FSMContext):
     await state.set_state(Register.phone_number)
     malumotlari.append(message.text)
     print(malumotlari)
     await message.answer("Telefon raqamingizni kiriting")




@router.message(Register.phone_number)
async def phon_number4_handler(message : Message , state : FSMContext):
     await state.set_state(Register.phone_number2)
     malumotlari.append(message.text)
     print(malumotlari)
     await message.answer("Qo'shimcha telefon raqam kiriting (agar yo'q bo'lsa \"yo'q\" deb yozib qoldiring)")



@router.message(Register.phone_number2)
async def hone_number23_handler(message : Message , state : FSMContext):
     await state.set_state(Register.week)
     malumotlari.append(message.text)
     print(malumotlari)
     await message.answer("Siz uchun maqul bo'lgan hafta kunini kiriting" , reply_markup=Kurslar2)     


@router.message(Register.week)
async def Wek2_handler(message : Message , state : FSMContext):
     await state.set_state(Register.time)
     malumotlari.append(message.text)
     print(malumotlari)
     await message.answer("Siz uchun qaysi vaqt qulayroq ?" , reply_markup=Kurslar3)


@router.message(Register.time)
async def ime2_handler(message : Message , state : FSMContext):
     await state.clear()
     malumotlari.append(message.text)
     print(malumotlari)
     await bot.send_message(6929399603 , f"<b>Kurs</b>:{malumotlari[0]}\n<b>F.I.SH</b>:{malumotlari[1]}\n<b>Yosh</b>:{malumotlari[2]}\n<b>Telefon raqam</b>:{malumotlari[3]}\n<b>Qo'shimcha telefon raqam</b>:{malumotlari[4]}\n<b>Borayotgan hafta kuni</b>:{malumotlari[5]}\n<b>Vaqti</b>:{message.text}")
     await message.answer("Ma'lumotlaringiz qabul qilindi.Tez orada siz bilan bog'lanamiz hurmatli mijoz" , reply_markup=boshmenyu)

     malumotlari.clear() 







@router.message(F.text == "Grafik dizayn" , BoshmenuKeyboardStates.register)
async def Grafik_dizayn_handler(message : Message , state : FSMContext):
     await state.set_state(Register.full_name)
     malumotlari.append("Grafik dizayn")
     await message.answer("Ro'yxatdan o'tishlik uchun Ism va Familyangizni kiriting")


@router.message(Register.full_name)
async def Ful_name3_handler(message : Message , state : FSMContext):
     await state.set_state(Register.age)
     malumotlari.append(message.text)
     print(malumotlari)
     await message.answer("Yoshingizni kiriting")
     


@router.message(Register.age)
async def ae3_handler(message : Message , state : FSMContext):
     await state.set_state(Register.phone_number)
     malumotlari.append(message.text)
     print(malumotlari)
     await message.answer("Telefon raqamingizni kiriting")




@router.message(Register.phone_number)
async def phone_numbe3_handler(message : Message , state : FSMContext):
     await state.set_state(Register.phone_number2)
     malumotlari.append(message.text)
     print(malumotlari)
     await message.answer("Qo'shimcha telefon raqam kiriting (agar yo'q bo'lsa \"yo'q\" deb yozib qoldiring)")



@router.message(Register.phone_number2)
async def phoe_number25_handler(message : Message , state : FSMContext):
     await state.set_state(Register.week)
     malumotlari.append(message.text)
     print(malumotlari)
     await message.answer("Siz uchun maqul bo'lgan hafta kunini kiriting" , reply_markup=Kurslar2)     


@router.message(Register.week)
async def Wee3_handler(message : Message , state : FSMContext):
     await state.set_state(Register.time)
     malumotlari.append(message.text)
     await message.answer("Siz uchun qaysi vaqt qulayroq ?" , reply_markup=Kurslar3)


@router.message(Register.time)
async def tile3_handler(message : Message , state : FSMContext):
     await state.clear()
     await bot.send_message(6929399603 , f"<b>Kurs</b>:{malumotlari[0]}\n<b>F.I.SH</b>:{malumotlari[1]}\n<b>Yosh</b>:{malumotlari[2]}\n<b>Telefon raqam</b>:{malumotlari[3]}\n<b>Qo'shimcha telefon raqam</b>:{malumotlari[4]}\n<b>Borayotgan hafta kuni</b>:{malumotlari[5]}\n<b>Vaqti</b>:{message.text}")
     await message.answer("Ma'lumotlaringiz qabul qilindi.Tez orada siz bilan bog'lanamiz hurmatli mijoz" , reply_markup=boshmenyu)
  
     malumotlari.clear()


    