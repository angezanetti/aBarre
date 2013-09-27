#!/usr/bin/python
import socket, ssl
nick = 'aBarre'
chan = '#lentremise'
debug = False
network = 'irc.freenode.net'
port = 6697
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((network,port))
irc = ssl.wrap_socket(socket)
irc.recv (4096)
irc.send('NICK ' + nick + '\r\n') #Send our Nick(Notice the Concatenation)
irc.send('USER AffixBot AffixBot AffixBot :Affix IRC\r\n') #Send User Info to the server
irc.send('JOIN ' + chan + '\r\n') # Join the pre defined channel
irc.send('PRIVMSG ' + chan + ' :Hello.\r\n') #Send a Message to the  channel
while True: #While Connection is Active
  data = irc.recv (4096) #Make Data the Receive Buffer
  print data #Print the Data to the console(For debug purposes)

  if data.find('PING') != -1: #If PING is Found in the Data
    irc.send('PONG ' + data.split()[1] + '\r\n') #Send back a PONG
