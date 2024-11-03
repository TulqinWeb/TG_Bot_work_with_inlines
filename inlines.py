from config import DATA_BASE
from database import Database
from send_buttons import send_regions, send_countries, send_employees, send_jobs

db = Database(DATA_BASE)


async def inline_handler(update, context):
    query = update.callback_query

    data_sp = str(query.data).split("_")
    if data_sp[0] == "region":
        if data_sp[1].isdigit():
            countries = db.get_countries_by_region(int(data_sp[1]))
            await send_countries(context=context, countries=countries, chat_id=query.message.chat_id,
                                 message_id=query.message.message_id)

        elif data_sp[1] == "back":
            regions = db.get_all_regions()
            await send_regions(context=context, regions=regions, chat_id=query.message.chat_id,
                               message_id=query.message.message_id)

    if data_sp[0] == 'job':
        if data_sp[1].isdigit():
            employees = db.get_employee_by_job(int(data_sp[1]))
            await send_employees(context=context, employees=employees, chat_id=query.message.chat_id,
                                 message_id=query.message.message_id)

        elif data_sp[1] == 'back':
            jobs = db.get_all_jobs()
            await send_jobs(context=context, jobs=jobs, chat_id=query.message.chat_id,
                            message_id=query.message.message_id)

    if data_sp[0] == "country":
        pass

    if data_sp[0] == "employee":
        pass

    if data_sp[0] == "close":
        msg = query.message.edit_text(
            text='⏱',
            reply_markup=None
        )
        await context.bot.delete_message(chat_id=query.message.chat_id, message_id=msg.message_id)
