# TSH-Protocol
## Latest update
* api.txt removed, Api Key must add to TSH.py "apiKey" variable.
* requirements.txt updated.
* Unnecessary library's removed (pyautogui)
* * Pyautogui removed because this library for take screenshot from bot computer but if this computer don't have desktop environment or windows manager, pyautogui isn't working properly.

## Usage
0) First give "pip install -r requirements.txt" command from Terminal.
1) Create Telegram bot with @BotFather
2) Copy your Api Key and paste to apiKey variable.
3) Run TSH.py
4)  "/start" command will start your conversation with your bot.
    "/t Terminal Command" will run your commands
5) That's it!

If you wanna start this bot at every startup;
give "crontab -e" command and add this line,
* @reboot cd ~/TSH-Protocol/ && python TSH.py