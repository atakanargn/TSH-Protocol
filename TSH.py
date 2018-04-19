# - *- coding: utf- 8 - *-
from telegram.ext import Updater, CommandHandler
import os
import pyautogui as pag
from sys import argv

### SETTINGS ###

# BOT API TOKEN
config  = open("api.txt","r")
apiKey  = config.read()
config.close()

# START PATH
START_PATH = str(os.getcwd()+"/")

# HOME PATH
HOME_PATH = os.path.expanduser('~')

# /START COMMAND
def start(bot, update):
    update.message.reply_text("""Hi!\nYoda is my name!\n\
If control this computer you wanna;\n login with this command you can:\n/login username password\n""")

# /HELP COMMAND
def helpFunc(bot,update):
    update.message.reply_text("Available Commands;\n\
/t terminalCommand >> shell any terminal command, you can with this command!\n\
/w words >> write like keyboard\n\
/screen >> Screenshot from computer\n\
/help >> All of commands!\n\
")

# /T COMMAND
def terminalFunc(bot,update,args):
    incomeText = " ".join(args)
    os.system(incomeText+str("  | tee "+START_PATH+"lastCommands.txt"))
    sCmdFile = open(START_PATH+"lastCommands.txt")
    update.message.reply_text("Your Command : \""+incomeText+"\"\n\n\
Output ;\n\n"+sCmdFile.read())
    sCmdFile.close()
    os.system("rm "+START_PATH+"lastCommands.txt")

# /W COMMAND
def writeFunc(bot,update,args):
    incomeText = " ".join(args)
    pag.typewrite(incomeText)

# /SCREEN COMMAND
def screenshotFunc(bot,update):
    pic = pag.screenshot()
    pic.save("ss.png")
    bot.send_photo(chat_id=update.message.chat_id, photo=open("ss.png","rb"))
    os.system("rm ss.png")

def main():
    updater = Updater(token=apiKey)
    dispatcher = updater.dispatcher
    print("Bot started...\n\tyour commands from Telegram, Awaiting, I am!")

    ### BOT COMMANDS
    start_handler = CommandHandler('start',start)
    help_handler = CommandHandler('help',helpFunc)
    terminal_handler = CommandHandler('t',terminalFunc,pass_args=True)
    write_handler = CommandHandler('w',writeFunc,pass_args=True)
    screen_handler = CommandHandler('screen',screenshotFunc)

    # COMMAND DISPATCH
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(terminal_handler)
    dispatcher.add_handler(write_handler)
    dispatcher.add_handler(screen_handler)

    # START THE BOT
    updater.start_polling()

    # RUN
    updater.idle()

if __name__ == '__main__':
    main()