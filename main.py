from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import re

TOKEN = "YOUR_BOT_TOKEN"

IGNORE_USERS = {
    8572236236,
    8527260019
}

AUTO_REPLY = """💎 KY UC & DIA SHOP

🙏 မင်္ဂလာပါ 🙏

⚠️ သတိပေးချက် ⚠️

❌ GP မှာ စာမရေးပါနဲ့။

❌ Group ထဲမှာ စာရေးပြီးနောက် DM ကနေ စာလာပို့သူများသည် Owner မဟုတ်ပါ။ မယုံပါနဲ့။

💳 KPay / Wave / AYA Pay
📱 09776649597

📩 မေးချင်တာများကို Owner / Admin ကိုသာ ဆက်သွယ်ပါ။
➡️ @YENAINGSOE4007
"""

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    # Ignore specific users
    if update.effective_user.id in IGNORE_USERS:
        return

    # Ignore photos (payment receipts)
    if update.message.photo:
        return

    text = update.message.text or ""

    # Ignore PUBG ID (8-12 digits only)
    if re.fullmatch(r"\d{8,12}", text.strip()):
        return

    await update.message.reply_text(AUTO_REPLY)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(
    MessageHandler(
        filters.TEXT | filters.PHOTO,
        auto_reply
    )
)

print("Bot is running...")
app.run_polling()
