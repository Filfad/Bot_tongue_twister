from telegram.ext import Updater

def main():
    mybot = Updater("6093246395:AAHDBK6JFUdb8y73LBjwgQEHFG_Lq-uTE9g", use_context=True)
    mybot.start_polling()
    mybot.idle()
main()