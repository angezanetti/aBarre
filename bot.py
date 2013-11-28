#!/usr/bin/python
import socket, ssl, re
import urllib2
from bs4 import BeautifulSoup

bot = 'aBarre'
chan = '#coworkinglille'
network = 'irc.freenode.net'
port = 6697
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((network,port))
irc = ssl.wrap_socket(socket)
irc.send('NICK ' + bot + '\r\n') #Send our Nick(Notice the Concatenation)
irc.send('USER Bot Bot Bot :aBarre IRC\r\n') #Send User Info to the server
irc.send('JOIN ' + chan + '\r\n') # Join the pre defined channel
irc.send('PRIVMSG ' + chan + ' :\_O< coin!! \r\n') #Send a Message to the  channel

# Set up our commands function
def commands(user,channel,message):
    if message.find('mutualab?')!=-1:
      irc.send('PRIVMSG %s :%s: Mutualab is awesome!!!!!!!\r\n' % (channel,user))
    elif message.find(bot+': help')!=-1:
      irc.send('PRIVMSG %s :%s: you can find all the help you need here: http://mutualab.org.\r\n' % (channel,user))
    elif message.find('coffee')!=-1:
      coffee(channel)
    elif message.find('http')!=-1:
      GimmeUrlInfos(channel, message)
    elif message.find('Hello ')!=-1:
      hello(channel, user)
    elif message.find(bot)!=-1:
      irc.send('PRIVMSG %s :%s: umm ? \r\n' % (channel,user))

def ping(): # This is our first function! It will respond to server Pings.
  irc.send("PONG :pingis\n")  

def sendmsg(chan , msg): # This is the send message function, it simply sends messages to the channel.
  irc.send("PRIVMSG "+ chan +" :"+ msg +"\n") 

def hello(channel, user):
  irc.send("PRIVMSG %s :Hello %s !\n" % (channel, user))

def coffee(channel):
  irc.send("PRIVMSG %s :( (      \n" % (channel)) 
  irc.send("PRIVMSG %s :  ) )    \n" % (channel)) 
  irc.send("PRIVMSG %s :........ \n" % (channel)) 
  irc.send("PRIVMSG %s :|      |]\n" % (channel)) 
  irc.send("PRIVMSG %s :\      / \n" % (channel)) 
  irc.send("PRIVMSG %s : `----'  \n" % (channel)) 

def GimmeUrlInfos(channel,message):
  link = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message) 
  response = urllib2.urlopen(link[0])
  html = BeautifulSoup(response.read())
  urlTitle = html.find('title')
  irc.send("PRIVMSG %s :  --> " % (channel) + urlTitle.contents[0].encode('utf-8') + "\r\n" )

while True: #While Connection is Active
  ircmsg = irc.recv(2048) # receive data from the server
  ircmsg = ircmsg.strip('\n\r') # removing any unnecessary linebreaks.
  # print(ircmsg) # Here we print what's coming from the server
  user=ircmsg.split('!')[0][1:]

  if ircmsg.find(' PRIVMSG ')!=-1:
    channel=ircmsg.split(' PRIVMSG ')[-1].split(' :')[0]
    commands(user,channel,ircmsg)
  if ircmsg.find("PING :") != -1:
    ping()
  if ircmsg.find(" JOIN ") != -1:
    channel=ircmsg.split(' JOIN ')[-1].split(' :')[0]
    hello(channel, user)
