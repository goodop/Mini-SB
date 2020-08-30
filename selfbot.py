# -*- coding: utf-8-*-
from Goperation.linepy import *
from Goperation.akad import *
from time import sleep
from gtts import gTTS
from datetime import datetime
from bs4 import BeautifulSoup
from Liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, six, ast, pytz, urllib, urllib3, urllib.parse, traceback, atexit, wikipedia, subprocess, errno, asyncio
with open('token.json', 'r') as fp:
    connecting = json.load(fp)
if connecting['token'] == "":client = LINE("bangsatline@gmail.com","Bangsat11")
else:client=LINE(idOrAuthToken=connecting['token'])
with open('cctv.json', 'r') as fp:
    cctv = json.load(fp)
with open('setting.json', 'r') as fp:
    manage = json.load(fp)
#================================================================================#

#================================================================================#
client.log("User Token: {}\n────────────────────────────────────────────────────────────────".format(str(client.authToken)))
clientMid = client.profile.mid
clientProfile = client.getProfile()
clientSettings = client.getSettings()
clientPoll = OEPoll(client)
botStart = time.time()
msg_dict = {}
msg_send = {}
lcol = "#800000"
tcol = "#ffffff"
botkey = manage["keyname"]
protectMax = manage["proMax"]
protectStaff = manage["proStaff"]
Goperation = client.getContact(manage["dontRemove"]).mid
Gopera = manage["dontRemove1"]
settings = {
   "addwhitelist": False,
   "delwhitelist": False,
   "addblacklist": False,
   "delblacklist": False,
   "footer": True,
   "autoTicket": False,
   "logout": False,
    "setKey": False,
    "ChangeVideoProfile": False,
    "ChangeVideoProfile2": False,
    "changePictureProfile": False,
    "changeGroupPicture": {}
}
#================================================================================#

#================================================================================#
def restartBot():
    print ("[ INFO ] BOT RESTART")
    python = sys.executable
    os.execl(python, python, *sys.argv)
def cTime_to_datetime(unixtime):
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    return datetime.fromtimestamp(str(timeNow))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Hours %02d Minute %02d Secs' % (hours, mins, secs)      
def waktuReb(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d' % (secs)      
def gbirth(id,to,text):
    date = "%d-%m-%Y"
    timer = "%H:%M:%S"
    datecrt = time.strftime("Mini Selfbot:\n@! it, \nGroup created:\n  • Date:{}\n  • Time:{}".format(str(date),timer), time.localtime(int(text.createdTime) / 1000))
    client.sendReplyMention(id,to,datecrt,"",[Goperation])
def time_converter(time):
    converted_time = datetime.datetime.fromtimestamp(
        int(time)
    ).strftime('%I:%M %p')
    return converted_time    
def allowLiff():
    url = 'https://access.line.me/dialog/api/permissions'
    data = {
        'on': [
            'P',
            'CM'
        ],
        'off': []
    }
    headers = {
        'X-Line-Access': client.authToken,
        'X-Line-Application': client.server.APP_NAME,
        'X-Line-ChannelId': '1602876096',
        'Content-Type': 'application/json'
    }
    requests.post(url, json=data, headers=headers)
def sendFooter(to,text):
       ang = Gopera
       itu = Goperation
       ultraman = "https://thumbs.gfycat.com/DirectUnkemptLeafwing-size_restricted.gif"
       cosmos = {"type": "text","text":text,"sentBy": {"label": "{}".format(client.getContact(itu).displayName),"iconUrl": ultraman,"linkUrl": ang}}
       client.sendTemp(to, cosmos)
def imageFooter(to,image):
       ang = Gopera
       itu = Goperation
       ultraman = "https://thumbs.gfycat.com/DirectUnkemptLeafwing-size_restricted.gif"
       cosmos = {"type":"image","originalContentUrl":"{}".format(image),"previewImageUrl":"{}".format(image),"animated":True,"extension":"jpg","sentBy":{"label": "{}".format(client.getContact(itu).displayName),"iconUrl":"{}".format(ultraman),"linkUrl":ang}}
       client.sendTemp(to, cosmos)
def sendOpera(to, profile):
    try:
        goperation = "https://obs.line-scdn.net/" + profile.pictureStatus
    except:
    	goperation = "https://obs.line-scdn.net/0hP_lfR1H3D3BRHyeUYWFwJ21aAR0mMQk4KSsXRX0bVxQoLRwgOH5FFnQeURAoJ0khbXhGEndLVBV6"
    opera1 = {
  "type": "bubble",
  "size": "kilo",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "size": "md",
        "aspectMode": "cover",
        "aspectRatio": "1.30:1.26",
        "url": goperation,
        "position": "absolute",
        "align": "center",
        "offsetTop": "8px",
        "offsetStart": "2px",
        "action": {
          "type": "uri",
          "uri": goperation
        }
      },
      {
        "type": "image",
        "aspectMode": "cover",
        "aspectRatio": "2.40:2.10",
        "offsetTop": "0px",
        "offsetBottom": "0.5px",
        "offsetStart": "2px",
        "offsetEnd": "2px",
        "size": "full",
        "gravity": "top",
        "url": "https://i.ibb.co/cJqyvG1/20200507-224553.png"
      }
    ],
    "paddingAll": "0px",
    "spacing": "none",
    "backgroundColor": "#000000",
    "height": "245px",
    "width": "260px"
  },
  "action": {
    "type": "uri",
    "uri": "https://www.jurustupai.com/2020/05/cara-membuat-simple-selfbot-template.html?m=1" #jangan di hapus
  }
  }
    opera2 = {
  "type": "bubble",
  "size": "kilo",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "size": "md",
        "aspectMode": "cover",
        "aspectRatio": "1.30:1.26",
        "url": goperation,
        "position": "absolute",
        "align": "center",
        "offsetTop": "8px",
        "offsetStart": "2px",
        "action": {
          "type": "uri",
          "uri": goperation
        }
      },
      {
        "type": "image",
        "aspectMode": "cover",
        "aspectRatio": "2.40:2.10",
        "offsetTop": "0px",
        "offsetBottom": "0.5px",
        "offsetStart": "2px",
        "offsetEnd": "2px",
        "size": "full",
        "gravity": "top",
        "url": "https://i.ibb.co/LRjXWjN/20200507-225055.png"
      }
    ],
    "paddingAll": "0px",
    "spacing": "none",
    "backgroundColor": "#000000",
    "height": "245px",
    "width": "260px"
  },
  "action": {
    "type": "uri",
    "uri": "https://www.jurustupai.com/2020/05/cara-membuat-simple-selfbot-template.html?m=1" #jangandihapus
  }
}

    opera3 = {
  "type": "bubble",
  "size": "kilo",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "size": "md",
        "aspectMode": "cover",
        "aspectRatio": "1.30:1.26",
        "url": goperation,
        "position": "absolute",
        "align": "center",
        "offsetTop": "8px",
        "offsetStart": "2px",
        "action": {
          "type": "uri",
          "uri": goperation
        }
      },
      {
        "type": "image",
        "aspectMode": "cover",
        "aspectRatio": "2.40:2.10",
        "offsetTop": "0px",
        "offsetBottom": "0.5px",
        "offsetStart": "2px",
        "offsetEnd": "2px",
        "size": "full",
        "gravity": "top",
        "url": "https://i.ibb.co/98f2Qcy/20200507-224745.png"
      }
    ],
    "paddingAll": "0px",
    "spacing": "none",
    "backgroundColor": "#000000",
    "height": "245px",
    "width": "260px"
  },
  "action": {
    "type": "uri",
    "uri": "https://www.jurustupai.com/2020/05/cara-membuat-simple-selfbot-template.html?m=1"#jangandihapus
  }
}
    opera = [opera1,opera2,opera3]
    senorita = {"type": "flex","altText": "The G - Operation","contents": {"type": "carousel","contents": opera}}
    client.sendTemp(to,senorita)
 
