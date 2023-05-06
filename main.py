import requests
import configparser
import telebot
# from selenium import webdriver


# driver = webdriver.Chrome()

config = configparser.ConfigParser()
config.read('config.txt')           # make config.txt:
                                    # [TELEGRAM]
                                    # bot_token={your_token}
                                    # chat_id={your_chat_id}

bot_token = config.get('TELEGRAM', 'bot_token')
chat_id = config.get('TELEGRAM', 'chat_id')
url = 'https://api.opendota.com/api'
bot = telebot.TeleBot(bot_token)

def main():
    def get_last_matches(account_id):
        last_matches_url = url + f'/players/{account_id}/recentMatches'
        last_matches_data = requests.get(last_matches_url).json()
        return last_matches_data

    last_matches_info = get_last_matches(371887209)

    if len(last_matches_info) > 0:
        last_match_data = last_matches_info[0]
        print(last_match_data)
        bot.send_message(chat_id, str(last_match_data), parse_mode='html')
    else:
        print("Нет информации о последних матчах.")
        bot.send_message(chat_id, "Нет информации о последних матчах.")

    last_match_id = last_match_data['match_id']
    # last_match_id = '7118994693'

    # def request_detailed_info(url, match_id):
    #     driver.get(f'{url}/request#{match_id}')
    #     driver.implicitly_wait(10)
    #     driver.quit()
    #     page_source = driver.page_source
    #     return page_source
    #
    # requested_info = request_detailed_info(url, last_match_id)
    # print(requested_info)

    # def info_about_last_match(match_id):
    #     last_match_url = url + f'/matches/{match_id}/analyzed?include_analyzed=true'
    #     last_match_data = requests.get(last_match_url).json()
    #     return last_match_data

    # last_match_info = info_about_last_match(last_match_id)
    # print(last_match_info)

if __name__ == "__main__":
    main()