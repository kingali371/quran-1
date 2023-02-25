import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("/start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡**\n
● **انا بوت تشغيل القرآن الكريم وتنزيل الفديو**\n
● **اضفني مشرف في مجموعتك لأعمل**\n
● **اتبع مايلي لمعرفه كيفيه الاستخدام**\n
● **اضغط علي ذر طريقه الاستخدام**\n
● **مميزات الروبوت يعمل بجودة فائقه**\n
**♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡**\n""",
    reply_markup=InlineKeyboardMarkup(
             [
            [
                InlineKeyboardButton("أضف لبوت لمجموعتك ✅", url=f"https://t.me/{bu}?startgroup=true"),
            ],
            [
            InlineKeyboardButton( "𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴",url=f"https://t.me/S_EG_P"),
            ],
            [
            InlineKeyboardButton("𝗗𝗲𝘃𝘀", url=f"https://t.me/CR_CR_CR"),
              ],
              [ 
                  InlineKeyboardButton(
                         " 🎧¦ جـروب الدعم ", url=f"https://t.me/{SUPPORT_GROUP}"
                ),
            ],
            [
                InlineKeyboardButton(" 💯ĎẸϋƤỖЌẸϻỖŇ💯 ", url=f"https://t.me/devpokemon"),
            ]
         ]
     )
  )

@Client.on_message(
    command(["مبرمج السورس","زين"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/59d719a842df5560af6a1.jpg",
        caption=f""" منور يا هقر """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𓂄𓆩 ĎẸϋ ƤỖЌẸϻỖŇ 𓆪𓂁", url=f"https://t.me/devpokemon"),
                ],
                [
                    InlineKeyboardButton(
                    "𓂄𓆩𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴𓆪𓂁", url=f"https://t.me/S_EG_P"
                ),
            ],
            [
                InlineKeyboardButton("أضف لبوت لمجموعتك ✅", url=f"https://t.me/{bu}?startgroup=true"),
            ]
         ]
     )
  )

@Client.on_message(command(["المطور بارلو","بارلو","الاستاذ","الاستاذ بارلو"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b6a07921973cbc554e399.jpg",
        caption=f""" ŴẸĹČỖϻẸ βÃŘĹỖ """,
        reply_markup=InlineKeyboardMarkup(
         [
            [
                InlineKeyboardButton("𓂄𓆩βÃŘĹỖ𓆪𓂁", url=f"https://t.me/bar_lo0o0"),
           ],
            [ 
                InlineKeyboardButton(
                    "𓂄𓆩𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴𓆪𓂁", url=f"https://t.me/S_EG_P"
                ),
            ],
            [
                InlineKeyboardButton("أضف لبوت لمجموعتك ✅", url=f"https://t.me/{bu}?startgroup=true"),
            ]
         ]
     )
  )

@Client.on_message(command(["سورس","ياسورس","السورس","source","يا سورس"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/b489a489ea1b536511c42.jpg",
        caption=f"""[♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡](https://t.me/S_EG_P)

 [● قـنـاة الـسـورس 🎧](https://t.me/S_EG_P)
 [● مـبـرمـج الـسـورس 👨‍✈️](https://t.me/devpokemon)
 [● مـطـوريـن السورس 👨‍💻](https://t.me/CR_CR_CR)
 [● تنصيب تليثون 👨‍💻](https://t.me/S_EG_P/3970)

[♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡](https://t.me/S_EG_P)""",
        reply_markup=InlineKeyboardMarkup(
         [
            [
                InlineKeyboardButton("𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴", url=f"https://t.me/S_EG_P"),
            ],
            [
            InlineKeyboardButton("ŻẸĮŇ", url=f"https://t.me/devpokemon"),
            ],
            [
                InlineKeyboardButton(
                        "𝗗𝗲𝘃𝘀", url=f"https://t.me/CR_CR_CR"
                ),
            ],
            [
                InlineKeyboardButton("أضف لبوت لمجموعتك ✅", url=f"https://t.me/{bu}?startgroup=true"),
            ]
         ]
     )
  )


@Client.on_message(filters.new_chat_members)
async def new_chat(c: Client, m: Message):
    chat_id = m.chat.id
    if await is_served_chat(chat_id):
        pass
    else:
        await add_served_chat(chat_id)
    ass_uname = (await user.get_me()).username
    bot_id = (await c.get_me()).id
    for member in m.new_chat_members:
        if member.id == bot_id:
            return await m.reply(
                " **شكرا لإضافتي إلى مجموعتك لتشغيل الموسيقي!**\n\n"
                " **قم بترقيتي مسؤول في المجموعة لكي أتمكن من العمل بشكل صحيح\nولا تنسى كتابة `/انضم` لدعوة الحساب المساعد\nقم بكتابة`/تحديث` لتحديث قائمة المشرفين",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🌐 ¦ الـقـنـاة ", url=f"https://t.me/{UPDATES_CHANNEL}"),
                            ],
                            [
                            InlineKeyboardButton("🎧 ¦ جـروب الدعم", url=f"https://t.me/{GROUP_SUPPORT}")
                        ],
                        [
                            InlineKeyboardButton(
                        ALIVE_NAME, url=f"https://t.me/{ass_uname}"),
                        ],
                        [
                            InlineKeyboardButton(
                        "أضف لبوت لمجموعتك ✅", url=f'https://t.me/{bu}?startgroup=true'),
                        ],
                    ]
                )
            )


chat_watcher_group = 5