def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@Angopera "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    
def clientBot(op):
    try:
        if op.type == 0:
            return
        if settings["logout"] == True:
            sys.exit()
        if op.type == 26:
            msg = op.message            
            runS = botStart - time.time() 
            if waktuReb(runS) == waktuReb(5):
                if manage["target"] != {}:
                   client.sendMessage(msg.to,manage["target"],"Bot active again")
                   manage["target"] = {}
            else:pass
        if op.type == 55:
            try:
                if op.param1 in cctv['Point']:   
                    if op.param2 not in cctv['Point3'][op.param1]:
                       try:uprofile = "https://obs.line-scdn.net/" + client.getContact(op.param2).pictureStatus
                       except:uprofile = "https://imagizer.imageshack.com/v2/377x338q90/922/Z9ocJr.jpg"
                       Minum = client.getContact(op.param2).displayName
                       reading = {"type": "flex","altText": "Kesayangan membaca obrolan.","contents":{"type": "carousel","contents": [{"type": "bubble","size": "nano","body": {"type": "box","layout": "vertical","contents": [{"type": "image","url": uprofile,"size": "full","aspectMode": "cover","aspectRatio": "2:2.70","gravity": "top"},{"type": "box","layout": "vertical","contents": [{"type": "box","layout": "vertical","contents": [{"type": "text","text": "• " + Minum,"size": "xs","color": "#ffffff","weight": "bold","offsetBottom": "2px","offsetTop": "1px","offsetStart": "-1px","wrap": False,"align": "start"}],"position": "relative"},{"type": "text","text": "Hello,","size": "xs","weight": "bold","maxLines": 20,"align": "start","position": "absolute","offsetTop": "0px","offsetBottom":"-5px","gravity": "top","offsetStart": "3px","color": "#F10202"}],"position": "absolute","offsetBottom": "0px","offsetStart": "0px","offsetEnd": "0px","paddingAll": "16px","paddingTop": "12px","backgroundColor": "#000000"},{"type": "box","layout": "vertical","contents": [{"type": "text","text": "Reader","color": "#ffffff","align": "center","size": "xxs","offsetTop": "0px"}],"position": "absolute","cornerRadius": "20px","offsetTop": "8px","backgroundColor": "#ff334b","offsetStart": "7px","height": "15px","width": "40px"}],"paddingAll": "0px","offsetTop": "0px","offsetBottom": "20px","position": "relative"}}]}}
                       if settings["footer"] == True:client.sendTemp(op.param1,reading)
                       else:sendMention(op.param1,"Read by:\n• @!",[op.param2])
                       cctv['Point3'][op.param1][op.param2] = True
                       with open('cctv.json', 'w') as fp:
                           json.dump(cctv, fp, sort_keys=True, indent=4)
                    else:
                    	pass
                else:
                    pass
            except Exception as error:client.sendMessage(msg.to, "{}".format(str(error)))

        if op.type == 55:
            try:
                if op.param1 in cctv['readPoint']:
                    if op.param2 in cctv['readMember'][op.param1]:
                        pass
                    else:
                        cctv['readMember'][op.param1] += op.param2
                        cctv['ROM'][op.param1][op.param2] = op.param2
                        with open('cctv.json', 'w') as fp:
                            json.dump(cctv, fp, sort_keys=True, indent=4)
                else:pass
            except:pass

        if op.type == 19:
            if op.param3 in clientMid:
                if op.param2 not in manage["whitelist"]:
                   manage["blacklist"][op.param2] = True
                   with open('setting.json', 'w') as fp:
                      json.dump(manage, fp, sort_keys=True, indent=4)                  

        if op.type == 19:
           if op.param1 in protectStaff:
               if op.param3 in manage["whitelist"]:
                   if op.param2 not in manage["whitelist"]:
                      manage["blacklist"][op.param2] = True
                      with open('setting.json', 'w') as fp:
                          json.dump(manage, fp, sort_keys=True, indent=4)                  
                      try:
                         client.kickoutFromGroup(op.param1,[op.param2])
                         client.findAndAddContactsByMid(op.param3)
                         client.inviteIntoGroup(op.param1,[op.param3])
                      except:pass
                   else:pass               
               else:pass

        if op.type == 17:
           if manage["welcome"] == True:
               if op.param2 not in manage["blacklist"]:
                   jangan = client.getGroup(op.param1)
                   if op.param1 in manage["welcomsg"]:
                      ngentu = "Hi @! \nWelcome to " + jangan.name + "\n" + manage["welcomeSet"][op.param1]
                      sendMention(op.param1,ngentu,[op.param2])
                      client.sendContact(op.param1,Goperation)
                   else:
                      ngentu = "Hi @! \nWelcome to " + jangan.name 
                      sendMention(op.param1,ngentu,[op.param2])
                      client.sendContact(op.param1,Goperation)

        if op.type == 15:
           if manage["leave"] == True:
               if op.param2 not in manage["blacklist"]:
                   jangan = client.getGroup(op.param1)
                   if manage["leaveSet"] !="":
                      ngentu = "Good bye @! \n" + manage["leavemsg"]
                      sendMention(op.param1,ngentu,[op.param2])
                   else:
                      ngentu = "Good bye @! "
                      sendMention(op.param1,ngentu,[op.param2])

        if op.type == 5:
           if manage["adders"] == True:
               if op.param2 not in manage["blacklist"]:
                   if manage["addmsg"] == "":sendMention(op.param2,"Hi @! \nThank u for add me :)",[op.param2])
                   else:
                      text = "Hi @! \n" + manage["addmsg"]
                      sendMention(op.param2,text,[op.param2])

        if op.type == 19:
           if op.param1 in protectMax:
               if op.param2 not in manage["whitelist"]:
                  manage["blacklist"][op.param2] = True
                  with open('setting.json', 'w') as fp:
                      json.dump(manage, fp, sort_keys=True, indent=4)                  
                  try:
                      client.kickoutFromGroup(op.param1,[op.param2])
                      client.findAndAddContactsByMid(op.param3)
                      client.inviteIntoGroup(op.param1,[op.param3])
                  except:pass
               else:pass

        if op.type == 17 or op.type == 13 or op.type == 55:
          if op.param1 in protectMax:
            if op.param2 in manage["blacklist"]:
                try:client.kickoutFromGroup(op.param1,[op.param2])
                except:pass

        if op.type == 13:
           if op.param1 in protectMax:
               if op.param2 not in manage["whitelist"]:
                  manage["blacklist"][op.param2] = True
                  with open('setting.json', 'w') as fp:
                    json.dump(manage, fp, sort_keys=True, indent=4)
                  try:client.kickoutFromGroup(op.param1,[op.param2])                                         
                  except:pass
                  mbul = client.getGroup(op.param1)
                  no = 0
                  for a in mbul.invitee:
                      if a.mid in op.param3:
                          if no > 10:pass
                          else:
                             try:
                               no = (no+1)
                               client.cancelGroupInvitation(op.param1,[a.mid])
                               time.sleep(0.04)
                             except:pass
                  for b in mbul.members:
                      if b.mid in op.param3:
                          try:client.kickoutFromGroup(op.param1,[b.mid])
                          except:pass
               else:
                  mbul = client.getGroup(op.param1)
                  for a in mbul.invitee:
                      if a.mid in op.param3:
                          if a.mid in manage["blacklist"]:
                             try:
                                client.cancelGroupInvitation(op.param1,[a.mid])
                                client.sendMessage(msg.to,"Caution!, user in blacklist")
                             except:pass
                          else:pass
                  for b in mbul.members:
                      if b.mid in op.param3:
                          if b.mid in manage["blacklist"]:
                              try:client.kickoutFromGroup(op.param1,[b.mid])
                              except:pass

        if op.type == 32:
           if op.param1 in protectMax:
               if op.param2 not in manage["whitelist"]:
                  manage["blacklist"][op.param2] = True
                  with open('setting.json', 'w') as fp:
                    json.dump(manage, fp, sort_keys=True, indent=4)
                  try:
                     client.kickoutFromGroup(op.param1,[op.param2])                     
                     client.findAndAddContactsByMid(op.param3)
                     client.inviteIntoGroup(op.param1,[op.param3])
                  except:pass                   

        if op.type == 11:
           if op.param1 in protectMax and op.param3 == "4":
               if op.param2 not in manage["whitelist"]:
                   manage["blacklist"][op.param2] = True
                   with open('setting.json', 'w') as fp:
                      json.dump(manage, fp, sort_keys=True, indent=4)
                   hoax = client.getGroup(op.param1)
                   if hoax.preventedJoinByTicket == False:
                      abc = client.getGroup(op.param1)
                      abc.preventedJoinByTicket = True
                      client.updateGroup(abc)
                      try:client.kickoutFromGroup(op.param1,[op.param2])
                      except:pass
               else:
                  hoax = client.getGroup(op.param1)
                  if hoax.preventedJoinByTicket == False:
                     abc = client.getGroup(op.param1)
                     abc.preventedJoinByTicket = True
                     client.updateGroup(abc)                  

        if op.type == 11:
           if op.param1 in protectMax and op.param3 == "1":
               if op.param2 not in manage["whitelist"]:
                   manage["blacklist"][op.param2] = True
                   with open('setting.json', 'w') as fp:
                      json.dump(manage, fp, sort_keys=True, indent=4)
                   hoax = client.getGroup(op.param1).name
                   if hoax not in manage["gname"][op.param1]:
                      abc = client.getGroup(op.param1)
                      abc.name = manage["gname"][op.param1]
                      client.updateGroup(abc)
                      try:client.kickoutFromGroup(op.param1,[op.param2])
                      except:pass
               else:
                  abc = client.getGroup(op.param1).name                     
                  manage["gname"][op.param1] = abc
                  with open('setting.json', 'w') as fp:
                     json.dump(manage, fp, sort_keys=True, indent=4)


        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
               if settings["addwhitelist"] == True:
                   if msg.contentMetadata["mid"] not in clientMid:
                      if msg.contentMetadata["mid"] in manage["whitelist"]:
                          client.sendMessage(msg.to,"{} already in whitelist.".format(client.getContact(msg.contentMetadata["mid"]).displayName))
                          settings["addwhitelist"] = False
                      else:
                          if msg.contentMetadata["mid"] not in manage["blacklist"]:
                             manage["whitelist"][msg.contentMetadata["mid"]] = True
                             with open('setting.json', 'w') as fp:
                                json.dump(manage, fp, sort_keys=True, indent=4)
                             client.sendMessage(msg.to,"{} added in whitelist.".format(client.getContact(msg.contentMetadata["mid"]).displayName))
                             settings["addwhitelist"] = False
                          else:client.sendMessage(msg.to,"[ Failed ]\nuser in blacklist.")
                          settings["addwhitelist"] = False
               if settings["delwhitelist"] == True:
                   if msg.contentMetadata["mid"] not in clientMid:
                      if msg.contentMetadata["mid"] in manage["whitelist"]:
                         del manage["whitelist"][msg.contentMetadata["mid"]]
                         with open('setting.json', 'w') as fp:
                            json.dump(manage, fp, sort_keys=True, indent=4)
                         client.sendMessage(msg.to,"{} removed from whitelist.".format(client.getContact(msg.contentMetadata["mid"]).displayName))
                         settings["delwhitelist"] = False
                      else:client.sendMessage(msg.to,"[ Failed ]\nuser not in whitelist.")
                      settings["delwhitelist"] = False
               if settings["addblacklist"] == True:
                   if msg.contentMetadata["mid"] not in clientMid:
                      if msg.contentMetadata["mid"] in manage["blacklist"]:
                          client.sendMessage(msg.to,"{} already in blacklist.".format(client.getContact(msg.contentMetadata["mid"]).displayName))
                          settings["addblacklist"] = False
                      else:
                          if msg.contentMetadata["mid"] not in manage["whitelist"]:
                             manage["blacklist"][msg.contentMetadata["mid"]] = True
                             with open('setting.json', 'w') as fp:
                                json.dump(manage, fp, sort_keys=True, indent=4)
                             client.sendMessage(msg.to,"{} added in blacklist.".format(client.getContact(msg.contentMetadata["mid"]).displayName))
                             settings["addblacklist"] = False
                          else:client.sendMessage(msg.to,"[ Failed ]\nuser in whitelist.")
                          settings["addblacklist"] = False
               if settings["delblacklist"] == True:
                   if msg.contentMetadata["mid"] not in clientMid:
                      if msg.contentMetadata["mid"] in manage["blacklist"]:
                         del manage["blacklist"][msg.contentMetadata["mid"]]
                         with open('setting.json', 'w') as fp:
                            json.dump(manage, fp, sort_keys=True, indent=4)
                         client.sendMessage(msg.to,"{} removed from blacklist.".format(client.getContact(msg.contentMetadata["mid"]).displayName))
                         settings["delblacklist"] = False
                      else:client.sendMessage(msg.to,"[ Failed ]\nuser not in blacklist.")
                      settings["delblacklist"] = False

        if op.type == 25:
            try:
                msg = op.message
                msg.to = msg.to
                msg_id = msg.id
                if msg.toType == 0 or msg.toType == 2:
                 if msg.contentType == 2:      	
                    if settings['ChangeVideoProfile'] == True:
                        client.downloadObjectMsg(msg.id,'path','video.mp4')
                        print('[NOTIF] VIDEO PROFILE PROCESSING')
                        client.sendMessage(msg.to, "Send picture to be profiled")
                        settings['ChangeVideoProfile']=False
                        settings['ChangeVideoProfile2']=True
                 if msg.contentType == 1: 
                    if settings['ChangeVideoProfile2'] == True:
                       client.downloadObjectMsg(msg.id,'path','foto.jpg')
                       client.updateProfileVideoPicture('video.mp4','foto.jpg')
                       print('[NOTIF] UPDATE PROFILE VIDEO SUCCES')
                       client.sendMessage(msg.to, 'Success change profile video.')
                       client.deleteFile('path')
                       settings['ChangeVideoProfile2']=False
                    if settings["changePictureProfile"] == True:
                       path = client.downloadObjectMsg(msg_id)
                       settings["changePictureProfile"] = False
                       client.updateProfilePicture(path)
                       client.deleteFile(path)
                       client.sendMessage(msg.to, "Profile image updated.")                                             
                    if msg.to in settings["changeGroupPicture"]:
                       path = client.downloadObjectMsg(msg_id)
                       del settings["changeGroupPicture"][msg.to]
                       client.updateGroupPicture(msg.to, path)
                       client.deleteFile(path)
                       client.sendMessage(msg.to, "Group image updated.")
            except Exception as error:
                client.sendMessage(msg.to, "{}".format(str(error))) 
                traceback.print_tb(error.__traceback__)                
        if op.type == 25:
            try:
                msg = op.message
                ang = msg.text
                msg_id = msg.id
                msg.to = msg.to
                msg._from = msg._from
                if manage["keyname"] =="":key = ""
                else:key = manage["keyname"] + " "
                if msg.toType == 0 or msg.toType == 2:
                 if msg.contentType == 0:
                    if ang is None:
                    	pass
                    else:                    	
                        if ang.lower() == "help":
                           if manage["keyname"]  !="":
                              client.sendReplyMessage(msg.id,msg.to,"Gunalan key anda!\nContoh: {} Help".format(manage["keyname"].title()))
                           else:pass
                        if ang.lower() == key + "help":
                           if manage["keyname"]=="":gop= ""
                           else: gop = manage["keyname"].title() + " "
                           try:
                             ang_ = "  💻 G-Oᴘᴇʀᴀᴛɪᴏɴ 💻"
                             ang_ += "\n   「 Mini Selfbot 」"
                             ang_ += "\n\nMain Menu:"
                             ang_ += "\n  1. " + gop + "Getmenu"
                             ang_ += "\n  2. " + gop + "Selfmenu"
                             ang_ += "\n  3. " + gop + "Groupmenu"
                             ang_ += "\n  4. " + gop + "Groupsetting"
                             ang_ += "\n  5. " + gop + "Groupprotect"
                             ang_ += "\n\n• G-Operation V.02"
                             if settings["footer"] == True:sendFooter(msg.to,ang_)
                             else:client.sendReplyMessage(msg.id,msg.to,ang_)
                           except:pass
                        if ang.lower() == "getmenu":
                           if manage["keyname"]  !="":
                              client.sendReplyMessage(msg.id,msg.to,"Gunakan key anda!\nContoh: {} Getmenu".format(manage["keyname"].title()))
                           else:pass
                        if ang.lower() == key + "getmenu":
                           if manage["keyname"]=="":gop= ""
                           else: gop = manage["keyname"].title() + " "
                           try:
                             ang_ = "  💻 G-Oᴘᴇʀᴀᴛɪᴏɴ 💻"
                             ang_ += "\n   「 Mini Selfbot 」"
                             ang_ += "\n\nGet Menu:"
                             ang_ += "\n  1. " + gop + "Geturl"
                             ang_ += "\n  2. " + gop + "Getmid @"
                             ang_ += "\n  3. " + gop + "Getpict @"
                             ang_ += "\n  4. " + gop + "Getcover @"
                             ang_ += "\n  5. " + gop + "Getname @"
                             ang_ += "\n  6. " + gop + "Getstatus @"
                             ang_ += "\n  7. " + gop + "Getgroups @"
                             ang_ += "\n\n• G-Operation V.02"
                             if settings["footer"] == True:sendFooter(msg.to,ang_)
                             else:client.sendReplyMessage(msg.id,msg.to,ang_)
                           except:pass
                        if ang.lower() == "selfmenu":
                           if manage["keyname"]  !="":
                              client.sendReplyMessage(msg.id,msg.to,"Gunakan key anda!\nContoh: {} Selfmanage".format(manage["keyname"].title()))
                           else:pass
                        if ang.lower() == key + "selfmenu":
                           if manage["keyname"]=="":gop= ""
                           else: gop = manage["keyname"].title() + " "
                           try:
                             ang_ = "  💻 G-Oᴘᴇʀᴀᴛɪᴏɴ 💻"
                             ang_ += "\n   「 Mini Selfbot 」"
                             ang_ += "\n\nSelf Menu:"
                             ang_ += "\n  1. " + gop + "Me"
                             ang_ += "\n  2. " + gop + "Help"
                             ang_ += "\n  3. " + gop + "Speed"
                             ang_ += "\n  4. " + gop + "Reboot"
                             ang_ += "\n  6. " + gop + "Logout"
                             ang_ += "\n  5. " + gop + "Runtime"
                             ang_ += "\n  7. " + gop + "Allowliff"
                             ang_ += "\n  4. " + gop + "Updatebio:"
                             ang_ += "\n  6. " + gop + "Updatepict"
                             ang_ += "\n  5. " + gop + "Updatedual"
                             ang_ += "\n  7. " + gop + "Updatename:"
                             ang_ += "\n\n• G-Operation V.02"
                             if settings["footer"] == True:sendFooter(msg.to,ang_)
                             else:client.sendReplyMessage(msg.id,msg.to,ang_)
                           except:pass
                        if ang.lower() == "groupmenu":
                           if manage["keyname"]  !="":
                              client.sendReplyMessage(msg.id,msg.to,"Gunakan key anda!\nContoh: {} Groupmenu".format(manage["keyname"].title()))
                           else:pass
                        if ang.lower() == key + "groupmenu":
                           if manage["keyname"]=="":gop= ""
                           else: gop = manage["keyname"].title() + " "
                           try:
                             ang_ = "  💻 G-Oᴘᴇʀᴀᴛɪᴏɴ 💻"
                             ang_ += "\n   「 Mini Selfbot 」"
                             ang_ += "\n\nGroup Menu:"
                             ang_ += "\n  1. " + gop + "/Bye"
                             ang_ += "\n  2. " + gop + "Ginfo"
                             ang_ += "\n  3. " + gop + "Gbirth"
                             ang_ += "\n  4. " + gop + "Mention"
                             ang_ += "\n  5. " + gop + "Gcreator"
                             ang_ += "\n  6. " + gop + "Groupid"
                             ang_ += "\n  7. " + gop + "Grouppict"
                             ang_ += "\n  8. " + gop + "Grouplist"
                             ang_ += "\n  9. " + gop + "Friendlist"
                             ang_ += "\n  10. " + gop + "Memberlist"
                             ang_ += "\n  11. " + gop + "Pendinglist"
                             ang_ += "\n\nGroup Option:"
                             ang_ += "\n  12. " + gop + "Kickall"
