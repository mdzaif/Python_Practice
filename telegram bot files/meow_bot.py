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
            InlineKeyboardButton('Pyhon', 'https://youtube.com/playlist?list=PLT98CRl2KxKGIazPd2nQEPbG7sQpT8LEj&si=jVNwk1eZHecmCCri'),
            InlineKeyboardButton('Shell Script', 'https://youtube.com/playlist?list=PLT98CRl2KxKGj-VKtApD8-zCqSaN2mD4w&si=CmjuUpimaJEeyhRz'),
            InlineKeyboardButton('Git', 'https://git-scm.com/docs/gittutorial'),
            InlineKeyboardButton('ollama Setup', 'https://ollama.com', 'https://github.com/ollama/ollama'),
            InlineKeyboardButton('Open Source AI Model', 'https://huggingface.co/models')
        ]
    ]
    await update.message.reply_text('Learn with us with best resources', reply_markup = InlineKeyboardMarkup(keyboard))

def main():
    application = Application.builder().token('6994561004:AAGLrnpXG8UrqFPI6R1ZnN2Uv6I_M0nePCI').build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help))
    application.add_handler(CommandHandler('services', services))
    application.add_handler(CommandHandler('favor', favor_keyboard))

    # Running the application
    application.run_polling()

if __name__ == '__main__':
    main()
