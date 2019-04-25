from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ChatAction

file = open("task_list.txt")

myList = []

for task in file:
    task = task.split('\n')[0]
    myList.append(task)

file.close()
# define a command handler. Command handlers usually take two arguments:
# bot and update


def showTasks(bot, update):
    for task in myList:
        update.message.reply_text(task)


def newTask(bot, update, args):
    task = ''
    for word in args:
        task += word + ' '
    myList.append(task)
    file = open("task_list.txt", 'w+')
    for task in myList:
        file.write("%s\n" % task)
    file.close()
    update.message.reply_text("Task created successfully.")


def reload(bot, update):
    file = open("task_list.txt")
    myList.clear()
    for task in file:
        task = task.split('\n')[0]
        myList.append(task)
    file.close()


def removeTask(bot, update, args):
    task = ''
    for word in args:
        task += word + ' '
    myList.remove(task)
    file = open("task_list.txt", 'w+')
    for task in myList:
        file.write("%s\n" % task)
    file.close()
    update.message.reply_text("Task removed successfully.")


def removeAllTasks(bot, update):
    file = open("task_list.txt", 'w+')
    myList.clear()
    for task in myList:
        file.write("%s\n" % task)
    file.close()
    update.message.reply_text("All tasks removed.")


# the non-command handler
def echo(bot, update):
    # simulate typing from the bot
    bot.sendChatAction(update.message.chat_id, ChatAction.TYPING)
    # send a message to the user
    update.message.reply_text("I'm sorry, I can't do that.")


def main():
    # create the EventHandler and pass it your bot's token
    updater = Updater("894225615:AAFSOZUygOTcQionsBsCe0xapsmLFdip_Zc")

    # get the dispatcher to register handlers
    dp = updater.dispatcher

    # add the command handlers
    dp.add_handler(CommandHandler("showTasks", showTasks))
    dp.add_handler(CommandHandler("newTask", newTask, pass_args=True))
    dp.add_handler(CommandHandler("removeTask", removeTask, pass_args=True))
    dp.add_handler(CommandHandler("removeAllTasks", removeAllTasks))
    dp.add_handler(CommandHandler("reload", reload))

    # on non-command textual messages - echo the original message
    dp.add_handler(MessageHandler(Filters.text, echo))

    # start the bot
    updater.start_polling()

    # run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == "__main__":
    main()
