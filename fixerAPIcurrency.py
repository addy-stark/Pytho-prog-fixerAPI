import requests
import time
money = 100 #GBP
url = "http://data.fixer.io/api/convert?access_key=0d27dd8ffbcfacd37de7f1e7111000bf&from=USD&to=GBP&amount=money"
result = False
i = 1
while result != True and i < 20:  
    res = requests.get(url)
    result = res.json()['success']
    if result == False:
        print(str(result) + ' -access restricted for this plan, ' + 'try ' + str(i))
        i+=1
        if i==20:
            print('API not providing conversion value. Please check your internet or your fixer plan and try again.')
    else:
        print('Current conversion rate ' + res.json()['info']['rate']) ##conversion to usd
    time.sleep(3)

