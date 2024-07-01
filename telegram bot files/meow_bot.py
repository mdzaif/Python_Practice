from telegram import Update
from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello, welcome to Meow Bot! How can I help you?')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
        /start --> start this bot
        /hlep --> bot command manual
        /services --> The services I have
        """)

async def services(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ['Python'], ['Shell Script'], ['Git'], ['ollama Setup'], ['Open Source AI Model']
    ]
    await update.message.reply_text('Do you want to see!'
                                    ,reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard = True,one_time_keyboard = True)
                                    )

async def favor_keyboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton('ser1', 'link1'),
            InlineKeyboardButton('ser2', 'link2'),
            InlineKeyboardButton('ser3', 'link3'),
            InlineKeyboardButton('ser4', 'link4'),
            InlineKeyboardButton('ser5', 'link5')
        ]
    ]
    await update.message.reply_text('Learn with us with best resources', reply_markup = InlineKeyboardMarkup(keyboard))

def main():
    application = Application.builder().token('api_key').build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help))
    application.add_handler(CommandHandler('services', services))
    application.add_handler(CommandHandler('favor', favor_keyboard))

    # Running the application
    application.run_polling()

if __name__ == '__main__':
    main()
