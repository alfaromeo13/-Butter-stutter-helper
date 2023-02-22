from auth import TELEGRAM_TOKEN
import telebot
from telebot import TeleBot
from speech_to_text import get_text, get_answer


def get_telegram_bot(token: str) -> None:
    bot: TeleBot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        intro_msg: str = "Hello! I'm Butter 🧈✨" \
                         "\nHelping people who stutter is my job." \
                         "\nSend me a voice message, and I'll transcribe it.🪄✨" \
                         "\nYou can also text me any question you have about stuttering.🤓📚" \
                         "\n" \
                         "\n" \
                         "To contact my creators: https://m.me/butterbot4u"
        bot.send_message(message.chat.id, intro_msg)

    @bot.message_handler(content_types=['voice'])
    def voice_processing(message):
        fid = bot.get_file(message.voice.file_id)
        audio_file = bot.download_file(fid.file_path)
        text: str = get_text(audio_file)
        bot.reply_to(message, text)

    @bot.message_handler(content_types=['text'])
    def message_text_replier(message):
        answer_msg: str = get_answer(message.text)
        bot.reply_to(message, answer_msg)

    bot.polling()


if __name__ == '__main__':
    get_telegram_bot(TELEGRAM_TOKEN)
