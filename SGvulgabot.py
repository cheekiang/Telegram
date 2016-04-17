from twx.botapi import TelegramBot, ReplyKeyboardMarkup
import os
import datetime
"""
Setup the bot
"""

bot = TelegramBot('173036865:AAGTS4HpLglqlLULSG3odoeYZr87d2GG9U0')
print bot
bot.update_bot_info().wait()

last_id = 0
print(bot.username)

TELEGRAM_MSGID=0;
TELEGRAM_MSG=1;
"""
Send a message to a user
"""
#create objects first
updates = bot.get_updates(offset= last_id, timeout=600).wait()
msg  = updates[len(updates)-1][TELEGRAM_MSG]

#result = bot.send_message(user_id, 'test message body').wait()
#print(result)

"""
Get updates sent to the bot
"""
pmsg = 'jbufs'

while True:
    updates = bot.get_updates(offset= last_id, timeout=600).wait()
    
    #for update in updates:
    #   print(update[TELEGRAM_MSGID])
    #print(updates[len(updates)-1][TELEGRAM_MSG])
    if len(updates) != 0:
        msg  = updates[len(updates)-1][TELEGRAM_MSG]
    chat= msg.chat
    print msg.text
    print pmsg

    if pmsg is not msg.text:
        if len(updates) != 0:
            last_id = int(updates[len(updates)-1][TELEGRAM_MSGID])+1    

        if "Damn" in msg.text:
            bot.send_message(msg.chat.id, 'No Vulgarity Please! ')
        elif "fuck" in msg.text:
            bot.send_message(msg.chat.id, 'Oh yes baby! ')
        elif "Fuck" in msg.text:
            bot.send_message(msg.chat.id, 'Oh yes baby! ')
        elif "shit" in msg.text:
            bot.send_message(msg.chat.id, 'No Vulgarity Please! ')
        elif "Shit" in msg.text:
            bot.send_message(msg.chat.id, 'No Vulgarity Please! ')
        elif "ass" in msg.text:
            bot.send_message(msg.chat.id, 'Whose? ')
        elif "Ass" in msg.text:
            bot.send_message(msg.chat.id, 'Whose? ')
        elif "Boobs" in msg.text:
            bot.send_message(msg.chat.id, 'What size? ')
        elif "boobs" in msg.text:
            bot.send_message(msg.chat.id, 'What size? ')
        elif "Cheeby" in msg.text:
            bot.send_message(msg.chat.id, 'No Vulgarity Please!! ')
        elif "cheeby" in msg.text:
            bot.send_message(msg.chat.id, 'No Vulgarity Please!! ')
        elif "damn" in msg.text:
            bot.send_message(msg.chat.id, 'No Vulgarity Please! ')
        elif "knn" in msg.text:
            bot.send_message(msg.chat.id, 'No Vulgarity Please! ')
        elif "Knn" in msg.text:
            bot.send_message(msg.chat.id, 'No Vulgarity Please! ')
        elif "Kns" in msg.text:
            bot.send_message(msg.chat.id, 'Agree with that! ')
        elif "kns" in msg.text:
            bot.send_message(msg.chat.id, 'Agree with that! ')
        elif "nabei" in msg.text:
            bot.send_message(msg.chat.id, 'No Vulgarity Please! ')
        elif "Nabei" in msg.text:
            bot.send_message(msg.chat.id, 'No Vulgarity Please! ')

    pmsg=msg.text
