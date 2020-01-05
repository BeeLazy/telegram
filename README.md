# telegram
A telegramclient to delete group messages. It is written in python and uses telethon to do the heavy lifting

# Android how to
1. Create a telegram api user. Go to https://my.telegram.org/apps, and select create new application. Fill in whatever you want as 'App title' and 'Short name'. You can leave the other fields blank. Push the create application button. Write down your api_id and api_hash. You will need those later.
2. On your android phone, install the termux application from Play
3. Start termux
4. pkg install python -y
5. pip install telethon
6. pkg install wget -y
7. wget https://raw.githubusercontent.com/BeeLazy/telegram/master/DeleteGroupMessages.py
8. python DeleteGroupMessages.py -ai YOUR_API_ID -ah YOUR_API_HASH -ci TELEGRAM_CHANNEL_ID

You will get 2 deprecation warnings. Never mind those, they are just warnings. I will update the code after I have updated my linux installation to the new api

Point 1 to 7 only needs to be done once. Point 8 needs to be run each time you want to delete messages. You can use the up arrow in termux to get previous commands. Saves the headache of typing the api_id and api_hash more than once.
