import argparse
import sys
import asyncio

prog_help_text = "This program will delete the users messages from a telegram group older than a set age."
prog_version = "1.0.1"

# Initiate the parser
parser = argparse.ArgumentParser(description = prog_help_text)
parser.add_argument("--apiid", "-ai", help="your telegram api id", required=True, type=int)
parser.add_argument("--apihash", "-ah", help="your telegram api hash", required=True)
parser.add_argument("--channelid", "-ci", help="your telegram channel id", required=True, type=int)
parser.add_argument("--messageage", "-ma", help="how many minutes old the messages have to be to be deleted", default=1440, type=int)
parser.add_argument("--version", "-V", help="show program version", action="store_true")
args = parser.parse_args()

# Check for input parameters
if args.version:
    print("This is version %s of the program" % prog_version)

if args.apiid:
    print("Setting api_id to %s" % args.apiid)
    api_id = args.apiid

if args.apihash:
    print("Setting api_hash to %s" % args.apihash)
    api_hash = args.apihash

if args.channelid:
    print("Setting channelid to %s" % args.channelid)
    channelid = args.channelid

if args.messageage:
    print("Setting delete_delta to %sminutes" % args.messageage)
    delete_delta = args.messageage

from telethon import TelegramClient, sync
client = TelegramClient("session_name", api_id, api_hash)
print("If asked input phonenumber with countrycode like +4791234567 and the OTP you get as a message from Telegram")
client.start()

if client.is_connected() is False:
    print("Failed to connect client. Exiting")
    sys.exit()

me = client.get_me()
my_id = me.id
my_username = me.username

print("Getting channel access_hash")
from telethon.tl.types import InputPeerChannel, PeerChannel
channel_entity = client.get_entity(PeerChannel(channelid))
access_hash = channel_entity.access_hash
print("Your channel access_hash is %s" % access_hash)
channel = InputPeerChannel(channelid, access_hash)
entity = client.get_entity(channel)

from datetime import datetime, timedelta, timezone
delete_delta_timestamp = datetime.now(timezone.utc) - timedelta(minutes=delete_delta)

msg_newer = 0
msg_deleted = 0
msg_other = 0

print("Processing messages. This could take a while, depending on the amount of messages")
with TelegramClient(my_username, api_id, api_hash) as client:
    for message in client.iter_messages(channel):
        if (msg_newer + msg_deleted + msg_other) % 500 == 0 and msg_newer + msg_deleted + msg_other > 0:
            print("Processed %dmessages" % (msg_newer + msg_deleted + msg_other))
        if message.from_id == my_id:
            if delete_delta_timestamp >= message.date:
                client.delete_messages(channel, [message.id])
                msg_deleted += 1
            else:
                msg_newer += 1
        else:
            msg_other += 1


print("Finised processing messages")
print("Deleted %d messages from channel on behalf of user %s. Channel has %d of your messages newer than the delete delta of %dminutes. Channel also has %d messages from other users." % (msg_deleted, my_username, msg_newer, delete_delta, msg_other))

if client.is_connected() is True:
    client.disconnect()

print("Exiting program")
del client
for task in asyncio.Task.all_tasks():
    task.cancel()
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(asyncio.Task.all_tasks(loop)))
loop.close()
