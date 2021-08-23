# 终端输入使用LittleServer功能

### 1 接口说明

LittleServer目前支持 `tinyurl` , `pastebin` , `filesave`功能

```python
# 1）tinyURL:/api/tinyurl/encode
# 请求body
data = {'surl': surl}
headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}


# 2）pastebin:/api/pastebin/submit
# 请求body
data = {'poster': POSTER, 'syntax': SYNTAX, 'content': CONTENT}
headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}


# 3）filesave:/api/filesave/put
# 请求body
f = open(FILE, 'rb')
data = {'files': {'file': f}, 'key': {'key': PASSKEY}}
```



###2 使用说明

切换到项目所在根目录，然后用命令行输入

```python
# 三种功能的输入字符是不区分大小的
# 比如：tinyurl , TinyURL都可以调用tinyurl的功能

python main.py tinyurl TEST_URL 

python main.py pastebin POSTER SYNTAX CONTENT

python main.py filesave FILE PASSKEY

# eg:
(venv) ➜  CMDTool git:(main) ✗ python main.py tinyuRL https://binacs.cn
https://kiki.zone/r/6VniAr

```

