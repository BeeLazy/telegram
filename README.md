# telegram
A telegramclient to delete group messages. It is written in python and uses telethon to do the heavy lifting

# Android how to
1. Create a telegram api user at https://my.telegram.org/apps, and write down your api_id and api_hash
2. On your android phone, install the termux application from Play
3. Start termux
4. pkg install python -y
5. pip install telethon
6. pkg install wget -y
7. wget https://raw.githubusercontent.com/BeeLazy/telegram/master/DeleteGroupMessages.py
8. python DeleteGroupMessages.py -ai YOUR_API_ID -ah YOUR_API_HASH -ci TELEGRAM_CHANNEL_ID
