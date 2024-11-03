from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def send_regions(context, regions, chat_id, message_id=None):
    buttons = []
    for region in regions:
        buttons.append(
            [InlineKeyboardButton(
                text=f"{region["region_name"]}",
                callback_data=f"region_{region['region_id']}"
            )]
        )

    buttons.append([InlineKeyboardButton(text="close", callback_data="close")])
    reply_markup = InlineKeyboardMarkup(inline_keyboard=buttons)

    if message_id:
        await context.bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="<b> Choose region </b>",
            reply_markup=reply_markup,
            parse_mode="HTML"
        )

    else:
        await context.bot.send_message(
            chat_id=chat_id,
            text="<b> Choose region </b>",
            reply_markup=reply_markup,
            parse_mode="HTML"
        )