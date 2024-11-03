from telegram import InlineKeyboardButton, InlineKeyboardMarkup


async def send_countries(context, countries, chat_id, message_id=None):
    buttons = []
    for country in countries:
        buttons.append(
            [InlineKeyboardButton(
                text=f"{country["country_name"]}",
                callback_data=f"country_{country['country_id']}"
            )]
        )

    buttons.append([InlineKeyboardButton(text="Back", callback_data="region_back")])
    reply_markup = InlineKeyboardMarkup(inline_keyboard=buttons)

    if message_id:
        await context.bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="<b> Choose country </b>",
            reply_markup=reply_markup,
            parse_mode="HTML"
        )

    else:
        await context.bot.send_message(
            chat_id=chat_id,
            text="<b> Choose counrtry </b>",
            reply_markup=reply_markup,
            parse_mode="HTML"
        )