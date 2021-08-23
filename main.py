# -*- coding: UTF-8 -*-
import requests
import sys, getopt

data = dict()
svc_name = ['tinyurl', 'pastebin', 'filesave']
svc_api = {'tinyurl': 'https://kiki.zone/api/tinyurl/encode',
           'pastebin': 'https://kiki.zone/api/pastebin/submit',
           'filesave': 'https://kiki.zone/api/filesave/put'}

svc_test_map = {'tinyurl': 'http://127.0.0.1:8000/api/tinyurl/encode',
                'pastebin': 'http://127.0.0.1:8000/api/pastebin/submit',
                'filesave': 'http://127.0.0.1:8000/api/filesave/put'}

def go_request(svcType, data, type):
    requests.packages.urllib3.disable_warnings()
    if not type:
        r = requests.post(svcType, data=data, headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
                      verify=False)
    else:
        r = requests.post(svcType, files=data['files'], data = data['key'],verify=False)  # 文件类型的header格式默认即可
    print(r.text)


def main():
    opts, args = getopt.getopt(sys.argv[1:], "ho:", ["help", "output="])  # 用sys.argv[1:]过滤掉第一个参数（它是执行脚本的名字，不应算作参数的一部分）
    svc = args[0].lower()
    type = 0
    if svc == svc_name[0]:
        if len(args) != 2:
            print(' Error input! Re-enter Please.')
            print(" only SURL is required in tinyurl-api. Re-enter Please")
            return
        svc_url = svc_api[svc_name[0]]
        data = {'surl': args[1]}
    elif svc == svc_name[1]:
        if len(args) != 4:
            print(' Error input! Re-enter Please.')
            print(" POSTER, SYNTAX and CONTENT are required in pastebin-api.")
            return
        svc_url = svc_api[svc_name[1]]
        data = {'poster': args[1], 'syntax': args[2], 'content': args[3]}
    elif svc == svc_name[2]:
        if len(args) != 3:
            print(' Error input! Re-enter Please.')
            print(" FILE and PASSKEY are required in filesave-api. Re-enter Please")
            return
        type = 1
        svc_url = svc_api[svc_name[2]]
        f = open(args[1], 'rb')
        data = {'files': {'file': f}, 'key': {'key': args[2]}}
    else:
        print(' Error SVC-API! Re-enter Please.')
        print(" TinyURL, PasteBin and FileSave are only supported By TracyYaoYao's LittleServer until now.")
        return
    go_request(svc_url, data, type)

if __name__ == '__main__':
    main()
