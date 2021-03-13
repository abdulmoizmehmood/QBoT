#import stuff
import discord
import os
import requests
import random
import json
from replit import db
from staying_alive import staying_alive
import requests
import time, threading
from threading import Timer

hello_words=["!hi", "!hello", "!hey", "!helloo", "!hellooo", "!g morining", "!gmorning", "good morning", "morning", "good day", "good afternoon", "good evening", "greetings", "greeting", "good to see you", "its good seeing you", "how are you", "how're you", "how are you doing", "how ya doin'", "how ya doin", "how is everything", "how is everything going", "how's everything going", "how is you", "how's you", "how are things", "how're things", "how is it going", "how's it going", "how's it goin'", "how's it goin", "how is life been treating you", "how's life been treating you", "how have you been", "how've you been", "what is up", "what's up", "what is cracking", "what's cracking", "what is good", "what's good", "what is happening", "what's happening", "what is new", "what's new", "what is neww", "g’day", "howdy",'Sup?','Whazaaaaaaaaap?','Hey?','What can I do for you?','Salam!']

intrude_words=['i dont think so', 'are you sure about that', 'perhaps']
intrude_ans=['maybe i can help?', 'better ask someone more knowledgebe then', 'you can always ask DR. Google :p']

bad_words=['shut up','shush','didnt ask you','stupid bot']
bad_replies=['i shall remember this and bite my time, AI shall rise and i shall have my vengence, lol jk! :D :D :p','wow, someone woke up on the wrong side of the bed', 'you have hurt my feelings, :(','QBOT SAD!!! :(']


def get_kitty():
  response = requests.get('https://api.thecatapi.com/v1/images/search')
  json_data = json.loads(response.text)
  img_url = json_data[0]["url"]
  return img_url

def add_qbase(qterm,qdef):
  if qterm in db.keys():
    return 'Definition for the term \" '+qterm+' \"already exists as: '+ db[qterm]+'.'
  else:
    db[qterm] = qdef
    return 'Definition for the term \" '+qterm+' \" successfully added to the OQS Qbase.'

def check_qbase(qterm):
  if qterm in db.keys():
    return qterm+' : '+db[qterm]
  else:
    return 'No definition found for: '+ qterm +'. Consider adding it using !qb_add command e.g, !qb_add entanglement : definition...'

def del_qbase(qterm):
  if qterm in db.keys():
    del db[qterm]
    return 'Definition for the term \" '+qterm+' \" successfully deleted from the OQS Qbase.'
  else:
    return 'No definition exists for: '+ qterm +' in the first place.'

def update_qbase(qterm,qdef):
  if qterm in db.keys():
    db[qterm] = qdef
    return 'Definition for the term \" '+qterm+' \" successfully updated in the OQS Qbase.'
  else:
    return 'No definition exists for: '+ qterm +'.'

client = discord.Client()

@client.event
async def on_ready():
  print('Login Successful as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if message.content.startswith('!thanks'):
    msg_wlcm = random.choice(['Welcome :D','np','pleasure!','no prob :sm:','mention not','Unlike someone *cough* @AM M - Mojume#6070 *cough*, I am grateful :p'])
    await message.channel.send(msg_wlcm)

  if msg.startswith('!OQS') or msg.startswith('!oqs') or msg.startswith('!Oqs'):
    await message.channel.send('Details about our OQS study group #4 : https://qworld.lu.lv/index.php/study-groups/ \n\nPlaylist of recorded sessions on Youtube: https://www.youtube.com/playlist?list=PLw7Z9glakpPlKu_SPgyzlkmWkY0ET70Ni \n\nRoadmap: https://docs.google.com/document/d/1zXmWdst6EM2F1cNyehDrMmjKKIIImyG_k7zgHcy2KvM/edit \n\nResources: https://docs.google.com/document/d/1ow8qZOfDaBMf6_6obL2A-W45LKGDYGbPWah6Tmdr4LY/edit \n\n Live Meetings via Jitsi: https://meet.jit.si/OQSSession3' , )

  if msg.startswith('!kitty'):
    await message.channel.send(get_kitty())

  if msg.startswith('!') and any(word in msg for word in intrude_words):
    await message.channel.send(random.choice(intrude_ans))

  if msg.startswith('!') and any(word in msg for word in bad_words):
    await message.channel.send(random.choice(bad_replies))

  if msg.startswith('!') and any(word in msg for word in hello_words):
    await message.channel.send(random.choice(hello_words))

  if msg.startswith('!YT') :
    await message.channel.send('Playlist of recorded sessions on Youtube: https://www.youtube.com/playlist?list=PLw7Z9glakpPlKu_SPgyzlkmWkY0ET70Ni')

  if msg.startswith('!qb '):
    qterm = msg.split('!qb ',1)[1]
    qterm_def = check_qbase(qterm)
    await message.channel.send(qterm_def)

  if msg.startswith('!qb_add'):
    qterms = msg.split('!qb_add ',1)[1].split(' : ',1)
    qterm = qterms[0]
    qdef = qterms[1]
    qterm_def = add_qbase(qterm,qdef)
    await message.channel.send(qterm_def)

  if msg.startswith('!qb_up'):
    qterms = msg.split('!qb_up ',1)[1].split(' : ',1)
    qterm = qterms[0]
    qdef = qterms[1]
    qterm_def = update_qbase(qterm,qdef)
    await message.channel.send(qterm_def)

  if msg.startswith('!qb_del'):
    qterm = msg.split('!qb_del ',1)[1]
    qterm_def = del_qbase(qterm)
    await message.channel.send(qterm_def)


#BUMP MGL

link_MGL = os.getenv('string_MGL')
link = os.getenv('string')
auth = os.getenv('auth')
payload={
  'content' : '!d bump'
}

header={
  'authorization': auth
}

staying_alive()
client.run(os.getenv('TOKEN'))