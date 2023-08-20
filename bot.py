from time import sleep
import asyncio
import threading
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# def poty_function(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#         asyncio.run(update.message.reply_text(f'{update.effective_user.first_name}: checked poty. Will remind in 30 minutes.'))
#         sleep(5)
#         asyncio.run(update.message.reply_text(f'CHECK POTY'))

# def feed_function(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#         asyncio.run(update.message.reply_text(f'{update.effective_user.first_name}: fed. Will remind in 2 hours 15 minutes.'))
#         sleep(8100)
#         asyncio.run(update.message.reply_text(f'FEED'))

# async def poty(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#         x = threading.Thread(target=poty_function, args=(update, context,))
#         x.start()


# async def feed(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#          x = threading.Thread(target=feed_function, args=(update, context,))
#          x.start()

async def poty(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    await context.bot.send_message(chat_id=chat_id, text='Checked poty. Will remind in 30 minutes.')
    # Set the alarm:
    context.job_queue.run_once(callback_alarm, 1800, data='CHECK POTY', chat_id=chat_id)

async def feed(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    await context.bot.send_message(chat_id=chat_id, text='Fed. Will remind in 2 hours 15 minutes.')
    # Set the alarm:
    context.job_queue.run_once(callback_alarm, 1800, data='FEED', chat_id=chat_id)


async def callback_alarm(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=context.job.chat_id, text=f'{context.job.data}!')


app = ApplicationBuilder().token("<TELEGRAM_TOKEN>").build()

app.add_handler(CommandHandler("p", poty))

app.add_handler(CommandHandler("f", feed))

app.run_polling()