#                          ang_ += "\n  13. " + gop + "Nukerjs" //Nanti Aja :v
#                          ang_ += "\n  14. " + gop + "Doublejs"//Nanti Aja :v
                             ang_ += "\n  13. " + gop + "Mykey"
                             ang_ += "\n  14. " + gop + "Kick @"
                             ang_ += "\n  15. " + gop + "Invite @"
                             ang_ += "\n  16. " + gop + "Resetkey"
                             ang_ += "\n  17. " + gop + "Setkey: txt"
#                          ang_ += "\n  18. " + gop + "Jskey set: txt" //Nanti Aja :v
#                          ang_ += "\n  19. " + gop + "Jscancel: txt" //Nanti Aja :v
                             ang_ += "\n  18. " + gop + "Nuke set: txt"
                             ang_ += "\n  19. " + gop + "Groupcast: txt"
                             ang_ += "\n  20. " + gop + "Groupname: txt"
                             ang_ += "\n\n• G-Operation V.02"
                             if settings["footer"] == True:sendFooter(msg.to,ang_)
                             else:client.sendReplyMessage(msg.id,msg.to,ang_)
                           except:pass
                        if ang.lower() == "groupsetting":
                           if manage["keyname"]  !="":
                              client.sendReplyMessage(msg.id,msg.to,"Gunakan key anda!\nContoh: {} Groupsetting".format(manage["keyname"].title()))
                           else:pass
                        if ang.lower() == key + "groupsetting":
                           if manage["keyname"]=="":gop= ""
                           else: gop = manage["keyname"].title() + " "
                           try:
                             ang_ = "  💻 G-Oᴘᴇʀᴀᴛɪᴏɴ 💻"
                             ang_ += "\n   「 Mini Selfbot 」"
                             ang_ += "\n\nGroup settings:"
                             ang_ += "\n  1. " + gop + "Settings"
                             ang_ += "\n  2. " + gop + "Lurk reset"
                             ang_ += "\n  3. " + gop + "Sider on/off"
                             ang_ += "\n  4. " + gop + "Lurk on/off"
                             ang_ += "\n  5. " + gop + "Join link: Url"
                             ang_ += "\n  6. " + gop + "Autojoin on/off"
                             ang_ += "\n  7. " + gop + "Jointicket on/off"
                             ang_ += "\n  8. " + gop + "Respon add: text"
                             ang_ += "\n  9. " + gop + "Add message on/off"
                             ang_ += "\n  10. " + gop + "Leavemsg set: text"
                             ang_ += "\n  11. " + gop + "Auto Leave on/off"
                             ang_ += "\n  12. " + gop + "Welcome set: text"
                             ang_ += "\n  13. " + gop + "Auto welcome on/off"
                             ang_ += "\n  14. " + gop + "Welcome msg on/off"
                             ang_ += "\n\n• G-Operation V.02"
                             if settings["footer"] == True:sendFooter(msg.to,ang_)
                             else:client.sendReplyMessage(msg.id,msg.to,ang_)
                           except:pass

                        if ang.lower() == "groupprotect":
                           if manage["keyname"]  !="":
                              client.sendReplyMessage(msg.id,msg.to,"Gunakan key anda!\nContoh: {} Groupprotect".format(manage["keyname"].title()))
                           else:pass
                        if ang.lower() == key + "groupprotect":
                           if manage["keyname"]=="":gop= ""
                           else: gop = manage["keyname"].title() + " "
                           try:
                             ang_ = "  💻 G-Oᴘᴇʀᴀᴛɪᴏɴ 💻"
                             ang_ += "\n   「 Mini Selfbot 」"
                             ang_ += "\n\nGroup Protect:"
                             ang_ += "\n  1. " + gop + "Protect staff"
                             ang_ += "\n  2. " + gop + "Protect max"
                             ang_ += "\n  3. " + gop + "Protect none"
                             ang_ += "\n  4. " + gop + "Add Whitelist"
                             ang_ += "\n  5. " + gop + "Dell Whitelist"
                             ang_ += "\n  6. " + gop + "Add Blacklist"
                             ang_ += "\n  7. " + gop + "Del Blacklist"
                             ang_ += "\n  8. " + gop + "Whitelisting"
                             ang_ += "\n  9. " + gop + "Blacklisting"
                             ang_ += "\n  10. " + gop + "Whitelist on @"
                             ang_ += "\n  11. " + gop + "Whitelist del @"
                             ang_ += "\n  12. " + gop + "Blacklist on @"
                             ang_ += "\n  13. " + gop + "Blacklist del @"
                             ang_ += "\n  14. " + gop + "Clearwhitelist"
                             ang_ += "\n  15. " + gop + "Clearblacklist"
                             ang_ += "\n  16. " + gop + "Findblacklist"
                             ang_ += "\n\n• G-Operation V.02"
                             if settings["footer"] == True:sendFooter(msg.to,ang_)
                             else:client.sendReplyMessage(msg.id,msg.to,ang_)
                           except:pass
