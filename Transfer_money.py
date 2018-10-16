import requests

def transfer(API_Key, secret_key, currency, amount, type):
    try:
        if type == 0 or 'bankToExchange':
            type_str = 'bankToExchange'
        elif type == 1 or 'exchangeToBank':
            type_str = 'exchangeToBank'
        else:
            raise Exception('Please input correct type， 1 :exchangeToBank, 0 :bankToExchange')
        post_data = {'currency': currency, 'amount': float(amount), 'type': type_str}
        url = 'https://api.hitbtc.com/api/2/account/transfer'
        ret = requests.post(url, data=post_data, auth=(API_Key, secret_key))
        if ret.status_code == 200:
            print('Transfer succeed')
        else:
            print('Failed:', ret.json())

    except Exception as e:
        print(e)


if __name__ == '__main__':
    api = '5316750db2dc5f96837ef3840560cd3b'
    key = '29f3f44e59e834d1cf383c2861d375e2'
    transfer(api, key, "INSUR", 100, 0)