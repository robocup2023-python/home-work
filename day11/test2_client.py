import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8888)) 
text_to_translate = input("your text:")
client.send(text_to_translate.encode('utf-8'))
response = client.recv(1024)
print(response.decode('utf-8'))
client.close()