#=============( G E T    M E N U    C O M M A N D)====================)                       
                        if ang.lower() == key +  "geturl":
                            if msg.toType == 2:
                                entot = client.getGroup(msg.to)
                                if entot.preventedJoinByTicket == True:
                                   entot.preventedJoinByTicket = False
                                   client.updateGroup(entot)
                                   set = client.reissueGroupTicket(msg.to)
                                   client.sendReplyMessage(msg.id,msg.to, "Group Ticket : \nhttps://line.me/R/ti/g/{}".format(str(set)))
                                else:
                                   client.updateGroup(entot)
                                   set = client.reissueGroupTicket(msg.to)
                                   client.sendReplyMessage(msg.id,msg.to, "Group Ticket : \nhttps://line.me/R/ti/g/{}".format(str(set)))                        
                        if ang.lower().startswith(key + "getmid "):
                           if msg.toType == 2:
                              key = eval(msg.contentMetadata["MENTION"])
                              key1 = key["MENTIONEES"][0]["M"]
                              mi = client.getContact(key1)
                              client.sendReplyMessage(msg.id,msg.to,key1)                        
                        if ang.lower().startswith(key + "getpict "):
                         if msg.toType == 2:
                           if msg.contentMetadata is not None:
                              targets = []
                              key = eval(msg.contentMetadata["MENTION"])
                              key["MENTIONEES"][0]["M"]
                              for x in key["MENTIONEES"]:
                                  targets.append(x["M"])
                              for target in targets:
                                  profile = client.getContact(target)
                                  angimg = "https://obs.line-scdn.net/" + profile.pictureStatus
                                  if settings["footer"] == True:imageFooter(msg.to,angimg)
                                  else:client.sendImageWithURL(msg.to, angimg)
                           else:client.sendReplyMessage(msg.id,msg.to,"No image found")                        
                        if ang.lower().startswith(key + "getcover "):
                         if msg.toType == 2:
                           if msg.contentMetadata is not None:
                              targets = []
                              key = eval(msg.contentMetadata["MENTION"])
                              key["MENTIONEES"][0]["M"]
                              for x in key["MENTIONEES"]:
                                  targets.append(x["M"])
                              for target in targets:
                                  profile = client.getContact(target)
                                  angimg = client.getProfileCoverURL(target)
                                  if settings["footer"] == True:imageFooter(msg.to,angimg)
                                  else:client.sendImageWithURL(msg.to, angimg)
                           else:client.sendReplyMessage(msg.id,msg.to,"No image found")
                        if ang.lower().startswith(key + "getstatus "):
                         if msg.toType == 2:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]
                            contact = client.getContact(key1)
                            if contact.statusMessage is None or contact.statusMessage =="":
                               client.sendReplyMessage(msg.id,msg.to,"Status not found.")
                            else:
                               client.sendReplyMessage(msg.id, msg.to, "「 Status Message 」\n" + contact.statusMessage)
                        if ang.lower().startswith(key + "getname "):
                         if msg.toType == 2:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]
                            contact = client.getContact(key1)
                            if contact.statusMessage is None or contact.displayName =="":
                               client.sendReplyMessage(msg.id,msg.to,"Display name not found.")
                            else:
                               client.sendReplyMessage(msg.id, msg.to, "「 Profile Name」\n" + contact.displayName)                        
                        if ang.lower().startswith("getgroups "):
                          if msg.toType == 2:
                             if 'MENTION' in msg.contentMetadata.keys() != None:                    
                               names = re.findall(r'@(\w+)', ang)
                               mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                               mentionees = mention['MENTIONEES']
                               ilike = client.getGroupIdsJoined()
                               mmk = client.getGroups(ilike)
                               becek = ""
                               no = 1
                               for mention in mentionees:
                                  for a in range(len(mmk)):
                                      eWee = [act.mid for act in mmk[a].members]
                                      if mention['M'] in eWee:
                                          becek += "\n     %i. " %no + mmk[a].name
                                          no = (no+1)
                               if becek == "":client.sendMessage(msg.to, "User Not found")                                  
                               else:
                                  tobat =  "• G-Oᴘᴇʀᴀᴛɪᴏɴ\n• Tracking user🔎\n\n   User found in:%s"%(becek)
                                  if settings["footer"] == True:sendFooter(msg.to,tobat)
                                  else:client.sendReplyMessage(msg.id, msg.to,tobat)
#=============( E N D   O F   G  E T    M E N U   )====================)




#=============( S E L F   M E N U  C O M M A N D )====================)
                        if ang.lower() == key + "me":                          
                            client.sendContact(msg.to,clientMid)
                        if ang.lower() == key + "me":
                            if msg.toType == 2:
                                haha = client.getContact(msg._from)
                                datax = {"type": "flex","altText": "G-Opera mengirim foto.","contents": {"type": "bubble","header": {"type": "box","layout": "vertical","contents": [{"type": "box","layout": "horizontal","contents": [{"type": "image","url":"https://obs.line-scdn.net/" + "{}".format(client.getContact(msg._from).pictureStatus),"size": "full","aspectMode": "cover","aspectRatio": "60:50","gravity": "center","flex": 1},{"type": "box","layout": "horizontal","contents": [{"type": "text","text": "Image","size": "xs","color": "#ffffff","align": "center","gravity": "center"}],"backgroundColor": "#EC3D44","paddingAll": "2px","paddingStart": "4px","paddingEnd": "4px","flex": 0,"position": "absolute","offsetStart": "18px","offsetTop": "18px","cornerRadius": "100px","width": "48px","height": "25px"}]}],"paddingAll": "0px"},"body": {"type": "box","layout": "vertical","contents": [{"type": "box","layout": "vertical","contents": [{"type": "box","layout": "vertical","contents": [{"type": "image","url": "https://imagizer.imageshack.com/v2/280x200q90/923/H1uMrZ.png","size": "full","aspectMode": "cover","aspectRatio": "80:25","gravity": "center","flex": 1}]}],"paddingAll": "13px","backgroundColor": "#000000","cornerRadius": "2px","margin": "xl"}],"paddingAll": "10px","backgroundColor": "#000000"}},}
                                client.sendTemp(msg.to,datax)
                        if ang.lower() == "reboot":
                           if manage["keyname"]  !="":
                              client.sendReplyMessage(msg.id,msg.to,"Gunakan key anda!\nContoh: {} Reboot".format(manage["keyname"].title()))
                           else:pass
                        if ang.lower() == key +  "reboot":
                            client.sendMessage(msg.to, "Bot rebooting..")
                            time.sleep(0.03)
                            client.sendMessage(msg.to, "Rebooted.")
                            restartBot()
                        if ang.lower() == key + "sp" or ang.lower() == key + "speed":
                             japri = time.time()
                             client.getProfile() 
                             ngegas = time.time() - japri
                             client.sendMessage(msg.to, "Time: %.4f"%(ngegas))
                        if ang.lower() == key + "runtime":
                           kopi = time.time() - botStart
                           ang = "Selfbot has been running for:\n"+waktu(kopi)
                           client.sendMessage(msg.to,ang)
                        if ang.lower() == key + "logout":
                           client.sendReplyMessage(msg.id,msg.to,"System shutdown. . .")
                           time.sleep(3)
                           client.sendMessage(msg.to,"Selfbot logout.")
                           settings["logout"] = True
                        if ang.lower() == key + "allowliff" or ang.lower() == "allowliff":
                            try:
                                allowLiff()
                                client.sendReplyMessage(msg.id, msg.to,"Flex mode enabled")
                            except:client.sendMessage(msg.to,"Click and verify to use fiture  template.\nhttps://liff.line.me/1602876096-e9QWgjyo")
                        if ang.lower() == key +  "updatedual":
                           settings['ChangeVideoProfile']=True
                           client.sendMessage(msg.to, "Please send video.")
                        if ang.lower() == key + "updatepict":
                           settings['changePictureProfile']=True
                           client.sendMessage(msg.to, "Please send image.")
                        if ang.lower() == key + "updategpict":
                           settings['changeGroupPicture'][msg.to] = True
                           client.sendMessage(msg.to, "Please send image.")
                        if ang.lower().startswith(key + "updatebio: "):                       
                         if msg.toType == 2:
                            jap = ang.lower().replace("updatebio: ","")
                            if len(jap) <= 100:
                               profile = client.getProfile()
                               profile.statusMessage = jap
                               client.updateProfile(profile)
                               client.sendReplyMessage(msg.id,msg.to, "Status bio changed to:\n" + jap)
                            else:client.sendReplyMessage(msg.id,msg.to,"Maksimal 100 karakter.")
                        if ang.lower().startswith(key + "updatename: "):                       
                         if msg.toType == 2:
                            jap = ang.lower().split("updatename: ")[1]
                            if len(jap) <= 30:
                               profile = client.getProfile()
                               profile.displayName = jap.title()
                               client.updateProfile(profile)
                               client.sendReplyMessage(msg.id,msg.to, "Profile name changed to:\n" + jap.title())
                            else:client.sendReplyMessage(msg.id,msg.to,"Maksimal 30 karakter.")
                        if ang.lower().startswith(key + "lineid: "):                       
                            ang_id = ang.replace(key + "lineid: ","")
                            line_id = client.findContactsByUserid(line_id)
                            if True:
                                client.sendMessage(msg.to,"http://line.me/ti/p/~" + angg_id)
                                client.sendContact(msg.to,line_id.mid)
                            else:client.sendReplyMessage(msg.id,msg.to,"Invalid Id name")                    
