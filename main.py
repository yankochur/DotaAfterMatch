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

    if len(last_matches_info) > 0:
        last_match_data = last_matches_info[0]  # получить информацию о последнем матче
        print(last_match_data)
        bot.send_message(chat_id, str(last_match_data), parse_mode='html')
    else:
        print("Нет информации о последних матчах.")
        bot.send_message(chat_id, "Нет информации о последних матчах.")


if __name__ == "__main__":
    main()