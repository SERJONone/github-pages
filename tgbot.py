from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import hashlib

TOKEN = "8122511731:AAEbsjayDGv05Y_QUgyJ_gi1XOjHDGKKC8w"  # Tokenni to'g'ri kiriting

# Pastda doimiy menyu uchun tugmalar
reply_keyboard = [
    ["/help", "/hash"],
    ["/dork", "/linux"],
    ["/tools"]
]
markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)

# /start komandasi
async def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    username = user.username if user.username else user.first_name
    
    await update.message.reply_text(
        f"👋 Salom @{username}! Xush kelibsiz!\n\n",
        reply_markup=markup  # Pastdagi menyuni qo'shish
    )

# /help komandasi
async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "⚡ Mavjud buyruqlar:\n"
        "/hash - Matnni hash qilish (MD5, SHA256)\n"
        "/dork - Google Dorking bo'yicha qo'llanma\n"
        "/linux - Linux komandalar ro'yxati\n"
        "/tools - Pentesting vositalari\n"
        "❓ Savollar uchun: @Serjan_BSY"
    )

# /hash komandasi (MD5, SHA256 hashing)
async def hash_text(update: Update, context: CallbackContext):
    if not context.args:
        await update.message.reply_text("⚠️ Iltimos, hash qilish uchun matn yuboring!\nMisol: `/hash hello`")
        return
    
    text = " ".join(context.args)
    md5_hash = hashlib.md5(text.encode()).hexdigest()
    sha256_hash = hashlib.sha256(text.encode()).hexdigest()

    await update.message.reply_text(
        f"🔐 **Hash natijalari:**\n"
        f"🔹 **MD5:** `{md5_hash}`\n"
        f"🔹 **SHA256:** `{sha256_hash}`"
    )

# /dork komandasi
async def dork_info(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "🔍 **Google Dorking** - maxsus qidiruv usuli.\n"
        "Misollar:\n"
        "`site:example.com` - faqat example.com saytidan ma'lumot qidirish\n"
        "`intitle:\"admin login\"` - sarlavhada 'admin login' bor sahifalarni qidirish\n"
        "`filetype:pdf site:edu` - .pdf fayllarni universitet saytlarida qidirish\n"
        "⚠️ Ishlatishda ehtiyot bo'ling!"
    )

# /linux komandasi
async def linux_commands(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "💻 **Linux buyruqlari**:\n"
        "`ls` - Fayllarni ko'rish\n"
        "`pwd` - Joriy katalogni ko'rish\n"
        "`cd` - Katalogni o'zgartirish\n"
        "`mkdir` - Yangi papka yaratish\n"
        "`rm -rf` - Fayl yoki papkani o'chirish\n"
        "⚠️ Foydalanishda ehtiyot bo'ling!"
    )

# /tools komandasi
async def pentesting_tools(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "🛠 **Pentesting vositalari**:\n"
        "🔹 **Nmap** - tarmoqni skanerlash\n"
        "🔹 **Metasploit** - eksploit vositasi\n"
        "🔹 **Burp Suite** - veb hujumlar uchun\n"
        "🔹 **Wireshark** - tarmoq trafikini tahlil qilish\n"
        "🔹 **John the Ripper** - parol kreking vositasi\n"
        "Ko'proq: https://tools.kali.org/"
    )

# Botni ishga tushirish
app = Application.builder().token(TOKEN).build()

# Buyruqlarni botga qo'shish
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("hash", hash_text))
app.add_handler(CommandHandler("dork", dork_info))
app.add_handler(CommandHandler("linux", linux_commands))
app.add_handler(CommandHandler("tools", pentesting_tools))

# Botni ishga tushirish
print("🤖 Bot ishga tushdi...")
app.run_polling()
