import asyncio
from pyrogram import Client
from helpers.filters import command
from config import SUDO_USERS, BOT_NAME as bn, BOT_USERNAME as lel, PMPERMIT, OWNER_USERNAME
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from callsmusic import client as USER

PMSET =True
pchats = []

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    if PMPERMIT == "ENABLE":
        if PMSET:
            chat_id = message.chat.id
            if chat_id in pchats:
                return
            await USER.send_message(
                message.chat.id,
                f"يحب {message.from_user.mention()},\nᴛʜɪs ɪs [{bn}](t.me/{lel}) انا حساب مساعد.\n\nمتبعتش رسايل كتير هنا كلم مطور البوت  [𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴](t.me/S_EG_P).\n",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " 🐥 ¦ ΒỖŤ ", url=f"https://t.me/{lel}"
                    ),
                    InlineKeyboardButton(
                        " 🦦 ¦ جـروب الدعم ", url="https://t.me/{SUPPORT_GROUP}"
                    )
                ],[ 
                    InlineKeyboardButton(
                        " 𓂄𓆩أَلا بِذِكرِ اللَّهِ تَطمَئِنُّ القُلوبُ𓆪𓂁 ", url=f"https://t.me/AzkarMusIim")
                    )]
            ]
        ),

    )
            return


@Client.on_message(filters.command(["الحماية", "pmpermit"]))
async def bye(client: Client, message: Message):
    if message.from_user.id in SUDO_USERS:
        global PMSET
        text = message.text.split(" ", 1)
        queryy = text[1]
        if queryy == "تشغيل":
            PMSET = True
            await message.reply_text("**✅ تم تفعيل الحماية...**")
            return
        if queryy == "تعطيل":
            PMSET = None
            await message.reply_text("**❎ تم تعطيل الحماية...**")
            return

@USER.on_message(filters.text & filters.private & filters.me)        
async def autopmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("**✅ تم قبوله بسبب ارسالك رساله...**")
        return
    message.continue_propagation()    
    
@USER.on_message(filters.command("س", ["!", ".", ""]) & filters.me & filters.private)
async def pmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("**✅ تم قبوله...**")
        return
    message.continue_propagation()    
    

@USER.on_message(filters.command("ر", ["!", ".", ""]) & filters.me & filters.private)
async def rmpmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id in pchats:
        pchats.remove(chat_id)
        await message.reply_text("**❎ تم رفضه...**")
        return
    message.continue_propagation()
