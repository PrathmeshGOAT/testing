from pyrogram import Client,filters
import os

app = Client(
        "wow",
        api_id=int(os.getenv("API_ID")),
        api_hash=os.getenv("API_HASH"),
        bot_token=os.getenv("BOT_TOKEN")
    )
    
@app.on_message(filters.command("start"))
async def start(client,message):
    await message.reply("working...")
    
    
print("running...")
app.run()
