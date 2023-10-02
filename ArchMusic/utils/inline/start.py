#
# Copyright (C) 2021-2023 by ArchBots@Github, < https://github.com/ArchBots >.
#
# This file is part of < https://github.com/ArchBots/ArchMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/ArchBots/ArchMusic/blob/master/LICENSE >
#
# All rights reserved.

from typing import Union

from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from ArchMusic import app


def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="✯ᴀᴅᴅ ᴛᴏ ɢʀᴏᴜᴘ✯",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="˹ᴀᴅᴅ ᴛᴏ ᴄʜᴀɴɴᴇʟ˼",
                url=f"https://t.me/{BOT_USERNAME}?startchannel=new",
            )
        ],
        [
            InlineKeyboardButton(
                text="˹ʜᴇʟᴩ & ᴄᴏᴍᴍᴀɴᴅs˼",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="˹sᴇᴛᴛɪɴɢs˼", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="˹ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴜʜ ɢʀᴏᴜᴘ˼",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="˹ᴀᴅᴅ ᴛᴏ ᴄʜᴀɴɴᴇʟ˼",
                url=f"https://t.me/{BOT_USERNAME}?startchannel=new",
            )
        ],
        [
            InlineKeyboardButton(
                text="˹ʜᴇʟᴩ & ᴄᴏᴍᴍᴀɴᴅs˼", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="💙", url="https://t.me/+m4oVCt2zFhYyMTdl"),
            InlineKeyboardButton(
                text="💚", url="https://t.me/+xWcg-WBN1oBjMjk1"),
            InlineKeyboardButton(
                text="𓆩🖤𓆪", user_id="1777270311"),
            InlineKeyboardButton(
                text="💛", url="https://t.me/+8YcptfHoxgY2NThl"),
            InlineKeyboardButton(
                text="💜", url="https://youtube.com/@LofiBoyraj"
            ),
        ],
     ]
    return buttons
