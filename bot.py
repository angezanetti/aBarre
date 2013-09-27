#!/usr/bin/python
import socket, ssl

bot = 'aBarre'
chan = '#lentremise'
debug = False
network = 'irc.freenode.net'
port = 6697
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((network,port))
irc = ssl.wrap_socket(socket)
irc.send('NICK ' + bot + '\r\n') #Send our Nick(Notice the Concatenation)
irc.send('USER AffixBot AffixBot AffixBot :Affix IRC\r\n') #Send User Info to the server
irc.send('JOIN ' + chan + '\r\n') # Join the pre defined channel
irc.send('PRIVMSG ' + chan + ' :Hello.\r\n') #Send a Message to the  channel

# Set up our commands function
def commands(user,channel,message):
    if message.find(bot +': mutualab?')!=-1:
      irc.send('PRIVMSG %s :%s: Mutualab is awesome!!!!!!!\r\n' % (channel,user))
    elif message.find(bot+': help')!=-1:
      irc.send('PRIVMSG %s :%s: you can find all the help you need here: http://mutualab.org.\r\n' % (channel,user))

def ping(): # This is our first function! It will respond to server Pings.
  irc.send("PONG :pingis\n")  

def sendmsg(chan , msg): # This is the send message function, it simply sends messages to the channel.
  irc.send("PRIVMSG "+ chan +" :"+ msg +"\n") 

def hello(): # This function responds to a user that inputs "Hello Mybot"
  irc.send("PRIVMSG "+ channel +" :Hello!\n")

while True: #While Connection is Active
  ircmsg = irc.recv(2048) # receive data from the server
  ircmsg = ircmsg.strip('\n\r') # removing any unnecessary linebreaks.
  print(ircmsg) # Here we print what's coming from the server

  if ircmsg.find(' PRIVMSG ')!=-1:
    user=ircmsg.split('!')[0][1:]
    channel=ircmsg.split(' PRIVMSG ')[-1].split(' :')[0]
    commands(user,channel,ircmsg)
  if ircmsg.find(":Hello "+ bot) != -1: # If we can find "Hello Mybot" it will call the function hello()
    hello()

  if ircmsg.find("PING :") != -1: # if the server pings us then we've got to respond!
    ping()
