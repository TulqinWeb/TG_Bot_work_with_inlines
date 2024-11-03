from telegram import InlineKeyboardButton, InlineKeyboardMarkup


async def send_jobs(context, jobs, chat_id, message_id=None):
    buttons = []
    for job in jobs:
        buttons.append(
            [InlineKeyboardButton(
                text=f"{job["job_title"]}",
                callback_data=f"job_{job['job_id']}"
            )]
        )

    buttons.append([InlineKeyboardButton(text="close", callback_data="close")])
    reply_markup = InlineKeyboardMarkup(inline_keyboard=buttons)

    if message_id:
        await context.bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="<b> Choose job </b>",
            reply_markup=reply_markup,
            parse_mode="HTML"
        )

    else:
        await context.bot.send_message(
            chat_id=chat_id,
            text="<b> Choose job </b>",
            reply_markup=reply_markup,
            parse_mode="HTML"
        )