#=============( E N D    O F    S E L F M E N U )====================)



#=============( G R O U P  M E N U  C O M M A N D )====================)
                        if ang.lower() == key + "/bye":
                         if msg.toType == 2:
                             hoax = client.getGroup(msg.to)
                             client.sendMessage(msg.to,"Goodbye " + hoax.name)
                             client.leaveGroup(msg.to)
                        if ang.lower() == key + "gcreator":
                           if msg.toType == 2:
                              japri = client.getGroup(msg.to)
                              if japri.creator:
                                  petruk = client.getGroup(msg.to)
                                  gareng = petruk.creator.mid
                                  msg.text = ""
                                  msg.contentMetadata = {'mid': gareng}
                                  client.sendMessage(msg.to, "Group Creator:")
                                  client.sendMessage(msg.to,"",msg.contentMetadata,13)
                              else:client.sendReplyMessage(msg.id,msg.to,"Group creator galau.")                       
                        if ang.lower() == key + "ginfo":
                            if msg.toType == 2:
                                group = client.getGroup(msg.to)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "Not Found"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "Clossed"
                                    gTicket = "Nothing"
                                else:
                                    gQr = "Opened"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(client.reissueGroupTicket(group.id)))
                                japri = "♡Group info♡"
                                japri += "\n\n•Group Name : {}".format(str(group.name))
                                japri += "\n•ID Group :\n {}".format(group.id)
                                japri += "\n•Created By : {}".format(str(gCreator))
                                japri += "\n•Total Members : {}".format(str(len(group.members)))
                                japri += "\n•Total Pending : {}".format(gPending)
                                japri += "\n•Group Qr : {}".format(gQr)
                                japri += "\n•Group Ticket : {}".format(gTicket)
                                if settings["footer"]==True:sendFooter(msg.to,japri)
                                else:client.sendReplyMessage(msg.id,msg.to,japri)
                        if ang.lower() == key + "groupid":
                         if msg.toType == 2:
                            gid = client.getGroup(msg.to)
                            client.sendReplyMessage(msg.id,msg.to, "ID Grup : \n" + gid.id + "\n\nGroup name: \n" + str(gid.name))
                        if ang.lower() == key +  "panduan" or ang.lower() == "panduan":
                           data = {"type": "flex","altText": "The G - Operation","contents": {"type": "bubble","styles": {"body": {"backgroundColor": "#000000"}},"body": {"type": "box","layout": "vertical","spacing": "lg","contents": [{"type": "image","url": "https://imagizer.imageshack.com/img922/9913/pz3ZBp.png","size": "xxl","aspectRatio": "6.50:2","aspectMode": "cover","action": {"type": "uri","uri": "http://line.me/ti/p/~@kmj4856d"}},{"type": "box","layout": "horizontal","spacing": "xl","contents": [{"type": "image","url":"https://lh3.googleusercontent.com/avr-Ht9lKzM9RdG0fr3Ev4cacXfUhHzKqSb3XHyqSQVrYhtMhyH__pZN6HuXu-9Zbdw","size": "full","aspectRatio": "1:1","aspectMode": "cover","action": {"type": "uri","uri":"line://home/public/profile?id=kmj4856d"}},{"type": "box","layout": "vertical","spacing": "sm","contents": [{"type": "text","text": "Panduan","size": "lg","weight": "bold","color": "#D32608","wrap": True},{"type": "text","text": "Cara menggunakan perintah pada simple selfbot G-Operation.\nKlik tombol READ.","size": "sm","color": "#ffffff","wrap": True},{"type": "button","style": "primary","color":"#800000","action": {"type": "uri","label": "READ","uri": "https://www.jurustupai.com/2020/05/panduan-menggunakan-perintah-pada.html?m=1"}}]}]}]}}}
                           client.sendTemp(msg.to,data)
                        if ang.lower() == key + "grouppict":
                         if msg.toType == 2:
                            hoax = client.getGroup(msg.to)
                            if hoax.pictureStatus is None or hoax.pictureStatus == "":client.sendMessage(msg.to,"Group picture not found")                                
                            else:
                                ang = "https://obs.line-scdn.net/"+ hoax.pictureStatus
                                if settings["footer"]== True:sendFooter(msg.to,ang)
                                else:client.sendImageWithURL(msg.to,ang)
                        if ang.lower() == key +  "friendlist":
                         if msg.toType == 2:
                            contactlist = client.getAllContactIds()
                            contacts = client.getContacts(contactlist)
                            num=1
                            msgs="•My Friendlist:\n"
                            for ids in contacts:
                                msgs+="\n%i. %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n\nTotal Friendlist: %i" % len(contacts)
                            if settings["footer"] == True:sendFooter(msg.to, msgs)
                            else:client.sendReplyMessage(msg.id, msg.to, msgs)
                        if ang.lower() == key + "creator":
                             credit = "uc6e436ae77d2d1f5b5f6bd13ea7b671c"
                             client.sendMessage(msg.to,"Bot creator:")
                             client.sendContact(msg.to,credit)
                        if ang.lower() == key + 'mention' or ang.lower() == key +  'tagall' or ang.lower() == "tagall":
                         if msg.toType == 2:
                            group = client.getGroup(msg.to)
                            midMembers = [contact.mid for contact in group.members]
                            midSelect = len(midMembers)//20
                            for mentionMembers in range(midSelect+1):
                                no = 0
                                ret_ = "「 Mention Group 」\n• G-Operation\n• Simple SB\n"
                                dataMid = []
                                for dataMention in group.members[mentionMembers*20 : (mentionMembers+1)*20]:
                                    dataMid.append(dataMention.mid)
                                    no += 1
                                    ret_ += "\n{}. @!\n".format(str(no))
                                ret_ += "\n\n「 Total {} Members 」".format(str(len(dataMid)))
                                sendMention(msg.to, ret_, dataMid)
                        if ang.lower() == key + "grouplist":
                         if msg.toType == 2:
                            gruplist = client.getGroupIdsJoined()
                            kontak = client.getGroups(gruplist)
                            num=0
                            msgs="My Grouplist:\n"
                            for ids in kontak:
                               msgs+="\n%i - %s" % (num, ids.name) + " (" + str(len(ids.members)) + ")"
                               num=(num+1)
                            msgs+="\n\n            「 Total : %i Groups 」" % len(kontak)
                            if settings["footer"]== True:sendFooter(msg.to,"{}".format(msgs))
                            else:client.sendMessage(msg.to,"{}".format(str(msgs)))
                        if ang.lower() == key + "pendinglist":
                         if msg.toType == 2:
                            groups = client.getGroup(msg.to)
                            no = 1
                            ngentot = "• G-Operation\n• Pendinglist:\n"
                            if groups.invitee is None:client.sendMessage(msg.to,"Pending member not found.")
                            else:
                               for s in groups.invitee:
                                   try:
                                     ngentot += "\n{}. {}".format(no,client.getContact(s.mid).displayName)
                                     no = (no+1)
                                   except:pass
                               ngentot += "\n\nTotal: {}".format(len(groups.invitee))
                               if settings["footer"]== True:client.sendFooter(msg.id,msg.to,ngentot)
                               else:client.sendReplyMessage(msg.id,msg.to,ngentot)
                        if ang.lower() == key + "memberlist":
                         if msg.toType == 2:
                            groups = client.getGroup(msg.to)
                            no = 1
                            ngentot = "• G-Operation\n• Memberlist:\n"
                            if groups.members is None:client.sendMessage(msg.to,"Pending member not found.")
                            else:
                               for s in groups.members:
                                     ngentot += "\n{}. {}".format(no,client.getContact(s.mid).displayName)
                                     no = (no+1)
                               ngentot += "\n\nTotal: {}".format(len(groups.members))
                               if settings["footer"] == True:sendFooter(msg.to,ngentot)
                               else:client.sendReplyMessage(msg.id,msg.to,ngentot)
                        if ang.lower() == key + "gbirth":
                          if msg.toType == 2:
                             text = client.getGroup(msg.to)
                             gbirth(msg.id,msg.to,text)
#=============( E N D    O F  G R O U P   M E N U )====================)



