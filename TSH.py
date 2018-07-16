# Author   : Atakan Argın
# Website  : https://atakanargn.blogspot.com/
# Linkedin : https://linkedin.com/in/atakanargn
# Github   : https://github.com/atakanargn

# - *- coding: utf- 8 - *-
from telegram.ext import Updater, CommandHandler
import os

### SETTINGS ###

# BOT API TOKEN
apiKey  = "YOUR-BOT'S-API-TOKEN"

# /START COMMAND
def start(bot, update):
    update.message.reply_text("TERMINAL ENABLED!")

# /T COMMAND
def terminalFunc(bot,update,args):
    incomeText = " ".join(args)
    os.system(incomeText+str("  | tee lastCommands.txt"))
    sCmdFile = open("lastCommands.txt")
    update.message.reply_text(str(sCmdFile.read()))
    sCmdFile.close()
    os.system("rm lastCommands.txt")

def main():
    updater = Updater(token=apiKey)
    dispatcher = updater.dispatcher
    print("BOT STARTED!")

    ### BOT COMMANDS
    start_handler = CommandHandler('start',start)
    terminal_handler = CommandHandler('t',terminalFunc,pass_args=True)

    # COMMAND DISPATCH
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(terminal_handler)

    # START THE BOT
    updater.start_polling()

    # RUN
    updater.idle()

if __name__ == '__main__':
    main()