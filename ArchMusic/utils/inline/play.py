import random

from pyrogram.types import InlineKeyboardButton

selection = [
    if 0 < anon <= 10:
        bar = "♪━━━━━━━━━"
    elif 10 < anon < 20:
        bar = "━♪━━━━━━━━"
    elif 20 <= anon < 30:
        bar = "━━♪━━━━━━━"
    elif 30 <= anon < 40:
        bar = "━━━♪━━━━━━"
    elif 40 <= anon < 50:
        bar = "━━━━♪━━━━━"
    elif 50 <= anon < 60:
        bar = "━━━━━♪━━━━"
    elif 60 <= anon < 70:
        bar = "━━━━━━♪━━━"
    elif 70 <= anon < 80:
        bar = "━━━━━━━♪━━"
    elif 80 <= anon < 95:
        bar = "━━━━━━━━♪━"
    else:
        bar = "━━━━━━━━━♪",
]

def time_to_sec(time: str):
    x = time.split(":")

    if len(x) == 2:
        min = int(x[0])
        sec = int(x[1])

        total_sec = (min*60) + sec
    elif len(x) == 3:
        hour = int(x[0])
        min = int(x[1])
        sec = int(x[2])

        total_sec = (hour*60*60) + (min*60) + sec

    return total_sec

def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_sec(played)
    total_sec = time_to_sec(dur)

    x, y = str(round(played_sec/total_sec,1)).split(".")
    pos = int(y)

    line = "━"
    circle = "♪"

    bar = line*(pos-1)
    bar += circle
    bar += line*(10-len(bar))

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="↻", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="‣‣", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ), 
        ],
    ]
    return buttons


def telegram_markup_timer(_, chat_id, played, dur):
    bar = random.choice(selection)
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="↻", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="‣‣", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
    ]
    return buttons

# Rest of the functions remain the same...



## Inline without Timer Bar


def stream_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="˹sᴏᴜʀᴄᴇ˼", url="https://t.me/+m4oVCt2zFhYyMTdl"
            ),
            InlineKeyboardButton(
                text="˹ᴘᴀɴᴇʟ˼",
                callback_data=f"PanelMarkup None|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="𓆩💜𓆪", url="https://t.me/+xWcg-WBN1oBjMjk1")
             InlineKeyboardButton(
                text="𓆩🖤𓆪", user_id="1777270311")
        InlineKeyboardButton(
                text="𓆩💙𓆪", url="https://youtube.com/@LofiBoyraj",
            )
        ],
    ]
    return buttons


def telegram_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["PL_B_3"],
                callback_data=f"PanelMarkup None|{chat_id}",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"], callback_data="close"
            ),
        ],
    ]
    return buttons


## Search Query Inline


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"ArchMusicPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"ArchMusicPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


## Live Stream Markup


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text="˹ʟɪᴠᴇ˼",
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="˹sᴜᴘᴘᴏʀᴛ˼", url="https://t.me/+xWcg-WBN1oBjMjk1",
            ),
            InlineKeyboardButton(
                text="˹ᴄʜᴀɴɴᴇʟ˼", url="https://t.me/+m4oVCt2zFhYyMTdl",
            ),
        ],
        [
            InlineKeyboardButton(
                text="˹ᴘʟᴀʏʟɪsᴛ˼", callback_data=f"add_playlist {videoid}",
                ),
            InlineKeyboardButton(
                text="˹ᴏᴡɴᴇʀ˼", user_id="1777270311",
            ),
        ],
        [
            InlineKeyboardButton(
                text="˹ʏᴏᴜᴛᴜʙᴇ˼", url="https://youtube.com/@LofiBoyraj",
             ),
        ],
        [
            InlineKeyboardButton(
                text="˹ᴄʟᴏsᴇ˼",
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


## Slider Query Markup


def slider_markup(
    _, videoid, user_id, query, query_type, channel, fplay
):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❮",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="❯",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons


## Cpanel Markup


def panel_markup_1(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="☆", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="◃◃",
                callback_data=f"Pages Back|0|{videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="𓆩🖤𓆪", user_id="1777270311",
            ),
            InlineKeyboardButton(
                text="▹▹",
                callback_data=f"Pages Forw|0|{videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="˹sᴜᴘᴘᴏʀᴛ˼", url="https://t.me/+xWcg-WBN1oBjMjk1"
            ),
        ],
    ]
    return buttons


def panel_markup_2(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="˹ᴍᴜᴛᴇ˼", callback_data=f"ADMIN Mute|{chat_id}"
            ),
            InlineKeyboardButton(
                text="˹ᴜɴᴍᴜᴛᴇ˼",
                callback_data=f"ADMIN Unmute|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="˹sʜᴜғғʟᴇ˼",
                callback_data=f"ADMIN Shuffle|{chat_id}",
            ),
            InlineKeyboardButton(
                text="˹ʟᴏᴏᴘ˼", callback_data=f"ADMIN Loop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="◃◃",
                callback_data=f"Pages Back|1|{videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="𓆩🖤𓆪", user_id="1777270311",
            ),
            InlineKeyboardButton(
                text="▹▹",
                callback_data=f"Pages Forw|1|{videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="˹sᴜᴘᴘᴏʀᴛ˼", url="https://t.me/+xWcg-WBN1oBjMjk1"
            ),
        ],
    ]
    return buttons


def panel_markup_3(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="˹◃◃10˼",
                callback_data=f"ADMIN 1|{chat_id}",
            ),
            InlineKeyboardButton(
                text="˹10▹▹˼",
                callback_data=f"ADMIN 2|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="˹◃◃30˼",
                callback_data=f"ADMIN 3|{chat_id}",
            ),
            InlineKeyboardButton(
                text="˹30▹▹˼",
                callback_data=f"ADMIN 4|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◃◃",
                callback_data=f"Pages Back|2|{videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="𓆩🖤𓆪", user_id="1777270311",
            ),
            InlineKeyboardButton(
                text="▹▹",
                callback_data=f"Pages Forw|2|{videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="˹sᴜᴘᴘᴏʀᴛ˼", url="https://t.me/+xWcg-WBN1oBjMjk1"
            ),
        ],
    ]
    return buttons
