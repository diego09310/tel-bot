#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from urllib2 import urlopen
import transmissionrpc
import datetime

# Load configuration file
f=open('config.txt', 'r')
TOKEN=f.readline()[:-1]
USER_ID=int(f.readline()[:-1])
TORRENT=f.readline()[:-1].split(" ")
f.close()

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

waiting_torrent = False
tc = transmissionrpc.Client(TORRENT[0], port=int(TORRENT[1]), user=TORRENT[2], password=TORRENT[3])

def get_out(bot, update):
  bot.sendMessage(chat_id=update.message.chat_id, text="Sorry, this is a private bot")
  f=open('unauthorized.log', 'a')
  date=datetime.datetime.now()
  log = "Date: " + date.strftime('%a %b %d %H:%M:%S %Y') + "\nUsername: " + update.message.from_user.username + " Name: " + update.message.from_user.first_name + " LastName: " + update.message.from_user.last_name + " ID: " + str(update.message.from_user.id)
  f.write("%s\n" % log.encode("utf-8"))
  f.close()

def start(bot, update):
  if update.message.from_user.id == USER_ID:
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm Yoda, please talk to me!")
  else:
    get_out(bot, update)

def ip(bot, update):
  if update.message.from_user.id == USER_ID:
    ip=urlopen('http://ip.42.pl/raw').read()
    bot.sendMessage(chat_id=update.message.chat_id, text="This is my IP: "+ip)
  else:
    get_out(bot, update)

def add_torrent(bot, update, args):
  if update.message.from_user.id == USER_ID:
    if (len(args) > 0):
      link=args
      torrent=tc.add_torrent(link[0])
      #bot.sendMessage(chat_id=update.message.chat_id, text=torrent)
    else:
      bot.sendMessage(chat_id=update.message.chat_id, text="Send me the magnet link:")
      global waiting_torrent
      waiting_torrent = True
  else:
    get_out(bot, update)
  
def nch(bot, update):
  if update.message.from_user.id == USER_ID:
    if waiting_torrent:
      torrent=tc.add_torrent(update.message.text)
      global waiting_torrent
      waiting_torrent = False
    else:
      bot.sendMessage(chat_id=update.message.chat_id, text="Sorry, didn't understood")
      

def main():
  start_handler=CommandHandler('start', start)
  ip_handler=CommandHandler('ip', ip)
  add_torrent_handler=CommandHandler('add_torrent', add_torrent, pass_args=True)
  nch_handler=MessageHandler([Filters.text], nch)
  dispatcher.add_handler(start_handler)
  dispatcher.add_handler(ip_handler)
  dispatcher.add_handler(add_torrent_handler)
  dispatcher.add_handler(nch_handler)
  
  updater.start_polling()
    
  updater.idle()

if __name__ == '__main__':
  main()
