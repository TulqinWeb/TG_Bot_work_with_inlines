from lib2to3.fixes.fix_input import context

from telegram import ReplyKeyboardMarkup, KeyboardButton

async def send_main_menu(context,chat_id):
    buttons = [
        [KeyboardButton(text="Regions"),
         KeyboardButton(text="Jobs")]
    ]
    await context.bot.send_message(
        chat_id=chat_id,
        text="Menu:",
        reply_markup=ReplyKeyboardMarkup(buttons,resize_keyboard=True)
    )

