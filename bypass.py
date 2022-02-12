# -*- coding: utf-8 -*-
# ʜᴀʀɢᴀɪ ᴋᴀʀʏᴀ ᴏʀᴀɴɢ ʏᴏ
# ʙʏ : sᴀᴍᴜᴅʀᴀ
# ᴛᴇᴀᴍ sᴀᴍᴜᴅʀᴀ___ʙᴏᴛs
# ᴀsʟɪ ᴅᴀʀɪ ʟᴏᴍʙᴏᴋ
from Naked.toolshed.shell import execute_js
from SamudraBots import *
from BangSamudra.ttypes import Message
from BangSamudra.ttypes import ContentType as Type
from BangSamudra.ttypes import TalkException
from multiprocessing import Pool, Process
from datetime import datetime, timedelta
from time import sleep
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, html5lib, traceback, atexit
import urllib, urllib3
from humanfriendly import format_timespan, format_size, format_number, format_length
from urllib.parse import urlencode
import requests.packages.urllib3.exceptions as urllib3_exceptions
from thrift import transport, protocol, server
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol, server
from threading import Thread
from multiprocessing import Pool, Process
from time import sleep
from bs4 import BeautifulSoup
from random import randint
from Naked.toolshed.shell import execute_js
from urllib.parse import urlencode
#==============<SAMUDRABOTS>===================================================================#
from random import randint
botStart = time.time()
print("""\033["""+str(randint(0,1))+""";"""+str(randint(31,36))+"""mBOT Samudrabot\nBy Samudra\033[0m""")
samudra = LINE("samudrantb@gmail.com","keder12345",appName ="DESKTOPWIN\t7.3.1\tWindows\t10")
samudra.log("Auth Token : " + str(samudra.authToken))
print ("❚❚█ʟoԍιɴ suκsᴇs ᴅᴀʀι sᴀмuᴅʀᴀ__ʙoтs█❚❚")
print ("   ____________________")
print ("▕╮╭┻┻╮╭┻┻╮╭▕╮╲")
print ("▕╯┃╭╮┃┃╭╮┃╰▕╯╭▏")
print ("▕╭┻┻┻┛┗┻┻┛   ▕  ╰▏")
print ("▕╰━━━┓┈┈┈╭╮▕╭╮▏")
print ("▕╭╮╰┳┳┳┳╯╰╯▕╰╯▏")
print ("▕╰╯┈┗┛┗┛┈╭╮▕╮┈▏")
print ("▕__________________▕")
print (" ☠↘sᴀмuᴅʀᴀ__ʙoтs↙☠")
print ("☾тᴇᴀм sᴀмuᴅʀᴀ___ʙoтs☽")
print ("cʀᴇᴀтoʀ sᴀмuᴅʀᴀ__ʙoтs☛ʙʏ : sᴀмuᴅʀᴀ")
print ("❚❚█ʟoԍιɴ suκsᴇs ᴅᴀʀι sᴀмuᴅʀᴀ__ʙoтs█❚❚")

oepoll = OEPoll(samudra)
creator = ["uc28284eca396bd65511797a2ce6d6167","ud9e93f564195bf069e43b9801d8af3a5"]
owner = ["uc28284eca396bd65511797a2ce6d6167","ud9e93f564195bf069e43b9801d8af3a5"]
admin = ["uc28284eca396bd65511797a2ce6d6167","ud9e93f564195bf069e43b9801d8af3a5"]
staff = ["uc28284eca396bd65511797a2ce6d6167","ud9e93f564195bf069e43b9801d8af3a5"]

samudraMID = samudra.getProfile().mid
samudra = samudra
samudraProfile = samudra.getProfile()
mid = samudra.getProfile().mid
Keder = [samudra]
botlist = [samudra]
Bots = [mid]
SAMUDRABOTS = admin + staff + owner
samudraMID = samudra.profile.mid
samudraSettings = samudra.getSettings()
responsename = samudra.getProfile().displayName

proName = []
pro_name = []
protectjoin = []
proLink = []
proKick = []
proCancel = []
proInvite = []
ghostJs = []
unsendchat = {}
protectantijs = []
groupName = {}
groupImage = {}
wbanlist = []
welcome = []
msg_dict = {}
msg_dict1 = {}
settings = {
    "Picture":False,
    "videoProfile":False,
    "displayName":False,
    "coverId":False,
    "myProfile":False,
    "pictureStatus":False,
    "picture":False,
    "group":{},
    "changeCover":False,
    "changeVideo":False,
    "groupPicture":False,
    "changePicture":False,
    "autoJoinTicket":False,
    "userMention":{},
    "autoJoin": True,
    "mimic": {},
    "target": {},
    "timeRestart": {},
    "server": {},
    "simiSimi":{},
    "rnameComand": {},
    "rname":{},
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}

SamColi = {
    "Limit": 1,
    "owner":{},
    "admin":{},
    "myProfile":{},
    "coverId":{},
    "keyCommand": "",
    "setKey": False,
    "undang":False,
    "changevid":False,
    "addadmin":False,
    "delladmin":False,
    "staff":{},
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "autoCancel": {
        "members": 1,
        "on": True
    },
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":False,
    "Js":True,
    "protect":True,
    "Kick":True,
    "Cancel":True,
    "Link":True,
    "contact":False,
    "invite":False,
    'autoJoin':True,
    'autoAdd':False,
    'autoBlock':False,
    'Timeline':False,
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":False,
    "mentionKick":False,
    "welcomeOn":False,
    "stickerOn":False,
    "likeOn":True,
    "chatbot": True,
    "tagall": "halo",
    "kikuk": "cubit",
    "cekUnsend": False,
    "limitinvite": False,
    "limitkick": False,
    "limitcancel": False,
    "AddstickerWelcome":{
        "sid": "",
        "spkg": "",
        "status":False
    },
    "AddstickerLeave":{
        "sid": "",
        "spkg": "",
        "status":False
    },
    "AddstickerSider":{
        "sid": "",
        "spkg": "",
        "status":False
    },
    "AddstickerTag":{
        "sid": "",
        "spkg": "",
        "status":False
    },
    "Addsticker":{
            "name": "",
            "status":False
            },
    "stk":{},
    "selfbot":True,
    "Images":{},
    "Img":{},
    "Addimage":{
            "name": "",
            "status":False
            },
    "Videos":{},
    "Addaudio":{
            "name": "",
            "status":False
            },
    "Addvideo":{
            "name": "",
            "status":False
            },
    "unsend":False,
    "mention":"ʜᴇᴍ ɴɢɪɴᴛɪᴘ ʙᴇʙ",
    "Respontag":"\nTag terus ampe crot",   
    "welcome":"sᴇᴍᴏɢᴀ ʙᴇᴛah",
    "Leave":"sᴇʟᴀᴍᴀᴛ tinggal",
    "comment":"╭───────────────\n│╭──────────────\n│├• ᴛᴇʀɪᴍᴀᴋᴀsɪʜ\n│├• sᴀмuᴅʀᴀ \n│╰──────────────\n├──•〔 ᴏ ᴘ ᴇ ɴ ʀ ᴇ ɴ ᴛ ᴀ ʟ 〕\n│╭──────────────\n│├─•  sᴇʟғʙᴏᴛ :\n││( 𝟏 )• ғᴜʟʟ ᴛᴇᴍᴘʟᴀᴛᴇ\n││( 𝟐 )• ɴᴏ ᴛᴇᴍᴘʟᴀᴛᴇ\n│├─•  ᴘʀᴏᴛᴇᴄᴛ / ᴡᴀʀ :\n││( 𝟏 )• 𝟑 ᴀssɪsᴛ\n││( 𝟐 )• 𝟓 ᴀssɪsᴛ\n││( 𝟑 )• 𝟕 ᴀssɪsᴛ\n││( 𝟒 )• ᴄʟɪᴇɴᴛ ᴘʀᴏᴛᴇᴄᴛ\n│╰──────────────\n├──•〔 sᴇʟʟ   ᴛʜᴇ   sᴄʀɪᴘᴛ 〕\n│╭──────────────\n││( 𝟏 )• ʜᴇʟᴘᴇʀs\n││( 𝟐 )• sʙ ᴡᴀʀ\n││( 𝟑 )• sʙ ᴘʀᴏᴛᴇᴄᴛ\n││( 𝟒 )• ᴄʟ/ᴄʟɪᴇɴᴛ\n││( 𝟓 )• sʙ ғᴜʟʟ ᴛᴇᴍᴘʟᴀᴛᴇ\n│╰──────────────\n│ ན ᴄʀ : line://ti/p/~samudrabots.py\n│ ན ᴄʀ : line://ti/p/~pembantairoom112\n╰───────────────",
    "message":"╭───────────────\n│╭──────────────\n│├• ᴛʜᴀɴᴋᴢ ғᴏʀᴅ ᴀᴅᴅ ᴍᴇ\n│├• sᴀмuᴅʀᴀ \n│╰──────────────\n├──•〔 ᴏ ᴘ ᴇ ɴ ʀ ᴇ ɴ ᴛ ᴀ ʟ 〕\n│╭──────────────\n│├─•  sᴇʟғʙᴏᴛ :\n││( 𝟏 )• ғᴜʟʟ ᴛᴇᴍᴘʟᴀᴛᴇ\n││( 𝟐 )• ɴᴏ ᴛᴇᴍᴘʟᴀᴛᴇ\n│├─•  ᴘʀᴏᴛᴇᴄᴛ / ᴡᴀʀ :\n││( 𝟏 )• 𝟑 ᴀssɪsᴛ\n││( 𝟐 )• 𝟓 ᴀssɪsᴛ\n││( 𝟑 )• 𝟕 ᴀssɪsᴛ\n││( 𝟒 )• ᴄʟɪᴇɴᴛ ᴘʀᴏᴛᴇᴄᴛ\n│╰──────────────\n├──•〔 sᴇʟʟ   ᴛʜᴇ   sᴄʀɪᴘᴛ 〕\n│╭──────────────\n││( 𝟏 )• ʜᴇʟᴘᴇʀs\n││( 𝟐 )• sʙ ᴡᴀʀ\n││( 𝟑 )• sʙ ᴘʀᴏᴛᴇᴄᴛ\n││( 𝟒 )• ᴄʟ/ᴄʟɪᴇɴᴛ\n││( 𝟓 )• sʙ ғᴜʟʟ ᴛᴇᴍᴘʟᴀᴛᴇ\n│╰──────────────\n│ ན ᴄʀ : line://ti/p/~samudrabots.py\n│ ན ᴄʀ : line://ti/p/~pembantairoom112\n╰───────────────",
}

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('staff.json', 'r') as fp:
    staff = json.load(fp)