#=============( G R O U P   S  E  T T I N G    M E N U  )====================)
                        if ang.lower().startswith(key + "groupname: "):                       
                         if msg.toType == 2:
                            angg = client.getGroup(msg.to)
                            anng = ang.lower().split("groupname: ")[1]
                            angg.name = anng.title()
                            client.updateGroup(angg)
                        if ang.lower().startswith(key + "groupcast: "):                       
                            ang_ = ang.lower().split("groupcast: ")[1]
                            garp = client.getGroupIdsJoined()
                            monkey = "Mini Selfbot By: @! \nBroadcasted by: @! \n────────────────\n" + ang_
                            target = client.getGroups(garp)
                            for a in range(len(target)):
                               sendMention(target[a].id, monkey,[Goperation,[msg._from]]) 
                               time.sleep(0.06)                        
                            client.sendReplyMessage(msg.id,msg.to,"Broadcasted to %s groups"%(str(len(target))))
                        if ang.lower().startswith(key + "setkey: "):
                           if msg.toType == 2:
                               stopcoli = ang.lower().split("setkey: ")[1]
                               manage["keyname"] = stopcoli
                               with open('setting.json', 'w') as fp:
                                   json.dump(manage, fp, sort_keys=True,indent=4)
                               client.sendReplyMessage(msg.id,msg.to,"Your key setup:\n{}".format(stopcoli))
                        if ang.lower() == "mykey":
                           if manage["keyname"]  !="":
                              client.sendReplyMessage(msg.id,msg.to,"Gunakan key anda!\nContoh: {} Mykey".format(manage["keyname"].title()))
                           else:pass
                        if ang.lower()== key + "mykey":
                           if msg.toType == 2:
                              if manage["keyname"] == "":client.sendReplyMessage(msg.id,msg.to,"Yourkey not set.")
                              else:client.sendReplyMessage(msg.id,msg.to,"Yourkey is\n'{}'".format(manage["keyname"]))
                        if ang.lower() == "resetkey":
                           if manage["keyname"]  !="":
                              client.sendReplyMessage(msg.id,msg.to,"Gunakan key anda!\nContoh: {} Resetkey".format(manage["keyname"].title()))
                           else:pass
                        if ang.lower()== key + "resetkey":
                            manage["keyname"] = ""
                            with open('setting.json', 'w') as fp:
                               json.dump(manage, fp, sort_keys=True,indent=4)
                            client.sendReplyMessage(msg.id,msg.to,"Your key reseted.")
                        if ang.lower().startswith(key + "kick"):
                         if msg.toType == 2:
                             if 'MENTION' in msg.contentMetadata.keys()!= None:
                                  names = re.findall(r'@(\w+)', msg.text)
                                  mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                  mentionees = mention['MENTIONEES']
                                  for mention in mentionees:
                                     client.kickoutFromGroup(msg.to,[mention['M']])
                             else:pass
                        if ang.lower().startswith(key + "invite"):
                         if msg.toType == 2:
                             if msg.contentMetadata is not None:
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                   targets.append(x["M"])
                                for target in targets:
                                   client.findAndAddContactsByMid(target)
                                   client.inviteIntoGroup(msg.to, [target])
                                   client.sendMessage(msg.to, client.getContact(target).displayName + " has been invited.")
                             else:pass                        
                        if ang.lower() == manage["nukekey"]:
                           if manage["nukekey"] !="":
                               hoax = client.getGroup(msg.to)
                               client.sendMessage(msg.to,"Goodbye Bitch ~")
                               for angg in hoax.members:
                                   if angg.mid not in manage["whitelist"]:
                                       client.kickoutFromGroup(msg.to,[angg.mid])
                               client.sendMessage(msg.to,"Rubish has been cleared")
                        if ang.lower() == key + "kickall" or ang.lower() == "kickall":
                            if manage["nukekey"] =="":
                               hoax = client.getGroup(msg.to)
                               client.sendMessage(msg.to,"Goodbye Bitch ~")
                               for angg in hoax.members:
                                   if angg.mid not in manage["whitelist"]:
                                       client.kickoutFromGroup(msg.to,[angg.mid])
                               client.sendMessage(msg.to,"Rubish has been cleared")
                            else:sendMention(msg.to,"• @! \nNuke key: {}\nPake Nuke key lu goblok!".format(manage["nukekey"]),[clientMid])
                        if ang.lower().startswith(key + "nuke set: "):
                           if msg.toType == 2:
                               stopcoli = ang.lower().split("set: ")[1]
                               manage["nukekey"] = stopcoli
                               with open('setting.json', 'w') as fp:
                                   json.dump(manage, fp, sort_keys=True,indent=4)
                               client.sendReplyMessage(msg.id,msg.to,"Key Nuke updated to:\n{}".format(stopcoli))
#=============( E N D    O F    G R O U P  S E T T I N G S )====================)



