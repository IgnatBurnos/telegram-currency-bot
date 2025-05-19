from telegram.ext import ApplicationBuilder, CommandHandler
from telegram import BotCommand
from config import BOT_TOKEN
from handler import start_handler, convert_handler, rates_handler

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(CommandHandler("convert", convert_handler))
    app.add_handler(CommandHandler("rates", rates_handler))

    app.bot.set_my_commands([
        BotCommand("start", "Start"),
        BotCommand("convert", "Convertation: /convert 100 USD to EUR"),
        BotCommand("rates", "Actual currency to USD")
    ])

    print("Bot is working")
    app.run_polling()

if __name__ == "__main__":
    main()
