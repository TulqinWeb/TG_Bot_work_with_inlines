from telegram.ext import ApplicationBuilder, CommandHandler,  MessageHandler, filters, CallbackQueryHandler

from config import BOT_TOKEN
from send_buttons import send_main_menu
from message_handler import message_handler
from inlines import inline_handler


async def start(update, context):
    await send_main_menu(context=context, chat_id=update.message.from_user.id)


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, message_handler))
    app.add_handler(CallbackQueryHandler(inline_handler))

    app.run_polling()


if __name__ == '__main__':
    main()