#=============( START   O F   S E L F B O T  S E T T I N G)====================)
                        if ang.lower() == "settings":
                           if manage["keyname"]  !="":
                              client.sendReplyMessage(msg.id,msg.to,"Gunakan key anda!\nContoh: {} Settings".format(manage["keyname"].title()))
                           else:pass
                        if ang.lower() == key + "settings":
                           jamb = "💻 G-Oᴘᴇʀᴀᴛɪᴏɴ 💻\n     「 Settings 」"
                           if msg.to not in protectMax and msg.to not in protectStaff:jamb += "\n\n🔴 All Protection"
                           else:
                              if msg.to in protectMax:jamb += "\n\n🟢 Protect max"
                              elif msg.to in protectStaff:jamb += "\n\n🟢 Protect staff"
                           if settings["autoTicket"] == True: jamb += "\n🟢 Join ticket"
                           else:jamb += "\n🔴 Join ticket"
                           if manage["welcome"] == True:jamb += "\n🟢 Auto Welcome"
                           else:jamb += "\n🔴 Auto Welcome"
                           if msg.to in manage["welcomsg"]: jamb += "\n🟢 Welcome msg"
                           else:jamb += "\n🔴 Welcome msg"
                           if manage["leave"] == True:jamb += "\n🟢 Auto Leave"
                           else:jamb += "\n🔴 Auto Leave"
                           if manage["adders"] == True:"\n🟢 Add Message"
                           else:jamb += "\n🔴 Add Message"
                           jamb += "\n\n• G-Operation V.0.2"
                           if settings["footer"] == True:sendFooter(msg.to,jamb)
                           else:client.sendReplyMessage(msg.id,msg.to,jamb)
                        if ang.lower() == "sider on":
                           if manage["keyname"]  !="":
                              client.sendReplyMessage(msg.id,msg.to,"Gunakan key anda!\nContoh: {} Sider on".format(manage["keyname"].title()))
                           else:pass
                        if ang.lower() == key + "sider on":
                            if msg.toType == 2:                     
                                if msg.to in cctv["Point"]:
                                    cctv["Point3"][msg.to] = {}
                                    with open('cctv.json', 'w') as fp:                            
                                        json.dump(cctv, fp, sort_keys=True, indent=4)
                                    client.sendReplyMessage(msg.id,msg.to,"Cek radar restarting..")
                                else:
                                    cctv["Point"][msg.to]= True
                                    cctv["Point3"][msg.to] = {}
                                    with open('cctv.json', 'w') as fp:                            
                                        json.dump(cctv, fp, sort_keys=True, indent=4)
                                    client.sendReplyMessage(msg.id,msg.to,"Cek radar running..")
                        if ang.lower() == "sider off":
                           if manage["keyname"]  !="":
                              client.sendReplyMessage(msg.id,msg.to,"Gunakan key anda!\nContoh: {} Sider on".format(manage["keyname"].title()))
                           else:pass
                        if ang.lower() == key +  "sider off":
                            if msg.toType == 2:                     
                                if msg.to in cctv["Point"]:
                                    del cctv["Point"][msg.to]
                                    with open('cctv.json', 'w') as fp:                            
                                        json.dump(cctv, fp, sort_keys=True, indent=4)
                                    client.sendReplyMessage(msg.id,msg.to,"Cek radar disabled.")
                                else:
                                    client.sendReplyMessage(msg.id,msg.to,"Cek radar already disabled.")              
                        if ang.lower() == key +  'lurk on':
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            readTime = "Starting read point\nTime: " + timeNow.strftime('%H:%M:%S')
                            if msg.to in cctv['readPoint']:
                                    try:
                                        del cctv['readPoint'][msg.to]
                                        del cctv['readMember'][msg.to]
                                        del cctv['readTime'][msg.to]
                                    except:
                                        pass
                                    cctv['readPoint'][msg.to] = msg.id
                                    cctv['readMember'][msg.to] = ""
                                    cctv['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                                    cctv['ROM'][msg.to] = {}
                                    with open('cctv.json', 'w') as fp:
                                        json.dump(cctv, fp, sort_keys=True, indent=4)
                                    client.sendReplyMessage(msg.id,msg.to,"Lurking already enabled")
                            else:
                                 try:
                                   del cctv['readPoint'][msg.to]
                                   del cctv['readMember'][msg.to]
                                   del cctv['readTime'][msg.to]
                                   with open('cctv.json', 'w') as fp:
                                       json.dump(cctv, fp, sort_keys=True,indent=4)
                                 except:
                                     pass
                                 cctv['readPoint'][msg.to] = msg.id
                                 cctv['readMember'][msg.to] = ""
                                 cctv['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                                 cctv['ROM'][msg.to] = {}
                                 with open('cctv.json', 'w') as fp:
                                     json.dump(cctv, fp, sort_keys=True, indent=4)
                                 client.sendReplyMessage(msg.id, msg.to, readTime)                                       
                                 client.sendReplyMessage(msg.id, msg.to, "Type 'Lurkers' to read sider.")                                       
                        if ang.lower() == key + 'lurk off':
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            readTime =  "Lurk point deleted\nTime: " + timeNow.strftime('%H:%M:%S')
                            if msg.to not in cctv['readPoint']:
                                client.sendReplyMessage(msg.id,msg.to,"Lurking already enabled.")
                            else:
                                try:
                                        del cctv['readPoint'][msg.to]
                                        del cctv['readMember'][msg.to]
                                        del cctv['readTime'][msg.to]
                                        with open('cctv.json', 'w') as fp:
                                            json.dump(cctv, fp, sort_keys=True,indent=4)
                                except:
                                      pass
                                client.sendReplyMessage(msg.id, msg.to,readTime)                
                        if ang.lower() == key + 'lurk reset':
                            if msg.toType == 2:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                readTime = "\nTime: " + timeNow.strftime('%H:%M:%S')
                                if msg.to in cctv["readPoint"]:
                                    try:
                                        cctv["readPoint"][msg.to] = True
                                        cctv["readMember"][msg.to] = {}
                                        cctv["readTime"][msg.to] = readTime
                                        cctv["ROM"][msg.to] = {}
                                        with open('cctv.json', 'w') as fp:
                                            json.dump(cctv, fp, sort_keys=True,indent=4)
                                    except:
                                        pass
                                    client.sendReplyMessage(msg.id, msg.to, "Reset reading point." + readTime)
                                    client.sendReplyMessage(msg.id, msg.to, "Type 'Lurkers' to read sider.")
                                else:
                                    client.sendMessage(msg.id, msg.to, "Type 'Lurk on' first.")                                    
                        if ang.lower() == key +  'lurkers':
                            if msg.toType == 2:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                readTime = "Time : " + timeNow.strftime('%H:%M:%S')
                                if msg.to in cctv['readPoint']:
                                    if cctv["ROM"][msg.to].items() == []:
                                        client.sendReplyMessage(msg.id, msg.to,"Reader None")
                                    else:
                                        chiya = []
                                        for rom in cctv["ROM"][msg.to].items():
                                            chiya.append(rom[1])
                                        cmem = client.getContacts(chiya) 
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = 'G-Operation\nGroup reader:\n\n'
                                    for x in range(len(cmem)):
                                        xname = str(cmem[x].displayName)
                                        pesan = ''
                                        pesan2 = pesan+"@Goperation\n"
                                        xlen = str(len(zxc)+len(xpesan))
                                        xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                        zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    text = xpesan+ zxc + "\nLurking " + readTime + "\nGroup: " + client.getGroup(msg.to).name
                                    try:
                                        client.sendReplyMessage(msg.id, msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as error:
                                        print (error)
                                    pass
                                else:client.sendReplyMessage(msg.id, msg.to,"Lurk on first.")
                        if ang.lower().startswith(key + "jointicket "):
                          if msg.toType == 2:
                            text = ang.lower().split("jointicket ")[1]
                            if text == "on":
                                if settings["autoTicket"] == True:
                                   client.sendMessage(msg.to,"Auto Join QR already enabled.")
                                else:
                                   settings["autoTicket"] = True
                                   client.sendMessage(msg.to,"Auto Join QR enabled.")
                            if text == "off":
                                if settings["autoTicket"] == False:
                                   client.sendMessage(msg.to,"Auto Join QR already disabled.")
                                else:
                                   settings["autoTicket"] = False
                                   client.sendMessage(msg.to,"Auto Join QR disabled.")

                        if ang.lower().startswith(key + "auto welcome "):
                          if msg.toType == 2:
                            text = ang.lower().split("welcome ")[1]
                            if text == "on":
                                if manage["welcome"] == True:
                                   client.sendMessage(msg.to,"Auto Welcome already enabled.")
                                else:
                                   manage["welcome"] = True
                                   with open('setting.json', 'w') as fp:
                                      json.dump(manage, fp, sort_keys=True,indent=4)
                                   client.sendMessage(msg.to,"Auto Welcome enabled.")
                            if text == "off":
                                if manage["welcome"] == False:
                                   client.sendMessage(msg.to,"Auto Welcome disabled.")
                                else:
                                   manage["welcome"] = False
                                   with open('setting.json', 'w') as fp:
                                      json.dump(manage, fp, sort_keys=True,indent=4)
                                   client.sendMessage(msg.to,"Auto Welcome disabled.")
                        if ang.lower().startswith(key + "welcome msg "):
                          if msg.toType == 2:
                            text = ang.lower().split("welcome msg ")[1]
                            if text == "on":
                                if msg.to in manage["welcomsg"]:
                                   client.sendMessage(msg.to,"Welcome Message already enabled.")
                                else:
                                   if manage["welcome"] == False:
                                      client.sendMessage(msg.to,"Please turn on auto welcome first.")
                                   else:
                                         manage["welcomsg"][msg.to] = True
                                         with open('setting.json', 'w') as fp:
                                             json.dump(manage, fp, sort_keys=True, indent=4)                                     
                                         if manage["welcomeSet"] !="":client.sendMessage(msg.to,"Welcome message in group\n" + client.getGroup(msg.to).name + " now is active")
                                         else:client.sendMessage(msg.to,"Welcome message not set.\nType 'welcome set: your message' to set it,")
                            if text == "off":
                                if msg.to not in manage["welcomsg"]:
                                   client.sendMessage(msg.to,"Welcome Message already disabled.")
                                else:
                                   del manage["welcomsg"][msg.to]
                                   with open('setting.json', 'w') as fp:
                                       json.dump(manage, fp, sort_keys=True,indent=4)
                                   client.sendMessage(msg.to,"Welcome Message disabled.")
                        if ang.lower().startswith(key + "welcome set: "):
                           if msg.toType == 2:
                            if msg.to not in manage["welcomsg"]:client.sendReplyMessage(msg.id,msg.to,"Please turn on welcome message first.")
                            else:
                               stopcoli = ang.lower().split("set: ")[1]
                               manage["welcomeSet"][msg.to] = stopcoli
                               with open('setting.json', 'w') as fp:
                                   json.dump(manage, fp, sort_keys=True,indent=4)
                               client.sendReplyMessage(msg.id,msg.to,"Welcome message updated to:\n{}".format(stopcoli))
                        if ang.lower().startswith(key + "add message "):
                          if msg.toType == 2:
                            text = ang.lower().split("message ")[1]
                            if text == "on":
                                if manage["adders"] == True:
                                   client.sendMessage(msg.to,"Respon adders already enabled.")
                                else:
                                   manage["adders"] = True
                                   with open('setting.json', 'w') as fp:
                                       json.dump(manage, fp, sort_keys=True,indent=4)
                                   client.sendMessage(msg.to,"Auto Respon adders enabled.")
                            if text == "off":
                                if manage["adders"] == False:
                                   client.sendMessage(msg.to,"Auto Respon adders disabled.")
                                else:
                                   manage["adders"] = False
                                   with open('setting.json', 'w') as fp:
                                       json.dump(manage, fp, sort_keys=True,indent=4)
                                   client.sendMessage(msg.to,"Auto Respon adders disabled.")
                        if ang.lower().startswith(key + "respon add: "):
                           if msg.toType == 2:
                               stopcoli = ang.lower().split("add: ")[1]
                               manage["addmsg"] = stopcoli
                               with open('setting.json', 'w') as fp:
                                   json.dump(manage, fp, sort_keys=True,indent=4)
                               client.sendReplyMessage(msg.id,msg.to,"Respon adders updated to:\n{}".format(stopcoli))
                        if ang.lower().startswith(key + "auto leave "):
                          if msg.toType == 2:
                            text = ang.lower().split("auto leave ")[1]
                            if text == "on":
                                if manage["leave"] == True:
                                   client.sendMessage(msg.to,"Auto Leave already enabled.")
                                else:
                                   manage["leave"] = True
                                   with open('setting.json', 'w') as fp:
                                       json.dump(manage, fp, sort_keys=True,indent=4)
                                   client.sendMessage(msg.to,"Auto Leave enabled.")
                            if text == "off":
                                if manage["leave"] == False:
                                   client.sendMessage(msg.to,"Auto Leave disabled.")
                                else:
                                   manage["leave"] = False
                                   with open('setting.json', 'w') as fp:
                                      json.dump(manage, fp, sort_keys=True,indent=4)
                                   client.sendMessage(msg.to,"Auto Leave disabled.")
                        if ang.lower().startswith(key + "leavemsg set: "):
                           if msg.toType == 2:
                               stopcoli = ang.lower().split("set: ")[1]
                               manage["leavemsg"] = stopcoli
                               with open('setting.json', 'w') as fp:
                                   json.dump(manage, fp, sort_keys=True,indent=4)
                               client.sendReplyMessage(msg.id,msg.to,"Leave message updated to:\n{}".format(stopcoli))
                        if ang.lower().startswith(key + "join link: "):
                           if msg.toType == 2:
                              text = ang.split("/ti/g/")[1]
                              try:
                                 hoax = client.findGroupByTicket(text)
                                 client.acceptGroupInvitationByTicket(hoax.id,text)
                                 client.sendMessage(msg.to, "Success join to %s" % str(hoax.name))
                              except:pass     
                        if '/ti/g/' in ang.lower():
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(ang)
                            n_links=[]
                            mygrp = client.getGroupIdsJoined()
                            for l in links:
                                if l not in n_links:
                                    n_links.append(l)
                            for ticket_id in n_links:
                                if settings["autoTicket"] == True:
                                    group=client.findGroupByTicket(ticket_id)
                                    if group.id in mygrp:client.sendReplyMessage(msg.id,msg.to,"Already in this group")
                                    else:
                                       client.acceptGroupInvitationByTicket(group.id,ticket_id)                                       
                                       client.sendMessage(msg.to,"Success join to %s" % str(group.name))
#=============( E N D   O F   S E L F B O T  S E T T I N G)====================)





 #=============( START   O F   G R O U P  P R O T E C T)====================)
                        
                        if ang.lower() == key + "add whitelist":
                          settings["addwhitelist"] = True
                          client.sendMessage(msg.to,"Send a contact")
                        if ang.lower() == key + "del whitelist":
                          settings["delwhitelist"] = True
                          client.sendMessage(msg.to,"Send a contact") 
                        if ang.lower() == key + "add blacklist":
                          settings["addblacklist"] = True
                          client.sendMessage(msg.to,"Send a contact")
                        if ang.lower() == key + "del blacklist":
                          settings["delblacklist"] = True
                          client.sendMessage(msg.to,"Send a contact")                         
                        if ang.lower().startswith(key + "whitelist on "):                           
                         if msg.toType == 2:
                            key = eval(msg.contentMetadata["MENTION"])
                            key["MENTIONEES"][0]["M"]
                            targets = []
                            for x in key["MENTIONEES"]:
                                targets.append(x["M"])
                            for target in targets:
                                if target in manage["whitelist"]:client.sendReplyMessage(msg.id,msg.to, "Already in whitelist.")
                                else:
                                      try:
                                         manage["whitelist"][target] = True
                                         with open('setting.json', 'w') as fp:
                                             json.dump(manage, fp, sort_keys=True, indent=4)
                                         client.sendReplyMessage(msg.id,msg.to,client.getContact(target).displayName +" add to whitelist.")
                                      except:pass
                        
                        if ang.lower().startswith(key + "whitelist del "):
                            key = eval(msg.contentMetadata["MENTION"])
                            key["MENTIONEES"][0]["M"]
                            targets = []
                            for x in key["MENTIONEES"]:
                                targets.append(x["M"])
                            for target in targets:
                                if target not in manage["whitelist"]:client.sendReplyMessage(msg.id,msg.to, "User not in whitelist.")
                                else:
                                    try:
                                        del manage["whitelist"][target]
                                        with open('setting.json', 'w') as fp:
                                            json.dump(manage, fp, sort_keys=True, indent=4)
                                        client.sendReplyMessage(msg.id,msg.to,client.getContact(target).displayName +" removed from whitelist.")
                                    except:pass
                        if ang.lower() == key + "whitelisting":
                         if msg.toType == 2:
                            if manage["whitelist"] == {}:client.sendReplyMessage(msg.id, msg.to,"Whitelist empty!")
                            else:
                               hoax = [o for o in manage["whitelist"]]
                               cekmid = len(hoax)//20
                               no = 1
                               for xang in range(cekmid +1): 
                                   males = "The G-Operation\nWhitelist:\n"
                                   asw = []
                                   for target in hoax[xang*20:(xang+1)*20]:
                                       males += "\n{}. @!\n".format(no)
                                       no = (no +1)
                                       asw.append(target)
                                   males += "\n\nTotal: {} User.".format(len(asw))
                                   sendMention(msg.to, males,asw)
                        if ang.lower() == key + "clearwhitelist":
                         if msg.toType == 2:
                            if manage["whitelist"] == {}:client.sendReplyMessage(msg.id, msg.to,"Whitelist not found.")
                            else:
                               manage["whitelist"] = {}
                               with open('setting.json', 'w') as fp:
                                  json.dump(manage, fp, sort_keys=True, indent=4)                               
                               client.sendReplyMessage(msg.id,msg.to,"Whitelist cleared.")
                        if ang.lower().startswith(key + "blacklist on "):                           
                         if msg.toType == 2:
                            key = eval(msg.contentMetadata["MENTION"])
                            key["MENTIONEES"][0]["M"]
                            targets = []
                            for x in key["MENTIONEES"]:
                                targets.append(x["M"])
                            for target in targets:
                                if target in manage["blacklist"]:
                                   client.sendReplyMessage(msg.id,msg.to, "Already in blacklist.")
                                else:
                                      try:
                                         manage["blacklist"][target] = True
                                         with open('setting.json', 'w') as fp:
                                             json.dump(manage, fp, sort_keys=True, indent=4)
                                         client.sendReplyMessage(msg.id,msg.to,client.getContact(target).displayName +" has been blacklist.")
                                      except:pass
                        if ang.lower().startswith(key + "blacklist del "):
                            key = eval(msg.contentMetadata["MENTION"])
                            key["MENTIONEES"][0]["M"]
                            targets = []
                            for x in key["MENTIONEES"]:
                                targets.append(x["M"])
                            for target in targets:
                                if target not in manage["blacklist"]:client.sendReplyMessage(msg.id,msg.to, "User not in blacklist.")
                                else:
                                    try:
                                        del manage["blacklist"][target]
                                        with open('setting.json', 'w') as fp:
                                            json.dump(manage, fp, sort_keys=True, indent=4)
                                        client.sendReplyMessage(msg.id,msg.to,client.getContact(target).displayName +" removed from blacklist.")
                                    except:pass
                        if ang.lower() == key + "blacklisting":
                         if msg.toType == 2:
                            if manage["blacklist"] == {}:client.sendReplyMessage(msg.id, msg.to,"blacklist empty!")
                            else:
                               hoax = [o for o in manage["blacklist"]]
                               cekmid = len(hoax)//20
                               no = 1
                               for xang in range(cekmid +1): 
                                   males = "The G-Operation\nBlacklist:\n"
                                   asw = []
                                   for target in hoax[xang*20:(xang+1)*20]:
                                       males += "\n{}. @!\n".format(no)
                                       no = (no +1)
                                       asw.append(target)
                                   males += "\n\nTotal: {} User.".format(len(asw))
                                   sendMention(msg.to, males,asw)
                        if ang.lower() == key + "clearblacklist":
                         if msg.toType == 2:
                            if manage["blacklist"] == {}:client.sendReplyMessage(msg.id, msg.to,"Blacklist not found.")
                            else:
                               manage["blacklist"] = {}
                               with open('setting.json', 'w') as fp:
                                  json.dump(manage, fp, sort_keys=True, indent=4)                               
                               client.sendReplyMessage(msg.id,msg.to,"Blacklist cleared.")
                        if ang.lower() == key + "findblacklist":
                         if msg.toType == 2:
                             if manage["blacklist"] == {}:client.sendReplyMessage(msg.id, msg.to,"Blacklist empty!")
                             else:
                                mari = client.getGroup(msg.to)
                                ngewe = []
                                for ewe in mari.members:
                                    if ewe.mid in manage["blacklist"]:
                                        ngewe.append(ewe.mid)                                
                                if ngewe == []:client.sendReplyMessage(msg.id,msg.to,"No blacklist found\nin '{}'".format(mari.name))
                                else:
                                   hoax = [o for o in ngewe]
                                   cekmid = len(hoax)//20
                                   for angx in range(cekmid +1): 
                                      enak = "• G-Operation\n• Find Blacklist:\n"
                                      asw = []
                                      no = 1
                                      for target in hoax[angx*20:(angx+1)*20]:
                                            enak += "\n  {}. @!\n".format(no)
                                            no = (no+1)
                                            asw.append(target)
                                      enak += "\n\nBe alert!「 {} 」here.\nGroup: {}".format(len(asw),mari.name)             
                                      sendMention(msg.to,enak,asw)

                        if ang.lower().startswith(key + "protect "):
                          if msg.toType == 2:
                            text = ang.lower().split("protect ")[1]
                            if text == "max":
                               if msg.to in protectMax:
                                  client.sendMessage(msg.to,"Max protection already enabled.")
                               else:
                                 if msg.to in protectStaff:
                                     del manage["proStaff"][msg.to]
                                     manage["proMax"][msg.to] = True
                                     jap = client.getGroup(msg.to)
                                     manage["gname"][msg.to] = jap.name
                                     with open('setting.json', 'w') as fp:
                                         json.dump(manage, fp, sort_keys=True, indent=4)
                                     if client.getGroup(msg.to).preventedJoinByTicket == False:
                                        hoax = client.getGroup(msg.to)
                                        hoax.preventedJoinByTicket = True
                                        client.updateGroup(hoax)
                                        client.sendMessage(msg.to,"Protect max enabled.")
                                     else:client.sendMessage(msg.to,"Protect max enabled.")
                                 else:
                                    if msg.to not in protectStaff and msg.to not in protectMax:    
                                        manage["proMax"][msg.to] = True
                                        jap = client.getGroup(msg.to)
                                        manage["gname"][msg.to] = jap.name
                                        with open('setting.json', 'w') as fp:
                                            json.dump(manage, fp, sort_keys=True, indent=4)
                                        if client.getGroup(msg.to).preventedJoinByTicket == False:
                                           hoax = client.getGroup(msg.to)
                                           hoax.preventedJoinByTicket = True
                                           client.updateGroup(hoax)           
                                           client.sendMessage(msg.to,"Protect max enabled.")
                                        else:client.sendMessage(msg.to,"Protect max enabled.")
                            elif text == "staff":               
                               if msg.to in protectStaff:
                                  client.sendMessage(msg.to,"Protect staff already enabled.")
                               elif msg.to in protectMax:
                                      del manage["proMax"][msg.to]
                                      manage["proStaff"][msg.to] = True
                                      jap = client.getGroup(msg.to)
                                      manage["gname"][msg.to] = jap.name
                                      with open('setting.json', 'w') as fp:
                                          json.dump(manage, fp, sort_keys=True, indent=4)
                                      if client.getGroup(msg.to).preventedJoinByTicket == False:
                                         hoax = client.getGroup(msg.to)
                                         hoax.preventedJoinByTicket = True
                                         client.updateGroup(hoax)
                                         client.sendMessage(msg.to,"Protect staff enabled.")
                                      else:client.sendMessage(msg.to,"Protect staff enabled.")
                               else:
                                   manage["proStaff"][msg.to] = True
                                   jap = client.getGroup(msg.to)
                                   manage["gname"][msg.to] = jap.name
                                   with open('setting.json', 'w') as fp:
                                       json.dump(manage, fp, sort_keys=True, indent=4)
                                   if client.getGroup(msg.to).preventedJoinByTicket == False:
                                      hoax = client.getGroup(msg.to)
                                      hoax.preventedJoinByTicket = True
                                      client.updateGroup(hoax)           
                                      client.sendMessage(msg.to,"Protect staff enabled.")
                                   else:client.sendMessage(msg.to,"Protect staff enabled.")
                            elif text == "none":    
                               if msg.to not in protectStaff and msg.to not in protectMax:
                                  client.sendMessage(msg.to,"Protection already disabled.")
                               else:
                                  if msg.to in protectMax:
                                      del manage["proMax"][msg.to]
                                      with open('setting.json', 'w') as fp:
                                          json.dump(manage, fp, sort_keys=True, indent=4)
                                      client.sendMessage(msg.to,"Protection disabled.")
                                  else:
                                     if msg.to in protectStaff:
                                         del manage["proStaff"][msg.to]
                                         jap = client.getGroup(msg.to)
                                         manage["gname"][msg.to] = jap.name
                                         with open('setting.json', 'w') as fp:
                                             json.dump(manage, fp, sort_keys=True, indent=4)
                                         client.sendMessage(msg.to,"Protection disabled.")
            except Exception as error:client.log("[ GOPERA ERROR ]\n{}".format(str(error)))
    except Exception as error:client.log("[ GOPERA ERROR ]\n{}".format(str(error)))
while True:
    try:
        ops = clientPoll.singleTrace(count=50)
        oups = Goperation
        oupid = "angid&ucfb857ee3e7d641101ae90610752e4d7"
        if ops is not None:
            for op in ops:
                if oups == "" or oups not in oupid.split("d&")[1]:
                   print (manage["setanCredit"])
                   sys.exit()
                else:
                   clientBot(op)
                   clientPoll.setRevision(op.revision)
    except Exception as error:
        client.log("[GOP ERROR]\n{}".format(str(error)))
#===============[ NOTE ]======================]
# LINE PYTHON3: LINEPY
# AUTHOR : FADHIIL RACHMAN
# SB COMMAND CREATED BY : ANG
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
# JANGAN MELAKUKAN PERUBAHAN PADA SCRIPT KECUALI ANDA YAKIN DAN TAU MENGENAI ITU
# PUBLISHED ON: https://www.jurustupai.com/2020/05/cara-membuat-simple-selfbot-template.html