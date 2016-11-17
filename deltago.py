# HexChat w/ Python 3
"""GoN regex challenge...?"""

from datetime import datetime
import hexchat
import random
import re

__module_name__ = "DeltaGo"
__module_version__ = "2.1"
__module_description__ = "The Seed of Slackbot Go, a GoN AI developed by ShallowMind Corporation"

dt = datetime.now()

def bot_write(channel, message, su=0):
    if su == 0:
        p = "*ΔGo$* "
    elif su == 1:
        p = "*ΔGo#* "
    else:
        p = ""
    hexchat.command("PRIVMSG " + channel + " :" + p + message)

def bot_write_ex(channel, s, message, pattern):
    if re.search(pattern, s):
        bot_write(channel, message)

def bot_write_ex_su(channel, s, message, pattern):
    if re.search(pattern, s):
        bot_write(channel, message, 1)

def message_cb(word, word_eol, userdata):
    global dt

    c = word[2]
    s = " ".join(word[3:])[1:]
    if c not in ["#cs322", "#yb"]:
        return

    bot_write_ex(c, s, ":gaon:", "아이도루")
    bot_write_ex(c, s, "~이미늦었다~", "트윗덱")
    bot_write_ex(c, s, "twitter.com", "해로운 새")
    bot_write_ex(c, s, "그녀를 java요..", "var로 char서")
    bot_write_ex(c, s, "그녀를 java요..", "발로 char서")
    bot_write_ex(c, s, "그녀를 java요..", "발로 차서")
    bot_write_ex(c, s, "숨-죽이기", "인성[왕킹]")
    bot_write_ex(c, s, "안녕!", r"안녕[!\?]?")
    bot_write_ex(c, s, "좆무위키 꺼라", "좆무위키")
    bot_write_ex(c, s, "ㅎㅎㅎ", r"\bㅎㅎㅎ$")
    bot_write_ex(c, s, "해로운 새", "파랑새")
    bot_write_ex(c, s, random.choice(["~하지말아라~", "~해도된다~", "~선동과 날조~", "~선조와 날동~"]), "[트투][위이][터타]")
    bot_write_ex(c, s, random.choice(["~하지말아라~", "~해도된다~", "~선동과 날조~", "~선조와 날동~"]), "짹짹이")
    bot_write_ex(c, s, random.choice(["응", "아니"]), "마법의 소라고[둥동]")
    bot_write_ex_su(c, s, "인생리셋 포탈이 창문 너머에 존재한다.", "^[\s;]*sudo\s+reboot(\s+now)?[\s;]*$")

    if word[0].find("junsoo") != -1:
        dt2 = datetime.now()
        if (dt2 - dt).total_seconds() >= 1200:
            bot_write(c, "헤헿ㅎ")
        dt = dt2

hexchat.hook_server("PRIVMSG", message_cb)
