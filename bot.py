from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.last_name}')


app = ApplicationBuilder().token('5595921459:AAG4GQKPf9mGXqqCKFgiS2Pow-OKG1tmBUQ').build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()