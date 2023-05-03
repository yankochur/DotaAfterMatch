import requests
import configparser
import telebot

config = configparser.ConfigParser()
config.read('config.txt')           # make config.txt:
                                    # [DEFAULT]
                                    # bot_token={your_token}
                                    # chat_id={your_chat_id}

bot_token = config.get('DEFAULT', 'bot_token')
chat_id = config.get('DEFAULT', 'chat_id')
url = 'https://api.opendota.com/api'
bot = telebot.TeleBot(bot_token)

def main():
    def get_last_matches(account_id):
        last_matches_url = url + f'/players/{account_id}/recentMatches'
        last_matches_data = requests.get(last_matches_url).json()
        return last_matches_data

    last_matches_info = get_last_matches(371887209)

    for last_matches_info_data in last_matches_info:
        print(last_matches_info_data)
        bot.send_message(chat_id, str(last_matches_info_data), parse_mode='html')

if __name__ == "__main__":
    main()