def autologin():
    import requests
    import json
    try:
        x=open('do.txt','r').read()
        x=json.loads(x)
    except FileNotFoundError:
        uname=input('please input username')
        pwd=input('please input password')
        ps={
            "uname":uname,
            "pwd":pwd
        }
        p=open('do.txt','x')
        p.write(json.dumps(ps))
        x=open('do.txt','r').read()
        x=json.loads(x)
    uname=x['uname']
    pwd=x['pwd']
    url='http://2.2.2.2/login'
    myobj={
        "username":uname,
        "password":pwd
    }
    xp=requests.post(url,myobj)
    print(x,xp)
autologin()