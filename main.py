import requests
import telegram


url = 'https://api.opendota.com/api'


def main():
    def get_last_matches(account_id):
        last_matches_url = url + f'/players/{account_id}/recentMatches'
        last_matches_data = requests.get(last_matches_url).json()
        return last_matches_data

    last_matches_info = get_last_matches(371887209)
    for last_matches_info_data in last_matches_info:
        print(last_matches_info_data)


def send_info_into_telegram():
    pass


if __name__ == "__main__" :
    main()