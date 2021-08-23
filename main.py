# -*- coding: UTF-8 -*-
import requests
import sys, getopt

data = dict()
url_svc = 'https://kiki.zone/tinyurl'
svc_name = ['tinyurl', 'pastebin', 'filesave']
svc_map = {'tinyurl': 'https://kiki.zone/api/tinyurl/encode',
           'pastebin': 'https://kiki.zone/api/pastebin/submit',
           'filesave': 'https://kiki.zone/api/filesave/put'}

svc_test_map = {'tinyurl': 'http://127.0.0.1:8000/api/tinyurl/encode',
                'pastebin': 'http://127.0.0.1:8000/api/pastebin/submit',
                'filesave': 'http://127.0.0.1:8000/api/filesave/put'}

# tinyURL:/api/tinyurl/encode
# pastebin:/api/pastebin/submit
# filesave:/api/filesave/put




def go_request(svcType, data, type):
    requests.packages.urllib3.disable_warnings()
    if type == 0:
        r = requests.post(svcType, data=data, headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
                      verify=False)
    else:
        print(data['key'])
        r = requests.post(svcType, files=data['files'], data = data['key'],
                          # headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
                          verify=False)
    print(r.text)


def main():
    opts, args = getopt.getopt(sys.argv[1:], "ho:", ["help", "output="])  # 用sys.argv[1:]过滤掉第一个参数（它是执行脚本的名字，不应算作参数的一部分）
    svc = args[0].lower()
    if svc == svc_name[0]:
        svc_url = svc_map[svc_name[0]]
        data = {'surl': args[1]}
        type = 0

    elif svc == svc_name[1]:
        svc_url = svc_map[svc_name[1]]
        data = {'poster': args[1], 'syntax': args[2], 'content': args[3]}
        type = 0
    else:
        svc_url = svc_map[svc_name[2]]
        f = open(args[1], 'rb')
        data = {'files': {'file': f}, 'key': {'key': args[2]}}
        type = 1
    go_request(svc_url, data, type)

if __name__ == '__main__':
    main()
