import requests

API_KEY = 'dd3f29660d187fdcc3bc73f7a9693cf6'
secret_key = '23843e6619ceb83c7d6703b829f6824a'
r = requests.get('https://api.hitbtc.com/api/2/trading/balance', auth=(API_KEY, secret_key))
print(r.status_code)

