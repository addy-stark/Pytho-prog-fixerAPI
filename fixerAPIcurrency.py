import requests
import time
money = 100
url = "http://data.fixer.io/api/convert?access_key=0d27dd8ffbcfacd37de7f1e7111000bf&from=USD&to=GBP&amount=money"
res = requests.get(url)
result = ''
while result != True:
    try:
        res = requests.get(url)
        result = res.json()['success']
        if result == False:
            print('fail' + ' -access restricted for this plan')
        else:
            print(res.json()['info']['rate'])
            print('success')
        time.sleep(3)
    except:
        pass
