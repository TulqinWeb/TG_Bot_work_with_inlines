from config import DATA_BASE
from database import Database
from send_buttons import send_regions, send_jobs

db = Database(DATA_BASE)


async def message_handler(update, context):
    text = update.message.text

    if text == "Regions":
        regions = db.get_all_regions()
        await send_regions(context=context, regions=regions, chat_id = update.message.from_user.id)

    elif text == "Jobs":
        jobs = db.get_all_jobs()
        await send_jobs(context=context, jobs=jobs,chat_id= update.message.from_user.id)