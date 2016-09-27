#!/usr/bin/env python3
"""GoN regex challenge...?"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
import hexchat
import random
import re
import time

__module_name__ = "DeltaGo"
__module_version__ = "1.0"
__module_description__ = "The Seed of Slackbot Go, a GoN AI developed by ShallowMind Corporation"

def bot_write(channel, message, su):
    if su == 1:
        p = "DeltaGo$ "
    elif su == 2:
        p = "DeltaGo# "
    else:
        p = ""
    hexchat.command("PRIVMSG " + channel + " :" + p + message)

def bot_write_ex(channel, s, message, pattern):
    if re.search(pattern, s):
        bot_write(channel, message, 1)

def bot_write_ex_su(channel, s, message, pattern):
    if re.search(pattern, s):
        bot_write(channel, message, 2)

def cafeteria_menu(cafeteria, t):
    dvs_cd = ["fclt", "east1", "emp"][cafeteria]
    html_doc = "https://www.kaist.ac.kr/_prog/fodlst/?menu_dvs_cd=050303&dvs_cd=" + dvs_cd
    soup = BeautifulSoup(urlopen(html_doc), "html.parser")
    m = soup.find(**{"class": "menuTb"}).find_all("td")[t]
    cafeteria_name = ["카이마루", "동맛골", "교수회관"][cafeteria]
    time_name = ["아침", "점심", "저녁"][t]
    bot_write("#test_for", cafeteria_name + " " + time_name, 1)
    s = m.get_text().strip().replace("\r\n", " ")
    bot_write("#test_for", s, 0)
    bot_write("#test_for", "=" * 19, 0)

def cafeteria_parse(s):
    if re.search("식단", s):
        cafeteria = 2
        cafeterias = {"북측": 0,
                      "동측": 1,
                      "카이?마루?": 0}
        for k, v in cafeterias.items():
            if re.search(k, s):
                cafeteria = v

        local_hour = time.localtime().tm_hour
        if local_hour < 11:
            t = 0
        elif local_hour < 15:
            t = 1
        else:
            t = 2
        times = {"아침": 0,
                 "점심": 1,
                 "저녁": 2,
                 "조식": 0,
                 "석식": 2}
        if re.search("저녘", s):
            bot_write("#test_for", "*저녁", 1)
            return
        if re.search("경원", s):
            bot_write("#test_for", "킹메 갓불바베큐", 1)
            return
        if re.search("홍철", s):
            bot_write("#test_for", "킹메 갓불바베큐", 1)
            return
        if re.search("[Rr]einose", s):
            bot_write("#test_for", "킹메 갓불바베큐", 1)
            return
        if re.search("실버", s):
            bot_write("#test_for", "롯데리아", 1)
            return
        if re.search("silver", s):
            bot_write("#test_for", "lotteria", 1)
            return
        for k, v in times.items():
            if re.search(k, s):
                t = v

        cafeteria_menu(cafeteria, t)

def message_cb(word, word_eol, userdata):
    c = word[2]
    s = " ".join(word[3:])[1:]

    bot_write_ex(c, s, ":gaon:", "아이도루")
    bot_write_ex(c, s, "~/.bash_logout executed /bin/bash", "^[\s;]*(sudo\s+)?exit[\s;]*$")
    bot_write_ex(c, s, "~이미늦었다~", "트윗덱")
    bot_write_ex(c, s, "Not enough root", "^reboot(\s+now)?$")
    bot_write_ex(c, s, "Not enough root", "^shutdown(\s+now)?$")
    bot_write_ex(c, s, "twitter.com", "해로운 새")
    bot_write_ex(c, s, "그녀를 java요..", "그녀를... 발로 char서...")
    bot_write_ex(c, s, "나무위키 꺼라", r"\b나무위키")
    bot_write_ex(c, s, "델타고!", r"\b이름.*[뭐뭘뭡뭥뭬]")
    bot_write_ex(c, s, "숨-죽이기", "인성[왕킹]")
    bot_write_ex(c, s, "ㅇㄲㄴ", "갓")
    bot_write_ex(c, s, "ㅇㄲㄴ", r"\b지[희히]")
    bot_write_ex(c, s, "안녕!", r"\b안녕\b")
    bot_write_ex(c, s, "응 아니야", r"\b완성")
    bot_write_ex(c, s, "이 세상 마지막 남은 갓겜.", "히오스")
    bot_write_ex(c, s, "ㅎㅎ", r"\bㅎㅎ$")
    bot_write_ex(c, s, "ㅎㅎㅎ", r"\bㅎㅎㅎ$")
    bot_write_ex(c, s, "해로운 새", "파랑새")
    bot_write_ex(c, s, random.choice(["~하지말아라~", "~해도된다~", "~선동과 날조~", "~선조와 날동~"]), "[투트]이타")
    bot_write_ex(c, s, random.choice(["~하지말아라~", "~해도된다~", "~선동과 날조~", "~선조와 날동~"]), "짹짹이")
    bot_write_ex(c, s, random.choice(["~하지말아라~", "~해도된다~", "~선동과 날조~", "~선조와 날동~"]), "트위터")
    bot_write_ex_su(c, s, "/bin/sh", r"^[\s;]*su([\s;]+\-)?[\s;]*$")
    bot_write_ex_su(c, s, "/bin/zsh", "^[\s;]*sudo\s+zsh[\s;]*$")
    bot_write_ex_su(c, s, "Zzz...", "^[\s;]*sudo\s+shutdown(\s+now)?[\s;]*$")
    bot_write_ex_su(c, s, "인생리셋 포탈이 창문 너머에 존재한다.", "^[\s;]*sudo\s+reboot(\s+now)?[\s;]*$")

    cafeteria_parse(s)

hexchat.hook_server("PRIVMSG", message_cb)
