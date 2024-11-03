from telegram import InlineKeyboardButton, InlineKeyboardMarkup


async def send_employees(context, employees, chat_id, message_id=None):
    buttons = []
    for employee in employees:
        buttons.append(
            [InlineKeyboardButton(
                text=f"{employee['first_name']}",
                callback_data=f"employee_{employee['job_id']}"
            )]
        )

    buttons.append([InlineKeyboardButton(text="back", callback_data="job_back")])
    reply_markup = InlineKeyboardMarkup(inline_keyboard=buttons)

    if message_id:
        await context.bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="<b> Choose employee </b>",
            reply_markup=reply_markup,
            parse_mode="HTML"
        )

    else:
        await context.bot.send_message(
            chat_id=chat_id,
            text="<b> Choose employee  </b>",
            reply_markup=reply_markup,
            parse_mode="HTML"
        )
