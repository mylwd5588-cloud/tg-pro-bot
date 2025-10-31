import os
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update

# سنضع القيم الحساسة في Render كمتغيرات بيئة، وليس داخل الكود
BOT_TOKEN = os.getenv("BOT_TOKEN")        # توكن تيليجرام (سنضيفه في Render)
OPENAI_KEY = os.getenv("OPENAI_KEY")      # مفتاح OpenAI (سنضيفه في Render)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ البوت يعمل.\n"
        "استخدم:\n"
        "/macro → تقرير ماكرو (سيُضاف لاحقًا)\n"
        "/risk → إشارة السوق (سيُضاف لاحقًا)\n"
    )

async def macro(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📊 تقرير الماكرو سيُضاف بعد تشغيل البوت على Render.")

async def risk(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📈 إشارة السوق ستُضاف بعد التشغيل. جرّب أولاً /start.")

def main():
    if not BOT_TOKEN:
        raise RuntimeError("❗ BOT_TOKEN غير مضبوط (أضفه في Render → Environment).")
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("macro", macro))
    app.add_handler(CommandHandler("risk", risk))
    app.run_polling()

if __name__ == "__main__":
    main()
