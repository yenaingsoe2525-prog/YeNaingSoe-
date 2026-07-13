# YeNaingSoe-
    Telegram bot for KY Game Shop * Python Telegram Auto Reply Bot * KY UC DIA Shop Bot
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = "YOUR_BOT_TOKEN"

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "uc" in text:
        await update.message.reply_text("💎 PUBG UC ဝယ်ယူလိုပါက Admin - @kyucdia969")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

app.run_polling()