Setbot = codecs.open("setting.json","r","utf-8")
imagesOpen = codecs.open("image.json","r","utf-8")
videosOpen = codecs.open("video.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
audiosOpen = codecs.open("audio.json","r","utf-8")
Setmain = json.load(Setbot)
images = json.load(imagesOpen)
videos = json.load(videosOpen)
stickers = json.load(stickersOpen)
audios = json.load(audiosOpen)

mulai = time.time()

def removeCmd(cmd, text):
	key = SamColi["keyCommand"]
	if SamColi["setKey"] == False: key = ''
	rmv = len(key + cmd) + 1
	return text[rmv:]  


def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
   
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = samudra.genOBSParams({'oid': samudraMID, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = samudra.server.postContent('{}/talk/vp/upload.nhn'.format(str(samudra.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        samudra.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))

def Musik(to,msgf):
    contentMetadata={'previewUrl': "http://dl.profile.line-cdn.net/"+samudra.getContact(msgf).picturePath, 'i-installUrl': 'http://itunes.apple.com/app/linemusic/id966142320', 'type': 'mt', 'subText': samudra.getContact(msgf).statusMessage if samudra.getContact(msgf).statusMessage != '' else 'creator By Samudra |ID LINE|\samudrabots.py', 'a-installUrl': 'market://details?id=jp.linecorp.linemusic.android', 'a-packageName': 'jp.linecorp.linemusic.android', 'countryCode': 'JP', 'a-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'i-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'text': samudra.getContact(msgf).displayName, 'id': 'mt000000000d69e2db', 'linkUri': 'https://music.me.me/launch?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1','MSG_SENDER_ICON': "https://os.me.naver.jp/os/p/"+msgf,'MSG_SENDER_NAME':  samudra.getContact(msgf).displayName,}
    return samudra.sendMessage(to, samudra.getContact(msgf).displayName, contentMetadata, 19)

def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = samudra.genOBSParams({'oid': samudraMID, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = samudra.server.postContent('{}/talk/vp/upload.nhn'.format(str(samudra.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "update profile failed"
        samudra.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))
 
def changeProfileVideo(to):
    if Setmain['changeProfileVideo']['picture'] == None:
        return samudra.sendMessage(to, "Foto tidak ditemukan")
    elif Setmain['changeProfileVideo']['video'] == None:
        return samudra.sendMessage(to, "Video tidak ditemukan")
    else:
        path = Setmaim['changeProfileVideo']['video']
        files = {'file': open(path, 'rb')}
        obs_params = samudra.genOBSParams({'oid': samudra.getProfile().mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = samudra.server.postContent('{}/talk/vp/upload.nhn'.format(str(samudra.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return samudra.sendMessage(to, "Gagal update profile")
        path_p = Setmain['changeProfileVideo']['picture']
        Setmain['changeProfileVideo']['status'] = False
        samudra.updateProfilePicture(path_p, 'vp')

def changetest(vids, picts):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = samudra.genOBSParams({'oid': samudraMID, 'type': 'video', 'ver': '2.0', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = samudra.server.postContent('{}/talk/vp/upload.nhn'.format(str(samudra.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return samudra.sendMessage(to, "Error")
        picture = picts
        samudra.updateProfilePicture(picture, 'vp')
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))
           
def mentionMembers(to, mid):
    try:
        arrData = ""
        ginfo = samudra.getGroup(to)
        textx = "「 Mentions Members 」\n\n1. "
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "{}. ".format(str(no))
            else:
                textx += "\n「 Mentions {} Member 」".format(str(len(mid)))
        samudra.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        samudra.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "Haii ".format(str(mid))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+settings["mention"]#+"\n "+str(ginfo.name)+"\nSamudra__bots"
            if no < len(mid):
                no += 1
                textx += " " % (num)
                num=(num+1)
            else:
                try:
                    no += "╚══[ {} ]".format(str(samudra.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        samudra.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        samudra.sendMessage(to, "[ INFO ] Error :\n" + str(error))
          
def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Eh ada ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+SamColi["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(samudra.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        samudra.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        samudra.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Hallo ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = samudra.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+SamColi["welcome"]+" Di "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(samudra.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        samudra.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        samudra.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "Selamat tinggal ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = samudra.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["leave"]
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(samudra.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        samudra.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        samudra.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        samudra.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        samudra.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendImage(to, path, name="image"):
    try:
        if setttings["server"] == "VPS":
            samudra.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)
                
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                samudra.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]
            
def command(text):
    pesan = text.lower()
    if Setmain["setKey"] == True:
        if pesan.startswith(Setmain["keyComand"]):
            cmd = pesan.replace(Setmain["keyComand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
    
def removeCmd(cmd, text):
	key = settings["keyCommand"]
	if settings["setKey"] == False: key = ''
	rmv = len(key + cmd) + 1
	return text[rmv:]
    
def removeCmd(cmd, text):
	key = Setmain["rnameComand"]
	if Setmain["rname"] == False: key = ''
	rmv = len(key + cmd) + 1
	return text[rmv:]
	
def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

#message.createdTime -> 00:00:00
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

#delete log if pass more than 24 hours
def delete_log1():
    ndt = datetime.now()
    for data in msg_dict1:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict1[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict1[msg_id]

def atend1():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict1, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")

#message.createdTime -> 00:00:00
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

#delete log if pass more than 24 hours
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
    
def lockqr(grup):
    G = samudra.getGroup(grup)
    G.preventedJoinByTicket = True
    try:
        samudra.updateGroup(G)
    except:
        pass

def lockqr1(grup):
    G = random.choice(Keder).getGroup(grup)
    G.preventedJoinByTicket = True
    try:
        samudra.updateGroup(G)
    except:
        pass

def black(target):
    if target not in SamColi["blacklist"]:
        SamColi["blacklist"][target] = True

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
            
#==================[PROTECT QR]===================        
        if op.type == 25 or op.type == 26:
          if SamColi['undang'] == True:
            msg = op.message
            user = msg._from
            kirim = msg.to    	
            if msg.contentType == 13:
                #if SamColi["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = cl.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            samudra.sendMessage(msg.to, _name + " Sudah hadir dalam grup")
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                samudra.findAndAddContactsByMid(target)
                                samudra.inviteIntoGroup(kirim,[target])
                                samudra.samudra(msg.to,"undang " + _name + "\nSUCCESS..")
                                SamColi['undang'] = False
                                break
                            except:             
                                 samudra.sendMessage(msg.to, 'Sukse Bos')
                                 SamColi['undang'] = False
                                 break

        if op.type == 11:
            if op.param1 in proLink:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == True:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            samudra.reissueGroupTicket(op.param1)
                            X = samudra.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            samudra.updateGroup(X)
                            samudra.kickoutFromGroup(op.param1,[op.param2])
                            samudra.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                except:
                    pass
#==================[BLACKLIST QR]=================== 
        if op.type == 11:
            if op.param2 in SamColi["blacklist"]:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    t = Thread(target=attck, args=(op.param1, op.param2))
                    t.start()
                    t1 = Thread(target=lockqr, args=(op.param1,))
                    t1.start()
                    t2 = Thread(target=lockqr1, args=(op.param1,))
                    t2.start()
            if op.param3 in SamColi["blacklist"]:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    t3 = Thread(target=attck, args=(op.param1, op.param2))
                    t3.start()
                    t4 = Thread(target=lockqr, args=(op.param1,))
                    t4.start() 
                    t5 = Thread(target=lockqr1, args=(op.param1,))
                    t5.start()
            if op.param1 in SamColi["blacklist"]:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    t6 = Thread(target=attck, args=(op.param1, op.param2))
                    t6.start()
                    t7 = Thread(target=lockqr, args=(op.param1,))
                    t7.start() 
                    t8 = Thread(target=lockqr1, args=(op.param1,))
                    t8.start()  
#==================[AUTO JOIN CANCELL]===================                                



        if op.type == 13:
            if mid in op.param3:
                if SamColi["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        samudra.acceptGroupInvitation(op.param1)
                    else:
                        samudra.acceptGroupInvitation(op.param1)

            if op.param2 in SamColi["blacklist"]:
                if op.param2 not in Bots:
                    t9 = Thread(target=attck, args=(op.param1, op.param2))
                    t9.start()
                    t10 = Thread(target=cancl, args=(op.param1, op.param3))
                    t10.start()
                    t11 = Thread(target=black, args=(op.param2,))
                    t11.start()
            if op.param3 in SamColi["blacklist"]:
                if op.param2 not in Bots:
                    t12 = Thread(target=attck, args=(op.param1, op.param2))
                    t12.start()
                    t13 = Thread(target=cancl, args=(op.param1, op.param3))
                    t13.start()
                    t14 = Thread(target=black, args=(op.param2,))
                    t14.start()                  #  t14.start()
#==================[AUTO LEAVE]===================                                
            if mid in op.param3:
                if SamColi["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        samudra.acceptGroupInvitation(op.param1)
                        ginfo = samudra.getGroup(op.param1)
                        samudra.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        samudra.leaveGroup(op.param1)
                    else:
                        samudra.acceptGroupInvitation(op.param1)
                        ginfo = samudra.getGroup(op.param1)
                        #samudra.sendMessage(op.param1," " + str(ginfo.name))
#==================[PROTECT INVITE]===================                                
        if op.type == 13:
            if op.param1 in proInvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = samudra.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            samudra.cancelGroupInvitation(op.param1,[op.param3])
                            samudra.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
#==================[WELCOME & LEAVE]===================                                
        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = samudra.getGroup(op.param1)
                contact = samudra.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                samudra.sendImageWithURL(op.param1, image)

        if op.type == 15:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = samudra.getGroup(op.param1)
                contact = samudra.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                leaveMembers(op.param1, [op.param2])
                samudra.sendImageWithURL(op.param1, image)
#==================[BLACKLIST JOIN PURGE]===================    
        if op.type == 17: #JOIN
            if op.param2 in SamColi["blacklist"]:
                t15 = Thread(target=attck, args=(op.param1, op.param2))
                t15.start()
                t16 = Thread(target=attck, args=(op.param1, op.param2))
                t16.start()
            if op.param1 in SamColi["blacklist"]:
                t17 = Thread(target=attck, args=(op.param1, op.param2))
                t17.start()
                t18 = Thread(target=attck, args=(op.param1, op.param2))
                t18.start()
#==================[PROTECT JOIN]===================                                                            
        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    SamColi["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in SamColi["blacklist"]:
                        	random.choice(Keder).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in SamColi["blacklist"]:
                                random.choice(Keder).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in SamColi["blacklist"]:
                                    random.choice(Keder).kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in SamColi["blacklist"]:
                                        random.choice(Keder).kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    pass
                return
#=============================================                                                            
        if op.type == 0:
            return
        if op.type == 5:
              if SamColi["autoAdd"] == True:
                  samudra.findAndAddContactsByMid(op.param1)
                  sendMention(op.param1, op.param1, "Hai broo ", ", ")
                  samudra.sendMessage(op.param1, SamColi["message"])

        if op.type == 5:
            print ("[ 5 ] NOTIFIED AUTO BLOCK CONTACT")
            if SamColi["autoBlock"] == False:
                samudra.blockContact(op.param1)
                samudra.sendMessage(op.param1,"╭───────────────\n│╭──────────────\n│├• ᴛᴇʀɪᴍᴀᴋᴀsɪʜ\n│├• sᴀмuᴅʀᴀ\n│╰──────────────\n├──•〔 ᴏ ᴘ ᴇ ɴ ʀ ᴇ ɴ ᴛ ᴀ ʟ 〕\n│╭──────────────\n│├─•  sᴇʟғʙᴏᴛ :\n││( 𝟏 )• ғᴜʟʟ ᴛᴇᴍᴘʟᴀᴛᴇ\n││( 𝟐 )• ɴᴏ ᴛᴇᴍᴘʟᴀᴛᴇ\n│├─•  ᴘʀᴏᴛᴇᴄᴛ / ᴡᴀʀ :\n││( 𝟏 )• 𝟑 ᴀssɪsᴛ\n││( 𝟐 )• 𝟓 ᴀssɪsᴛ\n││( 𝟑 )• 𝟕 ᴀssɪsᴛ\n││( ?? )• ᴄʟɪᴇɴᴛ ᴘʀᴏᴛᴇᴄᴛ\n│╰──────────────\n├──•〔 sᴇʟʟ   ᴛʜᴇ   sᴄʀɪᴘᴛ 〕\n│╭──────────────\n││( 𝟏 )• ʜᴇʟᴘᴇʀs\n││( 𝟐 )• sʙ ᴡᴀʀ\n││( 𝟑 )• sʙ ᴘʀᴏᴛᴇᴄᴛ\n││( 𝟒 )• ᴄʟ/ᴄʟɪᴇɴᴛ\n││( 𝟓 )• sʙ ғᴜʟʟ ᴛᴇᴍᴘʟᴀᴛᴇ\n│╰──────────────\n│ ན ᴄʀ : line://ti/p/~samudrabots.py\n│ ན ᴄʀ : line://ti/p/~samudrabots.py\n╰───────────────")

        if op.type == 65:
            if SamColi["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = samudra.getGroup(at)
                                MudraPekok = samudra.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "╭─「 Gambar Dihapus 」\n│ Pengirim : "
                                ret_ = "│ Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n│ Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(MudraPekok.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':MudraPekok.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                samudra.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                samudra.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = samudra.getGroup(at)
                                ryan = samudra.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "╭─「 Pesan Dihapus 」\n"
                                ret_ += "│ Pengirim : {}".format(str(ryan.displayName))
                                ret_ += "\n│ Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n│ Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n│ Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                ret_ += "\n╰───────────"
                                samudra.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if SamColi["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = samudra.getGroup(at)
                                MudraPekok = samudra.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "╭─「 Sticker Dihapus 」\n"
                                ret_ += "│ Pengirim : {}".format(str(MudraPekok.displayName))
                                ret_ += "\n│ Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n│ Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                ret_ += "\n╰───────────"
                                samudra.sendMessage(at, str(ret_))
                                samudra.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)
#=================[BACKUPS SAMUDRA BOTS]=================    
        if op.type == 19:
            if op.param3 in owner:
                    if op.param2 in owner:
                        pass
                    if op.param2 in admin:
                        pass
                    if op.param2 in staff:
                        pass
                    if op.param2 in Bots:
                        pass
                    else:
                        SamColi["blacklist"][op.param2] = True
                        try:
                            samudra.acceptGroupInvitation(op.param1)
                            random.choice(Keder).inviteIntoGroup(op.param1,[mid])
                        except:
                            pass
                            
            if op.param3 in admin:
                    if op.param2 not in owner:
                        pass
                    if op.param2 not in admin:
                        pass
                    if op.param2 not in staff:
                        pass
                    if op.param2 not in Bots:
                        pass
                    else:
                        SamColi["blacklist"][op.param2] = True
                        try:
                            samudra.acceptGroupInvitation(op.param1)
                            random.choice(Keder).inviteIntoGroup(op.param1,[mid])
                        except:
                            pass       
                                    
        if op.type == 19:
            if mid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    t19 = Thread(target=attck, args=(op.param1, op.param2))
                    t19.start()
                    t20 = Thread(target=black, args=(op.param2,))
                    t20.start()
                    t21 = Thread(target=backp, args=(op.param1, op.param3))
                    t21.start()
                return
            if Amid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    t22 = Thread(target=attck, args=(op.param1, op.param2))
                    t22.start()
                    t23 = Thread(target=black, args=(op.param2,))
                    t23.start()
                    t24 = Thread(target=backp, args=(op.param1, op.param3))
                    t24.start()
                return
#========================[BACKUP OWNER ADMIN & STAFF]=====================    

        if op.type == 19:
            if op.param3 in owner:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    own = op.param3.replace("",',')
                    ownX = own.split(",")
                    SamColi["blacklist"][op.param2] = True
                    for jack in ownX:
                        try:
                            samudra.kickoutFromGroup(op.param1,[op.param2])
                            samudra.findAndAddContactsByMid(jack)
                            samudra.inviteIntoGroup(op.param1,[jack])
                        except:
                            pass
            if op.param3 in admin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    own = op.param3.replace("",',')
                    ownX = own.split(",")
                    SamColi["blacklist"][op.param2] = True
                    for jack in ownX:
                        try:
                            samudra.kickoutFromGroup(op.param1,[op.param2])
                            samudra.findAndAddContactsByMid(jack)
                            samudra.inviteIntoGroup(op.param1,[jack])
                        except:
                            pass

            if op.param3 in staff:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    own = op.param3.replace("",',')
                    ownX = own.split(",")
                    SamColi["blacklist"][op.param2] = True
                    for jack in ownX:
                        try:
                            samudra.kickoutFromGroup(op.param1,[op.param2])
                            samudra.findAndAddContactsByMid(jack)
                            samudra.inviteIntoGroup(op.param1,[jack])
                        except:
                            pass
#========================[PROTECT KICK]=====================                                                            
        if op.type == 19:
            if op.param1 in proKick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    own = op.param3.replace("",',')
                    ownX = own.split(",")
                    SamColi["blacklist"][op.param2] = True
                    for jack in ownX:
                        try:
                            samudra.kickoutFromGroup(op.param1,[op.param2])
                            samudra.findAndAddContactsByMid(jack)
                            sdmudra.inviteIntoGroup(op.param1,[jack])
                        except:
                            pass

        if op.type == 19:
            if op.param1 in SamColi["Kick"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    own = op.param3.replace("",',')
                    ownX = own.split(",")
                    SamColi["blacklist"][op.param2] = True
                    for jack in ownX:
                        try:
                            random.choice(Keder).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(Keder).findAndAddContactsByMid(jack)
                            random.choice(Keder).inviteIntoGroup(op.param1,[jack])
                        except:
                            pass

        if op.type == 32:
            if op.param1 in SamColi["Cancel"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    SamColi["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in SamColi["blacklist"]:
                            random.choice(Keder).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(Keder).inviteIntoGroup(msg.to, [mid])
                    except:
                        pass

        if op.type == 11:
            if op.param1 in SamColi["Link"] == True:
                try:
                    if samudra.getGroup(op.param1).preventedJoinByTicket == True:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            random.choice(Keder).reissueGroupTicket(op.param1)
                            X = random.choice(Keder).getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            randon.choice(Keder).updateGroup(X)
                            random.choice(Keder).kickoutFromGroup(op.param1,[op.param2])
                except:
                    pass

#======================[PROTECT CANCEL]=======================                                                            
        
        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    pass
                else:
                    try:
                        if op.param3 not in SamColi["blacklist"]:
                            settings["blacklist"][op.param2] = True
                            if op.param3 not in settings["blacklist"]:
                                try:
                                    samudra.kickoutFromGroup(op.param1,[op.param2])
                                    samudra.findAndAddContactsByMid(op.param3)
                                    samudra.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    pass
                            else:pass
                        else:pass
                    except:
                        pass
#======================[BLACKLIST READ]=======================                                      
        if op.type == 55:
            if op.param2 in SamColi["blacklist"]:
                random.choice(Keder).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass
        if op.type == 55:
            if op.param2 in SamColi["blacklist"]:
                t52 = Thread(target=attck, args=(op.param1, op.param2))
                t52.start()      
            if op.param1 in SamColi["blacklist"]:
                t53 = Thread(target=attck, args=(op.param1, op.param2))
                t53.start()        
        
            if op.param1 in Setmain["readPoint"]:
                if op.param2 in Setmain["readMember"][op.param1]:
                    pass
                else:
                    Setmain["readMember"][op.param1][op.param2] = True
            else:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = samudra.getContact(op.param2).displayName
                    Np = samudra.getContact(op.param2).pictureStatus
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        #samudra.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                        sid = str(SamColi["AddstickerSider"]["sid"])
                        spkg = str(SamColi["AddstickerSider"]["spkg"])
                        samudra.sendSticker(op.param1, spkg, sid)

        if op.type == 26:
           if SamColi["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if SamColi["talkban"] == True:
                   if msg._from in SamColi["Talkblacklist"]:
                      try:
                          random.choice(Keder).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(Keder).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(Keder).kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                if msg._from not in Bots:
                 if SamColi["detectMention"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']                   
                   for mention in mentionees:
                        if mention ['M'] in admin:
                           contact = samudra.getContact(msg._from)
                           anu = contact.displayName
                           samudra.sendMessage(msg.to, "."+anu+"\n"+SamColi["Respontag"])
                           sid = str(SamColi["AddstickerTag"]["sid"])
                           spkg = str(SamColi["AddstickerTag"]["spkg"])
                           samudra.sendSticker(msg.to, spkg, sid)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                if msg._from not in Bots:
                 if SamColi["mentionKick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in admin:
                           samudra.sendMessage(msg.to, "Jangan tag saya ogeb")
                           samudra.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if SamColi["stickerOn"] == True:
                    msg.contentType = 0
                    samudra.sendMessage(msg.to,"╭─「 Cek ID Sticker 」\n├↘ STKID : " + msg.contentMetadata["STKID"] + "\n├↘ STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n├↘ STKVER : " + msg.contentMetadata["STKVER"]+ "\n├↘\n╰─「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if SamColi["contact"] == True:
                    msg.contentType = 0
                    samudra.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = samudra.getContact(msg.contentMetadata["mid"])
                        path = samudra.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        samudra.sendMessage(msg.to,"╭─「 Contact Info 」\n├↘ Nama : " + msg.contentMetadata["displayName"] + "\n├↘ MID : " + msg.contentMetadata["mid"] + "\n├↘ Status Msg : " + contact.statusMessage + "\n├↘ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        samudra.sendImageWithURL(msg.to, image)

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            stickername = str(text)
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 16:
                    if SamColi["Timeline"] == True:
                            ret_ = "「 Detail Postingan 」"
                            if msg.contentMetadata["serviceType"] == "GB":
                                contact = samudra.getContact(sender)
                                auth = "\n• Penulis : {}".format(str(contact.displayName))
                            else:
                                auth = "\n• Penulis : {}".format(str(msg.contentMetadata["serviceName"]))
                            ret_ += auth
                            if "stickerId" in msg.contentMetadata:
                                stck = "\n• Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                ret_ += stck
                            if "mediaOid" in msg.contentMetadata:
                                object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                if msg.contentMetadata["mediaType"] == "V":
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        murl = "\n• Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        murl = "\n• Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                    ret_ += murl
                                else:
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                ret_ += ourl
                            if "text" in msg.contentMetadata:
                                text = "\n• Tulisan : {}".format(str(msg.contentMetadata["text"]))
                                purl = "\n• Post URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += purl
                                ret_ += text
                            samudra.sendMessage(to, str(ret_))
               if msg.contentType == 16:
                if SamColi["likeOn"] == True:
                    url = msg.contentMetadata["postEndUrl"]
                    daftarLike = [1001,1002,1003,1004,1005,1006]
                    likeType = random.choice(daftarLike)
                    samudra.like(url[25:58], url[66:], likeType=1006)
                    samudra.comment(url[25:58], url[66:], SamColi["comment"])      
                    
               if msg.contentType == 7:
                 if msg._from in creator or msg._from in owner or msg._from in admin:
                    if SamColi["AddstickerTag"]["status"] == True:
                        SamColi["AddstickerTag"]["sid"] = msg.contentMetadata['STKID']
                        SamColi["AddstickerTag"]["spkg"] = msg.contentMetadata['STKPKGID']
                        samudra.sendMessage(msg.to, "Succses merubah sticker respon 🎵")
                        SamColi["AddstickerTag"]["status"] = False     
               if msg.contentType == 7:
                 if msg._from in creator or msg._from in owner or msg._from in admin:
                    if SamColi["AddstickerSider"]["status"] == True:
                        SamColi["AddstickerSider"]["sid"] = msg.contentMetadata['STKID']
                        SamColi["AddstickerSider"]["spkg"] = msg.contentMetadata['STKPKGID']
                        samudra.sendMessage(msg.to, "sukses menambahkan sticker sider 🎵")
                        SamColi["AddstickerSider"]["status"] = False
               if msg.contentType == 7:
                 if msg._from in creator or msg._from in owner or msg._from in admin:
                    if SamColi["AddstickerWelcome"]["status"] == True:
                        SamColi["AddstickerWelcome"]["sid"] = msg.contentMetadata['STKID']
                        SamColi["AddstickerWelcome"]["spkg"] = msg.contentMetadata['STKPKGID']
                        samudra.sendMessage(msg.to, "Succses merubah sticker welccome 🎵")
                        SamColi["AddstickerWelcome"]["status"] = False     
               if msg.contentType == 7:
                 if msg._from in creator or msg._from in owner or msg._from in admin:
                    if SamColi["AddstickerLeave"]["status"] == True:
                        SamColi["AddstickerLeave"]["sid"] = msg.contentMetadata['STKID']
                        SamColi["AddstickerLeave"]["spkg"] = msg.contentMetadata['STKPKGID']
                        samudra.sendMessage(msg.to, "sukses menambahkan leave 🎵")
                        SamColi["AddstickerLeave"]["status"] = False                   
                       
               if msg.contentType == 0:
                    msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
               if msg.text:
                    if msg.text.lower().lstrip().rstrip() in wbanlist:
                        if msg.text not in clientMID:
                            try:
                                samudra.kickoutFromGroup(msg.to,[sender])
                            except Exception as e:
                                 print(e)
               if msg.contentType == 1:
                    path = samudra.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\n「 Sticker Info 」"
                   ret_ += "\n➪ Sticker ID : {}".format(stk_id)
                   ret_ += "\n➪ Sticker Version : {}".format(stk_ver)
                   ret_ += "\n➪ Sticker Package : {}".format(pkg_id)
                   ret_ += "\n➪ Sticker Url : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = samudra.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 7:
                if SamColi["stickerOn"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        r = s.get("https://store.line.me/stickershop/product/{}/id".format(urllib.parse.quote(pkg_id)))
                        soup = BeautifulSoup(r.content, 'html5lib')
                        data = soup.select("[class~=mdBtn01Txt]")[0].text
                        if data == 'Lihat Produk Lain':
                            ret_ = "「 Sticker Info 」"
                            ret_ += "\n~STICKER ID : {}".format(stk_id)
                            ret_ += "\n~STICKER PACKAGES ID : {}".format(pkg_id)
                            ret_ += "\n~STICKER VERSION : {}".format(stk_ver)
                            ret_ += "\n~STICKER URL : line://shop/detail/{}".format(pkg_id)
                            samudra.sendMessage(msg.to, str(ret_))
                            query = int(stk_id)
                            if type(query) == int:
                               data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                               path = samudra.downloadFileURL(data)
                               samudra.sendImage(msg.to,path)
                        else:
                            ret_ = "「 Sticker Info 」"
                            ret_ += "\n~PRICE : "+soup.findAll('p', attrs={'class':'mdCMN08Price'})[0].text
                            ret_ += "\n~AUTHOR : "+soup.select("a[href*=/stickershop/author]")[0].text
                            ret_ += "\n~STICKER ID : {}".format(str(stk_id))
                            ret_ += "\n~STICKER PACKAGES ID : {}".format(str(pkg_id))
                            ret_ += "\n~STICKER VERSION : {}".format(str(stk_ver))
                            ret_ += "\n~STICKER URL : line://shop/detail/{}".format(str(pkg_id))
                            ret_ += "\n~DESCRIPTION :\n"+soup.findAll('p', attrs={'class':'mdCMN08Desc'})[0].text
                            samudra.sendMessage(msg.to, str(ret_))
                            query = int(stk_id)
                            if type(query) == int:
                               data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                               path = samudra.downloadFileURL(data)
                               samudra.sendImage(msg.to,path)
               if msg.contentType == 13:
                 if SamColi["contact"] == True:
                    msg.contentType = 0
                    samudra.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = samudra.getContact(msg.contentMetadata["mid"])
                        path = samudra.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        samudra.sendMessage(msg.to," 「 Contact Info 」\n➸ Nama : " + msg.contentMetadata["displayName"] + "\n➸ MID : " + msg.contentMetadata["mid"] + "\n➸ Status Msg : " + contact.statusMessage + "\n➸ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        samudra.sendImageWithURL(msg.to, image)
               if msg.contentType == 13:
                if msg._from in admin:
                  if SamColi["invite"] == True:
                    msg.contentType = 0
                    contact = samudra.getContact(msg.contentMetadata["mid"])
                    invite = msg.contentMetadata["mid"]
                    groups = samudra.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if invite in SamColi["blacklist"]:
                            samudra.sendMessage(msg.to, "...")
                            break
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                         for target in targets:
                             try:
                                  samudra.findAndAddContactsByMid(target)
                                  samudra.inviteIntoGroup(msg.to,[target])
                                  ryan = samudra.getContact(target)
                                  zx = ""
                                  zxc = ""
                                  zx2 = []
                                  xpesan =  ""
                                  ret_ = "Ketik invite off jika Sudah Selesai"
                                  ry = str(ryan.displayName)
                                  pesan = ''
                                  pesan2 = pesan+"@x\n"
                                  xlen = str(len(zxc)+len(xpesan))
                                  xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                  zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                  zx2.append(zx)
                                  zxc += pesan2
                                  text = xpesan + zxc + ret_ + ""
                                  samudra.sendMessage(msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                  SamColi["invite"] = False
                                  break
                             except:
                                  samudra.sendMessage(msg.to,"🔄Anda terkena limit")
                                  SamColi["invite"] = False
                                  break
#ADD Bots
               if msg.contentType == 13:
                 if msg._from in admin:
                  if SamColi["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        samudra.sendMessage(msg.to,"")
                        SamColi["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        SamColi["addbots"] = True
                        samudra.sendMessage(msg.to,"Succes add Bost~")
                 if SamColi["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        samudra.sendMessage(msg.to," Expelled")
                    else:
                        SamColi["dellbots"] = True
                        samudra.sendMessage(msg.to," Nothing from list")
#ADD STAFF
                 if msg._from in admin:
                  if SamColi["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        samudra.sendMessage(msg.to," Ready staff")
                        SamColi["addstaff"] = True
                    else:
                        staff[msg.contentMetadata["mid"]] = True
                        f=codecs.open('staff.json','w','utf-8')
                        json.dump(staff, f, sort_keys=True, indent=4,ensure_ascii=False)
                        SamColi["addstaff"] = True
                        samudra.sendMessage(msg.to,"Succes add to staff~")
                 if SamColi["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        del staff[msg.contentMetadata["mid"]]
                        f=codecs.open('staff.json','w','utf-8')
                        json.dump(staff, f, sort_keys=True, indent=4,ensure_ascii=False)
                        samudra.sendMessage(msg.to,"Succes expell staff")
                        SamColi["dellstaff"] = True
                    else:
                        SamColi["dellstaff"] = True
                        samudra.sendMessage(msg.to,"Nothing in list staff")
#ADD ADMIN
                 if msg._from in admin:
                  if SamColi["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        samudra.sendMessage(msg.to,"Ready in admin list")
                        SamColi["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        SamColi["addadmin"] = True
                        samudra.sendMessage(msg.to," Succes add to admin~")
                 if SamColi["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        samudra.sendMessage(msg.to," Succes expell in admin list~")
                    else:
                        SamColi["delladmin"] = True
                        samudra.sendMessage(msg.to,"Nothing in admin list")
#ADD BLACKLIST
                 if msg._from in admin:
                  if SamColi["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in SamColi["blacklist"]:
                        samudra.sendMessage(msg.to," User ready in blacklist")
                        SamColi["wblacklist"] = True
                    else:
                        SamColi["blacklist"][msg.contentMetadata["mid"]] = True
                        SamColi["wblacklist"] = True
                        samudra.sendMessage(msg.to,"Succes add blacklist user~")
                  if SamColi["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in SamColi["blacklist"]:
                        del SamColi["blacklist"][msg.contentMetadata["mid"]]
                        samudra.sendMessage(msg.to," Remove from blacklist user")
                    else:
                        SamColi["dblacklist"] = True
                        samudra.sendMessage(msg.to," Nothing in User blacklist")
#TALKBAN
                 if msg._from in admin:
                  if SamColi["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in SamColi["Talkblacklist"]:
                        samudra.sendMessage(msg.to," Ready in User Talkban")
                        SamColi["Talkwblacklist"] = True
                    else:
                        SamColi["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        SamColi["Talkwblacklist"] = True
                        samudra.sendMessage(msg.to," Succes add to Talkban user")
                  if SamColi["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in SamColi["Talkblacklist"]:
                        del SamColi["Talkblacklist"][msg.contentMetadata["mid"]]
                        samudra.sendMessage(msg.to," Remove Talkban user")
                    else:
                        SamColi["Talkdblacklist"] = True
                        samudra.sendMessage(msg.to," Ready in Talkban list")
#UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in admin:
                    if SamColi["Addimage"]["status"] == True:
                        path = samudra.downloadObjectMsg(msg.id)
                        images[SamColi["Addimage"]["name"]] = str(path)
                        f = codecs.open("image.json","w","utf-8")
                        json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                        samudra.sendMessage(msg.to, " Berhasil menambahkan gambar {}".format(str(SamColi["Addimage"]["name"])))
                        SamColi["Addimage"]["status"] = False                
                        SamColi["Addimage"]["name"] = ""
               if msg.contentType == 2:
                 if msg._from in admin:
                    if SamColi["Addvideo"]["status"] == True:
                        path = samudra.downloadObjectMsg(msg.id)
                        videos[SamColi["Addvideo"]["name"]] = str(path)
                        f = codecs.open("video.json","w","utf-8")
                        json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                        samudra.sendMessage(msg.to, " Berhasil menambahkan video {}".format(str(SamColi["Addvideo"]["name"])))
                        SamColi["Addvideo"]["status"] = False                
                        SamColi["Addvideo"]["name"] = ""
               if msg.contentType == 7:
                 if msg._from in admin:
                    if SamColi["Addsticker"]["status"] == True:
                        stickers[SamColi["Addsticker"]["name"]] = {"STKID":msg.contentMetadata["STKID"],"STKPKGID":msg.contentMetadata["STKPKGID"]}
                        f = codecs.open("sticker.json","w","utf-8")
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        samudra.sendMessage(msg.to, " Berhasil menambahkan sticker {}".format(str(SamColi["Addsticker"]["name"])))
                        SamColi["Addsticker"]["status"] = False                
                        SamColi["Addsticker"]["name"] = ""
               
               if msg.contentType == 3:
                 if msg._from in admin:
                    if SamColi["Addaudio"]["status"] == True:
                        path = samudra.downloadObjectMsg(msg.id)
                        audios[SamColi["Addaudio"]["name"]] = str(path)
                        f = codecs.open("audio.json","w","utf-8")
                        json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                        samudra.sendMessage(msg.to, " Berhasil menambahkan mp3 {}".format(str(SamColi["Addaudio"]["name"])))
                        SamColi["Addaudio"]["status"] = False                
                        SamColi["Addaudio"]["name"] = ""
               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = samudra.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     samudra.updateGroupPicture(msg.to, path)
                     samudra.sendMessage(msg.to, "Succes Update Profile Group~")
               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["RAfoto"]:
                            path = samudra.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][mid]
                            samudra.updateProfilePicture(path)
                            samudra.sendMessage(msg.to,"Update Profile Succes~")
               if msg.contentType == 2:
                   if msg._from in admin:
                       if mid in Setmain["RAvideo"]:
                            path = samudra.downloadObjectMsg(msg_id)
                            Setmain["RAvideo"][mid]
                            samudra.updateProfileVideoPicture(path)
                            samudra.sendMessage(msg.to," Succes~")
          
               if msg.contentType == 1:
                 if msg._from in admin:
                        if mid in Setmain["RAfoto"]:
                            path = samudra.downloadObjectMsg(msg_id)
                            Setmain["RAfoto"][mid]
                            samudra.updateProfilePicture(path)
                            samudra.sendMessage(msg.to,"Succes change~")
               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path = samudra.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     samudra.updateProfilePicture(path)
                     samudra.sendMessage(msg.to, " Succes ~")
               if msg.contentType == 0:
                 if Setmain["autoRead"] == True:
                     samudra.sendChatChecked(msg.to, msg_id)
                 if text is None:
                     return
                 else:
                        for sticker in stickers:
                         #if msg._from in admin:
                           if text.lower() == sticker:
                              sid = stickers[text.lower()]["STKID"]
                              spkg = stickers[text.lower()]["STKPKGID"]
                              samudra.sendSticker(to, spkg, sid)
                        for image in images:
                         if msg._from in admin:
                           if text.lower() == image:
                              samudra.sendImage(msg.to, images[image])
                        for audio in audios:
                         if msg._from in admin:
                           if text.lower() == audio:
                              samudra.sendAudio(msg.to, audios[audio])
                        for video in videos:
                         if msg._from in admin:
                           if text.lower() == video:
                              samudra.sendVideo(msg.to, videos[video])
                        cmd = command(text)
                        
                        if cmd == "bot on":
                            if msg._from in admin:
                                SamColi["selfbot"] = True
                                samudra.sendMessage(msg.to, " ➪ Selfbot diaktifkan")
                                
                        elif cmd == "bot off":
                            if msg._from in admin:
                                SamColi["selfbot"] = False
                                samudra.sendMessage(msg.to, " 🚫 Selfbot dinonaktifkan")
    
                        elif cmd == "help1":
                            samudra.sendMessage(to, "╭─────────\n│╭────────\n│├• 〔  ᴍᴇɴᴜ js  〕\n│╰────────\n│╭────────\n││➪ me \n││➪ menu1 \n││➪ menu2 \n││➪ mybot \n││➪ mycrot \n││➪ #bantai \n││➪ #hobah \n││➪ jiran <no> \n│╰────────\n│ ├•  ᴄʀ : sᴀᴍᴜᴅʀᴀ \n╰─────────")
    
                        elif cmd == "help2":
                            samudra.sendMessage(to, "╭──────────\n│╭─────────\n│├• 〔  ᴍᴜᴅʀᴀ_ᴍᴇɴᴜ  〕\n│╰─────────\n│╭─────────\n││➪ respon on/off \n││➪ autojoin on/off \n││➪ autoblock on/off \n││➪ autoriject on/off \n││➪ autoadd on/off \n││➪ autoreed on/off \n││➪ unsend on/off \n││➪ jointicket on/off \n││➪ chatbot on/off \n││➪ sticker on/off \n││➪ autolike on/off \n││➪ timeline on/off \n││➪ contact on/off \n││➪ invite on/off \n││➪ time on/off \n│╰─────────\n│ ├•  ᴄʀ : sᴀᴍᴜᴅʀᴀ \n╰──────────")
    
                        elif cmd == "help3":
                            samudra.sendMessage(to, "╭────────────\n│╭───────────\n│├• 〔  ᴍᴜᴅʀᴀ_ᴍᴇɴᴜ  〕\n│╰───────────\n│╭───────────\n││➪ set respon: <kata> \n││➪ set welcome: <kata> \n││➪ set leave: <kata> \n││➪ set tag: <kata> \n││➪ set ciluk: <kata> \n│╰─────────── \n│╭─────────── \n││➪ reboot \n││➪ hapus mantan \n││➪ ciluk ba \n││➪ colok ni \n││➪ blacklist \n││➪ ampuni \n││➪ maafin \n││➪ byeme \n││➪ blc \n││➪ ping \n││➪ open \n││➪ close \n││➪ link \n││➪ glist \n│╰─────────\n│ ├•  ᴄʀ : sᴀᴍᴜᴅʀᴀ \n╰──────────")
                            
                        elif cmd == "set":
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "    😡 My Setting 😡 \n"
                                if SamColi["selfbot"] == True: md+="😡 ✔ Auto Chat\n"
                                else: md+="😡 ❎  Auto Chat\n"
                                if SamColi["mentionKick"] == True: md+="😡 ✔ Respon Kick\n"
                                else: md+="😡 ❎ Respon Kick\n"
                                if SamColi["stickerOn"] == True: md+="😡 ✔ Check Sticker\n"
                                else: md+="😡 ❎ Check Sticker\n"
                                if SamColi["contact"] == True: md+="😡 ✔ Check Contact\n"
                                else: md+="😡 ❎ Check Contact\n"
                                if SamColi["talkban"] == True: md+="😡 ✔ Talkban「On」\n"
                                else: md+="😡 ❎ Talkban\n"
                                if SamColi["autoBlock"] == True: md+="😡 ✔ Auto Block\n"
                                else: md+="😡 ❎ Auto Block\n"
                                if SamColi["detectMention"] == True: md+="😡 ✔ Auto Respon\n"
                                else: md+="😡 ❎ Auto Respon\n"
                                if SamColi["Timeline"] == True: md+="😡 ✔ Detail Post\n"
                                else: md+="😡 ❎ Detail Post\n"
                                if SamColi["autoJoin"] == True: md+="😡 ✔ Auto Join\n"
                                else: md+="😡 ❎ Auto Join\n"
                                if SamColi["autoAdd"] == True: md+="😡 ✔ Auto Add\n"
                                else: md+="😡 ❎ Auto Add\n"
                                if settings["autoJoinTicket"] == True: md+="😡 ✔ Join Link\n"
                                else: md+="😡 ❎ Join Link\n"
                                if msg.to in welcome: md+="😡 ✔ Sambutan\n"
                                else: md+="😡 ❎ Sambutan\n"
                                if SamColi["autoLeave"] == True: md+="😡 ✔ Auto Leave\n"
                                else: md+="😡 ❎ Auto Leave\n"
                                if msg.to in proLink: md+="😡 ✔ Block Link\n"
                                else: md+="😡 ❎ Block Code Qr\n"
                                if msg.to in ghostJs: md+="😡 ✔ Block Js\n"
                                else: md+="😡 ❎ Block Js\n"
                                if msg.to in protectjoin: md+="😡 ✔ Block Join\n"
                                else: md+="😡 ❎ Block Join\n"
                                if msg.to in proKick: md+="😡 ✔ Block Kick\n"
                                else: md+="😡 ❎ Block Kick\n"
                                if msg.to in proInvite: md+="😡 ✔ Block Invite\n"
                                else: md+="😡 ❎ Block Invite\n"
                                if msg.to in proName: md+="?? ✔ Block Name\n"
                                else: md+="😡 ❎ Lock Name Group\n"
                                if msg.to in picon: md+="😡 ✔ Block Join\n"
                                else: md+="😡 ❎ Lock Icon Group\n"
                                if msg.to in protectantijs: md+="😡 ✔ Lock Js group\n"
                                else: md+="😡 ❎ Lock js Grouop\n"
                                if msg.to in proCancel: md+="😡 ✔ Block Cancel\n"
                                else: md+="😡 ❎ Lock Cancel\n"
                                samudra.sendMessage(msg.to, md+"\n↘Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"+"\n↘Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d'))
                                
                        elif cmd == "creator" or text.lower() == 'cr':
                            if msg._from in admin:
                                samudra.sendMessage(msg.to,"Ini creatornya: Samudra\n\nhttps://line.me/ti/p/~samudrabots.py") 
                                ma = ""
                                for i in creator:
                                    ma = samudra.getContact(i)
                                    samudra.sendMessage(msg.to, None, contentMetadata={'': i}, contentType=13)

                        elif cmd.startswith("joox"):
                            try:
                                proses = text.split(" ")
                                urutan = text.replace(proses[0] + " ","")
                                r = requests.get("http://api.zicor.ooo/joox.php?song={}".format(str(urllib.parse.quote(urutan))))
                                data = r.text
                                data = json.loads(data)
                                b = data
                                c = str(b["title"])
                                d = str(b["singer"])
                                e = str(b["url"])
                                g = str(b["image"])
                                hasil = "Penyanyi: "+str(d)
                                hasil += "\nJudul : "+str(c)
                                samudra.sendImageWithURL(to,g)
                                samudra.sendAudioWithURL(to,e)
                                samudra.sendMessage(msg.to,hasil)
                            except Exception as error:
                                samudra.sendMessage(to, "error\n" + str(error))
                                logError(error) 

                        elif cmd.startswith('about'):
                          if SamColi["selfbot"] == True:
                           if msg._from in admin:
                            try:
                                arr = []
                                today = datetime.today()
                                thn = 2018 
                                bln = 5     #isi bulannya yg sewa
                                hr = 17    #isi tanggalnya yg sewa
                                future = datetime(thn, bln, hr)
                                days = (str(future - today))
                                comma = days.find(",")
                                days = days[:comma]
                                contact = samudra.getContact(mid)
                                favoritelist = samudra.getFavoriteMids()
                                grouplist = samudra.getGroupIdsJoined()
                                contactlist = samudra.getAllContactIds()
                                blockedlist = samudra.getBlockedContactIds()
                                eltime = time.time() - mulai
                                bot = runtime(eltime)
                                start = time.time()
                                samudra.sendMessage("uc28284eca396bd65511797a2ce6d6167", '.')
                                elapsed_time = time.time() - start
                                SamPekok = samudra.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "😡 Info Selfbot 😡\n😡 Name : "
                                ret_ = "😡 Group : {} Group".format(str(len(grouplist)))
                                ret_ += "\n• Friend : {} Friend".format(str(len(contactlist)))
                                ret_ += "\n• Blocked : {} Blocked".format(str(len(blockedlist)))
                                ret_ += "\n• Favorite : {} Favorite".format(str(len(favoritelist)))
                                ret_ += "\n• Version : Py3"
                                ret_ += "\n• Expired : {} - {} - {}".format(str(hr), str(bln), str(thn))
                                ret_ += "\n•In days : {} again".format(days)
                                ret_ += "\n 😡 Speed Respon 😡\n• {} detik".format(str(elapsed_time))
                                ret_ += "\n😡 Selfbot Runtime 😡\n• {}".format(str(bot))
                                ry = str(SamPekok.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':SamPekok.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                samudra.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                samudra.sendContact(to, "uc28284eca396bd65511797a2ce6d6167")
                            except Exception as e:
                                samudra.sendMessage(msg.to, str(e))

                        elif cmd == "me":
                           if SamColi["selfbot"] == True:
                             if msg._from in admin:
                                 samudra.sendMentionFooter(to, '[ User self ]\n', sender, "https://line.me/ti/p/~samudrabots.py", "http://dl.profile.line-cdn.net/"+samudra.getContact(sender).pictureStatus, samudra.getContact(sender).displayName);samudra.sendMessage(to, samudra.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+samudra.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/samudrabots.py', 'type': 'mt', 'subText': "Samudra_Bots", 'a-installUrl': 'https://line.me/ti/p/samudrabots.py', 'a-installUrl': ' https://line.me/ti/p/samudrabots.py', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/samudrabots.py', 'i-linkUri': 'https://line.me/ti/p/samudrabots.py', 'id': 'mt000000000a6b79f9', 'text': 'Samudra__Bots', 'linkUri': 'https://line.me/ti/p/samudrabots.py'}, contentType=19)
                        elif text.lower() == "mid":
                               samudra.sendMessage(msg.to, msg._from)
                        elif cmd.startswith("mid "):
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = samudra.getContact(key1)
                               samudra.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               samudra.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Steal " in msg.text):
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = samudra.getContact(key1)
                               a = samudra.getProfileCoverURL(mid=key1)
                               samudra.sendMessage(msg.to, "「 Contact Info 」\n• Nama : "+str(mi.displayName)+"\n• Mid : " +key1+"\n• Status Msg"+str(mi.statusMessage))
                               samudra.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   samudra.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                                   samudra.sendImageWithURL(receiver, a)
                               else:
                                   samudra.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))
                                   samudra.sendImageWithURL(receiver, a)

                        elif ("Cover " in msg.text):
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = samudra.getProfileCoverURL(mid=u)
                                    samudra.sendImageWithURL(receiver, a)
                                except Exception as e:
                                    samudra.sendMessage(receiver, str(e))

                        elif ("Sticker: " in msg.text):
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    query = msg.text.replace("Sticker: ", "")
                                    query = int(query)
                                    if type(query) == int:
                                        samudra.sendImageWithURL(receiver, 'https://stickershop.line-scdn.net/stickershop/v1/product/'+str(query)+'/ANDROID/main.png')
                                        samudra.sendMessage(receiver, 'https://line.me/S/sticker/'+str(query))
                                    else:
                                        samudra.sendMessage(receiver, 'gunakan key sticker angka bukan huruf')
                                except Exception as e:
                                    samudra.sendMessage(receiver, str(e))

                        elif "/ti/g/" in msg.text.lower():
                           if msg._from in admin:
                             if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                    if l not in n_links:
                                       n_links.append(l)
                                 for ticket_id in n_links:
                                    group = samudra.findGroupByTicket(ticket_id)
                                    samudra.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    samudra.sendMessage(msg.to, "~Joint : %s" % str(group.name))
                                    group1 = samudra1.findGroupByTicket(ticket_id)
                                    samudra1.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                    samudra1.sendMessage(msg.to, "~Joint : %s" % str(group.name))
                                    
                        elif cmd.startswith('cek'):
                          if SamColi["selfbot"] == True:
                            if msg._from in creator or msg._from in owner or msg._from in admin:
                                try:samudra.kickoutFromGroup(msg.to, ["u5d72909e8c37e0ab805952336f872361"]);wait["limitkick"] = False
                                except:SamColi["limitkick"] = True
                                md = ""
                                if SamColi["limitkick"]== True: md+="❎ Limite"
                                else: md+="😡✔ Sehat"
                                samudra.sendMessage(msg.to, md)
                                
                        elif cmd == "reject":
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                              ginvited = cl.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      samudra.rejectGroupInvitation(gid)
                                  samudra.sendMessage(to, "~ Berhasil tolak sebanyak {} undangan grup".format(str(len(ginvited))))
                              else:
                                  samudra.sendMessage(to, "~ Tidak ada undangan yang tertunda")
                                  
                        elif cmd.startswith("delfriend "):
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = samudra.getContact(ls)
                                    samudra.deleteContact(ls)
                                samudra.sendMessage(to, "Success Del " + str(contact.displayName) + " to Friendlist")
                        elif cmd.startswith("addfriend "):
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = samudra.getContact(ls)
                                    samudra.findAndAddContactsByMid(ls)
                                samudra.sendMessage(to, "Success Add " + str(contact.displayName) + " to Friendlist")

                        elif text.lower() == "hapus chat":
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   cl.removeAllMessages(op.param2)
                               except:
                                   pass

                        elif text.lower() == "hapus mantan":
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   samudra.removeAllMessages(op.param2)
                                   samudra.sendMessage(msg.to,"мᴀɴтᴀɴ ᴅιмusɴᴀнκᴀɴ~.")
                                   samudra.sendMessage(msg.to,"мᴀɴтᴀɴ мusɴᴀн~.")
                               except:
                                   pass

                        elif cmd.startswith("bc: "):
                           if msg._from in admin:
                             sep = text.split(" ")
                             bc = text.replace(sep[0] + " ","")
                             saya = samudra.getGroupIdsJoined()
                             for group in saya:
                                SamPekok = samudra.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "◀Broadcast ▶\n↘By "
                                ret_ = "{}".format(str(bc))
                                ry = str(SamPekok.displayName)
                                pesan = '~'
                                pesan2 = pesan+"@x\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                samudra.sendMessage(group, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                             
                        elif text.lower() == "mykey":
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                               samudra.sendMessage(msg.to, "↘ " + str(Setmain["keyCommand"]) + " ")
                               
                        elif cmd.startswith("setkey "):
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   samudra.sendMessage(msg.to, "🔄Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   samudra.sendMessage(msg.to, "↘Setkey diganti jadi「{}」".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               samudra.sendMessage(msg.to, " Setkey Anda telah direset")

                        elif cmd == "reboot":
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                               samudra.sendMessage(to,"Waaiiit..... ⏳")
                               Setmain["restartPoint"] = msg.to
                               time.sleep(3)
                               samudra.sendMessage(to,"███▒▒▒▒▒▒▒")
                               time.sleep(2)
                               samudra.sendMessage(to,"█████▒▒▒▒▒")
                               time.sleep(2)
                               samudra.sendMessage(to,"██████████")
                               time.sleep(2)
                               samudra.sendMessage(to,"~Bots Actived..✔")
                               restartBot()                            
                            
                        elif cmd == "runtime":
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                eltime = time.time() - mulai
                                bot = runtime(eltime)
                                SamPekok = samudra.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "↘User : "
                                ret_ = "• {}".format(str(bot))
                                ry = str(SamPekok.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':SamPekok.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                samudra.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = samudra.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                samudra.sendMessage(msg.to, "↘Group Info↖\n↘Nama Group : {}".format(G.name)+ "\n↘ID Group : {}".format(G.id)+ "\n↘Pembuat : {}".format(G.creator.displayName)+ "\n↘Waktu Dibuat : {}".format(str(timeCreated))+ "\n↘Jumlah Member : {}".format(str(len(G.members)))+ "\n↘Jumlah Pending : {}".format(gPending)+ "\n↘Group Qr : {}".format(gQr)+ "\n↘Group Ticket : {}".format(gTicket))
                                samudra.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                samudra.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                samudra.sendMessage(msg.to, str(e))

                        elif cmd == "invite":
                          if msg._from in admin:
                                SamColi['undang'] = True
                                samudra.sendMessage(to,"Send Contact For Invite Target")
                         
                        elif cmd.startswith("infogrup "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = samudra.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = samudra.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += " ◀ Group Info ▶"
                                ret_ += "\n➥Nama Group : {}".format(G.name)
                                ret_ += "\n➥ID Group : {}".format(G.id)
                                ret_ += "\n➥Pembuat : {}".format(gCreator)
                                ret_ += "\n➥Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n➥Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n➥Jumlah Pending : {}".format(gPending)
                                ret_ += "\n➥Group Qr : {}".format(gQr)
                                ret_ += "\n➥Group Ticket : {}".format(gTicket)
                                ret_ += "\n➥Picture Url : http://dl.profile.line-cdn.net/{}".format(G.pictureStatus)
                                ret_ += ""
                                samudra.sendMessage(to, str(ret_))
                                samudra.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except:
                                pass
                                
                        elif cmd.startswith("outqr "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = samudra.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            G = samudra.getGroup(group)
                            #samudra.sendMessage(msg.to, "Bots di paksa keluar oleh Owner")
                            try:
                                samudra.leaveGroup(group)
                                samudra.sendMessage(msg.to,"~Succes Leave from~ Group \n"+str(G.name))
                            except:
                                pass
                        elif cmd.startswith("openqr "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = samudra.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            G = samudra.getGroup(group)
                            try:
                                samudra.updateGroup(G)
                                gurl = samudra.reissueGroupTicket(group)
                                samudra.sendMessage(msg.to, "Group "+str(G.name)+ "\nLink nya : http://line.me/R/ti/g/"+gurl)
                            except:
                            	samudra.sendMessage(msg.to,"I no there")
                                        
                        elif cmd.startswith("invitegid: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = samudra.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            G = samudra.getGroup(group)
                            if gid == "":
                                    samudra.sendMessage(msg.to,"Group id wrong")
                                    try:
                                        samudra.findAndAddContactsByMid(MID)
                                        samudra.inviteIntoGroup(gid,[MID])
                                    except:
                                    	pass
                        elif cmd.startswith("groupid: "):
                          if msg._from in owner or msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = samudra.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            G = samudra.getGroup(group)
                            gid = samudra.getGroup(to)
                            try:
                                samudra.sendMessage(to, "~"+str(G.name) + "\n" +gid.id)
                            except:
                            	pass     
                        elif cmd.startswith("leaveall "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = samudra.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            G = samudra.getGroup(group)
                            try:
                                samudra.leaveGroup(group)
                                samudra.sendMessage(msg.to,"Succes leaveall from group~\n" + str(G.name))
                            except:
                                pass

                        elif cmd.startswith("open "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = samudra.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = samudra.getGroup(group)
                                G.preventedJoinByTicket = False
                                samudra.updateGroup(G)
                                samudra.sendMessage(msg.to,"Succes Open Qr in group~\n" + str(G.name))
                            except:
                                pass

                        elif cmd.startswith("close "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = samudra.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = samudra.getGroup(group)
                                G.preventedJoinByTicket = True
                                samudra.updateGroup(G)
                                samudra.sendMessage(msg.to,"Succes Close Qr in group~\n" + str(G.name))
                            except:
                                pass
                                
                        elif cmd == "gid":
                          if msg._from in admin:
                            if msg.toType != 2: return
                            gid = samudra.getGroup(to)
                            samudra.sendMessage(to, "" + gid.id)
              
                        elif cmd.startswith("infomem "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = samudra.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = samudra.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "➥ "+ str(no) + ". " + mem.displayName
                                samudra.sendMessage(to,"~ Group Name : ◀ " + str(G.name) + " ▶\n\n   [ List Member ]\n" + ret_ + "\n\n[Total %i Members]" % len(G.members))
                            except: 
                                pass
                        elif cmd == "glist":
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = samudra.getGroupIdsJoined()
                               for i in gid:
                                   G = samudra.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               samudra.sendMessage(msg.to,"╭──〔Grup Bahan 〕\n│\n"+ma+"│\n╰──〔 Ada「"+str(len(gid))+"」BahanTest 〕")

                        elif cmd == "open":
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = samudra.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   samudra.updateGroup(X)
                                   samudra.sendMessage(msg.to, "➥Succes Open Code qr  ...")

                        elif cmd == "close":
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = samudra.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   samudra.updateGroup(X)
                                   samudra.sendMessage(msg.to, "➥Succes Closed Qr Code.....")
                                   
                        elif cmd == "link":
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = samudra.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      samudra.updateGroup(x)
                                   gurl = samudra.reissueGroupTicket(msg.to)
                                   samudra.sendMessage(msg.to, "Grup "+str(x.name)+ "\nLink nya : http://line.me/R/ti/g/"+gurl)

#===========BOT UPDATE============#
                        elif cmd == "updategrup":
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                samudra.sendMessage(msg.to,"➥Kirim fotonya.....")

                        elif cmd == "updatebot":
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                settings["changePicture"] = True
                                samudra.sendMessage(msg.to,"➥Kirim fotonya.....")
                                
                        elif cmd == "updatefoto":
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["RAfoto"][mid] = True
                                samudra.sendMessage(msg.to,"➥Kirim fotonya.....")

                        elif cmd == "cvp":
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["RAvideo"][mid] = True
                                samudra.sendMessage(msg.to,"➥Kirim videonya.....")
                                
                        elif cmd.startswith("status "):
                          if msg._from in admin:
                            string = removeCmd("updatestatus", text)
                            if len(string) <= 10000000000:
                                pname = samudra.getContact(sender).statusMessage
                                profile = samudra.getProfile()
                                profile.statusMessage = string
                                samudra.updateProfile(profile)
                                samudra.sendMessage(to ,"~Success")
                                
                        elif cmd.startswith("name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = samudra.getProfile()
                                profile.displayName = string
                                samudra.updateProfile(profile)
                                samudra.sendMessage(msg.to,"➥Nama diganti jadi " + string + "")
                                
                        elif cmd.startswith("jiran "):
                          if msg._from in admin:
                           separate = text.split(" ")
                           number = text.replace(separate[0] + " ","")
                           groups = samudra.getGroupIdsJoined()
                           groups = samudra.getGroupIdsJoined()
                           listGroup = groups[int(number)-1]
                           x = samudra.getGroup(listGroup)
                           x = samudra.getGroup(listGroup)
                           if x.invitee == None:nama = []
                           else:nama = [contact.mid for contact in x.invitee]
                           targets = []
                           for a in nama:
                           	if a not in ["ud9e93f564195bf069e43b9801d8af3a5",samudra.profile.mid]:targets.append(a) 
                           nami = [contact.mid for contact in x.members]
                           targetk = []
                           lolz = 'SaMuDrA.js gid={} token={}'.format(x.id, samudra.authToken)
                           for a in nami:
                           	if a not in ["ud9e93f564195bf069e43b9801d8af3a5",samudra.profile.mid]:targetk.append(a) 
                           for y in targets:
                           	lolz += ' uid={}'.format(y)
                           for y in targetk:
                           	lolz += ' uik={}'.format(y)
                           samudra.sendMessage(to,':..｡ᴏ○ sᴀᴍᴜᴅʀᴀ__ʙᴏᴛs ○ᴏ｡..:')
                           print(lolz)
                           success = execute_js(lolz)
                           if success:
                           	samudra.sendMention(to, "•ᴜsᴇʀ : @! \n•ᴛʏᴘᴇ : ᴍisɪᴏɴ bypas ᴛᴀʀɢᴇᴛ??\n•Jᴜᴍʟᴀʜ : %i" % len(targets)+"\n•sᴛᴀᴛᴜs : 𝘴𝘢𝘮𝘶𝘥𝘳𝘢 𝘴𝘶𝘤𝘴𝘦𝘴 𝘤𝘰𝘭𝘪", [sender])
                           else:
                           	samudra.sendMessage(to,'error')
         
                        elif cmd == "#bantai" or cmd == "#hobah":
                          if msg._from in admin:
                            xyz = samudra.getGroup(to)
                            if xyz.invitee == None:pends = []
                            else:pends = [c.mid for c in xyz.invitee]
                            targp = []
                            for x in pends:
                            	if x not in admin:
                                    targp.append(x)
                            mems = [c.mid for c in xyz.members]
                            targk = []
                            for x in mems:
                            	if x not in admin:
                                    targk.append(x)
                            imnoob = 'SaMuDrA.js gid={} token={}'.format(to, samudra.authToken, "DESKTOPWIN\t5.20.2\tWindows\t10")
                            for x in targp:imnoob += ' uid={}'.format(x)
                            for x in targk:imnoob += ' uik={}'.format(x)
                            execute_js(imnoob)
#===========BOT UPDATE============#     
                        elif msg.text.lower() in SamColi["tagall"]:
                          if msg._from in admin:        
                            if SamColi["selfbot"] == True:
                              if msg._from in owner or msg._from in admin or msg._from in staff:  
                                group = samudra.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                k = len(nama)//20
                                for a in range(k+1):
                                    txt = u''
                                    s=0
                                    b=[]
                                    for i in group.members[a*20 : (a+1)*20]:
                                        b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                        s += 7
                                        txt += u'@Alin \n'
                                    samudra.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                    samudra.sendMessage(to, "◀Mention {} Member▶".format(str(len(nama)))) 
                        elif cmd == "tag":
                          if msg._from in admin:        
                            if SamColi["selfbot"] == True:
                              if msg._from in owner or msg._from in admin or msg._from in staff:  
                                group = samudra.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                k = len(nama)//20
                                for a in range(k+1):
                                    txt = u''
                                    s=0
                                    b=[]
                                    for i in group.members[a*20 : (a+1)*20]:
                                        b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                        s += 7
                                        txt += u'@Alin \n'
                                    samudra.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                    samudra.sendMessage(to, "◀Mention {} Member▶".format(str(len(nama))))     
                                    
                        elif "ngikil" in msg.text:  
                           if msg._from in admin:
                            if msg.toType == 2:
                             #  print "Otw cleanse"
                               _name = msg.text.replace("ngikil","")
                               gs = samudra.getGroup(msg.to)
                               samudra.sendMessage(msg.to,"Assalamualaikum")
                               samudra.sendMessage(msg.to,"oit boskuh\n"
 "Ada room bahan kagak ni gua bawa tenk\n"
". ___________________\n"
"▕╮╭┻┻╮╭┻┻╮╭▕╮╲\n"
"▕╯┃╭╮┃┃╭╮┃╰▕╯╭▏\n"
"▕╭┻┻┻┛┗┻┻┛   ▕  ╰▏\n"
"▕╰━━━┓┈┈┈╭╮▕╭╮▏\n"
"▕╭╮╰┳┳┳┳╯╰╯▕╰╯▏\n"
"▕╰╯┈┗┛┗┛┈╭╮▕╮┈▏\n"
   " <,︻╦̵̵̿╤━ ҉     ~  •"
"   █۞██████]▄▄▄▄▄▄▃●●\n"
"   ▂▄▅███████▅▄▃▂…\n"
"[█████████████████]\n"
"[██████████████████]\n"
"◥⊙⊙▲⊙▲⊙▲⊙▲⊙▲⊙\n"
" ☠↘sᴀмuᴅʀᴀ__ʙoтs↙☠\n"
"☾тᴇᴀм sᴀмuᴅʀᴀ___ʙoтs☽\n"
"cʀᴇᴀтoʀ sᴀмuᴅʀᴀ__ʙoтs☛ʙʏ : sᴀмuᴅʀᴀ\n"
"cʀᴇᴀтoʀ : \nhttps://line.me/ti/p/~samudrabots.py")
                               invitee = [contact.mid for contact in group.invitee]
                               targets = []
                               for g in gs.members:
                                   #if group.invitee is None or group.invitee == []:
                                   if _name in g.displayName:
                                       targets.append(g.mid)
                               if targets == []:
                                  samudra.sendMessage(msg.to,"Sorry")
                              #    else:
                               for target in targets:
                                     if target not in Bots:
                                      try:
                                          kicker.cancelGroupInvitation(to, [inv])
                                          klist=[samudra]
                                          kicker=random.choice(klist)
                                          kicker.kickoutFromGroup(msg.to,[target])
                                          print (msg.to,[g.mid])
                                      except:
                                          samudra.sendMessage(msg.to,"I'm Sory")
 #============================================#
                              
                        elif cmd == "respon":
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                samudra1.sendMessage(msg.to,'☾тᴇᴀм sᴀмuᴅʀᴀ___ʙoтs☽✍')

                        elif cmd == "mybot":
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                Musik(to, mid)
                        
                        elif cmd == "ping":
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                samudra.sendMessage(msg.to,'pong.....😡😡😡!!')

                        elif cmd == "byme":
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                G = samudra.getGroup(msg.to)
                                samudra.sendMessage(msg.to, "Bye bye coy "+str(G.name))
                                samudra.leaveGroup(msg.to)

                        elif cmd == "speed" or cmd == "sp":
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               samudra.sendMessage(msg.to," 🔀 Wifi Direct")
                               elapsed_time = time.time() - start
                               samudra.sendMessage(msg.to, "↘{} Perdetik".format(str(elapsed_time)))
                               
                        elif cmd == "ciluk ba":
                          if SamColi["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  samudra.sendMessage(to,"Mode sider diaktivkan✔ By " + samudra.getContact(sender).displayName)
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "colok ni":
                          if SamColi["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  samudra.sendMessage(to,"Mode sider dinonaktivkan✔ By " + samudra.getContact(sender).displayName)
                              else:
                                  samudra.sendMessage(msg.to, " 🚫 Sudak tidak aktif")

#===================Protection============#
                        elif 'Welcome ' in msg.text:
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = " ➪ Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = samudra.getGroup(msg.to)
                                       msgs = ""
                                  samudra.sendMessage(to,"Welcome di aktifkan ✔ By " + samudra.getContact(sender).displayName)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = samudra.getGroup(msg.to)
                                         msgs = ""
                                    else:
                                         msgs = "➪ Sudah tidak aktif"
                                    samudra.sendMessage(to,"Non actived Welcome✔ By " + samudra.getContact(sender).displayName)
#===========KICKOUT============#
                        elif "Kick " in msg.text:
                            if msg._from in admin:                                                                                                                                       
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]                                                                                                                                
                                targets = []
                                for x in key["MENTIONEES"]:                                                                                                                                  
                                    targets.append(x["M"])
                                for target in targets:                                                                                                                                       
                                    try:
                                        samudra.kickoutFromGroup(msg.to,[target])
                                        samudra.inviteIntoGroup(msg.to,[target])
                                        samudra.cancelGroupInvitation(msg.to,[target])
                                    except:
                                        pass
            
#===========ADMIN ADD============#
                        elif ("Adminadd " in msg.text):
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin.append(target)
                                           samudra.sendMessage(to,"Add Admin ✔ By " + samudra.getContact(sender).displayName)
                                       except:
                                           pass

                        elif ("Staffadd " in msg.text):
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff[target] = True
                                           f=codecs.open('staff.json','w','utf-8')
                                           json.dump(staff, f, sort_keys=True, indent=4,ensure_ascii=False)
                                           samudra.sendMessage(to,"Add Staff ✔ By " + samudra.getContact(sender).displayName)
                                       except:
                                           pass

                        elif ("Admindell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin.remove(target)
                                           samudra.sendMessage(to,"Admin Expelled ✔ By " + samudra.getContact(sender).displayName)
                                       except:
                                           pass

                        elif ("Staffdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del staff[target]
                                           f=codecs.open('staff.json','w','utf-8')
                                           json.dump(staff, f, sort_keys=True, indent=4,ensure_ascii=False)
                                           samudra.sendMessage(to,"Staff Expelled ✔ By " + samudra.getContact(sender).displayName)
                                       except:
                                           pass

                        elif cmd == "refresh":
                            if msg._from in admin:
                                SamColi["addadmin"] = False
                                SamColi["delladmin"] = False
                                SamColi["addstaff"] = False
                                SamColi["dellstaff"] = False
                                SamColi["addbots"] = False
                                SamColi["dellbots"] = False
                                SamColi["wblacklist"] = False
                                SamColi["dblacklist"] = False
                                SamColi["Talkwblacklist"] = False
                                SamColi["Talkdblacklist"] = False
                                Setmain["RAfoto"] = False
                                settings["changePicture"] = False
                                samudra.sendMessage(msg.to," ✔ Aborting from bots ♩")

                        elif cmd == "mycrit" or text.lower() == 'mycrot':
                            if msg._from in admin:
                                ma = ""
                                for i in Bots:
                                    ma = samudra.getContact(i)
                                    samudra.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#===========COMMAND ON OFF============#
                        elif cmd == "unsend on" or text.lower() == 'unsend on':
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["cekUnsend"] = True
                                sendMention(msg.to, sender, "User ", "\n ✔ Silahkan unsend pesannya,\nKetik unsend off jika sudah slesai")

                        elif cmd == "unsend off" or text.lower() == 'unsend off':
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["cekUnsend"] = False
                                sendMention(msg.to, sender, "User ", " \n 🚫 Deteksi unsend dinonaktifkan")
                                
                        elif cmd == "timeline on" or text.lower() == 'timeline on':
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                SamColi["Timeline"] = True
                                samudra.sendMessage(msg.to," ✔ Check Timeline actived ")

                        elif cmd == "timeline off" or text.lower() == 'timeline off':
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                SamColi["Timeline"] = False
                                samudra.sendMessage(msg.to," 🚫 Check Timeline Nonactived ")
                                
                        elif cmd == "invite on" or text.lower() == 'invite on':
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                SamColi["invite"] = True
                                samudra.sendMessage(msg.to," ✔ Invte by Contact actived ")

                        elif cmd == "invite off" or text.lower() == 'invite off':
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                SamColi["invite"] = False
                                samudra.sendMessage(msg.to,"🚫 Nonactived ")
                                
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                SamColi["mentionKick"] = True
                                samudra.sendMessage(msg.to,"✔ Responkick Actived")

                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                SamColi["mentionKick"] = False
                                samudra.sendMessage(msg.to,"🚫Nonactived")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                SamColi["contact"] = True
                                samudra.sendMessage(msg.to," ✔ Check Contact actived ")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                SamColi["contact"] = False
                                samudra.sendMessage(msg.to,"?? Deteksi contact dinonaktifkan")

                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                SamColi["detectMention"] = True
                                samudra.sendMessage(msg.to,"✔Auto respon actived")

                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                SamColi["detectMention"] = False
                                samudra.sendMessage(msg.to,"🚫 Auto respon dinonaktifkan")

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoin"] = True
                                samudra.sendMessage(msg.to,"✔ Autojoin actived")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoin"] = False
                                samudra.sendMessage(msg.to,"🚫 Autojoin telah dinonaktifkan")
                                
                        elif cmd == "autoread off" or text.lower() == 'auto read off':
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                SamColi["autoRead"] = False
                                samudra.sendMessage(msg.to," 🚫 AutoRead telah dinonaktifkan")

                        elif cmd == "autoread on" or text.lower() == 'auto read on':
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                SamColi["autoRead"] = True
                                samudra.sendMessage(msg.to,"  ✔ AutoRead telah diaktifkan")
                                
                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                SamColi["autoLeave"] = True
                                samudra.sendMessage(msg.to," ✔ Autoleave telah diaktifkan")
                                
                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                SamColi["autoLeave"] = False
                                samudra.sendMessage(msg.to,"🚫 Autoleave Nonactived")
                                
                        elif cmd == "autoblock on" or text.lower() == 'block on':
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                SamColi["autoBlock"] = True
                                samudra.sendMessage(msg.to," ✔Autoblock Actived.....")

                        elif cmd == "autoblock off" or text.lower() == 'block off':
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                SamColi["autoBlock"] = False
                                samudra.sendMessage(msg.to," 🚫  Non Actived.....")                                
                        elif cmd == "autolike on" or text.lower() == 'like on':
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                SamColi["likeOn"] = True
                                samudra.sendMessage(msg.to," ✔ Autoalike Actived")
                        elif cmd == "autolike off" or text.lower() == 'like off':
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                SamColi["likeOn"] = False
                                samudra.sendMessage(msg.to," ✔ Autolike Nonactived")
                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                SamColi["autoAdd"] = True
                                samudra.sendMessage(msg.to,"✔ Autoadd telah diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                SamColi["autoAdd"] = False
                                samudra.sendMessage(msg.to,"🚫 Autoadd telah dinonaktifkan")

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                SamColi["stickerOn"] = True
                                samudra.sendMessage(msg.to," ✔ Check Sticker actived ")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                SamColi["stickerOn"] = False
                                samudra.sendMessage(msg.to," 🚫 Sticker check dinonaktifkan")

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = True
                                sendMention(msg.to, sender, " User ", "\n➪ Silahkan kirim link grupnya")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = False
                                samudra.sendMessage(msg.to," 🚫 Jointicket telah dinonaktifkan")
#============Chatbots================#
                        elif cmd == "chatbot on" or text.lower() == 'chatbots on':
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                SamColi["chatbot"] = True
                                samudra.sendMessage(msg.to,"✔ AutoChat Actived")
                                
                        elif cmd == "chatbot off" or text.lower() == 'chatbots off':
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                                SamColi["chatbot"] = False
                                sdmudra.sendMessage(msg.to," ↘ AutoChat 🚫 nonaktived")
                        
                        elif cmd == 'sepi':
                            if SamColi["chatbot"] == True:
                               samudra.sendMessage(to,"Hooh gara2 kk sih gak mandi (¬_¬)")
                               
                        elif cmd == 'naik':
                            if SamColi["chatbot"] == True:
                               samudra.sendMessage(to,"Moh ah takut di modusin (¬_¬)")

                        elif cmd == 'nah':
                            if SamColi["chatbot"] == True:
                               samudra.sendMessage(to,"Nah neh noh ¯\_(ツ)_/¯ ")                               
                               
                        elif cmd == 'siang':
                            if SamColi["chatbot"] == True:
                               samudra.sendMessage(to,"Iya kk Mat siang mat aktivitas (￣へ￣)") 

                        elif cmd == 'malam':
                            if SamColi["chatbot"] == True:
                               samudra.sendMessage(to,"Iya malam k waktunya bikin ╮(╯▽╰)╭")
                               
                        elif cmd == 'sp':
                            if SamColi["chatbot"] == True:
                               samudra.sendMessage(to," 🔀 Internet gratisan ¯\_(ツ)_/¯")
                               samudra.sendMessage(to,"↘0.005076800537109375 Perdetik")
                               
                        elif cmd == 'assalamualaikum':
                            if SamColi["chatbot"] == True:
                               samudra.sendMessage(to," Waalaikumsalam ")
                               samudra.sendMessage(to,"Σ(O_O；)")

                        elif cmd == 'waalaikumsalam':
                            if SamColi["chatbot"] == True:
                               samudra.sendMessage(to," Moga yg jwb salam jodoh nya banyak ")
                               samudra.sendMessage(to,"╮(╯▽╰)╭ ")

                        elif cmd == 'typo':
                            if SamColi["chatbot"] == True:
                               samudra.sendMessage(to," Tenggelamkan ae yg Typo¯\_(ツ)_/¯")
                               samudra.sendMessage(to,"hehehe")                               
                             
                        elif cmd == 'kuy':
                            if SamColi["chatbot"] == True:
                               samudra.sendMessage(to," Kemana k ¯\_(ツ)_/¯")
       
                        elif cmd == 'pagi':
                            if SamColi["chatbot"] == True:
                               samudra.sendMessage(to,"Pagi juga kk Mandi gih biar gak jones terus ヽ(｀⌒´)ノ")
                               
                        elif cmd == 'halo':
                            if SamColi["chatbot"] == True:
                               samudra.sendMessage(to,"Halo juga kk apa kabar ?Σ(⊙▽⊙) ")
                               
                        elif cmd == 'oke':
                            if SamColi["chatbot"] == True:
                               samudra.sendMessage(to,"Oke aja deh gue daripada bonyok (╥_╥)")
#===========COMMAND BLACKLIST============#

                        elif cmd == "blc" or text.lower() == 'blacklist':
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                              if SamColi["blacklist"] == {}:
                                    samudra.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in SamColi["blacklist"]:
                                        ma = samudra.getContact(i)
                                        samudra.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)
                        elif cmd == "ampuni" or cmd == "maafin":
                          if SamColi["selfbot"] == True:
                            if msg._from in admin:
                              samudra.sendMessage(msg.to,"↘Di Ampuni~ {} ~Tersangka.".format(str(len(wait["blacklist"]))))
                              SamColi["blacklist"] = {}                               
#===========COMMAND SET TEXT============#
                        elif 'Set pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  samudra.sendMessage(msg.to, "➪Gagal mengganti Pesan Msg")
                              else:
                                  SamColi["message"] = spl
                                  samudra.sendMessage(msg.to, "➪Pesan Msg diganti jadi :\n\n{}".format(str(spl)))

                        elif 'Set welcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  samudra.sendMessage(msg.to, " ➪Gagal mengganti Welcome Msg")
                              else:
                                  SamColi["welcome"] = spl
                                  samudra.sendMessage(msg.to, "➪Welcome Msg diganti jadi :\n\n{}".format(str(spl)))

                        elif 'Set leave: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set leave: ','')
                              if spl in [""," ","\n",None]:
                                  samudra.sendMessage(msg.to, "➪Gagal mengganti Leave Msg")
                              else:
                                  SamColi["leave"] = spl
                                  samudra.sendMessage(msg.to, "➪Leave Msg diganti jadi :\n\n{}".format(str(spl)))

                        elif 'Set respon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  samudra.sendMessage(msg.to, "➪Gagal mengganti Respon Msg")
                              else:
                                  SamColi["Respontag"] = spl
                                  samudra.sendMessage(msg.to, "➪ Respon Msg diganti jadi :\n\n{}".format(str(spl)))
                        elif 'Set ciluk: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set ciluk: ','')
                              if spl in [""," ","\n",None]:
                                  samudra.sendMessage(msg.to, "Gagal mengganti Sider Msg")
                              else:
                                  SamColi["mention"] = spl
                                  samudra.sendMessage(msg.to, "➪Sider Msg diganti jadi :\n\n{}".format(str(spl)))
                                  
                        elif 'Set tag: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set tag: ','')
                              if spl in [""," ","\n",None]:
                                  samudra.sendMessage(msg.to, "Gagal mengganti Key mention all member")
                              else:
                                  SamColi["tagall"] = spl
                                  samudra.sendMessage(msg.to, "key mention member ~ :\n\n{}".format(str(spl)))
 
#==================#  
                        elif cmd == "cancelall":
                          if msg._from in admin:
                            if msg.toType == 2:
                                group = samudra.getGroup(to)
                                if group.invitee is None or group.invitee == []:
                                    samudra.sendMessage(to, "Nothing")
                                else:
                                    invitee = [contact.mid for contact in group.invitee]
                                    for inv in invitee:
                                        samudra.cancelGroupInvitation(to, [inv])
                                        time.sleep(1)
                                    samudra.sendMessage(to, "Canceled {} user".format(str(len(invitee))))
                        elif cmd == "nuke":
                          if msg._from in admin:
                            if msg.toType == 2:
                                group = samudra.getGroup(to)
                                gMembers = [contact.mid for contact in group.members]
                                for i in gMembers:
                                    time.sleep(0.008)
                                    samudra.kickoutFromGroup(to,[i])
                                samudra.sendMessage(to,"Casual Cleasing")
                            else:
                                samudra.sendMessage(to,"failed >_<")

    except Exception as error:
        print (error)
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                oepoll.setRevision(op.revision)
                thread = threading.Thread(target=bot, args=(op,))
                thread.start()
    except Exception as e:
        print(e)
#==============Samudra Bots===========#
print ("============[Login Bot Samudra Sukses]==========")
thread1 = threading.Thread(target=bot1run)
thread2 = threading.Thread(target=bot2run)
thread3 = threading.Thread(target=bot3run)
thread4 = threading.Thread(target=bot4run)
thread1.start()
thread2.start()
thread3.start()
thread4.start()









