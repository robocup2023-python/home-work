#这个代码在55行client_socket, addr = server.accept()无法执行没有找出原因
import socket
import threading
import requests
import hashlib
import random
import string
# 生成随机的salt字符串
def generate_salt(length):
    salt = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    return salt 
def translate_text(text):
    appid= '20231018001850755'
    url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
    q=text
    salt = generate_salt(10)
    secret_key='3n5HoaNteYME7FWbKkBG'
    string_to_sign = appid + q + salt + secret_key
# 使用MD5哈希算法计算签名
    md5 = hashlib.md5()
    md5.update(string_to_sign.encode('utf-8'))
    sign = md5.hexdigest()
    params = {
        'q': text,
        'from': 'auto',
        'to': 'en',
        'appid': appid,
        'salt': salt,
        'sign': sign 
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        translated_data = response.json()
        return translated_data['trans_result'][0]['dst']
    else:
        return "Translation failed"

def client_handler(client_socket):
    request = client_socket.recv(1024)
    
    translated_text = translate_text(request.decode('utf-8'))
    
    response = "Translation: " + translated_text
    
    client_socket.send(response.encode('utf-8'))
    client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8888))

while True:
    client_socket, addr = server.accept() 
    client_thread = threading.Thread(target=client_handler, args=(client_socket,))
    client_thread.start()

