from telegram import Update
from telegram.ext import ContextTypes
from currency import CurrencyConventer
from config import CURRENCY_API_URL

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ok, let's go!")

async def convert_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text

    try:

        _, amount_str, from_currency, _, to_currency = message.split()
        amount = float(amount_str)

        converter = CurrencyConventer(CURRENCY_API_URL)
        result = await converter.convert(amount, from_currency.upper(), to_currency.upper())

        if result is None:
            await update.message.reply_text("Sorry - we can't get the currency(( ")
        else:
            await update.message.reply_text(f"💱 {amount} {from_currency.upper()} = {result:.2f} {to_currency.upper()}")
    
    except ValueError:
        await update.message.reply_text("Wrong format!!!!")
    except Exception as e:
        print(f"[ERROR] {e}")
        await update.message.reply_text(f"ERROR 404)$")

async def rates_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    converter = CurrencyConventer(CURRENCY_API_URL)
    rates = await converter.get_all_rates("USD")

    if not rates:
        await update.message.reply_text("Can't get the actual currency")
        return

   
    important = ["EUR", "GBP", "PLN", "UAH", "JPY", "CNY", "BTC"]
    text = "Actual currency:\n\n"
    for code in important:
        rate = rates.get(code)
        if rate:
            text += f"1 USD = {rate:.2f} {code}\n"

    await update.message.reply_text(text)
